import sys
import os
from PyQt4 import QtSql, QtGui

class dbconnection:

    def connect(self, host, database, user = "", password = "", path = "../database/"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        if QtSql.QSqlDatabase.contains():
            self.db = QtSql.QSqlDatabase.database()
        else:
            self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            self.db.setHostName(self.host)
            self.db.setDatabaseName(path + self.database + ".db")
            self.db.setUserName(self.user)
            self.db.setPassword(self.password)

        if self.db.isOpen():
            old = str(self.db.databaseName())
            new = str(path + self.database + ".db")
            if old != new:
                print("Error: a database connection to another database is active")
                print("new: " + new)
                print("old: " + old)
                sys.exit()
        else:
            self.db.open()
        print(self.db.lastError().text())

        return True

    def gettablemodel(self, table = ""):
        if(table == ""):
            return None
        model = QtSql.QSqlRelationalTableModel(None, self.db)
        model.setTable(table)
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.select()
        return model

