from Model.entities import *
import os, sys

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


def get_sprite(entity):
	entity_class = type(entity)
	if entity_class == Player:
		return get_player_sprite(entity)
	if entity_class == SolidBlock:
		return get_block_sprite(entity)
	if entity_class == SunSpot:
		return get_sunspot_sprite(entity)
	if entity_class == Lava:
		return get_lava_sprite(entity)

def get_player_sprite(entity):
	return os.path.join(imagesLocation,playerFile)

def get_block_sprite(entity):
	return os.path.join(imagesLocation,blockFile)

def get_sunspot_sprite(entity):
	return os.path.join(imagesLocation,sunspotFile)

def get_lava_sprite(entity):
	return os.path.join(imagesLocation,lavaFile)