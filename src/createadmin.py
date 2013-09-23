import sys
import os
import inspect
import hashlib
from PyQt4 import QtSql, QtGui
from dbconnection import *
from createadminui import *

class createadmin(QtGui.QWidget):
    def __init__(self, parent = None, userinterface = None, databasename = "", tablename = ""):
        if(not inspect.isclass(userinterface) or type(databasename) != str or type(tablename) != str):
            print("Unacceptable parameters")
            sys.exit()
        if(userinterface is None or databasename == "" or tablename == ""):
            print("Unacceptable parameters")
            sys.exit()
        db = dbconnection()
        db.connect("localhost", databasename)
        self.tablemodel = db.gettablemodel(tablename)
        print(self.tablemodel.lastError().text())

        QtGui.QWidget.__init__(self, parent)
        self.ui = userinterface()
        self.ui.setupUi(self)

        if hasattr(self.ui, "createButton"):
            QtCore.QObject.connect(self.ui.createButton, QtCore.SIGNAL('clicked()'), self.createRecords)
        if hasattr(self.ui, "verify"):
            QtCore.QObject.connect(self.ui.verify, QtCore.SIGNAL('textChanged(const QString&)'), self.compare)

    def set_parent_callback(self, callback_function):
        self.parent_callback_function = callback_function

    def compare(self, verify):
        if verify == "":
            self.ui.info.setPixmap(QtGui.QPixmap(None))
        elif verify != str(self.ui.password.text()):
            self.ui.info.setPixmap(QtGui.QPixmap("../images/bad.png"))
        else:
            self.ui.info.setPixmap(QtGui.QPixmap("../images/good.png"))

    def createRecords(self):
        username = str(self.ui.username.text())
        password = str(self.ui.password.text())
        verify = str(self.ui.verify.text())

        self.tablemodel.setFilter("user_name='" + username + "'")
        self.tablemodel.select()

        if self.tablemodel.rowCount() > 0:
            print("Error: Username exists!")
            return

        if password != verify:
            print("Error: Passwords don't match!")
            return

        # encrypt password
        encrypted = hashlib.sha256(password).hexdigest()

        newrecord = self.tablemodel.record()
        newrecord.setValue("user_name", username)
        newrecord.setValue("password", encrypted)
        self.tablemodel.insertRecord(-1, newrecord)
        self.tablemodel.submitAll()
        self.parent_callback_function()
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = createadmin(None, Ui_createadmin, "trunk", "administrators")
    myapp.show()
    sys.exit(app.exec_())

