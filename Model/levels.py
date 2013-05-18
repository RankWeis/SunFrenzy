"""
Eventually need to create some sort of level editor.
For simplicity, array string of nxm size can be used.
W = wall
G = ground (could be wall I guess)
B = Block, could be more descriptive later
I = invisible block, somehow need to feed in conditions, but for now can be on all enemies killed
E = Enemy
S = Starting Position
"""
"""
level1 - First level is not side scrolling, to get things up and running. 

For this level, I am assuming we can jump two x blocks, sprint 5.
"""

import pygame
from Model.entities import *

blockSizeX = 40
blockSizeY = 40

level1 = [
"WWWWWWWWWWWWWWWWWWWWWW",
"W                    W",
"W                    W",
"W F   E              W",
"W  BBBBB   II   BB   W",
"W                    W",
"W                  BBW",
"W  S                 W",
"WGGGGGG  GGG     GGGGW",
"WGGGGGG  GGG     GGGGW",
"WGGGGGG  GGG     GGGGW"
]

class Level(object):

	def __init__(self):
		self.collidable_blocks = None
		self.curr_lvl = self.get_level1()

	def level_ingestor(self, level):
		self.blocks = [ None for x in range(len(level) * len(level[0]))]
		i = 0
		for y in range(len(level)):
			for x in range(len(level[y])):
				self.blocks[i] = self.char_to_ent( level1[y][x], x, y)
				if x != 0:
					self.blocks[i].leftBlock = self.blocks[i-1]
					self.blocks[i-1].rightBlock = self.blocks[i]
				if y != 0:
					self.blocks[i].aboveBlock = self.blocks[i-len(level[y])]
					self.blocks[i-len(level[y])].belowBlock = self.blocks[i]
				i += 1
		return self.blocks


	def char_to_ent(self, entity_char, x, y ):
		rect = pygame.Rect( x * blockSizeX, y * blockSizeY, blockSizeX, blockSizeY )
		if entity_char == 'W' or entity_char == 'G' or entity_char == 'B':
			block = SolidBlock(rect)
			if not self.collidable_blocks:
				self.collidable_blocks = [block]
			else:
				self.collidable_blocks.append(block)
			return block
		elif entity_char == 'S':
			## Not the right way to do it, but I want to test ##
			rect = pygame.Rect( x * blockSizeX, (y - 1) * blockSizeY, blockSizeX, blockSizeY)
			self.player = Player( rect)
			print("Player Rect is " + str(rect))
			return self.player
		else:
			return Air( rect)

	def get_level1(self):
		return self.level_ingestor(level1)