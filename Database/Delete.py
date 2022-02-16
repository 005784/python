import sqlite3
from sqlite3 import Error


def sql_connection():   #Establish a connection
    try:                #Exception handling (try,except,finally)
        conn = sqlite3.connect('Student1.db') #Create or Open existing database
        return conn
    except Error:
        print(Error)
def sql_table(conn):  #student1.db
    cursorObj = conn.cursor() #points to the database student1.db
    # cursorObj.execute("CREATE TABLE student(std_id n(5), name char(30),city char(30),dept char(35) );")
    # #  # Insert records
    # cursorObj.executescript("""
    # INSERT INTO student VALUES(5001,'James Hoog','New York','ece' );
    # INSERT INTO student VALUES(5002,'Nail Knite','Paris','cse' );
    # INSERT INTO student VALUES(5003,'Pit Alex','London','eee' );
    # INSERT INTO student VALUES(5004,'Mc Lyon','Paris','mech' );
    # INSERT INTO student VALUES(5005,'Paul Adam','Rome','civil' );
    # """)
    # conn.commit() #STORE THE DATA PERMANENTLY
    # cursorObj.execute("SELECT * FROM student") # * -> all columns ->WHERE CLAUSE-SELECTED ROWS
    # rows = cursorObj.fetchall()  # rows-> all the records in the student table
    # print("student details:")
    # for row in rows:
    #     print(row)
    # print("\ninsert the student details:")
    cursorObj = conn.cursor()  # points to the database Student.db
    cursorObj.execute('''DELETE FROM student WHERE std_id in (5005)''')
    conn.commit()
    cursorObj.execute("SELECT * FROM student")
    # conn.commit()
    rows = cursorObj.fetchall()  # rows-> all the records in the salesman table
    print("student details:")
    for row in rows:
        print(row)
sqllite_conn = sql_connection() #student1.db
sql_table(sqllite_conn) #student1.db
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")