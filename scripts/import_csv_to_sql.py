import sqlite3
import csv

#scheudler.db is the sqlite db that will be created
sql = sqlite3.connect('.././db/scheduler.db')
cur = sql.cursor()
csv_file = open('preferences.csv','r')
next(csv_file, None)
reader = csv.reader(csv_file)

cur.execute('''DROP TABLE IF EXISTS employee_preferences''')
#creates employee_preferences table with the same column names as the csv file

cur.execute('''CREATE TABLE IF NOT EXISTS employee_preferences
            (employeeID INTIGER PRIMARY KEY, 
            first_name TEXT,
            last_name TEXT, 
            position TEXT,
            day1 TEXT, 
            day2 TEXT, 
            shift TEXT, 
            set_schedule TEXT);''')

#iterates through the table
for row in reader:
    cur.execute('''INSERT INTO employee_preferences VALUES (?, ?, ?, ?, ?, ?, ?, ?);''', row)

#close the csv connection, this file does not get changed throughout this process
#csv_file.close()
