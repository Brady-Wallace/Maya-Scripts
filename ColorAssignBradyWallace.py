import maya.cmds as cmds

def ColorAssign(colorValue):
    maya_select_lyst = cmds.ls(selection = True)
    for i in range(len(maya_select_lyst)):
        print(maya_select_lyst[i])
        cmds.setAttr(maya_select_lyst[i] + ".overrideEnabled", 1)
        cmds.setAttr(maya_select_lyst[i] + ".overrideColor", colorValue)
ColorAssign(9)

