from telebot import types

USER = [types.KeyboardButton("Г-525"),
        types.KeyboardButton("Г-529"),
        types.KeyboardButton("Узнать свой статус"),]

VOLUNTEER = USER + [types.KeyboardButton("Работа"),]

OWNER = USER + [types.KeyboardButton("Выдать роль"),
                types.KeyboardButton("Узнать кто работает"),
                types.KeyboardButton("Статистика волонтеров"),]