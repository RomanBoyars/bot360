import psycopg2
from configparser import ConfigParser

CONFIG_FILE_NAME = 'settings.ini' 
DB_SECTION = 'postgresql'

class DbHelper:    

    def __init__(self):
        self.config=ConfigParser()
        self.config.read(CONFIG_FILE_NAME,"utf_8_sig")
        

    def execute_select(self, query):
        conn = None
        rows = None
        try:
            # connect to the PostgreSQL server
            # print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(
                self.config.get(DB_SECTION,"database"), 
                self.config.get(DB_SECTION,"user"), 
                self.config.get(DB_SECTION,"password"), 
                self.config.get(DB_SECTION,"host"), 
                self.config.get(DB_SECTION,"port")))
            # create a cursor
            cur = conn.cursor()
            #execute a query
            cur.execute(query)
            #get all the rows
            rows = cur.fetchall()
            #close the cursor
            cur.close
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return rows
                

    def execute_sql(self, sql):
        conn = None
        affected_rows = 0
        try:
            # connect to the PostgreSQL server
            # print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(
                self.config.get(DB_SECTION,"database"), 
                self.config.get(DB_SECTION,"user"), 
                self.config.get(DB_SECTION,"password"), 
                self.config.get(DB_SECTION,"host"), 
                self.config.get(DB_SECTION,"port")))
            # create a cursor
            cur = conn.cursor()
            #execute a query
            cur.execute(sql)
            #get number of rows updated
            affected_rows = cur.rowcount
            #commit all the changes
            conn.commit()
            #close the cursor
            cur.close
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return affected_rows
        
 
        
    


