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


while True:
	level = Level()
	screen_writer = ScreenWriter( level)
	screen = screen_writer.screen
	player = level.player
	playerRect = player.rect
	clock = pygame.time.Clock()
	black = 0,0,0
	first = True
	print("Here")

	while True:
		clock.tick(50)

		addGravity([player], level)


		logger.debug("Handle input")
		logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
		if not first:
			if handleInput(player, pygame.event.get(), level):
				break
		first = False
		logger.debug("Moving player")
		logger.info("Rect1: " + str(player.rect))

		logger.debug("Draw")
		screen.fill(black)
		screen_writer.drawLevel()
		pygame.display.flip()

