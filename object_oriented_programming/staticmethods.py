import datetime

my_date = datetime.date(2016, 7, 10)

# Instance methods affect just that instance
# class methods affect all instances of a class
# static methods don't automatically take self OR cls as a parameter. They behave just like regular functions, just attached to a particualr class.

class Employee:

	# This variable defined before the init is known as a class variable. The instances themselves don't have this attribute, so it checks the next level up, which is the variables for the entire class.
	raise_amount = 1.04
	num_of_emps = 0 # declared as a class variable bc we cant think of a case where we would want the total number of workers to be different between instances.
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

		Employee.num_of_emps += 1 # increments the class variable. Prefixed with the class name so that it knows we aren't looking for a variable within the mapping of that particular instance.

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) # could also do Employee.raise_amount. That would then be applied to every member of the class not just that particular instance
 

	@classmethod # adding this decorator is all you need to do to specify that it applies/uses variables that are part of the class and not just an instance.
	def set_raise_amt(cls, amount): # used cls instead of class because class is a reserved word.
		cls.raise_amount = amount

	@classmethod # this now allows us to take strings and instatiate our class without having the users need to write a parser themselves.
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



print(Employee.is_workday(my_date))









