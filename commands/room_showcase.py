import telebot
from telebot import types
from datetime import date, datetime

from .templates.user_default_keyboard import USER, VOLUNTEER, OWNER
from .templates.keyboard_templates import KEYBOARD_525, KEYBOARD_529, USER_REGISTER, ROOM_REGISTER
from .templates.core import ROOM_525, ROOM_529
from .misis_lk import Schedule

class Room:
    def __init__(self) -> None:
        self.parser = Schedule()
        self.daysKeyboard_525 = None
        self.daysKeyboard_529 = None
        self.UserRegister = None
        self.RoomRegisterKeyboard = None
        self.UserKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.VolunteerKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.OwnerKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.lastUpdate = None
        self.room525 = {}
        self.room529 = {}


    def preloadInformation(self, value = 1):
        if (value):
            print("Парсинг информации с lk misis")
            for item in USER:
                self.UserKeyboard.add(item)
            for item in VOLUNTEER:
                self.VolunteerKeyboard.add(item)
            for item in OWNER:
                self.OwnerKeyboard.add(item)
        else:
            print("Обновление информации")
        self.room525['upper'] = self.parser.getSchedule(ROOM_525, self.parser.startDate(1))
        self.room525['lower'] = self.parser.getSchedule(ROOM_525, self.parser.startDate(0))

        self.room529['upper'] = self.parser.getSchedule(ROOM_529, self.parser.startDate(1))
        self.room529['lower'] = self.parser.getSchedule(ROOM_529, self.parser.startDate(0))
        print("Вся информация загружена, бот запускается...")


        return date.today()

    def loadDaysButtons(self):
        self.daysKeyboard_525 =  types.InlineKeyboardMarkup(KEYBOARD_525)
        self.daysKeyboard_529 =  types.InlineKeyboardMarkup(KEYBOARD_529)
        self.UserRegister = types.InlineKeyboardMarkup()
        for item in USER_REGISTER:
            self.UserRegister.add(item)
        self.RoomRegisterKeyboard = types.InlineKeyboardMarkup()
        for item in ROOM_REGISTER:
            self.RoomRegisterKeyboard.add(item)

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
            text += "\n\nСейчас вы просматриваете {0} неделю".format("текущую" if datetime.now().isocalendar()[1] % 2 == 0 else "следующую") 
            return text
        else:
            text += "К сожалению, нету свободных пар :c"
            return text