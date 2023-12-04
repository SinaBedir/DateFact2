from sqlite3 import connect

class Database:
    db=None

    @staticmethod
    def connectDatabase():
        Database.db = connect("number.db")
        cursor = Database.db.cursor()
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS USERS(
        ID INTEGER PRIMARY KEY,
        EMAIL TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
        )
        """
        )
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS FACT_TABLE(
        ID INTEGER PRIMARY KEY,
        EMAIL TEXT NOT NULL,
        FACT_TEXT TEXT NOT NULL
        )
        """
        )
        Database.db.commit()
        print("Connection successfull")

    @staticmethod
    def insertData(email, password):
        sql = """
        INSERT INTO USERS (EMAIL, PASSWORD)
        VALUES(?,?)
        """
        val = (email, password)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        print("Data successfully inserted to USERS table")
    
    @staticmethod
    def isValid(email):
        sql=f"SELECT * FROM USERS WHERE EMAIL='{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            return False
        else:
            return True

    @staticmethod
    def isExists(email, password):
        sql=f"SELECT * FROM USERS WHERE EMAIL='{email}' AND PASSWORD='{password}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            return True
        else:
            return False
        
    @staticmethod
    def insertFact(email, fact):
        sql="INSERT INTO FACT_TABLE (EMAIL, FACT_TEXT) VALUES (?,?)"
        val=(email, fact)
        cursor=Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()

    @staticmethod
    def getFacts(email):
        sql=f"SELECT * FROM FACT_TABLE WHERE EMAIL='{email}' ORDER BY 2 DESC"
        cursor=Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

