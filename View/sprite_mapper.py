from Model.entities import *
import os, sys, pygame

"""
File should map an entity to a sprite.

Current entities are:
* Sunspot
* Player
* Solid Block
* Lava
"""

imagesLocation = "../resources/images"
blockFile="block.jpg"
sunspotFile="block.jpg"
playerFile="snowman.bmp"
lavaFile="lava.jpg"
bulletFile="bullet.png"
fireFile="fire.png"
iceFile="ice.png"
laserFile="laser.jpg"

class SpriteMapper(object):

	def __init__(self):
		image = pygame.image.load( os.path.join(imagesLocation,blockFile))
		self.block_img = pygame.transform.scale( image, (40, 40))
		self.invisible_block_img = self.block_img
		image = pygame.image.load( os.path.join(imagesLocation, playerFile))
		self.player_img = pygame.transform.scale( image, (40, 40))
		image = pygame.image.load( os.path.join(imagesLocation, bulletFile))
		self.bullet_img = pygame.transform.scale( image, (5,5))
		image = pygame.image.load( os.path.join(imagesLocation, fireFile))
		self.fire_img = pygame.transform.scale(image, (20,20))
		image = pygame.image.load( os.path.join(imagesLocation, iceFile))
		self.ice_img = pygame.transform.scale(image, (40,40))
		image = pygame.image.load( os.path.join(imagesLocation, laserFile))
		self.laser_img = pygame.transform.scale(image, (20,20))

	def get_sprite(self, entity):
		entity_class = type(entity)
		if entity_class == Player:
			return self.get_player_sprite(entity)
		if entity_class == SolidBlock or entity_class == InvisibleBlock:
			return self.get_block_sprite(entity)
		if entity_class == Lava:
			return self.get_lava_sprite(entity)
		if entity_class == Bullet:
			return self.get_bullet_sprite(entity)
		if entity_class == Fire:
			return self.get_fire_sprite(entity)
		if entity_class == Ice:
			return self.get_ice_sprite(entity)
		if entity_class == Exploder:
			return self.get_bullet_sprite(entity)
		if entity_class == Missile:
			return self.get_bullet_sprite(entity)
		if entity_class == Snowball:
			return self.get_bullet_sprite(entity)
		if entity_class == RubberBall:
			return self.get_bullet_sprite(entity)
		if entity_class == Laser:
			return self.get_laser_sprite(entity)



	def get_bullet_sprite(self, entity):
		return pygame.transform.scale(self.bullet_img,entity.rect.size)

	def get_laser_sprite(self, entity):
		return pygame.transform.scale(self.laser_img,entity.rect.size)

	def get_player_sprite(self, entity):
		return self.player_img

	def get_block_sprite(self, entity):
		return self.block_img

	def get_sunspot_sprite(self, entity):
		return os.path.join(imagesLocation,sunspotFile)

	def get_lava_sprite(self, entity):
		return os.path.join(imagesLocation,lavaFile)

	def get_fire_sprite(self,entity):
		return self.fire_img

	def get_ice_sprite(self,entity):
		return self.ice_img