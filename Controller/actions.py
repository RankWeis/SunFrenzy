from Model.entities import *
from Controller.physics import *
import pygame

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
	### Do non collision based future calculations ###

	if isinstance(entity,Enemy):
		if entity.path == "repeat":
			if not isOnGround(future_rect, level):
				entity.xSpeed = -entity.xSpeed
				return


	### Do collision based future calculations ###
	collision = collision_detected(future_rect, blocks)
	if collision:
		if entity.destroy_on_collide:
			level.movers.remove(entity)
			return
		if isinstance(entity,Enemy):
			if entity.path == "unobstructed" or entity.path == "repeat":
				entity.xSpeed = -entity.xSpeed
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
	## There's gonna be way too much shit in this if, gotta find a better way to handle this ##
	if collision:
		if entity.destroy_on_collide:
			level.movers.remove(entity)
			return
		if move_amt < 0:
			entity.rect.top = collision.rect.bottom - 1
			# Bounce back with some force
			# Maybe this can be a property set by the block?
			# i.e. bumpers in pinball
			entity.ySpeed = -entity.ySpeed * .8
		else:
			entity.rect.bottom = collision.rect.top + 1
	else:
		entity.rect = future_rect

def shoot(entity, level):
	bulletXY = pygame.Rect(entity.rect.x+2,entity.rect.y + 10, 5, 5)
	level.movers.append( Bullet(bulletXY, (10,0)))

def doMovement(entity,level):
	moveX(entity,level)
	moveY(entity,level)


def jump(entity, level):
	if isOnGround(entity.rect, level):
		entity.ySpeed = entity.ySpeed + -entity.attributes[Y_SPEED]
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