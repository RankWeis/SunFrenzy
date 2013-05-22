from Model.entities import *

#TODO: This module NEEDS to use pygame collision detection because if
#      the player speed takes them past the top of a block, for example,
#	   it won't work. There's a hack in game.py that fixes this right now

def isOnGround(rect, level):
	blocks = level.get_bottom_blocks( rect)
	return collision_detected(rect, blocks)

def addGravity(characters, level):
	gravity = .1
	for character in characters:
		if not isOnGround(character.rect, level):
			character.ySpeed += gravity
		else:
			character.ySpeed = 0

def collision_detected(rect, blocks):
	for block in blocks:
		if (isinstance(block, Player)): 
			continue
		if not block.is_permeable() and rect.colliderect(block):
			return block
	return False