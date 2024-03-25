from pysondb import db
import os.path

class database():
    def create_db():
        dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dir, "db.json")
        a = db.getDb(filename)
        #a.addMany([{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}])
        b = a.getAll()
        print(b)