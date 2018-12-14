# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
import AMS_MAIN_ui
from types import *
import maya.cmds as cmds
from os.path import join as join
import sys
sys.path.append('D:/Student Data/Documents/AMS')
import _AMS_FetchDB_Data
from AMS_ListModel import ListModel as ListModel
from _AMS_FetchDB_Data import fetch_QueryDB as fetch


class AMS_Widget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        #call the widget constructor
        super(AMS_Widget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = AMS_MAIN_ui.Ui_Form()
        self.ui.setupUi(self)

        self.dataModel = ListModel()
        self.ui.listView.setModel(self.dataModel)

        self.currentSelection = None

        #create our context menu object
        self.menu = QtWidgets.QMenu()
        #make and attach QActions to our Menu Object
        openAction = QtWidgets.QAction(u"Open", self.menu)
        importAction = QtWidgets.QAction(u"Import", self.menu)
        referenceAction = QtWidgets.QAction(u"Reference", self.menu)
        self.menu.addAction(openAction)
        self.menu.addAction(importAction)
        self.menu.addAction(referenceAction)


        @QtCore.Slot(name='searchChanged')
        def searchChanged ():

            #cache local copy of search term
            searchTerm = self.ui.lineEdit.text()

            #search the database with the search term and update the list view
            self.dataModel.dataTable = self.dataModel.updateData(searchTerm)
            self.ui.listView.setModel(self.dataModel)
            self.ui.listView.reset()

        #, QtCore.QModelIndex
        @QtCore.Slot(name='onItemClicked')
        def onItemClicked(index=QtCore.QModelIndex()):
            print("inside Click")
            print("selected item index: " + str(index.data()))
            self.currentSelection = str(index.data())
            pos = QtGui.QCursor.pos()
            self.menu.exec_(pos)

        @QtCore.Slot(name='OpenAction')
        def OpenAction():
            print("Opening: " + str(self.currentSelection))
            DB_item = fetch(self.currentSelection)
            item = DB_item[0]
            print("Database retrieval: " + str(item))
            finalFileP1 = join(item[6],item[1])
            finalFileP2 = ("." + str(item[5]))
            finalFile = (str(finalFileP1)+ str(finalFileP2))
            print(str(finalFile))
            cmds.file(finalFile, open = True, f=True)


        @QtCore.Slot(name='ImportAction')
        def ImportAction():
            print("Importing: " + str(self.currentSelection))
            DB_item = fetch(self.currentSelection)
            item = DB_item[0]
            print("Database retrieval: " + str(DB_item))
            finalFileP1 = join(item[6], item[1])
            finalFileP2 = ("." + str(item[5]))
            finalFile = (str(finalFileP1) + str(finalFileP2))
            print(str(finalFile))
            cmds.file(finalFile, i=True, f=True)


        @QtCore.Slot(name='RefAction')
        def RefAction():
            print("Referencing: " + str(self.currentSelection))
            DB_item = fetch(self.currentSelection)
            item = DB_item[0]
            print("Database retrieval: " + str(DB_item))
            finalFileP1 = join(item[6], item[1])
            finalFileP2 = ("." + str(item[5]))
            finalFile = (str(finalFileP1) + str(finalFileP2))
            print(str(finalFile))
            cmds.file(finalFile, reference = True, f=True)

        #connecting slots
        self.ui.lineEdit.textChanged.connect(searchChanged)
        self.ui.listView.clicked.connect(onItemClicked)
        #connecting context menu slots
        openAction.triggered.connect(OpenAction)
        importAction.triggered.connect(ImportAction)
        referenceAction.triggered.connect(RefAction)

