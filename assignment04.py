import sqlite3
import sys

# database file connection
database = sqlite3.connect("assignment04.db")


# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()

## Function to setup/reset database
def setupDB():


    sql_command = """DROP TABLE IF EXISTS STUDENT"""
    cursor.execute(sql_command)
    sql_command = """DROP TABLE IF EXISTS INSTRUCTOR"""
    cursor.execute(sql_command)
    sql_command = """DROP TABLE IF EXISTS ADMIN"""
    cursor.execute(sql_command)
    sql_command = """DROP TABLE IF EXISTS COURSE"""
    cursor.execute(sql_command)
    sql_command = """DROP TABLE IF EXISTS SCHEDULE"""
    cursor.execute(sql_command)

    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE STUDENT (
    ID 		INT 	PRIMARY KEY 	NOT NULL,
    NAME		TEXT	NOT NULL,
    SURNAME		TEXT 	NOT NULL,
    GRADYEAR	INT 	NOT NULL,
    MAJOR		CHAR(4) NOT NULL,
    EMAIL		text	NOT NULL)
    ;"""

    # execute the statement
    cursor.execute(sql_command)
    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE INSTRUCTOR (
    ID 		INT 	PRIMARY KEY 	NOT NULL,
    NAME		TEXT	NOT NULL,
    SURNAME		TEXT 	NOT NULL,
    TITLE		TEXT 	NOT NULL,
    HIREYEAR	INT 	NOT NULL,
    DEPT		CHAR(4) NOT NULL,
    EMAIL		text	NOT NULL)
    ;"""

    # execute the statement
    cursor.execute(sql_command)

    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE ADMIN (
    ID 		INT 	PRIMARY KEY 	NOT NULL,
    NAME		TEXT	NOT NULL,
    SURNAME		TEXT 	NOT NULL,
    TITLE		TEXT 	NOT NULL,
    OFFICE		TEXT 	NOT NULL,
    EMAIL		text	NOT NULL)
    ;"""

    # execute the statement
    cursor.execute(sql_command)

    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE COURSE (
    TITLE       TEXT        NOT NULL,
    CRN         INT         PRIMARY KEY NOT NULL,
    DEPT        CHAR (4)    NOT NULL,
    INSTRUCTOR  TEXT        NOT NULL,
    TIME        TEXT        NOT NULL,
    DAYS        CHAR (3)    NOT NULL,
    SEMESTER    TEXT        NOT NULL,
    YEAR        INT         NOT NULL,
    CREDITS     INT         NOT NULL)
    ;"""

    # execute the statement
    cursor.execute(sql_command)


    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE SCHEDULE (
        ID       INT     PRIMARY KEY NOT NULL,
        COURSE01        INT,
        COURSE02        INT,
        COURSE03        INT,
        COURSE04        INT,
        COURSE05        INT,
        COURSE06        INT
    );"""

    # execute the statement
    cursor.execute(sql_command)





    # Student list
    cursor.execute("""INSERT INTO STUDENT VALUES(10001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""")
    cursor.execute("""INSERT INTO STUDENT VALUES(10010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""")

    # Instructor list
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""")
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")

    # Admin list
    cursor.execute("""INSERT INTO ADMIN VALUES(30001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""")
    cursor.execute("""INSERT INTO ADMIN VALUES(30002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""")

    # Course list
    cursor.execute("""Insert INTO COURSE VALUES ('OOPS', 5555, 'BSCO', 'Carpenter', '10:00am - 11:20am', 'MW', 'Spring', 2020, 5);""")
    cursor.execute("""Insert INTO COURSE VALUES ('APC', 1337, 'BSCO', 'Turing', '2:00pm - 3:20pm', 'TR', 'Summer', 2018, 3);""")
    cursor.execute("""Insert INTO COURSE VALUES ('ADCD', 48324, 'BSEE', 'Fourier', '8:00am - 9:20am', 'TR', 'Summer', 2020, 4);""")
    cursor.execute("""Insert INTO COURSE VALUES ('Calculus 5', 21488, 'BSAS', 'Galilei', '10:00am - 11:20am', 'MWF', 'Spring', 2020, 5);""")
    cursor.execute("""Insert INTO COURSE VALUES ('Discrete Math', 32157, 'BSME', 'Bernoulli', '11:30am - 1:20pm', 'TWR', 'Fall', 2020, 4);""")

class user:

    ## Class attributes for id
    id = 0
    ## Constructor for student. Needs to pass ID. ID will most likely get passed immediately after login
    ## This constructor is passed down through inheritance to student, instructor, and admin
    def __init__(self, id):
        self.id = id


    ## User function
    def searchAll(self):
        print("---COURSES---")
        cursor.execute("""SELECT * FROM COURSE""")  #query structure and sqlite syntax taken from assignment 2
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)


    ## User function
    def searchParam(self):
        choice = input("1 for CRN, 2 for Department, 3 for Day of the week, 4 for year, 5 for Credits: ")
        if choice == '1':
            find = input("Enter the CRN you are searching for: ")
            cursor.execute("""SELECT * FROM COURSE WHERE CRN = %s""" % (find))  #finds exact match
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif choice == '2':
            find = input("Enter the Department you are searching for: ")
            cursor.execute("""SELECT * FROM COURSE WHERE DEPT = '%s'""" % (find))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif choice == '3':
            find = input("Enter the Day of the week you are searching for: ")
            cursor.execute("SELECT * FROM COURSE WHERE DAYS LIKE '%" + find + "%'")  #finds similar results
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif choice == '4':
            find = input("Enter the Course year you are searching for: ")
            cursor.execute("""SELECT * FROM COURSE WHERE YEAR = '%s'""" % (find))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif choice == '5':
            find = input("Enter the number of Credits you are searching for: ")
            cursor.execute("""SELECT * FROM COURSE WHERE CREDITS = %s""" % (find))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
