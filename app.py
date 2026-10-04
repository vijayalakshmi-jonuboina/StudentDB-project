import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, course TEXT, marks INTEGER)''')

def add_student():
    id = int(input("ID: "))
    name = input("Name: ")
    course = input("Course: ")
    marks = int(input("Marks: "))
    c.execute("INSERT INTO students VALUES (?,?,?,?)", (id, name, course, marks))
    conn.commit()
    print("Student Added!")

def view_students():
    print("\n--- All Students ---")
    for row in c.execute("SELECT * FROM students"):
        print(row)

def search_student():
    name = input("Search Name: ")
    for row in c.execute("SELECT * FROM students WHERE name=?", (name,)):
        print("Found:", row)

while True:
    print("\n1.Add 2.View All 3.Search 4.Exit")
    ch = input("Choose: ")
    if ch == '1': add_student()
    elif ch == '2': view_students()
    elif ch == '3': search_student()
    elif ch == '4': break