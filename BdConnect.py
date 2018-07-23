import mysql.connector
class BdConnect:
    def __init__(self, db_name, db_upass, db_uname):
        self.db_name = db_name
        self.db_upass = db_upass
        self.db_uname = db_uname

    def connect(self):
        db = mysql.connector.connect(
                host="localhost",
                user = self.db_uname,
                password = self.db_upass
            )

        cursor = db.cursor()

    def insertion( self, namebd, nameUser, loginUser, passUser):
        self.namebd = namebd
        self.nameUser = nameUser
        self.loginUser = loginUser
        self.passUser = passUser 

        inserer = (""INSERT INTO user ""(name, login, password) " "VALUES (%s, %s, %s,)")")

        inserer = (namebd, nameUser, passUser)
        

