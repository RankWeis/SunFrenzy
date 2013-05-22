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

class SpriteMapper(object):

	def __init__(self):
		image = pygame.image.load( os.path.join(imagesLocation,blockFile))
		self.block_img = pygame.transform.scale( image, (40, 40))
		image = pygame.image.load( os.path.join(imagesLocation, playerFile))
		self.player_img = pygame.transform.scale( image, (40, 40))
		image = pygame.image.load( os.path.join(imagesLocation, bulletFile))
		self.bullet_img = pygame.transform.scale( image, (5,5))

	def get_sprite(self, entity):
		entity_class = type(entity)
		if entity_class == Player:
			return self.get_player_sprite(entity)
		if entity_class == SolidBlock:
			return self.get_block_sprite(entity)
		if entity_class == SunSpot:
			return self.get_sunspot_sprite(entity)
		if entity_class == Lava:
			return self.get_lava_sprite(entity)
		if entity_class == Bullet:
			return self.get_bullet_sprite(entity)

	def get_bullet_sprite(self, entity):
		return self.bullet_img

	def get_player_sprite(self, entity):
		return self.player_img

	def get_block_sprite(self, entity):
		return self.block_img

	def get_sunspot_sprite(self, entity):
		return os.path.join(imagesLocation,sunspotFile)

	def get_lava_sprite(self, entity):
		return os.path.join(imagesLocation,lavaFile)