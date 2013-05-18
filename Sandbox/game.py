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

logger.debug("Begin while loop")
while True:
	clock.tick(50)
	logger.debug("Check gravity")

	print("blah " + str(level.curr_lvl))
	addGravity([player], level.curr_lvl)


	logger.debug("Handle input")
	logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
	handleInput(player, level.blocks, pygame.event.get())
	logger.debug("Moving player")
	logger.info("Rect1: " + str(player.rect))
	# logger.error("Speed: " + str([player.xSpeed, player.ySpeed]))

	#get list of collidable blocks
	collidableBlocks = []
	i = 0
	for block in level.curr_lvl:
		print ("current block: " + str(type(block)))
		if (not isinstance(block, Player)) and block.is_permeable() == False:
			print "hahaha"
			collidableBlocks.append(block)
			i += 1
	print ("collides: " + str(collidableBlocks))
	collide = player.rect.collidelistall(collidableBlocks)
	if (collide): player.ySpeed = 0
	player.rect = player.rect.move([player.xSpeed, player.ySpeed])

	logger.debug("Draw")
	screen.fill(black)
	screen_writer.drawLevel()
	pygame.display.flip()

