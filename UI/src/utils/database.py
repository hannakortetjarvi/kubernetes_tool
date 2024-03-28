from pysondb import db
import os.path

class database():
    def __init__(self):
        super().__init__()
        dir = os.path.dirname(os.path.realpath(__file__))
        db_filename = os.path.join(dir, "db.json")
        users_filename = os.path.join(dir, "user.json")
        self.db = db.getDb(db_filename)
        self.users = db.getDb(users_filename)

    def migrations(self):
        self.db.add({"exercise":1, "part":1, "has_answer":False, "answer":""})
        self.db.add({"exercise":1, "part":2, "has_answer":False, "answer":""})
        self.db.add({"exercise":1, "part":3, "has_answer":True, "answer":"ok"})
        self.db.add({"exercise":1, "part":4, "has_answer":True, "answer":"ok"})

    def getItems(self):
        return self.db.getAll()
    
    def check_has_answer(self, ex, part):
        query = {"exercise": ex, "part": part}
        data = self.db.getByQuery(query)
        return data[0]["has_answer"]
    
    def get_answer(self, ex, part):
        query = {"exercise": ex, "part": part}
        data = self.db.getByQuery(query)
        return data[0]["answer"]
    
    def update_current_exercise(self, ex, part, user):
        query = {"username": user}
        data = self.users.update(query, {"completed":[ex, part]})
    
    def init_user(self, user):
        query = {"username": user}
        data = self.users.getByQuery(query)

        if data == []:
            self.users.add({"username": user, "completed":[1,0]})
            return [1, 0]
        else:
            found_user = data[0]
            return found_user["completed"]

    def init(self):
        self.db.deleteAll()
        self.users.deleteAll()
        self.migrations()