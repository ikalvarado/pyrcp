import sys
import os
from login import *

from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    if(os.path.dirname(__file__) != ""):
        os.chdir(os.path.dirname(__file__))

    app = QtGui.QApplication(sys.argv)
    myapp = Login()
    myapp.show()
    sys.exit(app.exec_())
