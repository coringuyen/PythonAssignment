
class boids:
	def __init__(self, velocity, position, speed, direction):
		self.vel  = velocity
		self.pos  = position
		self.sp   = speed
		self.dirc = direction
		
	def printInfo(self):
		print 'Velocity: ' , self.vel
		print 'Position: ' , self.pos
		print 'Speed: '    , self.sp
		print 'Direction: ', self.dirc


