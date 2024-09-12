# print("WELCOME TO ONLINE BANKING ")
# print(input("Enter your Account ID::"))
# print(input("Enter your Password::"))
# print("!! WELCOME  TO SBI !!")
# print("""
# 1.withdraw money
# 2.deposit money
# 3.log out
# """)
# a=10000
# user_choice= int(input("Enter your choice::"))
# if user_choice==1:
#
#     def withdraw (a,b):
#         return a-b
#     def deposit(a,b):
#         return a+b
# b= int(input("enter the amount of money you want withdraw::"))
# print("select(1) for withdraw")
# # print("select(2) for deposit")
# choice = int(input("enter the choice::"))
# if choice == 1:
#     print(f"{a}-{b} withdraw is :: ", withdraw(a,b))
# c= int(input("enter the amount of money you want deposit::"))
# if choice == 2:
#     print(f"{a}+{b} deposit is :: ", deposit(a,b))
#     print("Your bank balance amount is 200000")
# elif user_choice==2:
#     print("Enter the amount of money you want to withdraw::")

# Total_amount = 10000
# name=input("Enter the name:")
# password=input("enter the password:")
# print("welcome to SBI bank !")
#
#
# def withdraw(money,Total_amount):
#     Total_amount -= money
#     print(f"Your Bank Balance is {Total_amount}")
# def deposit(money,Total_amount):
#    Total_amount+=money
#    print(f"Your Bank Balance is {Total_amount}")
# def logout():
#      print("Thank you")
#      print("visit again")
#
#
# choice = [withdraw, deposit, logout]
# for i in choice:
#     choices = """
#     1)withdraw
#     2)deposit
#     3)logout
#     """
#     print(choices)
#     user_choice=int(input("enter the choice:"))
#     if user_choice == 1:
#         money = int(input("enter the money to withdraw"))
#         withdraw(money, Total_amount)
#
#     if user_choice == 2:
#         money = int(input("enter the money to deposit"))
#         deposit(money, Total_amount)
#
#     if user_choice == 3:
#         print("Thank you!!")
#     break


# ids = ['Anitha', 'Namitha']
# psw = ['12345', 'yo']
# bal = [2000000, 70000]
#
# idx_id = 0
#
#
# # login
# def acc():
#     print('')
#
#     accid = input('Enter your account id : ')
#     print('')
#
#     if (accid in ids):
#         idx_id = (ids.index(accid))
#
#         password = input('Enter your password : ')
#         if (password in psw and password == psw[idx_id]):
#
#             print('')
#             print('Welcome!!')
#
#             activity(idx_id)
#         else:
#             print('wrong password')
#             acc()
#     else:
#         print('wrong id......')
#
#         print('')
#
#         print('This id does not exist! ')
#         create_acc()
#
#
# # activities to do
# def activity(idx_id):
#     print('')
#     print('Your bank balance amount =', bal[idx_id])
#
#     opt = int(input('Do you want to withdraw money (1)/deposit money (2)/log out (3) : '))
#
#     while (opt != 3):
#
#         if (opt == 1):
#
#             print('')
#
#             x = int(input('Enter the amount of money you want to withdraw : '))
#             total = bal[idx_id] - x
#
#             bal[idx_id] = total
#
#             print('')
#
#             print('You have recieved rupees', x)
#
#             print('')
#
#             print('1.Your bank balance amount =', bal[idx_id])
#
#
#
#
#         elif (opt == 2):
#
#             print('')
#
#             x = int(input('Enter the amount of money you want to deposit : '))
#             total = bal[idx_id] + x
#
#             bal[idx_id] = total
#
#             print('')
#
#             print('You have deposited rupees', x)
#
#             print('')
#
#             print('2.Your bank balance amount =', bal[idx_id])
#
#         else:
#             print('ERROR')
#             activity(idx_id)
#
#         opt = int(input('Do you want to withdraw money (1)/deposit money (2)/log out (3) : '))
#
#     print('logging out...')
#     print('Thank You!')


# acc()

