from Model.entities import *

#TODO: This module NEEDS to use pygame collision detection because if
#      the player speed takes them past the top of a block, for example,
#	   it won't work. There's a hack in game.py that fixes this right now

def isOnGround(character, blocks):
	if not blocks:
		# Not ideal, but makes it work.
		# Shouldn't never be a case when there's no blocks...except in test
		print("With no blocks I can flyyyyyy")
		return True
	for block in blocks:
		#skip player, because player is in the block array. I dont think
		#it should be but I don't want to fix that right now
		if (isinstance(block, Player)): continue
		
		#if Air is below player
		#BUG: can't jump when hanging over a pit, I think because technically
		#     an air block is below you, even though you're hanging over an
		#     edge
		if (block.rect.collidepoint(character.rect.center) or block.rect.colliderect(character.rect)) and block.is_permeable():
			if isinstance(block.belowBlock, Player) or  block.belowBlock.is_permeable():
				return False

		#if block.is_permeable():
		#	continue
		#else:
		#	if character.rect.colliderect(block.rect):
		#		return True
	return True

def addGravity(characters, blocks):
	gravity = .1
	for character in characters:
		if not isOnGround(character, blocks):
			character.ySpeed += gravity
		else:
			character.ySpeed = 0