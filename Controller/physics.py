from Model.entities import *

#TODO: This module NEEDS to use pygame collision detection because if
#      the player speed takes them past the top of a block, for example,
#	   it won't work. There's a hack in game.py that fixes this right now

def isOnGround(character, blocks, level):
	blocks = level.get_bottom_blocks( character)
	for block in blocks:
		if (isinstance(block, Player)): 
			continue
		if not block.is_permeable() and character.rect.colliderect(block):
			return True
	return False

def addGravity(characters, blocks, level):
	gravity = .1
	for character in characters:
		if not isOnGround(character, blocks, level):
			character.ySpeed += gravity
		else:
			character.ySpeed = 0