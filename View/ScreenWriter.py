from Model.entities import *
from Model.levels import *
from pygame import display
from View.sprite_mapper import *

class ScreenWriter(object):
	
	SIZE = width, height = 880, 440
	BLACK = 0, 0, 0

	images = { }

	def __init__(self, level):
		self.screen = display.set_mode(self.SIZE)
		self.mapper = SpriteMapper()
		self.level = level

	def drawScreen(self, entityDict):
		self.screen.fill(self.BLACK)
		player = self.level.player

		"""Entities is a dict of arrays of characters/blocks,
			ordered by z index"""
		for i in range(5):
			player = self.level.player
			entityList = entityDict[i]
			scroll = False
			if not entityList:
				continue
			for entity in entityList:
				image = self.mapper.get_sprite( entity)
				if not image or not entity.is_visible:
					continue
				#Scrolling level
				if (scroll):
					if not entity == player:
						self.screen.blit(image, entity.rect.move(player.xdiff * -1,0))
					else:
						self.screen.blit(image, entity.rect)
				else:
					self.screen.blit(image,entity.getrect())
		myfont = pygame.font.SysFont("Times", 30)
		label = myfont.render("HP: {0}/{1}".format(str(player.hp),str(player.total_hp)), 1, (255,0,0))
		self.screen.blit(label, (10,10))
		clock = pygame.time.Clock()

	def drawLevel(self, level):
		level1 = {0 : level.get_sprites(), 1:None, 2:None,3:None,4:None }
		self.drawScreen(level1)