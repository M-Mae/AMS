# -*- coding: utf-8 -*-
#all Qt and maya stuff
from PySide2 import QtCore, QtWidgets, QtGui
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#import our widget to run
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/AssetManager')
from AMS_Widget import AMS_Widget as CoreWidget


def deleteControl(control):
    if cmds.workspaceControl(control, q=True, exists=True):
        cmds.workspaceControl(control,e=True, close=True)
        cmds.deleteUI(control,control=True)

class dockableAMSWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(dockableAMSWidget, self).__init__(parent=parent)
        #set the name and title of the widget
        self.setObjectName('dockableAMSWidget')
        self.setWindowTitle('Database Asset Search')
        self.setLayout(self.createLayout())

    #create a widget and lay it out vertically
    def createLayout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.central_widget = CoreWidget(parent=self)
        self.main_layout.addWidget(self.central_widget)
        return self.main_layout


def makeCoreWidgetMain():
    #delete any pre-existing widget before making a new one
    deleteControl("dockableAMSWidgetWorkspaceControl")
    Core = dockableAMSWidget()
    print("Got inside make widget")

    #configure and show the new widget
    Core.show(dockable=True, floating=False, area="right", allowedArea="right")
    cmds.workspaceControl("dockableAMSWidgetWorkspaceControl", e=True , ttc=["AttributeEditor", 0], wp="preferred", mw=420)
    #bring to the front
    Core.raise_()


