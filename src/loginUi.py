# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/login.ui'
#
# Created: Tue Jun 25 19:25:51 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CetiDialog(object):
    def setupUi(self, CetiDialog):
        CetiDialog.setObjectName(_fromUtf8("CetiDialog"))
        CetiDialog.resize(300, 300)
        CetiDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(CetiDialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 200, 132))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../images/logoCeti.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayoutWidget = QtGui.QWidget(CetiDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 150, 211, 128))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.tbPass = QtGui.QLineEdit(self.gridLayoutWidget)
        self.tbPass.setEchoMode(QtGui.QLineEdit.Password)
        self.tbPass.setObjectName(_fromUtf8("tbPass"))
        self.gridLayout.addWidget(self.tbPass, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tbUsuario = QtGui.QLineEdit(self.gridLayoutWidget)
        self.tbUsuario.setObjectName(_fromUtf8("tbUsuario"))
        self.gridLayout.addWidget(self.tbUsuario, 0, 1, 1, 1)
        self.btnLogin = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.gridLayout.addWidget(self.btnLogin, 2, 1, 1, 1)
        self.labelError = QtGui.QLabel(CetiDialog)
        self.labelError.setGeometry(QtCore.QRect(10, 280, 281, 17))
        self.labelError.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
        self.labelError.setText(_fromUtf8(""))
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName(_fromUtf8("labelError"))

        self.retranslateUi(CetiDialog)
        QtCore.QMetaObject.connectSlotsByName(CetiDialog)
        CetiDialog.setTabOrder(self.tbUsuario, self.tbPass)
        CetiDialog.setTabOrder(self.tbPass, self.btnLogin)

    def retranslateUi(self, CetiDialog):
        CetiDialog.setWindowTitle(QtGui.QApplication.translate("CetiDialog", "CETI: Sistema de Prestamos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CetiDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CetiDialog", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogin.setText(QtGui.QApplication.translate("CetiDialog", "Login", None, QtGui.QApplication.UnicodeUTF8))

