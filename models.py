import pymongo

client = pymongo.MongoClient("mongodb+srv://unity:unity@users.lalm7.mongodb.net/users?retryWrites=true&w=majority")
db = client.test

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password