# id=['Prajwal','Kumar']
# pwd=[123456,78910]
# print(":::WELCOME TO FLIGHT BOOKING::::")
# print("""
# SELECT THE TYPE OF FLIGHT
# 1.International Flight
# 2.Domestic Flight
# 3.QUIT
# """)
# flight_type=(int(input("Enter your choice::")))
# def international():
#     if flight_type==1:
#         print("""
#         WELCOME TO INTERNATIONAL FLIGHT TICKET BOOKING
#         1.SINGAPORE AIRLINES
#         2.BRITISH AIRWAYS
#         3.AIR INDIA
#         """)
#         type=int(input("Enter the option::"))
#         if(type==1):
#
#             print("SINGAPORE AIRLINES")
#             print("From:: ")
#             frm=input("")
#             print("Destination::")
#             Destination=input("")
#             print()
#     def domestic():
#         if flight_type==2:
#          print("""
#
#             WELCOME TO DOMESTIC FLIGHT TICKET BOOKING
#             1.INDIGO
#             2.VISTARA
#             3.SPICEJET
#             """)
#
#     def quit():
#         print("Thank you")
#         print("Visit again")
#         exit()
#
# def book_ticket(user_name, num_tickets, available_tickets):
#     """
#     Book tickets for an event.
#
#     Parameters:
#     user_name (str): Name of the user booking the tickets
#     num_tickets (int): Number of tickets to book
#     available_tickets (int): Total available tickets
#
#     Returns:
#     str: Booking confirmation or failure message
#     """
#     if num_tickets <= 0:
#         return "Number of tickets must be greater than zero."
#
#     if num_tickets > available_tickets:
#         return f"Sorry, only {available_tickets} tickets are available."
#
#     available_tickets -= num_tickets
#     return (f"Booking successful! {user_name}, you have booked {num_tickets} ticket(s). "
#             f"{available_tickets} tickets remaining.")
#
#
# # Example usage
# total_tickets = 100
# user_name = "Alice"
# num_tickets_to_book = 3
#
# confirmation_message = book_ticket(user_name, num_tickets_to_book, total_tickets)
# print(confirmation_message)
# defooking successful! {user_name} booked {num_tickets} ticket(s). {available_tickets} left."
choice = """
1) Domestic
2) International
3) Quit
"""

domestic_choices = """
1) Air India Express - Rs:3500
2) IndiGo - Rs:5000
3) SpiceJet - Rs:7000
"""
international_choices = """
1) Malaysia Airlines - Rs:15000
2) Etihad Airways - Rs:20000
3) Emirates - Rs:25000
"""
select = """
1) Book ticket
2) Cancel ticket
"""

ticket_prices = {
    "Domestic": [3500, 5000, 7000],
    "International": [15000, 20000, 25000]
}

def book_ticket(price):
    print(f"Your ticket price is {price}")
    print("Your ticket has been booked")

def cancel_ticket(price):
    print("Your ticket has been cancelled and your money has been refunded")

def quit_program():
    print("Thank you")
    print("Visit again")
    exit()

while True:
    print(choice)
    user_choice = int(input("Enter the choice:"))

    if user_choice == 1:
        print(domestic_choices)
        user_choiceD = int(input("Enter the choice:"))
        price = ticket_prices["Domestic"][user_choiceD - 1]
    elif user_choice == 2:
        print(international_choices)
        user_choiceI = int(input("Enter the choice:"))
        price = ticket_prices["International"][user_choiceI - 1]
    elif user_choice == 3:
        quit_program()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue

    print(select)
    user_select = int(input("Please select the option:"))
    if user_select == 1:
        book_ticket(price)
    elif user_select == 2:
        cancel_ticket(price)
    else:
        print("Invalid choice. Please select 1 or 2.")

