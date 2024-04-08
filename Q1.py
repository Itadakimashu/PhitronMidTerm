class Star_Cinema:
	__hall_list = []

	@property
	def hall_list(self):
		return self.__hall_list

	def entry_hall(self,hall):
		self.hall_list.append(hall)


	def main_menu(self):
		while True:
			print("1. View All Show Today")
			print("2. View Available Seats")
			print("3. Book Ticket")
			print("4. Exit")
			n = int(input("Enter option: "))
			print()
			if n == 4: break
			if n == 1: self.view_all_show()
			if n == 2: self.view_available_seats()
			if n == 3: self.book_ticket()


	def view_all_show(self):
		for hall in self.hall_list:
			for show in hall.show_list:
				id = show[0]
				movie = f'{show[1]}({id})'
				time = show[2]
				print(f"Movie: {movie} Show ID: {id} Time: {time}")
		print()

	def view_available_seats(self):
		id = int(input("Enter Show ID: "))
		h = None
		for hall in self.hall_list:
			for showID in hall.seats.keys():
				if id == showID:
					h = hall

		if h == None:
			print("The entered id is not valid!")
			input("press Enter to continue.")
			return

		h.view_available_seats(id)
		print()

	def book_ticket(self):
		id = int(input("Enter Show ID: "))
		h = None
		for hall in self.hall_list:
			for showID in hall.seats.keys():
				if id == showID:
					h = hall

		if h == None:
			print("The entered id is not valid!")
			input("press Enter to continue.")
			return

		n = int(input("number of Ticket: "))

		for x in range(n):
			while True:
				row = int(input("Enter Seat Row: "))
				col = int(input("Enter Seat Col: "))
				if h.is_valid_row_col(row,col) and h.is_seat_booked(id,row,col):
					break
			h.book_seats(id,[(row,col)])
			print(f"Seat({row},{col}) booked for {id}")
		print()
		


class Hall(Star_Cinema):
	def __init__(self,rows,cols,hall_no):
		self.__seats = dict()
		self.__show_list = list(tuple())
		self.__rows = rows
		self.__cols = cols
		self.__hall_no = hall_no

		self.entry_hall(self)

	@property
	def show_list(self):
		return self.__show_list

	@property
	def seats(self):
		return self.__seats

	@property
	def hall_no(self):
		return self.__hall_no

	@property
	def rows(self):
		return self.__rows

	@property
	def cols(self):
		return self.__cols
	
	
	 

	def entry_show(self,id,movie_name,time):
		self.seats[id] = [[0 for x in range(self.cols)] for y in range(self.cols)]
		self.__show_list.append((id,movie_name,time))

	def book_seats(self,id,listTuple):
		for row,col in listTuple:
			self.seats[id][row][col] = 1


	def view_show_list(self):
		for show in self.__show_list:
			print(show)

	def view_available_seats(self,id):
		seats = self.__seats[id]
		print("Available Seats:")
		for row in range(len(seats)):
			for col in range(len(seats[row])):
				if seats[row][col] == 0:
					print(f'Seat({row},{col})')

		print(f"Updated Seats Matrix for Hall {self.hall_no}")
		for seatrow in seats:
			print(seatrow)

	def is_valid_row_col(self,row,col):
		if row >= 0 and row <= self.rows and col >= 0 and col <= self.cols:
			return True
		print("invalid row,col")
		return False

	def is_seat_booked(self,id,row,col):
		if self.seats[id][row][col] == 0:
			return True
		print("Seat is already booked.")
		return False
 
h1 = Hall(4,5,1)
h2 = Hall(3,3,2)

h1.entry_show(111,'avengers','05/04/2024 09:30am')
h2.entry_show(333,'thor','05/04/2024 09:30am')


starCinema = Star_Cinema()
starCinema.main_menu()

