# tpl=()
# print(tpl)
#
# tpl=(1,2,3)
# print(tpl)
#
# # tpl=(1,2,3,4,5)
# # print(tpl[-])
# tpl=(1,2,3,4)
# print(tpl[-1])
#
# tpl=(1,2,3,4,(10,5,7),5)
# # # print(tpl[4][2])
# # tpl[5][1]=6
# # print(tpl)
#
# tpl=(1,2,3,4[10,5,7],6)
# tpl[4][1]=6
# print(tpl)
# my_data = (1, [9, 8, 7], "World")
# print(my_data)
# # changing the element of the list
# # this is valid because list is mutable
# my_data[1][2] = 99
# print(my_data)
#
# tupa=(2,)
# class mathematics:
#     import math
#     def _init_(self):
#         pass
#     def math_info(self):
#         print("mathematics is the study of numbers and how they are related to each other and to the real world!!")

# class algebra(mathematics):
#     def _init_(self):
#         pass
#     def alge_info(self):
#         print("""
# Algebra is a branch of mathematics that uses mathematical statements to describe relationships between things that vary.""")
#
# class traingle(algebra):
#     def _init_(self,base,height):
#         self.base = int(base)
#         self.height = int(height)
#     def values(self):
#         print("""
# area of rectangle is""",self.base * self.height)
#         return "Thank you"
# val = traingle(4,6)
# val.math_info()
# val.alge_info()
# print(val.values())
# def compute_hcf(x, y):
#     while (y):
#         x, y = y, x % y
#     return x
#
#
# def compute_lcm(x, y):
#     hcf = compute_hcf(x, y)
#     lcm = (x * y) // hcf
#     return lcm
#
#
# def multilevel_program():
#     print("Welcome to the HCF and LCM Calculator!")
#     while True:
#         print("\nPlease select an option:")
#         print("1. Calculate HCF")
#         print("2. Calculate LCM")
#         print("3. Exit")
#
#         choice = input("Enter your choice (1/2/3): ")
#
#         if choice == '1':
#             num1 = int(input("Enter the first number: "))
#             num2 = int(input("Enter the second number: "))
#             print(f"The HCF of {num1} and {num2} is: {compute_hcf(num1, num2)}")
#
#         elif choice == '2':
#             num1 = int(input("Enter the first number: "))
#             num2 = int(input("Enter the second number: "))
#             print(f"The LCM of {num1} and {num2} is: {compute_lcm(num1, num2)}")
#
#         elif choice == '3':
#             print("Exiting the program. Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
#
# # Run the multilevel program
# multilevel_program()
# # class MultiLevelMath:
# #     def __init__(self, num1, num2):
# #         self.num1 = num1
#         self.num2 = num2
#
#     def calculate_hcf(self):
#
#         x, y = self.num1, self.num2
#         while y:
#             x, y = y, x % y
#         return x
#
#     def calculate_lcm(self):
#
#         hcf = self.calculate_hcf()
#         return abs(self.num1 * self.num2)
#
# if __name__ == "__main__":
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#
#     math_obj = MultiLevelMath(num1, num2)
#
#     hcf = math_obj.calculate_hcf()
#     lcm = math_obj.calculate_lcm()
#
#     print(f"The HCF of {num1} and {num2} is: {hcf}")
#     print(f"The LCM of {num1} and {num2} is: {lcm}")


# Define the Patient class
class Patient:
    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.appointments = []

    # Method to display patient information
    def display_patient_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Medical History: {', '.join(self.medical_history)}")

    # Method to add an appointment
    def add_appointment(self, doctor, date):
        appointment = {'Doctor': doctor.name, 'Specialization': doctor.specialization, 'Date': date}
        self.appointments.append(appointment)
        print(f"Appointment scheduled with Dr. {doctor.name} on {date}.")

    # Method to display all appointments
    def display_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print(f"Appointments for {self.name}:")
            for appointment in self.appointments:
                print(
                    f"Doctor: {appointment['Doctor']}, Specialization: {appointment['Specialization']}, Date: {appointment['Date']}")


# Define the Doctor class
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    # Method to schedule an appointment with a patient
    def schedule_appointment(self, patient, date):
        patient.add_appointment(self, date)


# Example usage:

# Create a patient
patient1 = Patient("Jane Doe", 45, ["Hypertension", "Asthma"])

# Create a doctor
doctor1 = Doctor("Dr. Emily Clark", "Pulmonology")

# Display patient info
patient1.display_patient_info()

# Doctor schedules an appointment with the patient
doctor1.schedule_appointment(patient1, "2024-10-01")

# Display patient appointments
patient1.display_appointments()




































