def isOnGround(character, blocks):
	if not blocks:
		# Not ideal, but makes it work.
		# Shouldn't never be a case when there's no blocks...except in test
		print("With no blocks I can flyyyyyy")
		return True
	for block in blocks:
		print("Character bottom: {0}\nBlock Top: {1}".format(character.rect.top - character.rect.height, block.rect.top))
		print("Block Type: " + str(type(block)))
		if character.rect.top - character.rect.height != block.rect.top: 
			continue
		else:
			return True
		# if character.rect.left > block.rect.left and character.rect.left < block.rect.right:
		# 	return True
		# elif character.rect.right > block.rect.left and character.rect.right > block.rect.right:
		# 	return True

	return False

def addGravity(characters):
	for character in characters:
		if not isOnGround(character, blocks):
			character.ySpeed += gravity
