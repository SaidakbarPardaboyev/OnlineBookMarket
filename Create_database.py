import mysql.connector as mys
import os


class Database:
    def __init__(self,Username,Password):
        self.con = mys.connect(host='localhost', username=Username, password=Password)
        self.kursor = self.con.cursor()
        self.D_Name = "OnlineBookSale"
        self.T1_name = "Users"
        self.T2_name = "Books"
        self.T3_name = "Orders"

        self.Create_db()
        self.Create_Tables()

    def Create_db(self):
        buyruq = f"Create database if not exists {self.D_Name}"
        self.kursor.execute(buyruq)

    def Create_Tables(self):
        self.kursor.execute(f"use {self.D_Name}")
        self.kursor.execute("Show tables")
        tables = self.kursor.fetchall()
        # print(tables)
        if tables != [('books',), ('orders',), ('users',)]:
            self.kursor.execute(f"use {self.D_Name}")
            buyruq = f"""Create table if not exists {self.T1_name}(id int primary key auto_increment NOT NULL,Name varchar(100)
                        NOT NULL, Surname varchar(100) NOT NULL, Email varchar(100) NOT NULL, Password varchar(100) NOT NULL)"""
            self.kursor.execute(buyruq)

            buyruq = f"""Create table if not exists {self.T2_name}(id int primary key auto_increment NOT NULL,Name varchar(100)
                        NOT NULL, Page int NOT NULL, Price int NOT NULL, Author varchar(100) NOT NULL)"""
            self.kursor.execute(buyruq)

            self.Insert_to_Books()

            buyruq = f"""Create table if not exists {self.T3_name}(id int primary key auto_increment NOT NULL,User_id int
                        NOT NULL, Book_id int NOT NULL, Count int NOT NULL)"""
            self.kursor.execute(buyruq)

    def Insert_to_Books(self):
        self.kursor.execute(f"use {self.D_Name}")

        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Xamsa", 1500, 85000, 
                            "Alisher Navoiy")""")

        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Atom odatlar", 300, 150000, 
                            "Jeyms Klir")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Molxona", 100, 15000, 
                            "Jorj Oruell")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Moliyaviy mustaqillik va erkin hayot sari", 236, 40000, "Devid Bax")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Zukkolar va landavurlar", 480, 36000, 
                            "Malkolm Gladuell")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Chalg'ituvchi dunyoda muvaffaqiyat sirlari", 230, 80000, "Kel Nyuport")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Ikki imperiya to'qnashuvi", 744, 51000, 
                            "Piter Hopkirk")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Murakkab sohaning sodda qiyofasi ", 540, 42000, 
                            "Charlz Uilan")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("qudrat, farovonlik va kambag'allik manbalari", 676, 45000, "Daron Ajemo'g'li")""")
                            
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Savol ortidagi savol ", 104, 12000, 
                            "Jon G. Miller")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Stiv Jobs", 624, 91000, 
                            "Uolter Ayzekson")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Beparvolikning nozik san'ati ", 192, 34000, "Mark Menson")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Bir muhabbat tarixi ",
                            496, 42000, "Devid Nikolls")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Qo'rqma", 368, 21000, 
                            "Javlon Jovliyev")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Matematika va tabiiy fanlarni", 352, 41000, "Barbara Oukli")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Factfulness", 344, 18000, 
                            "Hans Rosling")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("To'rtinchi sanoat inqilobi", 248, 51000, 
                            "Klaus Shvab")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Yutaro Todanin asirlikda", 432, 21000, "Ato Hamdam")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Sarmoyador ", 700, 71000, 
                            "Teodor Drayzer")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Farengeyt bo'yicha", 224, 46000, 
                            "Rey Bredberi")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("O'tgan kunlar", 820, 89000, 
                            "Abdulla qodiriy")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Hazrati Umar", 500, 200000, 
                            "Ahmad Lutfiy")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("O'gay ona", 400, 12000, 
                            "Ahmad Lutfiy")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Saodat asri qissalari (1-kitob)", 1426, 450000, "Ahmad Lutfiy")""")
                            
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Saodat asri qissalari (2-kitob)", 1426, 450000, "Ahmad Lutfiy")""")
                            
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Saodat asri qissalari (3-kitob)", 1426, 450000, "Ahmad Lutfiy")""")
                            
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Saodat asri qissalari (4-kitob)", 1426, 450000, "Ahmad Lutfiy")""")
                            
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Xamsa", 1500, 85000, 
                            "Alisher Navoiy")""")

        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Atom odatlar", 300, 150000, 
                            "Jeyms Klir")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Molxona", 100, 15000, 
                            "Jorj Oruell")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Moliyaviy mustaqillik va erkin hayot sari", 236, 40000, "Devid Bax")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Zukkolar va landavurlar", 480, 36000, 
                            "Malkolm Gladuell")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Chalg'ituvchi dunyoda muvaffaqiyat sirlari", 230, 80000, "Kel Nyuport")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Ikki imperiya to'qnashuvi", 744, 51000, 
                            "Piter Hopkirk")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("Murakkab sohaning sodda qiyofasi ", 540, 42000, 
                            "Charlz Uilan")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Page, Price, Author) values("qudrat, farovonlik va kambag'allik manbalari", 676, 45000, "Daron Ajemo'g'li")""")
        self.con.commit()
                            

# os.system("cls")
# db = Database("root", "root")