import sys, pygame
from Controller.input import *
from Model.entities import *
from Model.MyLogger import *

logger = logging.getLogger("Game")
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
logger.addHandler(ch)


logger.debug("Start")

pygame.init()

size = width, height = 1000, 300
speed = [0, 0]
black = 0, 0, 0

gravity = .1
jumpAccel = 0;

screen = pygame.display.set_mode(size)

playerImage = pygame.image.load("../resources/images/snowman.bmp").convert()
playerRect = playerImage.get_rect()

playerRect.top = 0;
playerRect.bottom = height;

player = Player(playerRect)

logger.debug("Begin while loop")
while True:
	logger.debug("Check gravity")

	if player.rect.bottom < height:
		"""Add gravity"""
		player.ySpeed += gravity
		if player.ySpeed < .1 and player.ySpeed > -.1: player.ySpeed = 1
		print(player.ySpeed)


	logger.debug("Handle input")
	logger.info("Speed1: " + str([player.xSpeed, player.ySpeed]))
	handleInput(player, [], pygame.event.get())
	

	"""for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT: speed[0] = -2
			elif event.key == pygame.K_RIGHT: speed[0] = 2
			elif event.key == pygame.K_UP and ballrect.bottom == height: 
				speed[1] = -5
		elif event.type == pygame.KEYUP: 
			if event.key == pygame.K_LEFT and speed[0] < 0:
				speed[0] = 0
			if event.key == pygame.K_RIGHT and speed[0] > 0:
				speed[0] = 0
			elif event.key == pygame.K_UP and speed[1] < 0:
				speed[1] = 0"""
	logger.debug("Moving player")
	logger.info("Rect1: " + str(player.rect))
	logger.error("Speed: " + str([player.xSpeed, player.ySpeed]))
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
	screen.blit(playerImage, player.rect)
	pygame.display.flip()
