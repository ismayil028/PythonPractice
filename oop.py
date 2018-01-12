class Employee():

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
     	return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)

   # def __str__(self):
     #	return '{} - {}'.format(self.fullname() , self.email)
     
    def __add__(self , other):
     	return self.pay + other.pay

emp_1 = Employee('Ismayil', 'Ismayilov', 100000)
emp_2 = Employee('Aslan', 'Ismayilov', 99999)
 
print(emp_1)
print(emp_1 + emp_2)