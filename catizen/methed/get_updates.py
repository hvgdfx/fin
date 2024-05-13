import datetime
from methed.text_start_handler import text_start
from methed.text_help_handler import text_help
from methed.text_hello_handler import text_hello
from methed.text_today_handler import text_today

def handle_updates(updates):
    last_update_id = None
    for update in updates["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text == "/start":
            text_start(chat_id=chat_id)
        elif text == "/help":
            text_help(chat_id=chat_id)
        elif text == "/today":
            text_today(chat_id=chat_id)
        elif text == "/hello":
            text_hello(chat_id=chat_id)
    return last_update_id

