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
	move_amt = round(entity.xSpeed * level.tickseconds)
	blocks = None
	future_rect = entity.getrect().move(move_amt,0)
	if move_amt > 0:
		blocks = level.get_right_blocks(future_rect)
	elif move_amt < 0:
		blocks = level.get_left_blocks(future_rect)
	else: return
	
	### Do non collision based future calculations ###

	if isinstance(entity,Enemy):
		if entity.path == "repeat":
			if not isOnGround(future_rect, level):
				entity.xSpeed = -entity.xSpeed
				return
	### Do collision based future calculations ###
	collision = collision_detected(future_rect, blocks)
	if collision:
		entity.on_collisionX(level,move_amt,collision)
	else:
		entity.moveX(move_amt,level)

def moveY(entity,level):
	move_amt = round(entity.ySpeed * level.tickseconds)
	blocks = None
	future_rect = entity.getrect().move(0, move_amt)
	if move_amt > 0:
		blocks = level.get_bottom_blocks(future_rect)
	elif move_amt < 0:
		blocks = level.get_upper_blocks(future_rect)
	else: return

	collision = collision_detected(future_rect, blocks)
	if collision:
		entity.on_collisionY(level,move_amt,collision)
	else:
		entity.moveY(move_amt,level)

def shoot(entity, level):
	if entity.weapon:
		bullet =  entity.weapon.fire()
		if bullet:
			level.movers.append( bullet)

def doMovement(entity,level):		
	moveY(entity,level)
	moveX(entity,level)


def jump(entity, level):
	if isOnGround(entity.getrect(), level):
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

def switch_weapons(player,key):
	if key[pygame.K_1]:
		player.weapon = Gun(player)
	if key[pygame.K_2]:
		player.weapon = Gun(player,Bullet)
	if key[pygame.K_3]:
		player.weapon = Gun(player,Exploder)
	if key[pygame.K_4]:
		player.weapon = Gun(player,Missile)
	if key[pygame.K_5]:
		player.weapon = Gun(player,RubberBall)
	if key[pygame.K_6]:
		player.weapon = LaserCannon(player)