from Model.entities import *

#TODO: This module NEEDS to use pygame collision detection because if
#      the player speed takes them past the top of a block, for example,
#	   it won't work. There's a hack in game.py that fixes this right now

def isOnGround(rect, level):
	blocks = level.get_bottom_blocks( rect)
	return collision_detected(rect, blocks)

def addGravity(characters, level):
	gravity = 300
	for character in characters:
		rect = character.rect
		if character == level.player:
			rect = rect.move(character.xdiff,0)
		if not isOnGround(rect, level):
			character.ySpeed += gravity * level.tickseconds
		else:
			character.ySpeed = 0

def collision_detected(rect, blocks):
	if not blocks: return
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
		# if not level.is_onscreen(attacker.rect):
		# 	movers.remove(attacker)
		# 	continue
		for defender in movers:
			if attacker == defender or not isinstance(defender,Character): continue
			rect = defender.rect
			if defender == level.player:
				rect = defender.rect.move(defender.xdiff,0)
			if attacker.rect.colliderect(rect):
				if isinstance(attacker,Projectile):
					if isinstance(defender,Character):
						# No Friendly fire
						# if attacker.owner == defender:
						# 	continue
						defender.hp -= attacker.damage
						level.movers.remove(attacker)
				if isinstance(attacker,Enemy):
					if isinstance(defender,Player):
						defender.hp -= attacker.damage

			if defender.hp <= 0 and defender in level.movers:
				level.movers.remove(defender)
