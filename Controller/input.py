from Controller.actions import *
import sys, pygame

"""TODO: check game state to see if we're inside a level,
		 no current dialog box, etc etc"""
def handleInput(player, events, level):
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYUP:
			handleKeyUp(player, event, level)
	ret = handleKeyDown(player, pygame.key.get_pressed(), level)
	

def handleKeyDown(player, key, level):
	if key[pygame.K_LEFT]:
		moveLeft(player, level)
	if key[pygame.K_RIGHT]:
		moveRight(player, level)
	if key[pygame.K_UP]:
		jump(player, level)
	if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
		shoot(player, level)
	if key[pygame.K_r]:
		return True
	if key[pygame.K_1] or key[pygame.K_2] or key[pygame.K_3] or key[pygame.K_4] or key[pygame.K_5] or key[pygame.K_6]:
		switch_weapons(player,key)
	if key[pygame.K_ESCAPE]:
		sys.exit()

def handleKeyUp(player, event, level):
	if event.key == pygame.K_LEFT:
		stopMoveLeft(player)
	elif event.key == pygame.K_RIGHT:
		stopMoveRight(player)
	elif event.key == pygame.K_UP:
		stopJump(player)