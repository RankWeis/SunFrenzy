"""
The base for characters
"""

class Character(object):

	def __init__(self, rect):
		self.total_hp = 1
		self.hp = 1
		self.xSpeed = 1
		self.ySpeed = 1
		self.top = rect.top
		self.bottom = rect.bottom
		self.left = rect.left
		self.right = rect.right

	def get_hp(self):
		return self.hp

	def get_total_hp(self):
		return self.total_hp

	def get_xSpeed(self):
		return self.xSpeed

	def get_ySpeed(self):
		return self.ySpeed


class Enemy(Character):
	def __init__(position):
		super(position)
		self.total_hp = 8

class SunSupot(Enemy):
	def __init__(position):
		super(position)

class Player(Character):
	def __init__(position):
		super(position)
		self.total_hp = 10
		self.xSpeed = 2


