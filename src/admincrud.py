import sys
import os
import inspect
from PyQt4 import QtSql, QtGui
from createadmin import *
from crudbase import *
from dbconnection import *
from crudbaseui import *

class admincrud(crudbase):
    def __init__(self, parent = None, userinterface = None, databasename = "", tablename = ""):
        super(admincrud, self).__init__(parent, userinterface, databasename, tablename)
        # Hide the password column
        self.ui.tableView.setColumnHidden(2, True)

    def createRecords(self):
        self.prompt = createadmin(None, Ui_createadmin, "trunk", "administrators")
        self.prompt.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = admincrud(None, Ui_crudbase, "trunk", "administrators")
    myapp.show()
    sys.exit(app.exec_())

