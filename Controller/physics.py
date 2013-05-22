from Model.entities import *

#TODO: This module NEEDS to use pygame collision detection because if
#      the player speed takes them past the top of a block, for example,
#	   it won't work. There's a hack in game.py that fixes this right now

def isOnGround(rect, level):
	blocks = level.get_bottom_blocks( rect)
	return collision_detected(rect, blocks)

def addGravity(characters, level):
	gravity = 5
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

# Resolve all collisions by the movers in the level
# Shouldn't be in physics though...
# Types of collisions currently possible:
# Projectile vs character
# Projectile vs Enemy
# character vs Enemy
# character vs projectile
# enemy vs projectile
# enemy vs character
# enemy vs enemy
def movers_collisions(level):
	movers = list(level.movers)
	for attacker in movers:
		for defender in movers:
			if attacker == defender or not isinstance(defender,Character): continue
			if attacker.rect.colliderect(defender.rect):
				if isinstance(attacker,Projectile):
					if isinstance(defender,Enemy):
						defender.hp -= attacker.damage
				if isinstance(attacker,Enemy):
					if isinstance(defender,Player):
						defender.hp -= attacker.damage
			if defender.hp <= 0 and defender in level.movers:
				level.movers.remove(defender)
