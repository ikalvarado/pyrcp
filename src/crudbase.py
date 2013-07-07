import sys
import os
import inspect
from PyQt4 import QtSql, QtGui
from dbconnection import *
from crudbaseui import *

class crudbase(QtGui.QWidget):
    def __init__(self, parent = None, userinterface = None, databasename = "", tablename = ""):
        if(not inspect.isclass(userinterface) or type(databasename) != str or type(tablename) != str):
            print("Unacceptable parameters")
            sys.exit()
        if(userinterface is None or databasename == "" or tablename == ""):
            print("Unacceptable parameters")
            sys.exit()
        db = dbconnection()
        db.connect("localhost", "trunk")
        self.tablemodel = db.gettablemodel(tablename)
        print(self.tablemodel.lastError().text())

        QtGui.QWidget.__init__(self, parent)
        self.ui = userinterface()
        self.ui.setupUi(self)
        self.ui.tableView.setModel(self.tablemodel)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSortIndicatorShown(True)

        for i in xrange(self.tablemodel.columnCount()):
            if i == 0:
                continue
            oldcolumnname = self.tablemodel.headerData(i, QtCore.Qt.Horizontal).toString()
            newcolumnname =  str(oldcolumnname).replace("_", " ").title()
            self.tablemodel.setHeaderData(i, QtCore.Qt.Horizontal, newcolumnname)
            self.ui.fieldSelect.addItem(newcolumnname, oldcolumnname)

        if hasattr(self.ui, "updateButton"):
            QtCore.QObject.connect(self.ui.updateButton, QtCore.SIGNAL('clicked()'), self.updateChanges)
        if hasattr(self.ui, "cancelButton"):
            QtCore.QObject.connect(self.ui.cancelButton, QtCore.SIGNAL('clicked()'), self.cancelChanges)
        if hasattr(self.ui, "createButton"):
            QtCore.QObject.connect(self.ui.createButton, QtCore.SIGNAL('clicked()'), self.createRecords)
        if hasattr(self.ui, "deleteButton"):
            QtCore.QObject.connect(self.ui.deleteButton, QtCore.SIGNAL('clicked()'), self.deleteRecords)
        if hasattr(self.ui, "filterField"):
            QtCore.QObject.connect(self.ui.filterField, QtCore.SIGNAL('textChanged(const QString&)'), self.filterRecords)
        if hasattr(self.ui, "tableView"):
            QtCore.QObject.connect(self.ui.tableView.horizontalHeader(), QtCore.SIGNAL('sectionClicked(int)'), self.sortColumn)

    def echoEvent(self, args):
        print("PING! " + str(args))

    def updateChanges(self):
        self.tablemodel.submitAll()

    def cancelChanges(self):
        self.tablemodel.revertAll()

    def createRecords(self):
        self.tablemodel.insertRow(self.tablemodel.rowCount())

    def deleteRecords(self):
        self.tablemodel.removeRow(self.ui.tableView.currentIndex().row())

    def filterRecords(self, text):
        columnname = self.ui.fieldSelect.itemData(self.ui.fieldSelect.currentIndex()).toString()
        self.tablemodel.setFilter(columnname + " like '%" + text + "%'")

    def sortColumn(self, column):
        order = self.ui.tableView.horizontalHeader().sortIndicatorOrder()
        self.tablemodel.sort(column, 0 if order == QtCore.Qt.Horizontal else 1)
        self.ui.tableView.horizontalHeader().setSortIndicator(column, order)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = crudbase(None, Ui_crudbase, "trunk", "crudbasetable")
    myapp.show()
    sys.exit(app.exec_())
