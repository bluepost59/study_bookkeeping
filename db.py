import sqlite3

class dbHandler:
    def __init__(self):
        pass

    def initialize_db(self,db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            "create table journal({})".format(
                "string hoge,integer fuga"))

if __name__=="__main__":
    obj = dbHandler().initialize_db("test.db")


