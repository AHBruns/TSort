import uuid
from functools import reduce


class Bundle:
	def __init__(self, components: set):
		self.uuid = uuid.uuid4().hex
		self.components = components

	def parents(self):
		return reduce(
			lambda acc, e: acc | e.parents,
			self.components,
			set()
		) - self.components

	def children(self):
		return reduce(
			lambda acc, e: acc | e.children,
			self.components,
			set()
		) - self.components
