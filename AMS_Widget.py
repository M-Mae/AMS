# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
import AMS_MAIN_ui
from types import *
import maya.cmds as cmds
import sys
sys.path.append('D:/Student Data/Documents/AMS')
import _AMS_FetchDB_Data
from AMS_ListModel import ListModel as ListModel


class AMS_Widget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        #call the widget constructor
        super(AMS_Widget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = AMS_MAIN_ui.Ui_Form()
        self.ui.setupUi(self)

        self.dataModel = ListModel()
        self.ui.listView.setModel(self.dataModel)

        #Perhaps here we might add check for favorites and display in the results to start.

        #if the field is changed, check that against the database. For now we'll print some test strings
        @QtCore.Slot(name='searchChanged')
        def searchChanged ():

            #cache local copy of search term
            searchTerm = self.ui.lineEdit.text()

            #search the database with the search term and update the list view
            self.dataModel.dataTable = self.dataModel.updateData(searchTerm)
            self.ui.listView.setModel(self.dataModel)
            self.ui.listView.reset()



        #connecting slots
        self.ui.lineEdit.textChanged.connect(searchChanged)



