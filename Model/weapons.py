from entities import *
from datetime import timedelta,datetime
import pygame, math

class Projectile(Entity):

	'''speed is a 2d array [x, y]'''
	def __init__(self, rect, speed,damage=1):
		Entity.__init__(self, rect)
		self.xSpeed = speed[0]
		self.ySpeed = speed[1]
		self.destroy_on_collide = True
		self.totalMoved = [0,0]
		self.damage = damage

	def on_collision(self,level):
		if self in level.movers:
			level.movers.remove(self)

	def get_total_moved(self):
		return math.sqrt(self.totalMoved[0]**2 + self.totalMoved[1]**2)

	def on_move(self, xy, level):
		self.totalMoved = (self.totalMoved[0] + xy[0], self.totalMoved[1] + xy[1])

class Snowball(Projectile):

	def __init__(self, rect, direction):
		Projectile.__init__(self, rect, (250 * direction, 0))

class Bullet(Projectile):

	def __init__(self, rect, direction, speed=None):
		if not speed:
			speed = (1000 * direction, 0)
		Projectile.__init__(self, rect, speed)

class Exploder(Projectile):

	def __init__(self, rect, direction):
		Projectile.__init__(self, rect, (1000 * direction, 0))

	def on_collision(self,level):
		intensity = 500
		num_bullets = 20
		if self in level.movers:
			for i in range(1,num_bullets):
				current_deg = 360.0 / num_bullets * i
				angle = math.radians(current_deg)
				y = math.sin(angle) * intensity
				x = math.cos(angle) * intensity
				bulletXY = pygame.Rect(self.rect.x * (x / abs(x)), self.rect.y, 5 ,5)
				cur = Bullet(bulletXY, x, (x,y))
				level.movers.append(cur)
			level.movers.remove(self)

class Missile(Projectile):

	def __init__(self, rect, direction):
		Projectile.__init__(self, rect, (1000 * direction, 0))

	def on_move(self,xy,level):
		Projectile.on_move(self,xy,level)
		if self.get_total_moved() > 500:
			intensity = 500
			num_bullets = 20
			if self in level.movers:
				for i in range(1,num_bullets):
					current_deg = 360.0 / num_bullets * i
					angle = math.radians(current_deg)
					y = math.sin(angle) * intensity
					x = math.cos(angle) * intensity
					bulletXY = pygame.Rect(self.rect.x, self.rect.y, 5 ,5)
					cur = Bullet(bulletXY, x, (x,y))
					level.movers.append(cur)
				level.movers.remove(self)

class RubberBall(Projectile):

	def __init__(self, rect, direction):
		Projectile.__init__(self, rect, (1000 * direction, 0))
		self.numcollisions = 0

	def on_collision(self,level):
		self.numcollisions += 1
		print("Collisions",self.numcollisions)
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

	def fire(self):
		time = datetime.now()
		if time - self.last_fired > self.recharge_speed:
			self.last_fired = time
			xDir = int( self.owner.direction / abs(self.owner.direction) )
			startX = self.owner.rect.x
			if xDir > 0:
				startX = self.owner.rect.right
			bulletXY = pygame.Rect(self.owner.rect.x+2,self.owner.rect.y + 10, 5, 5)
			return self.ammo_type(bulletXY, xDir)
		else:
			return False


class Gun(Weapon):
	def __init__(self,owner,ammo_type=Snowball):
		Weapon.__init__(self,owner,.25,ammo_type)


#### START AMMO #####


