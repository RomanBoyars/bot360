import requests  
import json
import urllib
from dbpostgres import DbHelper

proxies = {
  'https': 'http://80.149.233.42:8080',
}

class BotHandler:

    def __init__(self, token):
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot{}/".format(token)

    def get_url(self, url, offset=None, timeout=100):
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(url, params, proxies = proxies)
        content = response.content.decode("utf8")
        return content


    def get_json_from_url(self, url):
        content = self.get_url(url)
        js = json.loads(content)
        return js


    def get_updates(self, offset=None, timeout=100):
        url = self.URL + "getUpdates".format(timeout)
        if offset:
            url += "?offset={}".format(offset)
        js = self.get_json_from_url(url)
        return js


    def get_last_update_id(self, updates):
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)


    def get_last_chat_id_and_text(self, updates):
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        text = updates["result"][last_update]["message"]["text"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        return (text, chat_id)


    def echo_all(self, updates):
        for update in updates["result"]:
            try:
                text = update["message"]["text"]
                chat = update["message"]["chat"]["id"]
                first_name = update["message"]["from"]["first_name"]
                if text=="/start":
                    self.subscribe(first_name,chat)
                if text=="/unsubscribe":
                    self.unsubscribe(first_name,chat)
            except Exception as e:
                print(e)

    def send_notifications(self):
        db = DbHelper()
        rows = db.execute_select("SELECT * FROM notificator.messages WHERE sended = FALSE")
        for row in rows:
            chat_id = db.execute_select("SELECT phone_number FROM notificator.users WHERE id = {}".format(row[1]))[0][0]
            self.send_message(row[2],chat_id)
            db.execute_sql("UPDATE notificator.messages SET sended = TRUE where id = {}".format(row[0]))
            

    def subscribe(self, first_name, chat_id):
        db = DbHelper()
        rows = db.execute_select("SELECT * FROM notificator.users WHERE user_name = '{}' AND phone_number = '{}'".format(first_name,chat_id))
        if len(rows)==0:
            db.execute_sql("INSERT INTO notificator.users (user_name, phone_number) VALUES ('{}', '{}')".format(first_name,chat_id))
            self.send_message("Подписка активна", chat_id)
        else:
            self.send_message("Вы уже подписаны", chat_id)
    
    def unsubscribe(self, first_name, chat_id):
        db = DbHelper()
        db.execute_sql("DELETE FROM notificator.users WHERE user_name = '{}' AND phone_number = '{}'".format(first_name,chat_id))
        self.send_message("Вы отписались", chat_id)

    def send_message(self, text, chat_id):
        text = urllib.parse.quote_plus(text)
        url = self.URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        self.get_url(url)