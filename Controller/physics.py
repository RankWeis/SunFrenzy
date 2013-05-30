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
		if attacker not in level.movers: continue
		if not level.is_onscreenY(level.map_to_arr(attacker.rect)) and not attacker == level.player:
		 	level.movers.remove(attacker)
		 	continue
		for defender in movers:
			if defender not in level.movers or attacker not in level.movers: continue
			if attacker == defender or not isinstance(defender,Character): continue
			rect = defender.rect
			if defender == level.player:
				rect = defender.rect.move(defender.xdiff,0)
			if attacker.rect.colliderect(rect):
				attacker.hit(level,defender)
				defender.got_hit(level,attacker)
			if defender.hp <= 0 and defender in level.movers:
				level.movers.remove(defender)
