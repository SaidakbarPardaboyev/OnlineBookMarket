from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mys
from os import *
from sys import *
from BuyBooks import BuyBooks
from Create_database import Database
from Log_Reg import Log_Reg
from Create_database import Database


class OnlineBook(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
                           background-color: #AB44AF""")
        self.move(0, 0)
        self.setFixedSize(1500, 900)

        self.Db_Username = input("Database ingizni username nini kiriting: ")
        self.Db_Password = input("Database ingizni password nini kiriting: ")
        self.DataB = Database(self.Db_Username, self.Db_Password)

        # self.selling = BuyBooks(self.Db_Username, self.Db_Password)
        # self.setCentralWidget(self.selling)

        self.LogReg = Log_Reg(self.Db_Username, self.Db_Password)
        self.setCentralWidget(self.LogReg)


if __name__ == "__main__":
    app = QApplication([])
    ilova = OnlineBook()
    ilova.show()
    app.exec_()