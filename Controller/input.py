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
	ret = handleKeyDown(player, pygame.key.get_pressed(), level)
	doMovement(player,level)
	if not level.is_onscreen(level.map_to_arr(player.rect.midtop)):
		return True
	return ret

def handleKeyDown(player, key, level):
	if key[pygame.K_LEFT]:
		moveLeft(player, level)
	if key[pygame.K_RIGHT]:
		moveRight(player, level)
	if key[pygame.K_UP]:
		jump(player, level)
	if key[pygame.K_r]:
		return True
	if key[pygame.K_ESCAPE]:
		sys.exit()

def handleKeyUp(player, event):
	if event.key == pygame.K_LEFT:
		stopMoveLeft(player)
	elif event.key == pygame.K_RIGHT:
		stopMoveRight(player)
	elif event.key == pygame.K_UP:
		stopJump(player)