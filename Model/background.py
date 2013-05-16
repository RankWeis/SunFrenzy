"""
The base for backgrounds. Backgrounds can be

-- implemented --
blocks - used for walls, platforms

--to implement--
lava - if you touch it, you diiiiiie

"""

class Block(object):

	def __init__(self, rect):
		self.bottom = rect.bottom
		self.top = rect.top
		self.left = rect.left
		self.right = rect.right

class SolidBlock(Block):

	def is_permeable(self):
		return False

	def is_deadly(self):
		return False

class Lava(Block):

	def is_permeable(self):
		return True

	def is_deadly(self):
		return True