import telebot
from settings import OWNERS_LIST

def is_owner(func):
    def wrapper(message):
        if message.from_user.id in OWNERS_LIST:
            return func(message)
        else:
            pass
    return wrapper