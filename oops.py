#ENCAPSULATION
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner #public attribute
#         self._balance = balance #private attribute
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount #updating the hidden field
#         else:
#             print("Amt should be +ve")
#     def withdraw(self, amount):
#         if 0 < amount <=self._balance:
#             self._balance -= amount
#         else:
#             print("Insufficient Funds")
#     def get_balance(self):
#         return self._balance

# acc = BankAccount("Purnima", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print(acc.get_balance())

#INHERITANCE

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name,age, emp_id,designation):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.designation = designation
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.emp_id}, Designation: {self.designation}")

emp = Employee("Purnima", 22, "E123", "Python Developer")
emp.display_info()


        