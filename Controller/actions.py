from Model.entities import *
from Controller.physics import *

"""TODO: I'm figuring the main game controller is going to look at entity
         speeds and decide whether to set them to 0 if they've hit a wall
         or the ground, but I'm not really sure. Something to consider
         moving forward"""
def moveLeft(entity, level):
	return moveX(entity, level, -1, level.get_left_blocks(entity.rect))
	#Works if you tap left key but not if you hold
	

def moveRight(entity, level):
	return moveX(entity, level, 1, level.get_right_blocks(entity.rect))

def moveX(entity,level,direction,blocks):
	move_amt = entity.attributes[X_SPEED] * direction
	future_rect = entity.rect.copy().move(move_amt,0)
	collision = collision_detected(future_rect, blocks)
	if collision:
		if direction < 0:
			entity.rect.left = collision.rect.right
		else:
			entity.rect.right = collision.rect.left
	else:
		entity.xSpeed = move_amt
		entity.rect = entity.rect.move(move_amt, 0)

def moveY(entity,level,direction, blocks, move_amt=None):
	if not move_amt:
		move_amt = (entity.attributes[Y_SPEED] * direction)
	future_rect = entity.rect.copy().move(0, move_amt)
	collision = collision_detected(future_rect, blocks)
	if collision:
		if direction < 0:
			entity.rect.top = collision.rect.bottom
		else:
			entity.rect.bottom = collision.rect.top
	else:
		entity.ySpeed = move_amt
		entity.rect = entity.rect.move(0, move_amt)

def doMovement(entity):
	entity.rect = entity.rect.move(entity.xSpeed,entity.ySpeed)


def jump(entity, level):
	if isOnGround(entity, level):
		moveY(entity, level, -1, level.get_upper_blocks(entity.rect))
		if isinstance(entity,Character):
			entity.jumping = True

def stopMoveLeft(entity):
	if entity.xSpeed < 0:
		entity.xSpeed = 0

def stopMoveRight(entity):
	if entity.xSpeed > 0:
		entity.xSpeed =0

def stopJump(entity):
	if entity.ySpeed < 0:
		if isinstance(entity,Character):
			entity.jumping = False
		entity.ySpeed = 0

def will_collideX(player, future_rect, level):
	if collision_detected(future_rect, level.get_right_blocks(player.rect)):
		return 1

def will_collideY(player, future_rect, level):
	if collision_detected(future_rect, level.get_upper_blocks(player.rect)):
		return 1
	return False