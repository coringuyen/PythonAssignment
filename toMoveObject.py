import maya.cmds as cmds
import random
cubelist = cmds.ls('myCube*') #to delete any object with the same name as myCube and the * is watever after it
if len( cubelist ) > 0:
    cmds.delete( cubelist )
    
result = cmds.polyCube(w=4, h=4, d=4, name='myCube@')

print 'Result ' + str(result)
transformName = result[0]

x = random.uniform(-6,6)
y = random.uniform(2,8)
z = random.uniform(-6,6)
cmds.move(x,y,z, transformName) # move to random place







