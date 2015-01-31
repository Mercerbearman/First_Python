'''
Created on Jan 29, 2015

@author: Fox
'''

def init_sqLite():
    '''
    This is a block comment..
    
    Oh yes it is.
    '''
    
    conn = None
    
    import sqlite3
    conn = sqlite3.connect('TestDB.db')
    
    with conn:
        c = conn.cursor()
        
        c.execute('SELECT SQLITE_VERSION()')
        
        data = c.fetchone()
        
        print("SQLite version: %s" % data)
        
        c.execute("DROP TABLE IF EXISTS Roster")
        c.execute("CREATE TABLE Roster(First TEXT, Last TEXT, MI CHARACTER, Age INT)")
        c.execute("INSERT INTO Roster VALUES('Robert', 'Smith', 'G', 23)")
        c.execute("INSERT INTO Roster VALUES('Ralph', 'Jenkins', 'A', 47)")
        c.execute("INSERT INTO Roster VALUES('Eddie', 'Patton', 'S', 34)")
        c.execute("INSERT INTO Roster VALUES('Ashley', 'Locke', 'A', 12)")
    
    
    cursor = conn.execute("SELECT Last, First, MI, Age from Roster")
    
    print("Starting to list data.")
    
    for row in cursor:
        print("Name = %s, %s %s" % (row[0], row[1], row[2]))
        print("Age = %d" % row[3])
    
    print("Huzzah, we are done.")
    conn.close()
    

if __name__ == '__main__':
    init_sqLite()
    pass