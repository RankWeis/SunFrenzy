
from Model import entities
from pygame import display

class ScreenWriter(object):
	
	SIZE = width, height = 1000, 300
	BLACK = 0, 0, 0

	images = { }

	def __init__(self):
		loadImages()

	def drawScreen(entityDict):
		screen = display.set_mode(SIZE)
		screen.fill(BLACK)

		"""Entities is a dict of arrays of characters/blocks,
			ordered by z index"""
		for i in range(5):
			entityList = entityDict[i]
			for entity in entityList:
				screen.blit(images[entity.imageFile], entity.getRect())

		display.flip()


	def loadImages():
		"""load block images"""
		for entity in entities:
			images[block.imageFile] = pygame.image.load(entity.imageFile).convert()