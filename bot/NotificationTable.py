
from dbpostgres import DbHelper
from NotificationSheet import NotificationSheet

class NotificationTable:

    def __init__(self, table_id):
        self.table_id = table_id
        db = DbHelper()
        sheets_db = db.execute_select("SELECT * FROM notificator.google_sheets WHERE table_id='{}'".format(table_id))
        self.sheets = []
        for sheet in sheets_db:
            self.sheets.append(NotificationSheet(sheet[1],sheet[2],sheet[3],sheet[4],sheet[5],sheet[6],sheet[7]))

        


