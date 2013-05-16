import sys, pygame
pygame.init()

size = width, height = 1000, 300
speed = [0, 0]
black = 0, 0, 0

gravity = .1
jumpAccel = 0;

screen = pygame.display.set_mode(size)

ball = pygame.image.load("snowman.bmp").convert()
ballrect = ball.get_rect()

ballrect.top = 0;
ballrect.bottom = height;

while True:
    
	if ballrect.bottom < height:
		"""Add gravity"""
		speed[1] += gravity
		if speed[1] < .1 and speed[1] > -.1: speed[1] = 1
		print speed[1]

	for event in pygame.event.get():
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
				speed[1] = 0

	ballrect = ballrect.move(speed)
	

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = 0
	if ballrect.bottom > height:
		speed[1] = 0
		ballrect.top = 0;
		ballrect.bottom = height;

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
