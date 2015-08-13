from boids import *

vel = (2,4)
pos = (5,2)
sp = 10
dir = (3, 4)

myboid = boids(vel, pos, sp, dir)
secondboid = boids((3,4),(4,1),20,(5,6))
print("Firstboid Info")
myboid.printInfo()
print("\n")
print("Secondboid Info")
secondboid.printInfo()