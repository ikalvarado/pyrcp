import sys
from adminMainUi import *
from admincrud import *
from crudbase import *

class adminMain(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AdminMain()
        self.ui.setupUi(self)

        self.signal_mapper = QtCore.QSignalMapper(self)
        self.views = [
                (admincrud(None, Ui_crudbase, "trunk", "administrators"), self.ui.btnCrudAdmin),
                (crudbase(None, Ui_crudbase, "trunk", "alumnos"), self.ui.btnCrudUsuarios)
            ]

        for i, v in enumerate(self.views):
            self.ui.stackedWidgetAdmin.addWidget(v[0])
            self.signal_mapper.setMapping(v[1], i)
            v[1].clicked.connect(self.signal_mapper.map)

        self.signal_mapper.mapped.connect(self.show_stack_section)

    def show_stack_section(self, view_select):
        self.ui.stackedWidgetAdmin.setCurrentIndex(view_select + 2)

    def reset(self):
        self.ui.stackedWidgetAdmin.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = adminMain()
    myapp.show()
    sys.exit(app.exec_())
