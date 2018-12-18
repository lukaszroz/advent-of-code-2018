from re import match
from collections import Counter, defaultdict
from heapq import *

with open('input_08.txt') as f:
	ins = list(map(int, f.read().rstrip().split(" ")))

class Node:
	def __init__(self, child_n, meta_n):
		self.child_n = child_n
		self.meta_n = meta_n
		self.children = []
		self.meta = []

	def add_children(self, ins):
		for _ in range(self.child_n):
			ins = self.add_child(ins)
		return ins

	def add_child(self, ins):
		child = Node(ins[0], ins[1])
		ins = child.add_children(ins[2:])
		ins = child.add_metas(ins)
		self.children.append(child)
		return ins

	def add_metas(self, ins):
		for idx in range(self.meta_n):
			self.meta.append(ins[idx])
		return ins[self.meta_n:]

	def meta_sum(self):
		_sum = 0
		for m in self.meta:
			_sum += m
		for child in self.children:
			_sum += child.meta_sum()
		return _sum

	def value(self):
		if self.child_n < 1:
			return self.meta_sum()
		_sum = 0
		for m in self.meta:
			idx = m - 1
			if idx > -1 and idx < len(self.children):
				_sum += self.children[idx].value()
		return _sum


root = Node(ins[0], ins[1])
ins = root.add_children(ins[2:])
ins = root.add_metas(ins)

# print(root.child_n, root.meta_n)
# for child in root.children:
# 	print("\t", child.child_n, child.meta_n)
# 	for c2 in child.children:
# 		print("\t\t", c2.child_n, c2.meta_n)


print("Star 1:", root.meta_sum())
print("Star 2:", root.value())