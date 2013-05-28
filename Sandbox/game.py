import sys, pygame
from Controller.input import *
from Controller.physics import *
from Model.entities import *
from Model.levels import *
from View.ScreenWriter import *
import time

logger = logging.getLogger("Game")
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.WARN)
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

	while True:
		milliseconds = clock.tick(60)
		level.tickseconds = milliseconds / 1000.0
		addGravity(level.movers, level)

		logger.debug("Handling input")
		if not first:
			if handleInput(player, pygame.event.get(), level):
				break
		first = False

		logger.debug("Moving Entities")
		for entity in level.movers:
			doMovement(entity,level)

		logger.debug("Resolving Collisions")
		movers_collisions(level)

		logger.debug("Updating Level")
		level.notify_all()

		logger.debug("Checking if won")
		if level.won_level():
			print("WINNER!!")
			myfont = pygame.font.SysFont("Times", 30)
			label = myfont.render("You won!", 1, (255,0,0))
			screen_writer.drawLevel(level)
			screen.blit(label, (100,100))
			pygame.display.flip()
			time.sleep(3)
			break
		if level.lost():
			myfont = pygame.font.SysFont("Times", 30)
			label = myfont.render("You lost!", 1, (255,0,0))
			screen_writer.drawLevel(level)
			screen.blit(label, (100,100))
			pygame.display.flip()
			time.sleep(1)
			break



		logger.debug("Draw")
		screen.fill(black)
		screen_writer.drawLevel(level)
		pygame.display.flip()

