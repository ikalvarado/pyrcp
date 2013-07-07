import sys
from systemUi import *
from adminMain import *

def printChildren(obj, indent):
  children=obj.children()
  if children==None:
    return
  for child in children:
    if "PyQt4" not in str(child.__class__):
      print indent, child.objectName(), child.__class__
      if hasattr(child, "reset"):
      #if child.property("reset") == 1:
        print "Ay nanita " + child.objectName()
        child.reset()
    printChildren(child, indent + "  ")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
        
class System(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_CetiSystemDialog()
    self.ui.setupUi(self)
    # Create empty dictionary that later will be populated with key=>TEXT value=>STACKED_WIDGET_INDEX
    self.views = {}
    # Create the list of views
    listofviews = ["adminMain"]
    # Assign to the views dictionary the key=>values
    for i, v in enumerate(listofviews):
      self.views[v] = i + 1      
    # Create objects according to the needed views (classes)
    self.viewAdminMain = adminMain()
    self.viewAdminMain.setObjectName(_fromUtf8("viewAdminMain"))
    # Create all views
    self.ui.stackedWidgetMain.addWidget(self.viewAdminMain)
    # Connect all signals
    QtCore.QObject.connect(self.ui.linkAdmin, QtCore.SIGNAL('clicked()'),self.showAdmin)    
    
  def showAdmin(self):       
    #self.viewAdminMain.ui.stackedWidgetAdmin.setCurrentIndex(0)
    printChildren(self.ui.stackedWidgetMain, " ")   
    self.ui.stackedWidgetMain.setCurrentIndex(self.views["adminMain"])
      
if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = System()
   myapp.show()
   sys.exit(app.exec_())
