import sys, pygame
pygame.init()

size = width, height = 1000, 300
speed = [0, 0]
black = 0, 0, 0

gravity = -.1

screen = pygame.display.set_mode(size)

ball = pygame.image.load("snowman.bmp")
ballrect = ball.get_rect()

ballrect.top = 0;
ballrect.bottom = height;

while 1:
	speed[1] = speed[1] - gravity

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT: speed[0] = -2
			elif event.key == pygame.K_RIGHT: speed[0] = 2
			elif event.key == pygame.K_UP: 
				if ballrect.bottom >= height: speed[1] = -5
		elif event.type == pygame.KEYUP: 
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				speed[0] = 0

	ballrect = ballrect.move(speed)
	

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = 0
	if ballrect.bottom > height:
		speed[1] = 0
		ballrect.top = 0;
		ballrect.bottom = height;
	if ballrect.top < 0:
		speed[1] = 0;

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
