import maya.cmds as cmds

#Create Body
moveAmount = 0
for i in range(10):
    cmds.polySphere()
    moveAmount += 0.75
    cmds. move(0, 0, moveAmount)

#Create Legs
moveAmount = 0
for i in range(9):
    cmds.polyCylinder()
    cmds.scale(0.2, 0.5, 0.2)
    cmds.rotate(0, 0, 13.819547)
    moveAmount += 0.75
    cmds. move(0.5, -1.25, moveAmount)
    cmds.polyMirrorFace()

#Create nose
cmds.polySphere()
cmds.move(0, 0, 8.524412)
cmds.scale(0.394222, 0.394222, 0.394222)

#Create eyes
cmds.polySphere()
cmds.move(0.50, 0.50, 8)
cmds.scale(0.2, 0.2, 0.2)
cmds.polyMirrorFace()

#Create tophat
cmds.polyCylinder()
cmds.move(0, 1.07, 7.5)
cmds.scale(0.6,0.1,0.6)
cmds.polyCylinder()
cmds.move(0, 1.5, 7.5)
cmds.scale(0.5,0.5,0.5)