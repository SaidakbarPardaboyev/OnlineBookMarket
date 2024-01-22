from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mys
from os import *
from sys import *
# from BuyBooks import BuyBooks
from Create_database import Database


class BookCard:
    def __init__(self, Name, Author, Price):
        self.wind_book = QWidget()
        self.wind_book.setFixedSize(1350, 100)
        self.book_layout = QHBoxLayout()

        self.book_name = QTextEdit()
        self.book_name.setPlainText(Name)
        self.book_name.setReadOnly(True)
        self.book_name.setAlignment(Qt.AlignCenter)
        self.book_name.setFixedSize(400, 80)
        self.book_name.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.book_name.setFont(QFont("Montserrat", 15, weight=100))

        self.book_author = QLabel()
        self.book_author.setText(Author)
        self.book_author.setAlignment(Qt.AlignCenter)
        self.book_author.setFixedSize(400, 80)
        self.book_author.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.book_author.setFont(QFont("Montserrat", 15, weight=100))

        self.book_price = QLabel()
        self.book_price.setText(Price)
        self.book_price.setAlignment(Qt.AlignCenter)
        self.book_price.setFixedSize(350, 80)
        self.book_price.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.book_price.setFont(QFont("Montserrat", 15, weight=100))

        self.Pilus = QPushButton("+")
        self.Pilus.setFixedSize(70, 80)
        self.Pilus.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.Pilus.setFont(QFont("Montserrat", 15, weight=100))
        self.Pilus.clicked.connect(lambda: self.PilusOrder(Price))

        self.Count = QLabel("0")
        self.Count.setAlignment(Qt.AlignCenter)
        self.Count.setFixedSize(50, 80)
        self.Count.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.Count.setFont(QFont("Montserrat", 15, weight=100))

        self.Minus = QPushButton("-")
        self.Minus.setFixedSize(70, 80)
        self.Minus.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.Minus.setFont(QFont("Montserrat", 15, weight=100))

        self.book_layout.addWidget(self.book_name)
        self.book_layout.addWidget(self.book_author)
        self.book_layout.addWidget(self.book_price)
        self.book_layout.addWidget(self.Pilus)
        self.book_layout.addWidget(self.Count)
        self.book_layout.addWidget(self.Minus)

        self.wind_book.setLayout(self.book_layout)

    def PilusOrder(self, Price):
        self.PilusCount()

    def PilusCount(self):
        self.Buyurtmalar_soni.setText(str(int(self.Buyurtmalar_soni.text()) + 1))