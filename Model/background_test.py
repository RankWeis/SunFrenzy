from entities import Background, Block
import unittest

class BasicBlockTest(unittest.TestCase):

	def setUp(self):
		self.block = Block(1,8)
		self.enemy = Enemy(1,9)
		self.player = Player(1,10)

	def test_perm(self):
		self.assertFalse(self.block.is_permeable())

	def test_pos(self):
		(xPos,yPos) = self.block.get_pos()
		self.assertEqual(xPos,1)
		self.assertEqual(yPos,8)

	def test_deadly(self):
		self.assertFalse(self.block.is_deadly())


if __name__ == '__main__':
	unittest.main()