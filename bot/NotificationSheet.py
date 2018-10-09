import gspread
from oauth2client.service_account import ServiceAccountCredentials

class NotificationSheet:
    def __init__(self, date, status, sended, text, number, table_id, sheet_id):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('bot360-6b65381d463a.json', scope)
        gc = gspread.authorize(credentials)
        self.date = date
        self.status = status
        self.sended=sended
        self.text=text
        self.number=number
        self.table_id=table_id
        self.sheet_id=sheet_id
        self.wks = gc.open_by_key(self.table_id).worksheet(self.sheet_id)

