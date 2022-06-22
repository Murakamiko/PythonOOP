from app import conn
from app.Forms.SaveUserForm import SaveUserForm
from app.Model.Person import Person

class SaveUserService:
    def __init__(self) -> None:
        pass

def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM contact;")
        tests = []
        for test in cur.fetchall():
            tests.append(Person(test[0], test[1], test[2], test[3]))

def findOne(self, userid):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contact WHERE transferid = {userid};")
        testData = cur.fetchone()
        conn.commit()

def insert(self, data: SaveUserForm):
        cur = conn.cursor()
        cur.execute("INSERT INTO contact(name, firstname, password, email, userdescription) VALUES(" + str(data.name.data) + ", " + str(data.firstname.data) + ", " + str(data.password.data) + str(data.email.data) + str(data.userdescription.data) + ");")
        conn.commit()

        return None