#This is the base for the login for all users.
#It assigns space for a first name, last name, and id number.
#The print function displays the name and ID on two separate lines.
    def setfirstName(self, a):
        self.firstName = a

    def setlastName(self, a):
        self.lastName = a

    def setstudentID(self, a):
        self.idNumber = a

    def printAll(self):
        print("Name: ", self.firstName, self.lastName)
        print("ID: ", self.idNumber)

class student(user):  # inheritance is done with the ()
    uac = 1
    course = [0, 0, 0, 0, 0, 0]

    def updateCourse(self, id):
        studentRow = getRow(id, "SCHEDULE")
        for i in range(1, len(studentRow)):
            self.course[i-1] = int(studentRow[i])
        ## check database and update course array accordingly

    def __init__(self, id):
        self.id = id
        self.updateCourse(self.id)


    def printCourses(self):
        print("\n\n\t\t\t\t---COURSES---\n")
        printTable("COURSE")
        # cursor.execute("""SELECT * FROM COURSE""")
        # query_result = cursor.fetchall()
        # for i in query_result:
        #     print(i)

    ## Class function to update the schedule of a student. Prompts input from user and updates student's attributes. Updates database accordingly
    def modifySchedule(self):
        self.updateCourse(self.id)
        choice = input("1: Add Course\n2: Remove Course\n")
        CRN = input("CRN: ")

        if(choice == "1"):

            for i in range(0, len(self.course)):
                if(self.course[i] == 0):
                    self.course[i] = CRN
                    query = cursor.execute("UPDATE SCHEDULE SET COURSE0" + str(i+1) + " = " + str(CRN) + " WHERE ID = " + str(self.id))
                    print(getRow(self.id, "SCHEDULE"))
                    break


        elif(choice == "2"):
            for i in range(0, len(self.course)):
                if(self.course[i] == CRN):
                    self.course[i] = 0
                    cursor.execute("UPDATE SCHEDULE SET COURSE0" + str(i+1) + " = 0 WHERE ID = " + str(self.id))
                    printTable("SCHEDULE")
                    break

class instructor(user):
    uac = 2
    schedule = [0, 0, 0, 0, 0, 0]

    def updateCourse(self, id):
        studentRow = getRow(id, "SCHEDULE")
        for i in range(1, len(studentRow)):
            self.course[i-1] = int(studentRow[i])
        ## check database and update course array accordingly


    def printSchedule(self):

        ## Simple query to get all records based on instructor's courses
        for i in range(1, len(self.schedule)):
            query = cursor.execute("SELECT * FROM COURSE WHERE CRN = " + str(self.schedule[i]))
            for i in query:
                print(i)

    ## Query to return Student IDs that are registered for a course
    def printRoster(self):
        CRN = input("CRN: ")
        query = cursor.execute("SELECT ID FROM SCHEDULE WHERE COURSE01 = " + CRN + " OR COURSE02 = " + CRN + " OR COURSE03 = " + CRN + " OR COURSE04 = " + CRN + " OR COURSE05 = " + CRN + " OR COURSE06 = " + CRN)
        for i in query:
            print(i)
#Class admin: inherits from user and can add course and remove course
class admin(user):
    uac = 3
    def __init__(self, id):
        self.id = id
#add course function takes input from user and sets it to variables which are then executed as an insert in the query line.
#This adds all necessary information to fill out the table in the database and create a fully functioning course.
    def addCourse(self):
        courseName = input("Course Name: ")
        courseID = input("Course ID: ")
        departmentName = input("Department Name: ")
        instructorName = input("Instructor Name: ")
        time = input("Time: ")
        day = input("Day: ")
        semester = input("Semester: ")
        year = input("Year: ")
        credits = input("Credits: ")
        query = cursor.execute("INSERT INTO COURSE VALUES ('" + courseName + "', " + courseID + ", '" + departmentName + "', '" + instructorName + "', '" + time + "', '" + day + "', '" + semester + "', " + year + ", " + credits + ")")
#remove course is a lot simpler than add, as it searches just for the CRN and removes the entry that matches in the table.
#The query line executes the remove using only the course id, or CRN
    def removeCourse(self):
        courseID = input("CRN: ")
        query = cursor.execute("DELETE FROM COURSE WHERE CRN = " + courseID)

####################################

