from utils import Int

class Memory(object):

	def __init__(self, reg_count):
		self.FLAGS = 0
		self.remainder = 0
		self.registers = [Int(0) for i in range(reg_count)]
		self.heap = []
		self.stack = []

	def push_stack(self, i):
		self.stack.append(int(i))

	def pop_stack(self):
		ret = self.stack.pop()
		return ret