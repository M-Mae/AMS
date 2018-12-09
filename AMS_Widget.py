# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
import AMS_MainUI
from types import *
import maya.cmds as cmds
import sys
sys.path.append('D:/Student Data/Documents/AMS')
import _AMS_FetchDB_Data


class AMS_Widget(QtWidgets.QWidget):
    def __init__(self, parent = None, currentName=None):
        #call the widget constructor
        super(AMS_Widget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = AMS_MainUI.Ui_Form()
        self.ui.setupUi(self)

        #Perhaps here we might add check for favorites and display in the results to start.

        #if the feild is changed, check that against the database. For now we'll print some test strings
        @QtCore.Slot(name='searchChanged')
        def searchChanged ():
            #get local version of array to search from

            #cache local copy of search term
            searchTerm = self.ui.lineEdit.text()

            #search array and return results
            #DB_Array = _AMS_FetchDB_Data.fetchDB_AsArray()
            #print out just the names in that results box

            #right click context menu to reference, import, etc



            message = ["Testing", "123", "Hello", "World"]
            message.append(searchTerm)
            self.ui.textBrowser.setText('\n'.join(str(mess) for mess in message))
            if len(searchTerm) == 0:
                self.ui.textBrowser.clear()


        #connecting slots
        self.ui.lineEdit.textChanged.connect(searchChanged)



