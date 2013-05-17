from Controller.actions import *

"""TODO: check game state to see if we're inside a level,
		 no current dialog box, etc etc"""
def handleInput(player):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN: handleKeyDown(player, event)
		elif event.type == pygame.KEYUP: handleKeyUp(player, event)

def handleKeyDown(player, event):
	if event.key == pygame.K_LEFT:
		moveLeft(player)
	elif event.key == pygame.K_RIGHT:
		moveRight(player)
	elif event.key == pygame.K_UP:
		jump(player)

def handleKeyUp(player, event):
	if event.key == pygame.K_LEFT:
		stopLeftMove(player)
	elif event.key == pygame.K_RIGHT:
		stopRightMove(player)
	elif event.key == pygame.K_UP:
		stopJump(player)