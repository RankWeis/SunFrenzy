import sys, pygame
from Controller.input import *
from Controller.physics import *
from Model.entities import *
from Model.levels import *
from View.ScreenWriter import *

logger = logging.getLogger("Game")
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
logger.addHandler(ch)


logger.debug("Start")

pygame.init()

size = width, height = 1000, 300
speed = [0, 0]
lastSpeed = 0
black = 0, 0, 0

gravity = .1
jumpAccel = 0;

level = Level()
screen_writer = ScreenWriter( level)
screen = screen_writer.screen
player = level.player
playerRect = player.rect
clock = pygame.time.Clock()

while True:
	clock.tick(50)

	addGravity([player], level)


	logger.debug("Handle input")
	logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
	handleInput(player, pygame.event.get(), level)
	logger.debug("Moving player")
	logger.info("Rect1: " + str(player.rect))
	# logger.error("Speed: " + str([player.xSpeed, player.ySpeed]))

	"""
	Below should go in the controller, but I'm just messing around to see if it works
	"""
	# collide = player.rect.collidelistall(level.collidable_blocks)
	# if (collide): 
	# 	player.ySpeed = 0
	temp_rectX = player.rect.copy().move([player.xSpeed, 0])
	temp_rectY = player.rect.copy().move([0,player.ySpeed])
	xSpeed = 0
	ySpeed = 0
	xCollide = will_collideX(player, temp_rectX, level)
	yCollide = will_collideY(player, temp_rectY, level)
	


	if xCollide:
		if (xCollide > 0 and player.xSpeed < 0) or (xCollide < 0 and player.xSpeed > 0):
			xSpeed = player.xSpeed
	else:
		xSpeed = player.xSpeed
	if player.ySpeed > 0 or not yCollide:
		ySpeed = player.ySpeed
	"""
	End controller bit
	"""

	player.rect = player.rect.move(xSpeed,ySpeed)

	logger.debug("Draw")
	screen.fill(black)
	screen_writer.drawLevel()
	pygame.display.flip()

