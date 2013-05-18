from Model.entities import *
from Controller.physics import *

"""TODO: I'm figuring the main game controller is going to look at entity
         speeds and decide whether to set them to 0 if they've hit a wall
         or the ground, but I'm not really sure. Something to consider
         moving forward"""
def moveLeft(entity):
	entity.xSpeed = -entity.attributes[X_SPEED]

def moveRight(entity):
	entity.xSpeed = entity.attributes[X_SPEED]

def jump(entity, blocks, level):
	if isOnGround(entity, blocks, level):
		entity.ySpeed = -entity.attributes[Y_SPEED]
		if isinstance(entity,Character):
			print("Set Jump")
			entity.jumping = True
	else:
		print ("Is not on ground")

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