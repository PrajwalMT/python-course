print(":::WELCOME TO AIRLINES BOOKING::::")
choice = """
1.INTERNATIONAL AIRLINES
2.DOMESTIC AIRLINES
3.QUIT
"""
International_choices = """
WELCOME TO INTERNATIONAL AIRLINES
1.SINGAPORE AIRLINES - Rs:35000,Bengaluru to new york
2.BRITISH AIRWAYS - Rs:50000,Bengaluru to Landon
3.AIR INDIA - Rs:70000,Bengaluru to Dubai
"""
Domestic_choices = """
WELCOME TO DOMESTIC AIRLINES
1.INDIGO- Rs:1500,shimogga to bengaluru
2.VISTARA- Rs:2000,bengaluru to new delhi
3.SPICEJET- Rs:2500,bengaluru to chennai
"""
select = """
1) Book ticket
2) Cancel ticket
"""
ticket_prices = {
    "International": [35000, 50000, 70000],
    "Domestic": [1500, 2000, 2500]
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
        print(International_choices)
        user_choiceI = int(input("Enter the choice:"))
        price = ticket_prices["International"][user_choiceI - 1]
    elif user_choice == 2:
        print(Domestic_choices)
        user_choiceD = int(input("Enter the choice:"))
        price = ticket_prices["Domestic"][user_choiceD - 1]
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

# choice = """
# 1) Domestic
# 2) International
# 3) Quit
# """
#
# # Define flight details for Domestic
# Domestic_choices = {
#     1: {"Airline": "Air India Express", "Price": 7000, "Seats": 10, "Departure": "10:00 AM", "Arrival": "12:00 PM"},
#     2: {"Airline": "IndiGo", "Price": 5000, "Seats": 20, "Departure": "1:00 PM", "Arrival": "3:00 PM"},
#     3: {"Airline": "SpiceJet", "Price": 3500, "Seats": 15, "Departure": "5:00 PM", "Arrival": "7:00 PM"},
# }
#
# # Define flight details for International
# International_choices = {
#     1: {"Airline": "Malaysia Airlines", "Price": 15000, "Seats": 8, "Departure": "6:00 AM", "Arrival": "12:00 PM"},
#     2: {"Airline": "Etihad Airways", "Price": 20000, "Seats": 12, "Departure": "8:00 AM", "Arrival": "2:00 PM"},
#     3: {"Airline": "Emirates", "Price": 25000, "Seats": 5, "Departure": "11:00 AM", "Arrival": "5:00 PM"},
# }
#
# select = """
# 1) Book ticket
# 2) Cancel ticket
# """
#
#
# def book_ticket(flight):
#     if flight["Seats"] <= 0:
#         print("Sorry, no available seats on this flight.")
#         return False
#
#     flight["Seats"] -= 1
#     print(f"Your Ticket price is {flight['Price']}")
#     print(f"Your Ticket has been booked with {flight['Airline']}")
#     print(f"Departure Time: {flight['Departure']}")
#     print(f"Arrival Time: {flight['Arrival']}")
#     return True
#
#
# def cancel_ticket(flight):
#     flight["Seats"] += 1
#     print(f"Your Ticket has been cancelled.")
#     return True
#
#
# def quit_program():
#     print("Thank you")
#     print("Visit again")
#     exit()
#
#
# while True:
#     print(choice)
#     user_choice = int(input("Enter the choice:"))
#
#     flight = None
#
#     if user_choice == 1:
#         for key, details in Domestic_choices.items():
#             print(
#                 f"{key}) {details['Airline']} - Rs:{details['Price']} - Seats available: {details['Seats']} - Dep: {details['Departure']} - Arr: {details['Arrival']}")
#         user_choiceD = int(input("Enter the choice:"))
#         flight = Domestic_choices.get(user_choiceD)
#
#     elif user_choice == 2:
#         for key, details in International_choices.items():
#             print(
#                 f"{key}) {details['Airline']} - Rs:{details['Price']} - Seats available: {details['Seats']} - Dep: {details['Departure']} - Arr: {details['Arrival']}")
#         user_choiceI = int(input("Enter the choice:"))
#         flight = International_choices.get(user_choiceI)
#
#     elif user_choice == 3:
#         quit_program()
#
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")
#         continue
#
#     if flight is None:
#         print("Invalid flight selection. Please try again.")
#         continue
#
#     print(select)
#     user_select = int(input("Please select the option:"))
#
#     if user_select == 1:
#         book_ticket(flight)
#     elif user_select == 2:
#         cancel_ticket(flight)
#     else:
#         print("Invalid choice. Please select 1 or 2.")


# choice = """
# 1) Domestic
# 2) International
# 3) Quit
# """
# Total_amount = 10000
#
# # Define flight details for Domestic
# Domestic_choices = {
#     1: {"Airline": "Air India Express", "Price": 7000, "Seats": 10, "Departure": "10:00 AM", "Arrival": "12:00 PM"},
#     2: {"Airline": "IndiGo", "Price": 5000, "Seats": 20, "Departure": "1:00 PM", "Arrival": "3:00 PM"},
#     3: {"Airline": "SpiceJet", "Price": 3500, "Seats": 15, "Departure": "5:00 PM", "Arrival": "7:00 PM"},
# }
#
# # Define flight details for International
# International_choices = {
#     1: {"Airline": "Malaysia Airlines", "Price": 15000, "Seats": 8, "Departure": "6:00 AM", "Arrival": "12:00 PM"},
#     2: {"Airline": "Etihad Airways", "Price": 20000, "Seats": 12, "Departure": "8:00 AM", "Arrival": "2:00 PM"},
#     3: {"Airline": "Emirates", "Price": 25000, "Seats": 5, "Departure": "11:00 AM", "Arrival": "5:00 PM"},
# }
#
# select = """
# 1) Book ticket
# 2) Cancel ticket
# """
#
#
# def book_ticket(flight, Total_amount):
#     if flight["Seats"] <= 0:
#         print("Sorry, no available seats on this flight.")
#         return Total_amount
#     if flight["Price"] > Total_amount:
#         print("Insufficient funds")
#         return Total_amount
#
#     Total_amount -= flight["Price"]
#     flight["Seats"] -= 1
#     print(f"Your Ticket price is {flight['Price']}")
#     print(f"Your Ticket has been booked with {flight['Airline']}")
#     print(f"Departure Time: {flight['Departure']}")
#     print(f"Arrival Time: {flight['Arrival']}")
#     print(f"Remaining Balance: {Total_amount}")
#     return Total_amount
#
#
# def cancel_ticket(flight, Total_amount):
#     Total_amount += flight["Price"]
#     flight["Seats"] += 1
#     print(f"Your Balance money is {Total_amount}")
#     print(f"Your Ticket has been cancelled and your money has been refunded")
#     return Total_amount
#
#
# def quit_program():
#     print("Thank you")
#     print("Visit again")
#     exit()
#
#
# while True:
#     print(choice)
#     user_choice = int(input("Enter the choice:"))
#
#     flight = None
#
#     if user_choice == 1:
#         for key, details in Domestic_choices.items():
#             print(
#                 f"{key}) {details['Airline']} - Rs:{details['Price']} - Seats available: {details['Seats']} - Dep: {details['Departure']} - Arr: {details['Arrival']}")
#         user_choiceD = int(input("Enter the choice:"))
#         flight = Domestic_choices.get(user_choiceD)
#
#     elif user_choice == 2:
#         for key, details in International_choices.items():
#             print(
#                 f"{key}) {details['Airline']} - Rs:{details['Price']} - Seats available: {details['Seats']} - Dep: {details['Departure']} - Arr: {details['Arrival']}")
#         user_choiceI = int(input("Enter the choice:"))
#         flight = International_choices.get(user_choiceI)
#
#     elif user_choice == 3:
#         quit_program()
#
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")
#         continue
#
#     if flight is None:
#         print("Invalid flight selection. Please try again.")
#         continue
#
#     print(select)
#     user_select = int(input("Please select the option:"))
#
#     if user_select == 1:
#         Total_amount = book_ticket(flight, Total_amount)
#     elif user_select == 2:
#         Total_amount = cancel_ticket(flight, Total_amount)
#     else:
#         print("Invalid choice. Please select 1 or 2.")
