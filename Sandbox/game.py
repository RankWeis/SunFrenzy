import sys, pygame
from Controller.input import *
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

logger.debug("Begin while loop")
while True:
	clock.tick(50)
	logger.debug("Check gravity")

	if player.rect.bottom < height:
		"""Add gravity"""
		player.ySpeed += gravity
		if player.ySpeed < .1 and player.ySpeed > -.1: 
			player.ySpeed = 1
		print("Y-speed: " + str(player.ySpeed))


	logger.debug("Handle input")
	logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
	handleInput(player, level.blocks, pygame.event.get())
	logger.debug("Moving player")
	logger.info("Rect1: " + str(player.rect))
	# logger.error("Speed: " + str([player.xSpeed, player.ySpeed]))
	collide = player.rect.collidelistall(level.blocks)
	
	player.rect = player.rect.move([player.xSpeed, player.ySpeed])

	logger.debug("Checking boundaries")
	if player.rect.left < 0 or player.rect.right > width:
		logger.info("Inside if")
		player.xSpeed = 0
	if player.rect.bottom > height:
	 	player.ySpeed = 0
	 	player.rect.top = 0;
	 	player.rect.bottom = height;

	logger.debug("Draw")
	screen.fill(black)
	screen_writer.drawLevel()
	pygame.display.flip()

