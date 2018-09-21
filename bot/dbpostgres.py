import psycopg2
from config import config

CONFIG_FILE_NAME = 'settings.ini' 
DB_SECTION = 'postgresql'

class DbHelper:    

    def __init__(self):
        self.params = config(CONFIG_FILE_NAME, DB_SECTION)

    def execute_select(self, query):
        conn = None
        rows = None
        try:
            # connect to the PostgreSQL server
            # print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**self.params)
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
            conn = psycopg2.connect(**self.params)
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
        
 
        
    


