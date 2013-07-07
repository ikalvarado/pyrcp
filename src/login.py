import sys
from PyQt4 import QtSql, QtGui
from loginUi import *
from dbconnection import *
from alerthandler import *
import hashlib
from system import *

class Login(QtGui.QDialog):
    def __init__(self, parent = None):
        db = dbconnection()
        db.connect("localhost", "trunk")
        self.tablemodel = db.gettablemodel("administrators")
        print(self.tablemodel.lastError().text())

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CetiDialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.btnLogin, QtCore.SIGNAL('clicked()'), self.authenticate)

    def authenticate(self):
        self.tablemodel.setFilter("user_name=\""+str(self.ui.tbUsuario.text())+"\"")
        self.tablemodel.filter()

        # encrypt password
        encrypted = hashlib.sha256(str(self.ui.tbPass.text())).hexdigest()
        record = self.tablemodel.record(0)
        storedpassword = str(record.value("password").toString())

        if encrypted == storedpassword:
            '''
            self.msg = alerthandler()
            self.msg.setinfo("User login successfull")
            self.msg.show()
            '''
            self.forma = System()
            self.forma.show()
            self.hide()
        else:
            '''
            self.msg = alerthandler()
            self.msg.setinfo("Login failed")
            self.msg.show()
            '''
            self.ui.labelError.setText("ERROR: Usuario y/o password invalidos")  
            print(self.tablemodel.lastError().text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Login()
    myapp.show()
    sys.exit(app.exec_())
