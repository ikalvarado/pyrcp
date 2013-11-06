import sys
from systemUi import *
from adminMain import *

def printChildren(obj, indent):
    children = obj.children()
    if children == None:
        return

    for child in children:
        if "PyQt4" not in str(child.__class__):
            print(indent, child.objectName(), child.__class__)
            if hasattr(child, "reset"):
                child.reset()
        printChildren(child, indent + "  ")

def resetChildren(obj):
    children = obj.children()
    if children == None:
        return

    for child in children:
        if "PyQt4" not in str(child.__class__):
            if hasattr(child, "reset"):
                child.reset()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class System(sliderbase):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CetiSystemDialog()
        self.ui.setupUi(self)

        views = [
                (adminMain(), self.ui.linkAdmin)
            ]
        self.slider_setup(views, 1, self.ui.stackedWidgetMain)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = System()
    myapp.show()
    sys.exit(app.exec_())

