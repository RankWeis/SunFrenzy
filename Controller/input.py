from Controller.actions import *
import sys, pygame

"""TODO: check game state to see if we're inside a level,
		 no current dialog box, etc etc"""
def handleInput(player, events, level):
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYUP:
			handleKeyUp(player, event)
	handleKeyDown(player, pygame.key.get_pressed(), level)

def handleKeyDown(player, key, level):
	if key[pygame.K_LEFT]:
		moveLeft(player, level)
	if key[pygame.K_RIGHT]:
		moveRight(player, level)
	if key[pygame.K_UP]:
		jump(player, level)

def handleKeyUp(player, event):
	if event.key == pygame.K_LEFT:
		stopMoveLeft(player)
	elif event.key == pygame.K_RIGHT:
		stopMoveRight(player)
	elif event.key == pygame.K_UP:
		stopJump(player)