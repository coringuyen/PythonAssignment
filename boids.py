
class boids:
	def __init__(self, velocity, position, speed, direction):
		self.vel  = velocity
		self.pos  = position
		self.sp   = speed
		self.dirc = direction
		
	def printVel(self):
		return self.vel
	def printPos(self):
		return self.pos
	def printSp(self):
		return self.sp
	def printDirc(self):
		return self.dirc

