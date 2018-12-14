from PySide2 import QtCore
import sqlite3

class ListModel (QtCore.QAbstractListModel):
    def __init__(self, parent = None):
        #construct
        super(ListModel, self).__init__(parent=parent)
        self.dataTable = None
        self.updateData("rig")


    def create_connection(self, db_file):
        # create a database connection to a SQLite database
        """
        create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return None

    def updateData(self, searchTerm):
        if len(searchTerm) == 0:
            searchTerm = " "
        print("ListModel is searching: "+ searchTerm)
        Term = ["%" + str(searchTerm) + "%", "%" + str(searchTerm) + "%"]
        sql = "SELECT * FROM files WHERE name LIKE (?) OR asset_pipelineState LIKE (?)"
        database = "D:\\Student Data\Documents\AMS\AssetManagementSystem.db"
        conn = self.create_connection(database)
        if conn is not None:
            with conn:
                cur = conn.cursor()
                cur.execute(sql, Term)
                self.dataTable = cur.fetchall()
                cur.close()
                return self.dataTable
        else:
            print("Unable to connect to Database")

    def rowCount(self, parent = QtCore.QModelIndex()):
        #figure out how many from query
        return len(self.dataTable)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        #query actual data
        curData = self.dataTable[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return curData[1]

        elif role == QtCore.Qt.ToolTipRole:
            return "File Name"

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section == 1:
                    return "Name"

            elif orientation == QtCore.Qt.Vertical:
                return section

