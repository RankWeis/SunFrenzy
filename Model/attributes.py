X_SPEED = "xSpeed"
Y_SPPED = "ySpeed"

class Attributes(PyDictObject):

	def __init__(self):
		self[X_SPEED] = 0
		self[Y_SPEED] = 0