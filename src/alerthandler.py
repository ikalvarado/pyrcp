import sys
from PyQt4 import QtSql, QtGui
from alert import *

class alerthandler(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.okButton, QtCore.SIGNAL('clicked()'), self.closewidget)

    def setinfo(self, text):
        self.ui.label.setText(text)

    def closewidget(self):
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = alerthandler()
    myapp.setinfo("standalone")
    myapp.show()
    sys.exit(app.exec_())