# def book_ticket(user_name):
#     if
#     # if money > Total_amount:
#     #     print("Insufficient funds")
#     else:
#         # Total_amount -= money
#         print(f"Your Ticket price is {money}")
#         print("your Ticket has been booked")
#         # print(f"Your Balance money is {Total_amount}")
#     return Total_amount
#
#
# # def cancel_ticket(money):
# #     Total_amount += money
# #     # print(f"Your Balance money is {Total_amount}")
# #     return Total_amount
#
# def quit():
#     print("Thank you")
#     print("Visit again")
#     exit()
#
# while True:
#     print(choice)
#     user_choice = int(input("Enter the choice:"))
#
#     if user_choice == 1:
#         print(International_choices)
#         user_choiceD = int(input("Enter the choice:"))
#         print(user_choiceD)
#
#     elif user_choice == 2:
#         print(Domestic_choices)
#         user_choiceI = int(input("Enter the choice:"))
#         print(user_choiceI)
#
#     elif user_choice == 3:
#         quit()
#
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")
#         continue
#
#     print(select)
#     user_select = int(input("Please select the option:"))
#     if user_select == 1:
#         moneyb = int(input("Enter the price to book the ticket:1st class:Rs:7000,2nd class:Rs:5000,3rd class:Rs:3500: "))
#         Total_amount = book_ticket(moneyb, Total_amount)
#     elif user_select == 2:
#         money=moneyb
#         Total_amount = cancel_ticket(money, Total_amount)
#         print("Your Ticket has been cancelled and your money has been refunded")
#     else:
#         print("Invalid choice. Please select 1 or 2.")
# #######################################################################################################################################################
# print("#################################################################################################################################")
# import datetime
#
# class Flight:
#     def __init__(self, flight_number, origin, destination, departure_time, arrival_time, seats):
#         self.flight_number = flight_number
#         self.origin = origin
#         self.destination = destination
#         self.departure_time = departure_time
#         self.arrival_time = arrival_time
#         self.seats = seats
#         self.bookings = []
#
#     def book_seat(self, passenger_name):
#         if len(self.bookings) < self.seats:
#             self.bookings.append(passenger_name)
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return f"Flight {self.flight_number}: {self.origin} to {self.destination}, Departure: {self.departure_time}, Arrival: {self.arrival_time}, Available seats: {self.seats - len(self.bookings)}"
#
# class BookingSystem:
#     def __init__(self):
#         self.flights = []
#         self.passenger_bookings = {}
#
#     def add_flight(self, flight):
#         self.flights.append(flight)
#
#     def view_flights(self):
#         for flight in self.flights:
#             print(flight)
#
#     def book_flight(self, flight_number, passenger_name):
#         for flight in self.flights:
#             if flight.flight_number == flight_number:
#                 if flight.book_seat(passenger_name):
#                     if passenger_name not in self.passenger_bookings:
#                         self.passenger_bookings[passenger_name] = []
#                     self.passenger_bookings[passenger_name].append(flight)
#                     print(f"Booking successful for {passenger_name} on flight {flight_number}")
#                     return
#                 else:
#                     print(f"No available seats on flight {flight_number}")
#                     return
#         print(f"Flight {flight_number} not found")
#
#     def view_bookings(self, passenger_name):
#         if passenger_name in self.passenger_bookings:
#             for flight in self.passenger_bookings[passenger_name]:
#                 print(flight)
#         else:
#             print(f"No bookings found for {passenger_name}")
#
# def main():
#     system = BookingSystem()
#
#     # Adding some flights
#     flight1 = Flight("AA101", "New York", "Los Angeles", datetime.datetime(2024, 8, 5, 8, 0), datetime.datetime(2024, 8, 5, 11, 0), 10)
#     flight2 = Flight("BB202", "Boston", "Chicago", datetime.datetime(2024, 8, 6, 9, 0), datetime.datetime(2024, 8, 6, 11, 30), 5)
#     flight3 = Flight("CC303", "San Francisco", "Miami", datetime.datetime(2024, 8, 7, 14, 0), datetime.datetime(2024, 8, 7, 18, 0), 8)
#
#     system.add_flight(flight1)
#     system.add_flight(flight2)
#     system.add_flight(flight3)
#
#     while True:
#         print("\n1. View Flights\n2. Book Flight\n3. View Bookings\n4. Exit")
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             system.view_flights()
#         elif choice == "2":
#             flight_number = input("Enter flight number: ")
#             passenger_name = input("Enter passenger name: ")
#             system.book_flight(flight_number, passenger_name)
#         elif choice == "3":
#             passenger_name = input("Enter passenger name: ")
#             system.view_bookings(passenger_name)
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# if __name__ == "__main__":
#     main()


