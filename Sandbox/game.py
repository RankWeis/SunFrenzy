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

	addGravity([player], level.curr_lvl, level)


	logger.debug("Handle input")
	logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
	handleInput(player, level.blocks, pygame.event.get(), level)
	logger.debug("Moving player")
	logger.info("Rect1: " + str(player.rect))
	# logger.error("Speed: " + str([player.xSpeed, player.ySpeed]))

	# collide = player.rect.collidelistall(level.collidable_blocks)
	# if (collide): 
	# 	player.ySpeed = 0
	player.rect = player.rect.move([player.xSpeed, player.ySpeed])

	logger.debug("Draw")
	screen.fill(black)
	screen_writer.drawLevel()
	pygame.display.flip()

