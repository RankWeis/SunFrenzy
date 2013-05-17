class Entity(object):

	def __init__(self, rect):
		self.rect = rect
		self.top = rect.top
		self.bottom = rect.bottom
		self.left = rect.left
		self.right = rect.right
		self.attributes = Attributes()


"""
The base for characters
"""

class Character(Entity):

	def __init__(self, rect):
		self.total_hp = 1
		self.hp = 1
		self.xSpeed = 1
		self.ySpeed = 1
		Entity.__init__(self, rect)
		
	def get_hp(self):
		return self.hp

	def get_total_hp(self):
		return self.total_hp

	def get_xSpeed(self):
		return self.xSpeed

	def get_ySpeed(self):
		return self.ySpeed


class Enemy(Character):
	def __init__(self, rect):
		Character.__init__(self, rect)
		self.total_hp = 8

class SunSpot(Enemy):
	def __init__(self,rect):
		Enemy.__init__(self, rect)

class Player(Character):
	def __init__(self, rect):
		Character.__init__(self, rect)
		self.total_hp = 10
		self.xSpeed = 2

"""
The base for backgrounds. Backgrounds can be

-- implemented --
blocks - used for walls, platforms

--to implement--
lava - if you touch it, you diiiiiie

"""

class Block(Entity):

	def __init__(self, rect):
		Entity.__init__(self, rect)

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

"""End of Blocks"""

class Bullet(Entity):

	'''speed is a 2d array [x, y]'''
	def __init__(self, rect, speed):
		Entity.__init__(self, rect)
		self.speed = speed
