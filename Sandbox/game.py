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

# So basically, jump sets a ySpeed and calls moveY()
# But only gets called when you're on the ground and jumping
# Which means that through the jump arc, you're not getting moveY() called
# And moveY is what does the collision detection
# Right now gravity is just setting the rect stupidly (no collision detection) based on the ySpeed
# If gravity could use moveY, that would be a simple fix, I don't know why there's
# dependency issues, but it's not working. 
# That's not the right way to do it though


# Right way is to have goLeft, goRight (in actions.py) just set the xSpeed/ySpeed
# The input handler (input.py I mean) should, after going through and updating all the speeds
# call a function (regardless of whether a key is pressed, so after handleKeyDown is called)
# And update the sprites based on those values.
# That's heavy refactoring of that bit of code.

# Also I'm breaking the game in hopes you read this, just uncomment the next line
# while True:
	clock.tick(50)

	addGravity([player], level)


	logger.debug("Handle input")
	logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
	handleInput(player, pygame.event.get(), level)
	logger.debug("Moving player")
	logger.info("Rect1: " + str(player.rect))

	logger.debug("Draw")
	screen.fill(black)
	screen_writer.drawLevel()
	pygame.display.flip()

