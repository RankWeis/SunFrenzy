from Model.entities import *
from Controller.physics import *

"""TODO: I'm figuring the main game controller is going to look at entity
         speeds and decide whether to set them to 0 if they've hit a wall
         or the ground, but I'm not really sure. Something to consider
         moving forward"""
def moveLeft(entity, level):
	entity.xSpeed = -entity.attributes[X_SPEED]
	
def moveRight(entity, level):
	entity.xSpeed = entity.attributes[X_SPEED]

def moveX(entity,level):
	move_amt = entity.xSpeed
	blocks = None
	if move_amt > 0:
		blocks = level.get_right_blocks(entity.rect)
	elif move_amt < 0:
		blocks = level.get_left_blocks(entity.rect)
	else: return
	future_rect = entity.rect.copy().move(move_amt,0)
	collision = collision_detected(future_rect, blocks)
	if collision:
		if move_amt < 0:
			entity.rect.left = collision.rect.right - 1
		else:
			entity.rect.right = collision.rect.left + 1
	else:
		entity.xSpeed = move_amt
		entity.rect = future_rect

def moveY(entity,level):
	move_amt = entity.ySpeed
	blocks = None
	if move_amt > 0:
		blocks = level.get_bottom_blocks(entity.rect)
	elif move_amt < 0:
		blocks = level.get_upper_blocks(entity.rect)
	else: return
	future_rect = entity.rect.copy().move(0, move_amt)
	collision = collision_detected(future_rect, blocks)
	if collision:
		if move_amt < 0:
			entity.rect.top = collision.rect.bottom - 1
			# Bounce back with some force
			# Maybe this can be a property set by the block?
			# i.e. bumpers in pinball
			entity.ySpeed = 2
		else:
			entity.rect.bottom = collision.rect.top + 1
	else:
		entity.rect = future_rect

def doMovement(entity,level):
	moveX(entity,level)
	moveY(entity,level)


def jump(entity, level):
	if isOnGround(entity, level):
		entity.ySpeed = -entity.attributes[Y_SPEED]
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