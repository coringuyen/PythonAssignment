class boids:
	def __init__(self, velocity, position, speed, direction):
		self.vel  = velocity
		self.pos  = position
		self.sp   = speed
		self.dirc = direction
	def printVel(self):
		return self.vel
	def printPos():
		print(self.pos)
	def printSp():
		print(self.sp)
	def printDirc():
		print(self.dirc)

myboids = boids(1,2,3,4)
myboids.printVel(myboids.vel)