global f
f = 0

def t_movie():
	global f
	f = f + 1
	print("Which movie do you want to watch?")
	print("1. Movie")
	print("2. Movie")
	print("3. Movie")
	print("4. Back")
	movie = int(input("Choose your movie: "))
	if movie == 4:
		center()
		theater()
		return 0
	if f == 1:
		theater()

def theater():
    print("Which screen do you want to watch the movie on?")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")
    a = int(input("Choose your screen: "))
    
    if a not in [1, 2, 3]:
        print("Select your screen correctly.")
        return
    
    ticket = int(input("Number of tickets do you want?: "))
    select_seat(a, ticket)

def select_seat(screen, num_tickets):
    print(f"Screen {screen} - Available seats:")

    # Example of current seat status (for demonstration purposes)
    seats = [['O' for _ in range(10)] for _ in range(5)]  # 'O' represents available seats

    # Suppose some seats are already booked (for demonstration purposes)
    seats[0][1] = 'X'
    seats[2][5] = 'X'
    seats[3][7] = 'X'

    for i, row in enumerate(seats, start=1):
        print(f"Row {i}: {' '.join(row)}")

    # Ticket price per seat
    ticket_price = 10  # Example ticket price, you can adjust this as needed

    # Ask user to select seats
    selected_seats = []
    for _ in range(num_tickets):
        while True:
            row = int(input("Select row (1-5): "))
            seat = int(input("Select seat (1-10): "))
            if seats[row - 1][seat - 1] == 'O':  # Check if the seat is available
                selected_seats.append((row, seat))
                seats[row - 1][seat - 1] = 'X'  # Mark the seat as booked
                break
            else:
                print("Seat already booked. Please select another seat.")

    # Calculate total amount
    total_amount = num_tickets * ticket_price

    # Display selected seats
    print(f"You have selected {num_tickets} seat(s):")
    for seat in selected_seats:
        print(f"Row {seat[0]}, Seat {seat[1]}")

    # Display total amount
    print(f"Total amount: ${total_amount}")

    # Display updated seat status
    print("Updated seat status:")
    for i, row in enumerate(seats, start=1):
        print(f"Row {i}: {' '.join(row)}")

    timing(screen)


def timing(a):
	time1 ={ 
		"1": "10.00-1.00",
		"2": "1.10-4.10",
		"3": "4.20-7.20",
		"4": "7.30-10.30"
}
	time2 ={ 
		"1": "10.15-1.15",
		"2": "1.25-4.25",
		"3": "4.35-7.35",
		"4": "7.45-10.45"
}
	time3 ={ 
		"1": "10.30-1.30",
		"2": "1.40-4.40",
		"3": "4.50-7.50",
		"4": "8.00-10.45"
}
	if a == 1:
		print("Choose your time:")
		print(time1)
		t = input("Select your time:")
		x = time1.get(t)
		if x:
			print("Successful! Enjoy the movie at", x)
		else:
			print("Invalid time selection")
	elif a == 2:
		print("Choose your time:")
		print(time2)
		t = input("Select your time:")
		x = time2.get(t)
		if x:
			print("Successful! Enjoy the movie at", x)
		else:
			print("Invalid time selection")
	elif a == 3:
		print("Choose your time:")
		print(time3)
		t = input("Select your time:")
		x = time3.get(t)
		if x:
			print("Successful! Enjoy the movie at", x)
		else:
			print("Invalid time selection")
	return 0

def movie(theater):
	if theater in [1, 2, 3]:
		t_movie()
	elif theater == 4:
		city()
	else:
		print("Wrong choice")

def center():
	print("Which theater do you wish to see the movie?")
	print("1. Inox")
	print("2. Icon")
	print("3. PVP")
	print("4. Back")
	a = int(input("Choose your option: "))
	if a in [1, 2, 3]:
		movie(a)
	elif a == 4:
		city()
	else:
		print("Wrong choice")
	return 0

def city():
	print("Hi, welcome to movie ticket booking:")
	print("Where do you want to watch the movie?")
	print("1. COIMBATORE")
	print("2. MADURAI")
	print("3. SALEM")
	place = int(input("Choose your option: "))
	if place in [1, 2, 3]:
		center()
	else:
		print("Wrong choice")

# Start the process by calling the city function
city()
