import uuid
from functools import reduce
import re


class Node:
	def __init__(self, children, parents, content):
		self.children = children
		self.parents = parents
		self.content = self.margin(content)
		self.mark = False
		self.uuid = uuid.uuid4().hex

	@staticmethod
	def margin(content):
		# SOURCE:
		#  - http://programmaticallyspeaking.com/split-on-separator-but-keep
		#    -the-separator-in-python.html
		def splitkeepsep(s, sep):
			return reduce(lambda acc, elem: acc[:-1] + [
				acc[-1] + elem] if elem == sep else acc + [elem],
				re.split("(%s)" % re.escape(sep), s), [])
		out = "\n".join(content)
		out = out.strip("\n")
		out = splitkeepsep(out, "\n")
		out[-1] += "\n\n"
		return out

	def __str__(self):
		return self.uuid

	def __repr__(self):
		return self.__str__()