## Print entire table. Only needs the table name as parameter
def printTable(tableName):
    query = cursor.execute("SELECT * FROM " + tableName)
    for i in query:
        print(i)

## Function to get all values of a column from any given table. parameters are column name and table name. This will mainly be used to get all IDs from tables
def getColumn(column, table):
    returnValue = []
    query = cursor.execute("SELECT " + column + " FROM " + table)
    for i in query:
        temp_returnValue = str(i)
        temp_returnValue = temp_returnValue.strip("(),")
        returnValue.append(temp_returnValue)
    return returnValue

## Function to get each row from either Student, Instructor, or Admin table based on ID
def getRow(ID, table):
    returnValue = []
    query = cursor.execute("SELECT * FROM " + table + " WHERE ID = " + ID + "")
    for i in query:
        temp_returnValue = str(i)
        temp_returnValue = temp_returnValue.strip("(),")
        returnValue = temp_returnValue.split(", ")
    return returnValue

## Takes a singular ID and creates a new row in the schedule table. All 6 courses are set to 0 by default
## This could be changed to just run inside the setupDB() function
def populateSchedule(ID):
    query = cursor.execute("INSERT INTO SCHEDULE VALUES(" + str(ID) + ", 0, 0, 0, 0, 0, 0)")

## Setup the schedule table helper function
## This also could be moved to setupDB() in the future
def setupSchedule():
    studentIDs = getColumn("ID", "STUDENT")
    instructorIDs = getColumn("ID", "INSTRUCTOR")
    adminIDs = getColumn("ID", "ADMIN")

    for i in range(0, len(studentIDs)):
        populateSchedule(studentIDs[i])
    for i in range(0, len(instructorIDs)):
        populateSchedule(instructorIDs[i])

## Login will create a user based on their ID. Will create the appropriate user (Student, Instructor, Admin) based on ID given
def login():
    uid = input("Enter your user ID: ")
    cursor.execute("""SELECT EXISTS(SELECT * FROM STUDENT WHERE ID = %s)""" % (uid))
    query_result = cursor.fetchall()
    x = str(query_result)

    cursor.execute("""SELECT EXISTS(SELECT * FROM INSTRUCTOR WHERE ID = %s)""" % (uid))
    query_result = cursor.fetchall()
    y = str(query_result)

    cursor.execute("""SELECT EXISTS(SELECT * FROM ADMIN WHERE ID = %s)""" % (uid))
    query_result = cursor.fetchall()
    z = str(query_result)

    if x == "[(1,)]":
        print("Welcome Student")
        return student(uid)
    elif y == "[(1,)]":
        print("Welcome Carpenter")
        return instructor(uid)
    elif z == "[(1,)]":
        print("Welcome Admin")
        return admin(uid)
    else:
        print("Access Denied")
        exit()

## Logout simply ends the program by exiting
def logout():
    print("You are now logged out")
    sys.exit(0)

## Menu function based on user attributes. Needs user object as parameter
def menu(user):
    if user.uac == 1:
        swit =input("1. Modify your schedule\n2. View all courses\n3. Search courses based on a parameter\n4. logout\nEnter: ")
        if swit == '1':
            user.modifySchedule()
        elif swit == '2':
            user.printCourses()
        elif swit == '3':
            user.searchParam()
        elif swit == '4':
            logout()
        else:
            print("Error: Enter a valid number")
            menu(user)
    if user.uac == 2:
        swit = input("1. Assemble and print course schedule\n2. View all courses\n3. Search courses based on a parameter\n4. Log out\nEnter: ")
        if swit == '1':
            user.printRoster()
            user.printSchedule()
        elif swit == '2':
            user.searchAll()
        elif swit == '3':
            user.searchParam()
        elif swit == '4':
            logout()
        else:
            print("Error: Enter a valid number")
            menu(user)
    if user.uac == 3:
        swit =input("1. Add or Remove a course from the schedule\n2. View all courses\n3. Search courses based on a parameter\n4. Log out\nEnter: ")
        if swit == '1':
            swit2 = input("1. Add a course\n2. Remove a course: ")
            if swit2 == '1':
                user.addCourse()
            elif swit2 =='2':
                user.removeCourse()
            else:
                print("Enter a valid number")
        elif swit == '2':
            user.searchAll()
        elif swit == '3':
            user.searchParam()
        elif swit == '4':
            logout()
        else:
            print("Error: Enter a valid number")
            menu(user)


## Main function to organize better. Logs user in, allows user to reset/setup DB, exit, or go to user menu
def main():
    testUser = login()
    while(True):
        print("\n\n-----------Main Menu------------")
        choice = input("1. Setup/Reset Database \n2. Continue to User Menu \n3. Exit\nEnter: ")
        if(choice == "1"):
            setupDB()
            setupSchedule()
        elif(choice == "2"):
            ## Would go into the menu section
            menu(testUser)
        elif(choice == "3"):
            ## Close database and exit
            database.close()
            exit()
        else:
            print("Please enter a valid selection")

        ## After every iteration, update the database for any potential changes that may have been made
        database.commit()


## Should eventually create a function to setup/reset DB if it does not exist yet
## call main function
main()
