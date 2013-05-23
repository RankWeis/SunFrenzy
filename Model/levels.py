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

import pygame, math
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
		self.curr_lvl = self.get_level1()
		self.curr_lvl_str = level1

		# Time since last refresh
		self.tickseconds = 0

	def level_ingestor(self, level):
		self.blocks = [ None for x in range(len(level) * len(level[0]))]
		self.blocks_rep = [[ 0 for y in range(len(level[0]))] for x in range(len(level))]
		i = 0
		for y in range(len(level)):
			for x in range(len(level[y])):
				curr_blk = self.char_to_ent( level1[y][x], x, y)
				self.blocks_rep[y][x] = curr_blk
				self.blocks[i] = curr_blk
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
		if entity_char == 'W' or entity_char == 'G' or entity_char == 'B' or entity_char == 'I' or entity_char == 'F':
			block = None
			if entity_char == 'I':
				block = InvisibleBlock(rect)
			elif entity_char == 'F':
				block = Ice(rect)
				self.final_block = block
			else:
				block = SolidBlock(rect)
			return block
		elif entity_char == 'S':
			## Not the right way to do it, but I want to test ##
			rect = pygame.Rect( x * blockSizeX, y  * blockSizeY, blockSizeX, blockSizeY)
			self.player = Player( rect)
			try:
				self.movers.append(self.player)
			except AttributeError:
				self.movers = [self.player]
			return Air( rect)
		elif entity_char == 'E':
			# Only one enemy right now, but should develop a system to determine type
			rect = pygame.Rect( x * blockSizeX, y * blockSizeY + blockSizeY/2 + 1, blockSizeX/2, blockSizeY/2)
			enemy = Fire(rect,(50,0))
			try:
				self.movers.append(enemy)
			except AttributeError:
				self.movers = [enemy]
			return Air(rect)
		else:
			return Air( rect)

	def get_level1(self):
		return self.level_ingestor(level1)

	def map_to_arr(self, xypos):
		xRet = int(math.floor((xypos[0]) / blockSizeX))
		yRet = int((math.floor((xypos[1])) / blockSizeY))
		return (xRet, yRet)

	def get_bottom_blocks(self, rect):
		bottomright = (rect.bottomright[0] - 2, rect.bottomright[1] + 2)
		bottomleft = (rect.bottomleft[0] + 2, rect.bottomleft[1] + 2)
		return self.get_blocks((rect.midbottom,bottomright,bottomleft))

	def get_left_blocks(self, rect):
		topleft = (rect.topleft[0] - 2,rect.topleft[1] + 2)
		bottomleft = (rect.bottomleft[0] - 2, rect.bottomleft[1] - 2)
		return self.get_blocks((rect.midleft, bottomleft, topleft))

	def get_right_blocks(self, rect):
		topright = (rect.topright[0] + 2,rect.topright[1] + 2)
		bottomright = (rect.bottomright[0] + 2, rect.bottomright[1] - 2)
		return self.get_blocks((rect.midright, bottomright, topright))

	def get_upper_blocks(self, rect):
		topright = (rect.topright[0] - 2, rect.topright[1] + 2)
		topleft = (rect.topleft[0] + 2, rect.topleft[1] + 2)
		return self.get_blocks((rect.midtop,topright,topleft))


	def get_blocks(self, check_blocks):
		curr_locs = []
		for pos in check_blocks:
			if not pos: continue
			arr_loc = self.map_to_arr(pos)
			if not arr_loc in curr_locs:
				curr_locs.append(arr_loc)
		ret = []
		for item in curr_locs:
			if not self.is_onscreen(item):
				continue
			blk = self.blocks_rep[item[1]][item[0]]
			if not isinstance(blk,Player):
				ret.append(blk)
		return ret

	def get_sprites(self):
		lvl = list(self.curr_lvl)
		for mover in self.movers:
			if mover not in lvl:
				lvl.append(mover)
		return lvl


	def is_onscreen(self, loc):
		if loc[1] >= 0 and loc[1] < len(self.curr_lvl_str):
			if loc[0] >= 0 and loc[0] < len(self.curr_lvl_str[0]):
				return True
		return False

	def has_enemies(self):
		for ent in self.movers:
			if isinstance(ent,Enemy):
				return True
		return False

	def notify_all(self):
		for entity in self.get_sprites():
			entity.notify(self)

	def won_level(self):
		return self.player.rect.colliderect(self.final_block.rect)

