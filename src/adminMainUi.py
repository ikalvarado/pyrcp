# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/adminMain.ui'
#
# Created: Thu Jul  4 21:12:46 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AdminMain(object):
    def setupUi(self, AdminMain):
        AdminMain.setObjectName(_fromUtf8("AdminMain"))
        AdminMain.resize(770, 590)
        self.stackedWidgetAdmin = QtGui.QStackedWidget(AdminMain)
        self.stackedWidgetAdmin.setGeometry(QtCore.QRect(0, 0, 770, 590))
        self.stackedWidgetAdmin.setObjectName(_fromUtf8("stackedWidgetAdmin"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.widget = QtGui.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(320, 40, 139, 62))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnCrudAdmin = QtGui.QPushButton(self.widget)
        self.btnCrudAdmin.setObjectName(_fromUtf8("btnCrudAdmin"))
        self.verticalLayout.addWidget(self.btnCrudAdmin)
        self.btnCrudUsuarios = QtGui.QPushButton(self.widget)
        self.btnCrudUsuarios.setObjectName(_fromUtf8("btnCrudUsuarios"))
        self.verticalLayout.addWidget(self.btnCrudUsuarios)
        self.label_5 = QtGui.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(5, 5, 185, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.stackedWidgetAdmin.addWidget(self.page)

        self.retranslateUi(AdminMain)
        QtCore.QMetaObject.connectSlotsByName(AdminMain)

    def retranslateUi(self, AdminMain):
        AdminMain.setWindowTitle(QtGui.QApplication.translate("AdminMain", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCrudAdmin.setText(QtGui.QApplication.translate("AdminMain", "ADMINISTRADOR", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCrudUsuarios.setText(QtGui.QApplication.translate("AdminMain", "USUARIO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AdminMain", "Administracion > Principal", None, QtGui.QApplication.UnicodeUTF8))

