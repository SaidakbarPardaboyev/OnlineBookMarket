from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mys
from os import *
from sys import *
from BuyBooks import BuyBooks
from Create_database import Database

class ONlineBook(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
                           background-color: #AB44AF""")
        self.move(200,100)
        # self.setFixedSize(1500, 800)
        self.selling = BuyBooks()
        self.setCentralWidget(self.selling)

        # Db_Username = input("Database ingizni username nini kiriting: ")
        # Db_Password = input("Database ingizni password nini kiriting: ")
        # self.DataB = Database(Db_Username, Db_Password)



if __name__ == "__main__":
    app = QApplication([])
    ilova = ONlineBook()
    ilova.show()
    app.exec_()