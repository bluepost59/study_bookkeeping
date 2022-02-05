import os

import sqlite3

class dbHandler:

    def __init__(self):
        pass

    def initialize_db(self,db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            "CREATE TABLE journal( \
                transaction_id integer not null, \
                transaction_time integer, \
                partner integer, \
                debit_index integer,\
                debit_amount integer,\
                credit_index integer,\
                credit_amount integer\
                );")

    def add_transaction():
        pass

if __name__=="__main__":
    if os.path.exists("test.db"):
        os.remove("test.db")

    obj = dbHandler().initialize_db("test.db")


