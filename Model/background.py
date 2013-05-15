"""
The base for backgrounds. Backgrounds can be

-- implemented --
blocks - used for walls, platforms

--to implement--
lava - if you touch it, you diiiiiie

"""

class Background(object):

	def __init__(self, x, y):
		self.xPos = x
		self.yPos = y


	
	def get_pos(self):
		"""Gets the x,y pair that makes the position"""
		return (self.xPos,self.yPos)

class Block(Background):

	def is_permeable(self):
		return False

	def is_deadly(self):
		return False

class Lava(Background):

	def is_permeable(self):
		return True

	def is_deadly(self):
		return True