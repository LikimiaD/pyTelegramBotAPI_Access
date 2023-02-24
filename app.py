#pip install pyTelegramBotAPI
import telebot
from settings import TELEGRAM_TOKEN
from templates import HELP_TEMPLATE, ERROR_TEMPLATE
from events import Events

from telebot import types

class TelegramBot:
    def __init__(self, telegram_token):
        self.telegram_bot = telebot.TeleBot(telegram_token)
        self.events = Events()

    def help(self, message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Г-521")
        item2=types.KeyboardButton("Г-525")
        markup.add(item1)
        markup.add(item2)
        self.telegram_bot.reply_to(message, text=HELP_TEMPLATE, parse_mode= 'Markdown',reply_markup=markup)
    def Kab521(self,message):
        '''
        markup=types.InlineKeyboardMarkup()
        item1= types.InlineKeyboardButton(text="ПН",switch_inline_query="")
        item2= types.InlineKeyboardButton(text="ВТ",switch_inline_query="Telegram")
        markup.add(item1,item2)
        '''
        keyboard = [[types.InlineKeyboardButton("ПН", callback_data='HElist8'),
                         types.InlineKeyboardButton("ВТ", callback_data='HRlist8'),
                        types.InlineKeyboardButton("СР", callback_data='CClist8'),
                          types.InlineKeyboardButton("ЧТ", callback_data='SPlist8'),
                        types.InlineKeyboardButton("ПТ", callback_data='CFlist8'),
                          types.InlineKeyboardButton("СБ", callback_data='ALLlist8'),
                            types.InlineKeyboardButton("ВС", callback_data='CFlist8')],
                    [types.InlineKeyboardButton("ПН", callback_data='HElist8'),
                         types.InlineKeyboardButton("ВТ", callback_data='HRlist8'),
                        types.InlineKeyboardButton("СР", callback_data='CClist8'),
                          types.InlineKeyboardButton("ЧТ", callback_data='SPlist8'),
                        types.InlineKeyboardButton("ПТ", callback_data='CFlist8'),
                          types.InlineKeyboardButton("СБ", callback_data='ALLlist8'),
                            types.InlineKeyboardButton("ВС", callback_data='CFlist8')]
                   ]
        
        markup =  types.InlineKeyboardMarkup(keyboard)
      
        self.telegram_bot.send_message(message.chat.id, text="Расписание кабинета Г-521", reply_markup=markup)

    '''def Kab525(self,message):
        markup=types.ReplyKeyboardMarkup()
        #markup.add(item)
        self.telegram_bot.send_message(message.chat.id, text="Расписание кабинета Г-525",reply_markup=markup)
    '''
    


    def echo(self, message):
        self.telegram_bot.reply_to(message, text="Затычка")
      
    def run(self):
        
        @self.telegram_bot.message_handler(commands=['help', 'start'])
        def help_handler(message):
            self.help(message)

        @self.telegram_bot.message_handler(content_types=['text'])
        def text_handler(message):
            if message.text=="Г-521": self.Kab521(message)
            elif message.text=="Г-525": self.Kab525(message)

        self.telegram_bot.polling()

if __name__ == '__main__':
    bot = TelegramBot(TELEGRAM_TOKEN)
    bot.run()