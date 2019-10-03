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


class Developer(Employee): # Employ is going to walk up the chain of inheritence until it finds what it needs.
	raise_amount = 1.10 # It will prioritize these values in the subclasses, and take the value from there. If one wasn't provided, it would have gone to Employee looking for it, then Python.

	# copying the init method from the parent class and then adding additional parameters allows your class to take on more attributes than the parent class.
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) # it's better that we just leave this stuff in the Employee class' court, our super class. It makes maintaining all this easier and is less writing for us.
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->' + emp.fullname())


dev_1 = Developer('Corey','Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')


# print(dev_1.email)
# #dev_1.apply_raise()
# print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.remove_emp(dev_2)
print(mgr_1.print_emps())
print(mgr_1.email)

#print(isinstance(inst, cls)) returns a boolean letting you know if inst is a instance of whatever cls you specify. issubclass is also a thing.
