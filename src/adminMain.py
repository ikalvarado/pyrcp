import sys
from sliderbase import *
from adminMainUi import *
from admincrud import *
from crudbase import *

class adminMain(sliderbase):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AdminMain()
        self.ui.setupUi(self)

        views = [
                (admincrud(None, Ui_crudbase, "trunk", "administrators"), self.ui.btnCrudAdmin),
                (crudbase(None, Ui_crudbase, "trunk", "alumnos"), self.ui.btnCrudAlumnos),
                (crudbase(None, Ui_crudbase, "trunk", "profesores"), self.ui.btnCrudProfesores),
                (crudbase(None, Ui_crudbase, "trunk", "grupos"), self.ui.btnCrudGrupos),
                (crudbase(None, Ui_crudbase, "trunk", "laboratorios"), self.ui.btnCrudLaboratorios),
            ]
        self.slider_setup(views, 1, self.ui.stackedWidgetAdmin)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = adminMain()
    myapp.show()
    sys.exit(app.exec_())
