# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/createadmin.ui'
#
# Created: Sun Jul  7 14:25:03 2013
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

class Ui_createadmin(object):
    def setupUi(self, createadmin):
        createadmin.setObjectName(_fromUtf8("createadmin"))
        createadmin.resize(480, 270)
        self.username = QtGui.QLineEdit(createadmin)
        self.username.setGeometry(QtCore.QRect(180, 45, 180, 27))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(createadmin)
        self.password.setGeometry(QtCore.QRect(180, 95, 180, 27))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.verify = QtGui.QLineEdit(createadmin)
        self.verify.setGeometry(QtCore.QRect(180, 145, 180, 27))
        self.verify.setEchoMode(QtGui.QLineEdit.Password)
        self.verify.setObjectName(_fromUtf8("verify"))
        self.createButton = QtGui.QPushButton(createadmin)
        self.createButton.setGeometry(QtCore.QRect(310, 200, 99, 27))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.label_1 = QtGui.QLabel(createadmin)
        self.label_1.setGeometry(QtCore.QRect(40, 50, 120, 17))
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(createadmin)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 120, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(createadmin)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 120, 17))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.info = QtGui.QLabel(createadmin)
        self.info.setGeometry(QtCore.QRect(370, 145, 27, 27))
        self.info.setText(_fromUtf8(""))
        self.info.setObjectName(_fromUtf8("info"))

        self.retranslateUi(createadmin)
        QtCore.QMetaObject.connectSlotsByName(createadmin)

    def retranslateUi(self, createadmin):
        createadmin.setWindowTitle(_translate("createadmin", "Form", None))
        self.createButton.setText(_translate("createadmin", "Create User", None))
        self.label_1.setText(_translate("createadmin", "User Name", None))
        self.label_2.setText(_translate("createadmin", "New Password", None))
        self.label_3.setText(_translate("createadmin", "Verify Password", None))

