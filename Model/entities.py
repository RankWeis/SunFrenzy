from Model.attributes import *
import logging, time

class Entity(object):

	def __init__(self, rect):
		self.rect = rect
		self.destroy_on_collide = False
		self.is_visible = True
		self.attributes = Attributes()

	def notify(self, level):
		pass

	def getrect(self):
		return self.rect

	def on_collisionY(self,level,move_amt,collideblk):
		if move_amt < 0:
			self.rect.top = collideblk.rect.bottom - 1
			# Bounce back with some force
			# Maybe this can be a property set by the block?
			# i.e. bumpers in pinball
			self.ySpeed = -2
		else:
			self.rect.bottom = collideblk.rect.top + 1

	def on_collisionX(self,level,moveamt,collideblk):
		if move_amt < 0:
			self.rect.left = collideblk.rect.right - 1
		else:
			self.rect.right = collideblk.rect.left + 1

	def got_hit(self,level,attacker):
		pass

	def hit(self,level,defender):
		pass

	def moveY(self, distance, level):
		self.rect = self.rect.move(0,distance)

	def moveX(self, distance, level):
		self.direction = self.xSpeed
		self.rect = self.rect.move(distance,0)


"""
The base for characters.
"""

class Character(Entity):

	def __init__(self, rect):
		self.total_hp = 10
		self.hp = 10
		self.xSpeed = 0
		self.ySpeed = 0
		self.jumping=False
		self.direction = 1
		self.lastShot = 0
		self.weapon = Gun(self) # Temporary, eventually want to find first gun maybe?
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
	def __init__(self, rect, starting_movement, path, damage=1):
		Character.__init__(self, rect)
		self.total_hp = 8
		self.hp = self.total_hp
		self.xSpeed = starting_movement[0]
		self.ySpeed = starting_movement[1]
		self.path = path
		self.damage = damage

	def on_collisionX(self,level,moveamt,collideblk):
		if self.path == "unobstructed" or self.path == "repeat":
			self.xSpeed = -self.xSpeed

	def hit(self, level, defender):
		if isinstance(defender,Player):
			defender.hp -= attacker.damage

class Fire(Enemy):

	def __init__(self,rect,starting_movement,path="repeat"):
		Enemy.__init__(self, rect,starting_movement,path)

class Player(Character):
	def __init__(self, rect):
		Character.__init__(self, rect)
		self.total_hp = 10
		self.xdiff = 0

	def getrect(self):
		return self.rect.move(self.xdiff,0)

	def on_collisionX(self,level,moveamt,collideblk):
		if collideblk == level.final_block:
			level.won_lvl = True

	def on_collisionY(self,level,moveamt,collideblk):
		if collideblk == level.final_block:
			level.won_lvl = True
		Character.on_collisionY(self,level,moveamt,collideblk)

	def moveX(self,distance,level):
		self.direction = distance
		self.xdiff += distance

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

class InvisibleBlock(SolidBlock):

	def __init__(self,rect):
		SolidBlock.__init__(self,rect)
		self.is_visible = False
		self.permeable = True

	def is_permeable(self):
		return self.permeable

	def is_deadly(self):
		return False

	def notify(self,level):
		if not level.has_enemies():
			self.is_visible = True
			self.permeable = False

class Air(Block):

	def is_permeable(self):
		return True

	def is_deadly(self):
		return False

class Ice(SolidBlock):
	pass

class Lava(Block):

	def is_permeable(self):
		return True

	def is_deadly(self):
		return True

"""End of Blocks"""



from Model.weapons import *


