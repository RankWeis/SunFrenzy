import os, sys
from Model.entities import *
import unittest
from sprite_mapper import *
import pygame

class BasicSpriteMapTest(unittest.TestCase):

	def setUp(self):
		self.player = Player(pygame.Rect(9,10,11,12))

	def test_player(self):
		sprite = get_sprite(self.player)
		try:
			pygame.image.load( sprite )
		except:
			print("Could not find image: " + sprite)



if __name__ == '__main__':
	unittest.main()