# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/crudbaseui.ui'
#
# Created: Thu Jul 11 19:59:22 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_crudbase(object):
    def setupUi(self, crudbase):
        crudbase.setObjectName(_fromUtf8("crudbase"))
        crudbase.resize(770, 590)
        self.updateButton = QtGui.QPushButton(crudbase)
        self.updateButton.setGeometry(QtCore.QRect(620, 500, 120, 27))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.cancelButton = QtGui.QPushButton(crudbase)
        self.cancelButton.setGeometry(QtCore.QRect(620, 540, 120, 27))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.deleteButton = QtGui.QPushButton(crudbase)
        self.deleteButton.setGeometry(QtCore.QRect(170, 500, 90, 27))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.filterField = QtGui.QLineEdit(crudbase)
        self.filterField.setGeometry(QtCore.QRect(140, 70, 200, 27))
        self.filterField.setObjectName(_fromUtf8("filterField"))
        self.label_1 = QtGui.QLabel(crudbase)
        self.label_1.setGeometry(QtCore.QRect(30, 70, 100, 20))
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.tableView = QtGui.QTableView(crudbase)
        self.tableView.setGeometry(QtCore.QRect(30, 110, 710, 381))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableView.setFont(font)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.createButton = QtGui.QPushButton(crudbase)
        self.createButton.setGeometry(QtCore.QRect(50, 500, 90, 27))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.fieldSelect = QtGui.QComboBox(crudbase)
        self.fieldSelect.setGeometry(QtCore.QRect(370, 70, 200, 27))
        self.fieldSelect.setObjectName(_fromUtf8("fieldSelect"))

        self.retranslateUi(crudbase)
        QtCore.QMetaObject.connectSlotsByName(crudbase)

    def retranslateUi(self, crudbase):
        crudbase.setWindowTitle(QtGui.QApplication.translate("crudbase", "Abstract", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("crudbase", "Save Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("crudbase", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("crudbase", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("crudbase", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("crudbase", "Insert", None, QtGui.QApplication.UnicodeUTF8))

