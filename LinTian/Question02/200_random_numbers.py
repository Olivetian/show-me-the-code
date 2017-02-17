#generate 200 random activation code and save them in MySQL database
import uuid
import MySQLdb

def generate_code(number):
    codelist = [str(uuid.uuid4()).replace('-','') for i in range(number)]
    return codelist

def save_code_in_db(codelist):
    with MySQLdb.connect('localhost', 'test', '123', 'testdb') as cur:
        #create table
        cur.execute("CREATE TABLE rcodes(code_value CHAR(40) NOT NULL)")

        for i in codelist:
            cur.execute("INSERT INTO rcodes(code_value) VALUES('%s')" % i)
