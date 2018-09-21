import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('bot360-6b65381d463a.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Test').sheet1

#wks.delete_row(2)

#print(wks.get_all_records())

#wks.append_row(['this goes into first column','even more into second column'])

#print (wks.acell('A2'))
#print (wks.cell(2,1))
#print (wks.cell(2,1).value)
#print (wks.cell(2,1).col)
#print (wks.cell(2,1).row)

#wks.update_acell('B2', 'A completely different value for B2')
#wks.update_cell(3, 2, 'New value for B3')

#print(wks.find('this is A3'))
#print(wks.findall('Test'))

list_of_cells = wks.findall('Test')

list_of_cells[2].value = 'New value'

wks.update_cells(list_of_cells)