import sqlite3

# Connect to a SQLite database by specifying the database file name
sqliteConnection    = sqlite3.connect("email.db",check_same_thread=False)
cursorObject        = sqliteConnection.cursor()
#cursorObject.execute("CREATE TABLE Emails(email VARCHAR,code VARCHAR);")
# Insert a row inton the orders table
def insert(email,code):
    insertStatement     = "INSERT INTO Emails VALUES('{}','{}')".format(email,code)
    cursorObject.execute(insertStatement)
    cursorObject.execute("COMMIT")

def fetch(email):
    try:
        selectStatement     = '''SELECT code FROM Emails\
                                WHERE email = '{}'
            '''.format(email)
        cursorObject.execute(selectStatement)
        rows = cursorObject.fetchall()
        return [i[0] for i in rows]
    except:
        print("yep")
        return False