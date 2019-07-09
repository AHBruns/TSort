import uuid


class Node:
	def __init__(self, children, parents, content):
		self.children = children
		self.parents = parents
		self.content = content
		self.mark = False
		self.uuid = uuid.uuid4().hex

	def __str__(self):
		return self.uuid

	def __repr__(self):
		return self.__str__()
