#pip install pyTelegramBotAPI
import telebot
import re
from settings import TELEGRAM_TOKEN
from templates import HELP_TEMPLATE

from commands.json_lib import UserJson, UserInfo
from commands.check_rights import is_owner, is_volunteer, is_user
from commands.room_showcase import Room
from commands.grid_correct_data import *

from commands.templates.check_values import USER_STATUS, USER_STATUS_DICT

from telebot import types
from datetime import date


class TelegramBot:
    def __init__(self, telegram_token):
        self.telegram_bot = telebot.TeleBot(telegram_token)
        self.UserInfo = UserInfo()
        self.UserJson = UserJson()
        self.Room = Room()
        self.lastUpdate = self.Room.preloadInformation()
        self.Room.loadDaysButtons()

        self.DICT_ROOM_NUM = {
            525 : [self.Room.daysKeyboard_525, self.Room.RegdaysKeyboard_525],
            529 : [self.Room.daysKeyboard_529, self.Room.RegdaysKeyboard_529]
            }

    def help(self, message):
        if (self.lastUpdate != date.today()):
            self.lastUpdate = self.Room.preloadInformation(1)
        match self.UserInfo.status_call(message):
            case "user":
                self.telegram_bot.reply_to(message, text=HELP_TEMPLATE, parse_mode= 'Markdown',reply_markup=self.Room.UserKeyboard)
            case "volunteer":
                self.telegram_bot.reply_to(message, text=HELP_TEMPLATE, parse_mode= 'Markdown',reply_markup=self.Room.VolunteerKeyboard)
            case "owner":
                self.telegram_bot.reply_to(message, text=HELP_TEMPLATE, parse_mode= 'Markdown',reply_markup=self.Room.OwnerKeyboard)

        
    def showInformation(self,message, room = False):
        if (self.lastUpdate != date.today()):
            self.Room.preloadInformation(0)
        if (self.Room.daysKeyboard_525 == None or self.Room.daysKeyboard_529 == None):
            self.Room.loadDaysButtons()
        if room:
            self.telegram_bot.send_message(message.chat.id, text="Расписание кабинета 525", reply_markup=self.Room.daysKeyboard_525)
        else:
            self.telegram_bot.send_message(message.chat.id, text=f"Расписание кабинета 529", reply_markup=self.Room.daysKeyboard_529)

      
    def run(self):
        @self.telegram_bot.message_handler(commands=['help', 'start'])
        def help_handler(message):
            self.help(message)

        @self.telegram_bot.message_handler(commands=['add_member'])
        @is_owner
        def add_member_handler(message):
            text = message.text.split(' ')
            try:
                if (text[2] in USER_STATUS):
                    if self.UserJson.add_member_status(int(text[1]), text[2]):
                        self.telegram_bot.reply_to(message, text="Информация успешно записана")
                        self.telegram_bot.send_message(int(text[1]), text='Добрый день! Администратор: {0} поднял ваш статус до "{1}". Пропишите снова /start или /help.'.format(message.from_user.username, USER_STATUS_DICT[text[2]]))
                    else:
                        self.telegram_bot.reply_to(message, text="Произошла ошибка :c\nВозможно, такой пользователь уже имеет статус.")
                else:
                    self.telegram_bot.reply_to(message, text="Такой роли не существует.")
            except Exception:
                self.telegram_bot.reply_to(message, text="Ошибка ввода.")

        @self.telegram_bot.message_handler(commands=['register'])
        def make_note_handler(message):
            self.telegram_bot.send_message(message.from_user.id, text="Выберите кабинет", reply_markup=self.Room.RoomRegisterKeyboard)

        @self.telegram_bot.message_handler(commands=['test'])
        def make_note_handler(message):
            if self.UserInfo.user_request(str(message.from_user.id), str(date.today())):
                self.telegram_bot.send_message(message.from_user.id, text="Done")
            else:
                self.telegram_bot.send_message(message.from_user.id, text="Fail")


        @self.telegram_bot.message_handler(content_types=['text'])
        def text_handler(message):
            if message.text=="Г-525": self.showInformation(message, room = True)
            elif message.text=="Г-529": self.showInformation(message, room = False)
            elif message.text=="Узнать свой статус": self.telegram_bot.reply_to(message, text=self.UserInfo.member_status_call(message))

            elif message.text=="Работа" and self.UserInfo.status_call(message) == "volunteer":
                self.UserInfo.volunteer_status(message)
                self.telegram_bot.reply_to(message, text="Ваш статус изменен")
            elif message.text=="Выдать роль" and self.UserInfo.status_call(message) == "owner": 
                self.telegram_bot.reply_to(message, text="Используйте функцию:\n\n/add_member telegram_user_id status")
            elif message.text=="Узнать кто работает" and self.UserInfo.status_call(message) == "owner":
                self.telegram_bot.reply_to(message, text=self.UserInfo.volunteer_online_status())
            elif message.text=="Статистика волонтеров" and self.UserInfo.status_call(message) == "owner":
                self.telegram_bot.reply_to(message, text=self.UserInfo.volunteer_stat())
            else:
                self.telegram_bot.reply_to(message, text=f"Я ничего не нашел.\n\nВарианты запроса: Г-525 или Г-529")

        @self.telegram_bot.callback_query_handler(func=lambda call: True)
        def callback_data(message):
            print(message.data)
            try:
                if ('_reg_upperDay' in message.data) or ('_reg_lowerDay' in message.data):
                    room_num = int(message.data[:3])
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text=self.Room.showDayInfo(room_num = room_num, room = message.data[8], day = (int(message.data[-1]))),
                                                        reply_markup= self.DICT_ROOM_NUM[room_num][1])
                elif ('_upperDay' in message.data) or ('_lowerDay' in message.data):
                    room_num = int(message.data[:3])
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text=self.Room.showDayInfo(room_num = room_num, room = message.data[4], day = (int(message.data[-1]))),
                                                        reply_markup= self.DICT_ROOM_NUM[room_num][0])
                    
                elif message.data == 'reg_day_append':
                    grid_information(message)
                    # self.telegram_bot.send_message(message, text="{0} {1} {2}".format(LIST[0], LIST[1], LIST[2]))
                     
                elif 'register_' in message.data:
                    room_num = int(message.data[-3:])
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text="Выберите день.\n\nВерхняя строчка - текущая неделя\n\nНидняя строчка - следующая неделя",
                                                        reply_markup= self.DICT_ROOM_NUM[room_num][1])
                elif 'register_Y':
                    telegram_id, start_time, end_time, date = correct_template(message)
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text="Спасибо за обработку! Ответ отправлен.")
                    self.telegram_bot.send_message(telegram_id, text= "Добрый день! Мы ждем вас {0} в {1}".format(date, start_time))
                elif 'register_N':
                    telegram_id, start_time, end_time, date = correct_template(message)
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text="Спасибо за обработку! Ответ отправлен.")
                    self.telegram_bot.send_message(telegram_id, text= "Добрый день! К сожалению мы не сможем вас принять {0} в {1}".format(date, start_time))
                    
                else:
                    pass
            except Exception as ex:
                print(ex)

        self.telegram_bot.polling()

if __name__ == '__main__':
    bot = TelegramBot(TELEGRAM_TOKEN)
    bot.run()