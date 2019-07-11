import sqlite3

# Connect to a SQLite database by specifying the database file name
sqliteConnection    = sqlite3.connect("Forms.db",check_same_thread=False)
cursorObject        = sqliteConnection.cursor()
#cursorObject.execute("CREATE TABLE Forms(email VARCHAR,code VARCHAR,response_path VARCHAR,post VARCHAR);")

def insert(email,code,response_path,post):
    insertStatement     = "INSERT INTO Forms VALUES('{}','{}','{}','{}')".format(email,code,response_path,post)
    print(insertStatement)
    cursorObject.execute(insertStatement)
    cursorObject.execute("COMMIT")

def fetch(email):
    try:
        selectStatement     = '''SELECT code,response_path,post FROM Forms\
                                WHERE email = '{}'
            '''.format(email)
        cursorObject.execute(selectStatement)
        rows = list(cursorObject.fetchall())
        return rows
    
    except:
        print("yep")
        return False