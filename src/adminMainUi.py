# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/adminMain.ui'
#
# Created: Sun Sep 22 19:02:58 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AdminMain(object):
    def setupUi(self, AdminMain):
        AdminMain.setObjectName(_fromUtf8("AdminMain"))
        AdminMain.resize(770, 590)
        self.stackedWidgetAdmin = QtGui.QStackedWidget(AdminMain)
        self.stackedWidgetAdmin.setGeometry(QtCore.QRect(0, 0, 770, 590))
        self.stackedWidgetAdmin.setObjectName(_fromUtf8("stackedWidgetAdmin"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.layoutWidget = QtGui.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 40, 142, 291))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnCrudAdmin = QtGui.QPushButton(self.layoutWidget)
        self.btnCrudAdmin.setObjectName(_fromUtf8("btnCrudAdmin"))
        self.verticalLayout.addWidget(self.btnCrudAdmin)
        self.btnCrudAlumnos = QtGui.QPushButton(self.layoutWidget)
        self.btnCrudAlumnos.setObjectName(_fromUtf8("btnCrudAlumnos"))
        self.verticalLayout.addWidget(self.btnCrudAlumnos)
        self.btnCrudProfesores = QtGui.QPushButton(self.layoutWidget)
        self.btnCrudProfesores.setObjectName(_fromUtf8("btnCrudProfesores"))
        self.verticalLayout.addWidget(self.btnCrudProfesores)
        self.btnCrudGrupos = QtGui.QPushButton(self.layoutWidget)
        self.btnCrudGrupos.setObjectName(_fromUtf8("btnCrudGrupos"))
        self.verticalLayout.addWidget(self.btnCrudGrupos)
        self.btnCrudLaboratorios = QtGui.QPushButton(self.layoutWidget)
        self.btnCrudLaboratorios.setObjectName(_fromUtf8("btnCrudLaboratorios"))
        self.verticalLayout.addWidget(self.btnCrudLaboratorios)
        self.label_path = QtGui.QLabel(self.page)
        self.label_path.setGeometry(QtCore.QRect(5, 5, 185, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_path.setFont(font)
        self.label_path.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_path.setObjectName(_fromUtf8("label_path"))
        self.stackedWidgetAdmin.addWidget(self.page)

        self.retranslateUi(AdminMain)
        QtCore.QMetaObject.connectSlotsByName(AdminMain)

    def retranslateUi(self, AdminMain):
        AdminMain.setWindowTitle(_translate("AdminMain", "Form", None))
        self.btnCrudAdmin.setText(_translate("AdminMain", "ADMINISTRADOR", None))
        self.btnCrudAlumnos.setText(_translate("AdminMain", "ALUMNOS", None))
        self.btnCrudProfesores.setText(_translate("AdminMain", "PROFESORES", None))
        self.btnCrudGrupos.setText(_translate("AdminMain", "GRUPOS", None))
        self.btnCrudLaboratorios.setText(_translate("AdminMain", "LABORATORIOS", None))
        self.label_path.setText(_translate("AdminMain", "Administracion > Principal", None))

