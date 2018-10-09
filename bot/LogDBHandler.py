from dbpostgres import DbHelper
from datetime import datetime

class LogDBHandler:

    def log(action, messenger,phone_number,message,result,direction,user_id=0,additional_info='',sended_json="{}",recieved_json="{}"):
        db = DbHelper()
        sql = "INSERT INTO notificator.logs (action_, messenger, phone_number, message, date_time, sended_json, recieved_json, result, direction, user_id, additional_info) values ('{}','{}','{}','{}', to_timestamp('{}', 'YY/mm/DD HH24:MI:SS'), '{}', '{}', '{}', '{}', {}, '{}')".format(action, messenger,phone_number, message, datetime.now().strftime("%Y/%m/%d %H:%M:%S"), sended_json,recieved_json,result,direction,user_id,additional_info)
        db.execute_sql(sql)