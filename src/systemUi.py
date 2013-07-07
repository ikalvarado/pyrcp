# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/system.ui'
#
# Created: Thu Jul  4 21:18:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CetiSystemDialog(object):
    def setupUi(self, CetiSystemDialog):
        CetiSystemDialog.setObjectName(_fromUtf8("CetiSystemDialog"))
        CetiSystemDialog.resize(1000, 750)
        CetiSystemDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(CetiSystemDialog)
        self.label.setGeometry(QtCore.QRect(5, 5, 200, 132))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../images/logoCeti.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.stackedWidgetMain = QtGui.QStackedWidget(CetiSystemDialog)
        self.stackedWidgetMain.setGeometry(QtCore.QRect(230, 159, 770, 590))
        self.stackedWidgetMain.setObjectName(_fromUtf8("stackedWidgetMain"))
        self.pageAdmin = QtGui.QWidget()
        self.pageAdmin.setObjectName(_fromUtf8("pageAdmin"))
        self.stackedWidgetMain.addWidget(self.pageAdmin)
        self.label_2 = QtGui.QLabel(CetiSystemDialog)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 741, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget = QtGui.QWidget(CetiSystemDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 160, 170, 122))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayoutLinks = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayoutLinks.setMargin(0)
        self.gridLayoutLinks.setObjectName(_fromUtf8("gridLayoutLinks"))
        self.linkReservas = QtGui.QCommandLinkButton(self.layoutWidget)
        self.linkReservas.setObjectName(_fromUtf8("linkReservas"))
        self.gridLayoutLinks.addWidget(self.linkReservas, 1, 0, 1, 1)
        self.linkPrestamos = QtGui.QCommandLinkButton(self.layoutWidget)
        self.linkPrestamos.setObjectName(_fromUtf8("linkPrestamos"))
        self.gridLayoutLinks.addWidget(self.linkPrestamos, 0, 0, 1, 1)
        self.linkAdmin = QtGui.QCommandLinkButton(self.layoutWidget)
        self.linkAdmin.setObjectName(_fromUtf8("linkAdmin"))
        self.gridLayoutLinks.addWidget(self.linkAdmin, 2, 0, 1, 1)
        self.pushButtonHidden = QtGui.QPushButton(CetiSystemDialog)
        self.pushButtonHidden.setGeometry(QtCore.QRect(10, 710, 0, 0))
        self.pushButtonHidden.setText(_fromUtf8(""))
        self.pushButtonHidden.setObjectName(_fromUtf8("pushButtonHidden"))
        self.line = QtGui.QFrame(CetiSystemDialog)
        self.line.setGeometry(QtCore.QRect(200, 160, 16, 561))
        self.line.setStyleSheet(_fromUtf8(""))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButtonLogout = QtGui.QPushButton(CetiSystemDialog)
        self.pushButtonLogout.setGeometry(QtCore.QRect(907, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonLogout.setFont(font)
        self.pushButtonLogout.setFlat(True)
        self.pushButtonLogout.setObjectName(_fromUtf8("pushButtonLogout"))

        self.retranslateUi(CetiSystemDialog)
        self.stackedWidgetMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CetiSystemDialog)
        CetiSystemDialog.setTabOrder(self.pushButtonHidden, self.linkPrestamos)
        CetiSystemDialog.setTabOrder(self.linkPrestamos, self.linkReservas)
        CetiSystemDialog.setTabOrder(self.linkReservas, self.linkAdmin)

    def retranslateUi(self, CetiSystemDialog):
        CetiSystemDialog.setWindowTitle(QtGui.QApplication.translate("CetiSystemDialog", "CETI: Sistema de Prestamos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CetiSystemDialog", "Bienvenido: USUARIO", None, QtGui.QApplication.UnicodeUTF8))
        self.linkReservas.setText(QtGui.QApplication.translate("CetiSystemDialog", "RESERVAS", None, QtGui.QApplication.UnicodeUTF8))
        self.linkPrestamos.setText(QtGui.QApplication.translate("CetiSystemDialog", "PRESTAMOS", None, QtGui.QApplication.UnicodeUTF8))
        self.linkAdmin.setText(QtGui.QApplication.translate("CetiSystemDialog", "ADMINISTRACION", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLogout.setText(QtGui.QApplication.translate("CetiSystemDialog", "CERRAR SESION", None, QtGui.QApplication.UnicodeUTF8))

