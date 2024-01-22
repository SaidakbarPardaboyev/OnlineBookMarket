from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mys
from os import *
from sys import *
import re
from BuyBooks import BuyBooks

class Log_Reg(QWidget):
    def __init__(self, Db_Username, Db_Password):
        super().__init__()

        self.Db_Username = Db_Username
        self.Db_Password = Db_Password
        self.con = mys.connect(host='localhost', username=Db_Username, password=Db_Password)
        self.kursor = self.con.cursor()
        self.D_Name = "OnlineBookSale"
        self.T1_name = "Users"
        self.T2_name = "Books"
        self.T3_name = "Orders"
        
        self.selling = None

        self.setStyleSheet("""background-color: #FFFFFF""")
        self.setGeometry(450, 75, 450, 535)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(450, 81, 50, 81)
        self.layout.setSpacing(0)

        self.label = QLabel("Login Form")
        self.label.setFont(QFont("Montserrat", 25, weight=80))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(550, 100)
        self.layout.addWidget(self.label)

        self.WButtons = QWidget()
        self.WButtons.setFixedSize(550, 100)
        self.nestedLayout = QHBoxLayout(self.WButtons)

        self.LogIn = QPushButton("Login", clicked=lambda: self.toggle_first_widget())
        self.LogIn.setFixedSize(225, 75)
        self.LogIn.setFont(QFont("Montserrat", 25, weight=50))
        self.LogIn.setStyleSheet("""background-color: #AB44AF;
                                 color: #FFFFFF;
                                 border: 2px solid #D8D6D6;""")
        self.nestedLayout.addWidget(self.LogIn)

        self.Register = QPushButton("Signup", clicked=lambda: self.toggle_second_widget())
        self.Register.setFixedSize(225, 75)
        self.Register.setFont(QFont("Montserrat", 25, weight=50))
        self.Register.setStyleSheet("""background-color: #FFFFFF;
                                 color: #131716;
                                 border: 2px solid #D8D6D6;""")
        self.nestedLayout.addWidget(self.Register)
        self.layout.addWidget(self.WButtons)

        self.LoginPage = self.LogPage()
        self.RegisterPage = self.RegisPage()

        self.layout.addWidget(self.LoginPage)
        self.layout.addWidget(self.RegisterPage)

        self.LoginPage.show()
        self.RegisterPage.hide()


    def toggle_first_widget(self):
        self.LoginPage.show()
        self.RegisterPage.hide()

    def toggle_second_widget(self):
        self.RegisterPage.show()
        self.LoginPage.hide()

    def LogPage(self):
        wind = QWidget()
        wind.setFixedSize(550, 540)
        wind.setStyleSheet("""background-color: white; """)

        self.Line_email_Login = QLineEdit(wind)
        self.Line_email_Login.setGeometry(35, 100, 480, 60)
        self.Line_email_Login.setPlaceholderText("Email Address")
        self.Line_email_Login.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_email_Login.setFont(QFont("Montserrat", 18))

        self.Line_Password_login = QLineEdit(wind)
        self.Line_Password_login.setGeometry(35, 220, 480, 60)
        self.Line_Password_login.setPlaceholderText("Password")
        self.Line_Password_login.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_Password_login.setFont(QFont("Montserrat", 18))

        self.Line_Password_check_login = QLabel("Invalid email or Invalid password", wind)
        self.Line_Password_check_login.setGeometry(45, 290, 480, 20)
        self.Line_Password_check_login.setStyleSheet("""color: white;""")
        self.Line_Password_check_login.setFont(QFont("Montserrat", 12))

        self.btn_login = QPushButton("Login", wind, clicked=lambda: self.check_db_Users())
        self.btn_login.setGeometry(35, 340, 480, 60)
        self.btn_login.setStyleSheet("""color: white;
                                background-color: #AB44AF;""")
        self.btn_login.setFont(QFont("Montserrat", 20))

        return wind
    
    def check_db_Users(self):
        email = self.Line_email_Login.text().strip()
        password = self.Line_Password_login.text().strip()

        try:
            self.kursor.execute(f"use {self.D_Name}")
            self.kursor.execute(f"SELECT * FROM {self.T1_name} WHERE Email = '{email}' AND Password = '{password}'")
            ls = self.kursor.fetchall()

            if len(ls) == 1:
                self.Line_Password_check_login.setStyleSheet("""color: white;""")
                self.close()
                print(ls)
                self.selling = BuyBooks(self.Db_Username, self.Db_Password, ls[0])
                self.selling.show()
            else:
                self.Line_Password_check_login.setStyleSheet("""color: red;""")

        except Exception as e:
            print(f"Error during database operation: {e}")



    def RegisPage(self):
        wind = QWidget()
        wind.setFixedSize(550, 540)
        wind.setStyleSheet("""background-color: white; """)

        self.Line_Name = QLineEdit(wind)
        self.Line_Name.setGeometry(35, 30, 480, 50)
        self.Line_Name.setPlaceholderText("Name")
        self.Line_Name.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_Name.setFont(QFont("Montserrat", 15))

        self.Line_Name_check = QLabel("Invalid Name", wind)
        self.Line_Name_check.setGeometry(45, 85, 480, 20)
        self.Line_Name_check.setStyleSheet("""color: white;""")
        self.Line_Name_check.setFont(QFont("Montserrat", 9))

        self.Line_Surname = QLineEdit(wind)
        self.Line_Surname.setGeometry(35, 115, 480, 50)
        self.Line_Surname.setPlaceholderText("Surname")
        self.Line_Surname.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_Surname.setFont(QFont("Montserrat", 15))

        self.Line_Surname_check = QLabel("Invalid Surname", wind)
        self.Line_Surname_check.setGeometry(45, 170, 480, 20)
        self.Line_Surname_check.setStyleSheet("""color: white;""")
        self.Line_Surname_check.setFont(QFont("Montserrat", 9))

        self.Line_email = QLineEdit(wind)
        self.Line_email.setGeometry(35, 200, 480, 50)
        self.Line_email.setPlaceholderText("Email Address")
        self.Line_email.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_email.setFont(QFont("Montserrat", 15))

        self.Line_email_check = QLabel("Invalid email", wind)
        self.Line_email_check.setGeometry(45, 255, 480, 20)
        self.Line_email_check.setStyleSheet("""color: white""")
        self.Line_email_check.setFont(QFont("Montserrat", 9))

        self.Line_Password = QLineEdit(wind)
        self.Line_Password.setGeometry(35, 285, 480, 50)
        self.Line_Password.setPlaceholderText("Password")
        self.Line_Password.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_Password.setFont(QFont("Montserrat", 15))

        self.Line_Password_check = QLabel("Invalid password", wind)
        self.Line_Password_check.setGeometry(45, 340, 480, 20)
        self.Line_Password_check.setStyleSheet("""color: white;""")
        self.Line_Password_check.setFont(QFont("Montserrat", 9))

        self.Line_Pre_Password = QLineEdit(wind)
        self.Line_Pre_Password.setGeometry(35, 370, 480, 50)
        self.Line_Pre_Password.setPlaceholderText("Password")
        self.Line_Pre_Password.setStyleSheet("""border: 2px solid #D9D7D7""")
        self.Line_Pre_Password.setFont(QFont("Montserrat", 15))

        self.Line_Pre_Password_check = QLabel("not same", wind)
        self.Line_Pre_Password_check.setGeometry(45, 425, 480, 20)
        self.Line_Pre_Password_check.setStyleSheet("""color: white""")
        self.Line_Pre_Password_check.setFont(QFont("Montserrat", 9))

        self.btn_regis = QPushButton("Register", wind, clicked=lambda: self.check_db_reg())
        self.btn_regis.setGeometry(35, 460, 480, 50)
        self.btn_regis.setStyleSheet("""color: white;
                                background-color: #AB44AF;""")
        self.btn_regis.setFont(QFont("Montserrat", 20))

        return wind
    
    def check_db_reg(self):
        lamp = True
        if not len(self.Line_Name.text().strip()) > 3:
            self.Line_Name_check.setStyleSheet("""color: red;""")
            lamp = False
        else:
            self.Line_Name_check.setStyleSheet("""color: white;""")

        if not len(self.Line_Surname.text().strip()) > 3:
            self.Line_Surname_check.setStyleSheet("""color: red""")
            lamp = False
        else:
            self.Line_Surname_check.setStyleSheet("""color: white""")

        if not self.is_valid_email(self.Line_email.text().strip()):
            self.Line_email_check.setText("Invalid email")
            self.Line_email_check.setStyleSheet("""color: red""")
            lamp = False
        else:
            self.kursor.execute(f"use {self.D_Name}")
            self.kursor.execute(f"SELECT * FROM {self.T1_name} where Email = '{self.Line_email.text().strip()}'")
            ls = self.kursor.fetchall()
            if len(ls) != 0:
                self.Line_email_check.setText("Email is already exists")
                self.Line_email_check.setStyleSheet("""color: red""")
                lamp = False
            else:
                self.Line_email_check.setText("Invalid email")
                self.Line_email_check.setStyleSheet("""color: white""")

        if not len(self.Line_Password.text().strip()) >= 8:
            self.Line_Password_check.setText("Invalid password")
            self.Line_Pre_Password_check.setText("Invalid password")
            self.Line_Password_check.setStyleSheet("""color: red""")
            self.Line_Pre_Password_check.setStyleSheet("""color: red""")
        elif not self.Line_Password.text().strip() == self.Line_Pre_Password.text().strip():
            self.Line_Password_check.setText("Invalid password")
            self.Line_Password_check.setStyleSheet("""color: white""")
            self.Line_Pre_Password_check.setText("Different password")
            self.Line_Pre_Password_check.setStyleSheet("""color: red""")
        else:
            self.Line_Password_check.setText("Invalid password")
            self.Line_Password_check.setStyleSheet("""color: white""")
            self.Line_Pre_Password_check.setText("Invalid password")
            self.Line_Pre_Password_check.setStyleSheet("""color: white""")

        if lamp:
            self.kursor.execute(f"use {self.D_Name}")
            tem = (self.Line_Name.text().strip(), self.Line_Surname.text().strip(), self.Line_email.text().strip(), self.Line_Password.text().strip())
            self.kursor.execute(f"""insert into {self.T1_name}(Name,Surname,Email,Password)
                                values(%s,%s,%s,%s)""", tem)
            self.con.commit()

            msg = QMessageBox()
            msg.setFixedSize(500,400)
            msg.setWindowTitle("Register")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Registered Successuly")

            info_book = list(map(lambda x: x[1], ls))
            info_book = "\n".join(info_book)
            msg.setInformativeText(info_book)

            self.Cleaner_register_page()
            msg.buttonClicked.connect(self.toggle_first_widget)

            msg.exec_()        

    def Cleaner_register_page(self):
        self.Line_Name.clear()
        self.Line_Name.setPlaceholderText("Name")
        self.Line_Surname.clear()
        self.Line_Surname.setPlaceholderText("Surname")
        self.Line_email.clear()
        self.Line_email.setPlaceholderText("Email Address")
        self.Line_Password.clear()
        self.Line_Password.setPlaceholderText("Password")
        self.Line_Pre_Password.clear()
        self.Line_Pre_Password.setPlaceholderText("Password")

    def is_valid_email(self, email):
        # Regular expression for a basic email validation
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        # Check if the email matches the pattern
        return bool(re.match(email_pattern, email))
        



if __name__ == "__main__":
    app = QApplication([])
    ilova = Log_Reg()
    ilova.show()
    app.exec_()
