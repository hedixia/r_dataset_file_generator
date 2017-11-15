"""
tdt is a two dimensional table.

"""
from collections import OrderedDict

class tdt:
	def __init__(self):
		self.label_1 = OrderedDict()
		self.label_2 = OrderedDict()
		self.table = {}
		
	def get(self, x_1, x_2, null_return=None):
		try:
			return self.table [(x_1,x_2)]
		except KeyError:
			return null_return 
		
	def update(self, source):
		self.delete(source[0], source[1])
		try:
			self.label_1 [source[0]] += 1
		except KeyError:
			self.label_1 [source[0]] = 1
		try:
			self.label_2 [source[1]] += 1
		except KeyError:
			self.label_2 [source[1]] = 1
		self.table [source[:2]] = source[2]

	def delete(self, x_1, x_2):
		try:
			self.table.pop((x_1,x_2))
		except KeyError:
			return 
		self.label_1 [x_1] -= 1
		self.label_2 [x_2] -= 1
		if self.label_1 [x_1] == 0:
			self.label_1.pop (x_1)
		if self.label_1 [x_2] == 0:
			self.lable_2.pop (x_2)
		
	def to_list(self, null_return=None):
		return [[self.get(i, j, null_return) for i in self.label_1] for j in self.label_2]
		
	def show(self):
		for j in self.label_2:
			print([self.get(i, j, null_return) for i in self.label_1])
