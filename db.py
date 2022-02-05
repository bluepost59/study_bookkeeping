import sqlite3

class dbHandler:
    def __init__(self):
        pass

    def connect(self,db_path):
        self.db = sqlite3.connect(db_path)