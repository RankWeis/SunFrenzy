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
		print("Character bottom: {0}\nBlock Top: {1}".format(character.rect.bottom, block.rect.top))
		print("Block Type: " + str(type(block)))
		#skip player, because player is in the block array. I dont think
		#it should be but I don't want to fix that right now
		if (isinstance(block, Player)): continue
		if block.is_permeable() or character.rect.bottom != block.rect.top:
			print("continue")
			continue
		else:
			if (character.rect.left >= block.rect.left and character.rect.left <= block.rect.right) or (character.rect.right >= block.rect.left and character.rect.right <= block.rect.right):
				print("rettrue")
				return True
		# if character.rect.left > block.rect.left and character.rect.left < block.rect.right:
		# 	return True
		# elif character.rect.right > block.rect.left and character.rect.right > block.rect.right:
		# 	return True
	print("retfalse")
	return False

def addGravity(characters, blocks):
	gravity = .1
	for character in characters:
		if not isOnGround(character, blocks):
			character.ySpeed += gravity
		else:
			character.ySpeed = 0
