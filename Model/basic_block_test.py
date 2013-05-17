import entities
import unittest
import pygame

class BasicBlockTest(unittest.TestCase):

	def setUp(self):
		self.block = SolidBlock(pygame.Rect(1,2,3,4))
		self.enemy = SunSpot(pygame.Rect(5,6,7,8))
		self.player = Player(pygame.Rect(9,10,11,12))

	def test_perm(self):
		self.assertFalse(self.block.is_permeable())

	def test_pos(self):
		rect = self.block.rect
		rect.left = 1
		rect.height = 4

	def test_deadly(self):
		self.assertFalse(self.block.is_deadly())


if __name__ == '__main__':
	unittest.main()