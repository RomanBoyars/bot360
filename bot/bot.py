from BotHandler import BotHandler
from multiprocessing import Pool

import time

bot = BotHandler("577977683:AAFSJJp1Hf_ej1Cve58v5mdY90UhaWdmlwI")  


def main():
    pool = Pool()
    pool.apply_async(notificate)
    pool.apply_async(answer)
    #answer()
    #notificate()
    
def notificate():
    while True:
        bot.send_notifications()
        time.sleep(5)

def answer():
    last_update_id = None
    while True:
        updates = bot.get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = bot.get_last_update_id(updates) + 1
            bot.echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()