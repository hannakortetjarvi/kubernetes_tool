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
        self.db.add({"exercise":1, "part":3, "has_answer":True, "answer":[10, 11, 8, 7, 1, 5, 9]})
        self.db.add({"exercise":1, "part":4, "has_answer":True, "answer":["minikube start*", "minikube stop"]})
        self.db.add({"exercise":2, "part":1, "has_answer":False, "answer":""})
        self.db.add({"exercise":2, "part":2, "has_answer":False, "answer":""})
        self.db.add({"exercise":2, "part":3, "has_answer":True, "answer":[['kubectl delete service palve','kubectl delete svc palve'], ['kubectl get replicationcontrollers','kubectl get rc'],
                                                                          ['kubectl edit role/johtaja'], ['kubectl scale --replicas=3 deployment/käyttö', 'kubectl scale --replicas=3 deploy/käyttö'],
                                                                          ['kubectl expose pod validi-säiliö'], ['kubectl describe jobs']]})
        self.db.add({"exercise":2, "part":4, "has_answer":True, "answer":["kubectl create deployment !insert --image=gcr.io/google-samples/kubernetes-bootcamp:v1", "kubectl get deployments"]})

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
        data = self.get_exercise(user)
        data[ex-1] = part
        data = self.users.update(query, {"completed":data})
    
    def init_user(self, user):
        query = {"username": user}
        data = self.users.getByQuery(query)

        if data == []:
            self.users.add({"username": user, "completed":[0, 0]})
            return [0, 0]
        else:
            found_user = data[0]
            return found_user["completed"]
        
    def get_exercise(self, user):
        query = {"username": user}
        data = self.users.getByQuery(query)
        return data[0]["completed"]
        
    def exercise_count(self, ex):
        query = {"exercise": ex}
        data = self.db.getByQuery(query)
        return len(data)

    def init(self):
        self.db.deleteAll()
        self.users.deleteAll()
        self.migrations()