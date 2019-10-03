

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
 

	@classmethod # adding this attribute is all you need to do to specify that it applies/uses variables that are part of the class and not just an instance.
	def set_raise_amt(cls, amount): # used cls instead of class because class is a reserved word.
		cls.raise_amount = amount

	@classmethod # this now allows us to take strings and instatiate our class without having the users need to write a parser themselves.
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)


	# you can actually run these methods from an instance but that's kind of unorthodox and generally not accepted.
empstring1 = 'John-Doe-70000'
empstring2 = 'Mary-Does-80000'
empstring3 = 'Steve-Smite-90000'

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

#Employee.set_raise_amt(1.05)

emp_3 = Employee.from_string(empstring1)
print(emp_3.email)

#print(Employee.num_of_emps)

#print(emp_1.__dict__) # turns out that this instance is just a mapping of keys to values in a dictionary.
#print(Employee.__dict__) # the Employee class contains the variable for the raise_amount that gets applied to every instance of that class. But if you modify one instance, that won't affect other instances.

#Employee.raise_amount = 1.05 # creates a change across every instance of the class.
#emp_1.raise_amount = 1.06 # Creates a change only across the specified instance. More importantly, it CREATES this as an attribute to that instance of the employee class. There is a mapping in it's own dictionary now, which is searched first.

'''
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''


# These are equivalent.
'''
print(emp_1.fullname())
print(Employee.fullname(emp_1))
'''







