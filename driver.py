from boids import *

vel = (2,4)
pos = (5,2)
sp = 10
dir = (3, 4)

myboid = boids(vel, pos, sp, dir)
print 'Velocity: ' , myboid.printVel()
print 'Position: ' ,myboid.printPos()
print 'Speed: '    ,myboid.printSp()
print 'Direction: ',myboid.printDirc()





