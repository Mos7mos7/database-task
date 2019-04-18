import sqlite3
conn=sqlite3.connect("cat.db")
c=conn.cursor()
def create_tables():
    c.execute("CREATE TABLE IF NOT EXISTS mentor (name varchar(255),circle varchar(255))")
    c.execute("CREATE TABLE IF NOT EXISTS leader (name varchar(255),circle varchar(255))")
    c.execute("CREATE TABLE IF NOT EXISTS members (name varchar(255),circle varchar(255),level varchar(255))")

create_tables()

def mentor(name,circle):
    c.execute("INSERT INTO mentor (name,circle) VALUES (?,?)",(name,circle))
    conn.commit()
    c.execute("SELECT * FROM mentor")
    data=c.fetchall()
    for row in data:
        print(row)


def leader(name,circle):
    c.execute("INSERT INTO leader (name,circle) VALUES (?,?)",(name,circle))
    conn.commit()
    c.execute("SELECT * FROM leader")
    data=c.fetchall()
    for row in data:
        print(row)

def members(name,circle,level):
    c.execute("INSERT INTO members (name,circle,level) VALUES (?,?,?)",(name,circle,level))
    conn.commit()
    c.execute("SELECT * FROM members")
    data=c.fetchall()
    for row in data:
        print(row)

person=input("mentor,leader or member : ")
if person == "mentor":
    name=input("What's your name:")
    circle=input("Your circle:")
    mentor(name,circle)
elif person=="leader":
    name=input("What's your name:")
    circle=input("Your circle:")
    leader(name,circle)
else :
    name=input("What's your name:")
    circle=input("Your circle:")
    level=input("Your level:")
    members(name,circle,level)
c.close()
conn.close()
