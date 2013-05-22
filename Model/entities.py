from Model.attributes import *
import logging

class Entity(object):

	def __init__(self, rect):
		self.rect = rect
		self.destroy_on_collide = False
		self.attributes = Attributes()

"""
The base for characters
"""

class Character(Entity):

	def __init__(self, rect):
		self.total_hp = 1
		self.hp = 1
		self.xSpeed = 0
		self.ySpeed = 0
		self.jumping=False
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
		# Path should be something like back and forth (repeat), unobstructed, follow player (follow), shoot player (shoot)
	def __init__(self, rect, starting_movement, path):
		Character.__init__(self, rect)
		self.total_hp = 8
		self.xSpeed = starting_movement[0]
		self.ySpeed = starting_movement[1]
		self.path = path

class Fire(Enemy):

	def __init__(self,rect,starting_movement,path="repeat"):
		Enemy.__init__(self, rect,starting_movement,path)

class Player(Character):
	def __init__(self, rect):
		Character.__init__(self, rect)
		self.total_hp = 10

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
		self.aboveBlock = None
		self.belowBlock = None
		self.leftBlock = None
		self.rightBlock = None

class SolidBlock(Block):

	def is_permeable(self):
		return False

	def is_deadly(self):
		return False

class Air(Block):

	def is_permeable(self):
		return True

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
	def __init__(self, rect, speed,damage=1):
		Entity.__init__(self, rect)
		self.xSpeed = speed[0]
		self.ySpeed = speed[1]
		self.destroy_on_collide = True
		self.damage = damage
