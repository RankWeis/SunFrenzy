from entities import *
from datetime import timedelta,datetime
import pygame, math

class Projectile(Entity):

	'''speed is a 2d array [x, y]'''
	def __init__(self, rect, speed, owner, damage=1):
		Entity.__init__(self, rect)
		self.xSpeed = speed[0]
		self.ySpeed = speed[1]
		self.destroy_on_collide = True
		self.totalMoved = [0,0]
		self.damage = damage
		self.owner = owner

	def on_collisionX(self,level,move_amt,collideblk):
		if self in level.movers:
			level.movers.remove(self)

	def on_collisionY(self,level,move_amt,collideblk):
		if self in level.movers:
			level.movers.remove(self)

	def get_total_moved(self):
		return math.sqrt(self.totalMoved[0]**2 + self.totalMoved[1]**2)

	def moveX(self, distance, level):
		self.totalMoved[0] += distance
		Entity.moveX(self, distance, level)

	def moveY(self, distance, level):
		self.totalMoved[1] += distance
		Entity.moveY(self, distance, level)

	def hit(self, level, defender):
		if isinstance(defender,Character):
			# No Friendly fire
			# if attacker.owner == defender:
			# 	continue
			defender.hp -= self.damage
			self.on_collisionX(level,0,defender)


class Snowball(Projectile):

	def __init__(self, rect, direction, owner):
		Projectile.__init__(self, rect, (250 * direction, 0), owner)

class Bullet(Projectile):

	def __init__(self, rect, direction, owner, speed=None):
		if not speed:
			speed = (1000 * direction, 0)
		Projectile.__init__(self, rect, speed, owner)

class Exploder(Projectile):

	def __init__(self, rect, direction, owner):
		Projectile.__init__(self, rect, (1000 * direction, 0), owner)

	def on_collisionX(self,level,move_amt,collideblk):
		intensity = 500
		num_bullets = 20
		if self in level.movers:
			for i in range(1,num_bullets):
				current_deg = 360.0 / num_bullets * i
				angle = math.radians(current_deg)
				y = math.sin(angle) * intensity
				x = math.cos(angle) * intensity
				bulletXY = pygame.Rect(self.getrect().x, self.rect.y, 5 ,5)
				cur = Bullet(bulletXY, x, self.owner, (x,y))
				level.movers.append(cur)
			level.movers.remove(self)

	def on_collisionY(self,level,move_amt,collideblk):
		self.on_collisionX(level,move_amt,collideblk)

class Missile(Projectile):

	def __init__(self, rect, direction, owner):
		Projectile.__init__(self, rect, (1000 * direction, 0), owner)

	def on_move(self,level):
		if self.get_total_moved() > 500:
			intensity = 500
			num_bullets = 20
			if self in level.movers:
				for i in range(1,num_bullets):
					current_deg = 360.0 / num_bullets * i
					angle = math.radians(current_deg)
					y = math.sin(angle) * intensity
					x = math.cos(angle) * intensity
					bulletXY = pygame.Rect(self.getrect().x, self.rect.y, 5 ,5)
					cur = Bullet(bulletXY, x, self.owner, (x,y))
					level.movers.append(cur)
				level.movers.remove(self)

	def moveX(self,distance,level):
		Projectile.moveX(self,distance,level)
		self.on_move(level)

	def moveY(self,distance,level):
		Projectile.moveY(self,distance,level)
		self.on_move(level)

class Laser(Projectile):
	def __init__(self,rect,direction,owner):
		Projectile.__init__(self, rect, (1000 * direction, 0), owner)

	def moveX(self, distance,level):
		self.direction = distance
		oldx = self.rect.x
		self.rect.inflate_ip(abs(distance),0)
		xDir = int( self.owner.direction / abs(self.owner.direction) )
		self.rect.right = self.owner.getrect().left - 2
		if xDir > 0:
			self.rect.left = self.owner.getrect().right + 2
		self.rect.y = self.owner.getrect().y

	def moveY(self, distance, level):
		pass

class RubberBall(Projectile):

	def __init__(self, rect, direction, owner):
		Projectile.__init__(self, rect, (1000 * direction, 0), owner)
		self.numcollisions = 0

	def on_collisionX(self,level,move_amt,collision):
		self.numcollisions += 1
		if self.xSpeed < .1 and self.ySpeed < .1:
			if self in level.movers:
				level.movers.remove(self)
		else:
			self.xSpeed = -self.xSpeed * .7
			self.ySpeed = -self.ySpeed * .5
		

class Weapon(object):
	def __init__(self,owner,recharge_speed, ammo_type=Snowball):
		self.owner = owner
		self.recharge_speed = timedelta(seconds=recharge_speed)
		self.ammo_type=ammo_type
		self.last_fired = datetime.min
		self.shotbullets = []

	def fire(self):
		time = datetime.now()
		if time - self.last_fired > self.recharge_speed:
			self.last_fired = time
			xDir = int( self.owner.direction / abs(self.owner.direction) )
			startX = self.owner.getrect().left - 2
			if xDir > 0:
				startX = self.owner.getrect().right + 2
			bulletXY = pygame.Rect(startX,self.owner.getrect().y + 10, 5, 5)
			return self.ammo_type(bulletXY, xDir, self.owner)
		else:
			return False

class Gun(Weapon):
	def __init__(self,owner,ammo_type=Snowball):
		Weapon.__init__(self,owner,.25,ammo_type)

class LaserCannon(Weapon):
	def __init__(self,owner):
		Weapon.__init__(self,owner,0,Laser)



#### START AMMO #####


