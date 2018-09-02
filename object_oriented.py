

class employee:
	# class variables
	#raise_amount = 1.05
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first +'.' + last +'@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amount)
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount
        
    #def raise(self):
    #	self.pay = int(self.pay * self.raise_amount)


employee.set_raise_amt(1.05)
emp1 = employee('Corey', 'schafer', '30000')
print(emp1.first, emp1.last, emp1.pay, emp1.raise_amount)