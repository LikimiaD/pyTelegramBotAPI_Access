#pip install pyTelegramBotAPI
import telebot
from settings import TELEGRAM_TOKEN
from templates import HELP_TEMPLATE, ROOM_525, ROOM_529
from misis_lk import Schedule

from telebot import types
from datetime import date, datetime

class TelegramBot:
    def __init__(self, telegram_token):
        self.telegram_bot = telebot.TeleBot(telegram_token)
        self.parser = Schedule()
        self.daysKeyboard_525 = None
        self.daysKeyboard_529 = None
        self.roomsKeyboard = None
        self.lastUpdate = None
        self.room525 = {}
        self.room529 = {}

    def preloadInformation(self, value = 1):
        if (value):
            print("Парсинг информации с lk misis")
        else:
            print("Обновление информации")
        self.room525['upper'] = self.parser.getSchedule(ROOM_525, self.parser.startDate(1))
        self.room525['lower'] = self.parser.getSchedule(ROOM_525, self.parser.startDate(0))

        self.room529['upper'] = self.parser.getSchedule(ROOM_529, self.parser.startDate(1))
        self.room529['lower'] = self.parser.getSchedule(ROOM_529, self.parser.startDate(0))
        print("Вся информация загружена, бот запускается...")
        self.lastUpdate = date.today()

    def loadDaysButtons(self):
        keyboard = [[types.InlineKeyboardButton("ПН", callback_data='525_upperDay1'),
                     types.InlineKeyboardButton("ВТ", callback_data='525_upperDay2'),
                     types.InlineKeyboardButton("СР", callback_data='525_upperDay3'),
                     types.InlineKeyboardButton("ЧТ", callback_data='525_upperDay4'),
                     types.InlineKeyboardButton("ПТ", callback_data='525_upperDay5'),
                     types.InlineKeyboardButton("СБ", callback_data='525_upperDay6')],

                    [types.InlineKeyboardButton("ПН", callback_data='525_lowerDay1'),
                     types.InlineKeyboardButton("ВТ", callback_data='525_lowerDay2'),
                     types.InlineKeyboardButton("СР", callback_data='525_lowerDay3'),
                     types.InlineKeyboardButton("ЧТ", callback_data='525_lowerDay4'),
                     types.InlineKeyboardButton("ПТ", callback_data='525_lowerDay5'),
                     types.InlineKeyboardButton("СБ", callback_data='525_lowerDay6')],
                   ]
        self.daysKeyboard_525 =  types.InlineKeyboardMarkup(keyboard)
        keyboard = [[types.InlineKeyboardButton("ПН", callback_data='529_upperDay1'),
                     types.InlineKeyboardButton("ВТ", callback_data='529_upperDay2'),
                     types.InlineKeyboardButton("СР", callback_data='529_upperDay3'),
                     types.InlineKeyboardButton("ЧТ", callback_data='529_upperDay4'),
                     types.InlineKeyboardButton("ПТ", callback_data='529_upperDay5'),
                     types.InlineKeyboardButton("СБ", callback_data='529_upperDay6')],

                    [types.InlineKeyboardButton("ПН", callback_data='529_lowerDay1'),
                     types.InlineKeyboardButton("ВТ", callback_data='529_lowerDay2'),
                     types.InlineKeyboardButton("СР", callback_data='529_lowerDay3'),
                     types.InlineKeyboardButton("ЧТ", callback_data='529_lowerDay4'),
                     types.InlineKeyboardButton("ПТ", callback_data='529_lowerDay5'),
                     types.InlineKeyboardButton("СБ", callback_data='529_lowerDay6')],
                   ]
        self.daysKeyboard_529 =  types.InlineKeyboardMarkup(keyboard)

    def loadRoomsButtons(self):
        self.roomsKeyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Г-525")
        item2=types.KeyboardButton("Г-529")
        self.roomsKeyboard.add(item1)
        self.roomsKeyboard.add(item2)

    def showDayInfo(self, room_num = 525, room = 'u', day = 0,):
        check: bool = True
        text = "Расписание для кабинета {0}\n\n".format("Г-525" if room == 'u' else "Г-529")
        if room_num == 525:
            if (room == 'u'):
                LIST = self.room525['upper'][list(self.room525['upper'].keys())[day]]
                if len(LIST) > 0:
                    text += "Кабинет свободен в период:\n\n"
                    for time in LIST:
                        time = time.split('-')
                        text += "с {0} до {1}\n".format(time[0],time[1])
                else:
                    check = False
            else:
                LIST = self.room525['lower'][list(self.room525['lower'].keys())[day]]
                if len(LIST) > 0:
                    text += "Кабинет свободен в период:\n\n"
                    for time in LIST:
                        time = time.split('-')
                        text += "с {0} до {1}\n".format(time[0],time[1])
                else:
                    check = False
        else:
            if (room == 'u'):
                LIST = self.room529['upper'][list(self.room529['upper'].keys())[day]]
                if len(LIST) > 0:
                    text += "Кабинет свободен в период:\n\n"
                    for time in LIST:
                        time = time.split('-')
                        text += "с {0} до {1}\n".format(time[0],time[1])
                else:
                    check = False
            else:
                LIST = self.room529['lower'][list(self.room529['lower'].keys())[day]]
                if len(LIST) > 0:
                    text += "Кабинет свободен в период:\n\n"
                    for time in LIST:
                        time = time.split('-')
                        text += "с {0} до {1}\n".format(time[0],time[1])
                else:
                    check = False
        if  check:
            text += "\n\nСейчас идет {0} неделя".format("верхняя" if datetime.now().isocalendar()[1] % 2 == 0 else "нижняя") 
            return text
        else:
            text += "К сожалению, нету свободных пар :c"
            return text


    def help(self, message):
        if (self.lastUpdate != date.today()):
            self.preloadInformation(0)
        if (self.roomsKeyboard == None):
            self.loadRoomsButtons()
        self.telegram_bot.reply_to(message, text=HELP_TEMPLATE, parse_mode= 'Markdown',reply_markup=self.roomsKeyboard)

        
    def showInformation(self,message, room = 1):
        if (self.lastUpdate != date.today()):
            self.preloadInformation(0)
        if (self.daysKeyboard_525 == None or self.daysKeyboard_529 == None):
            self.loadDaysButtons()
        if room:
            self.telegram_bot.send_message(message.chat.id, text="Расписание кабинета 525", reply_markup=self.daysKeyboard_525)
        else:
            self.telegram_bot.send_message(message.chat.id, text=f"Расписание кабинета 529", reply_markup=self.daysKeyboard_529)
    


      
    def run(self):
        
        @self.telegram_bot.message_handler(commands=['help', 'start'])
        def help_handler(message):
            self.help(message)

        @self.telegram_bot.message_handler(content_types=['text'])
        def text_handler(message):
            if message.text=="Г-525": self.showInformation(message)
            elif message.text=="Г-529": self.showInformation(message, 0)
            else:
                self.telegram_bot.reply_to(message, text=f"Я ничего не нашел.\n\nВарианты запроса: Г-525 или Г-529")

        @self.telegram_bot.callback_query_handler(func=lambda call: True)
        def callback_data(message):
            try:
                if '525' in message.data:
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text=self.showDayInfo(525, message.data[4], (int(message.data[-1])-1)),
                                                        reply_markup= self.daysKeyboard_525)
                elif '529' in message.data:
                    self.telegram_bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                                        text=self.showDayInfo(529, message.data[4], (int(message.data[-1])-1)),
                                                        reply_markup= self.daysKeyboard_529)
                else:
                    pass
            except Exception as ex:
                print(ex)

        self.telegram_bot.polling()

if __name__ == '__main__':
    bot = TelegramBot(TELEGRAM_TOKEN)
    bot.preloadInformation()
    bot.run()