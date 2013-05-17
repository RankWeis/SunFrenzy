def isOnGround(character, blocks):
	for block in blocks:
		if character.bottom != block.bottom: continue

		if character.left > block.left and character.left < block.right:
			return true
		elif character.right > block.left and character.right > block.right:
			return true

	return false

def addGravity(characters):
	for character in characters:
		if !isOnGround(character, blocks):
			character.ySpeed += gravity
