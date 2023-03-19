import telebot
from telebot import types

KEYBOARD_525 = [[types.InlineKeyboardButton("ПН", callback_data='525_upperDay1'),
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
KEYBOARD_529 = [[types.InlineKeyboardButton("ПН", callback_data='529_upperDay1'),
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

REG_KEYBOARD_529 = [[types.InlineKeyboardButton("ПН", callback_data='529_reg_upperDay1'),
                     types.InlineKeyboardButton("ВТ", callback_data='529_reg_upperDay2'),
                     types.InlineKeyboardButton("СР", callback_data='529_reg_upperDay3'),
                     types.InlineKeyboardButton("ЧТ", callback_data='529_reg_upperDay4'),
                     types.InlineKeyboardButton("ПТ", callback_data='529_reg_upperDay5'),
                     types.InlineKeyboardButton("СБ", callback_data='529_reg_upperDay6')],

                    [types.InlineKeyboardButton("ПН", callback_data='529_reg_lowerDay1'),
                     types.InlineKeyboardButton("ВТ", callback_data='529_reg_lowerDay2'),
                     types.InlineKeyboardButton("СР", callback_data='529_reg_lowerDay3'),
                     types.InlineKeyboardButton("ЧТ", callback_data='529_reg_lowerDay4'),
                     types.InlineKeyboardButton("ПТ", callback_data='529_reg_lowerDay5'),
                     types.InlineKeyboardButton("СБ", callback_data='529_reg_lowerDay6')],
                    [types.InlineKeyboardButton("Забронировать", callback_data='reg_day_append')],
                   ]

REG_KEYBOARD_525 = [[types.InlineKeyboardButton("ПН", callback_data='525_reg_upperDay1'),
                   types.InlineKeyboardButton("ВТ", callback_data='525_reg_upperDay2'),
                   types.InlineKeyboardButton("СР", callback_data='525_reg_upperDay3'),
                   types.InlineKeyboardButton("ЧТ", callback_data='525_reg_upperDay4'),
                   types.InlineKeyboardButton("ПТ", callback_data='525_reg_upperDay5'),
                   types.InlineKeyboardButton("СБ", callback_data='525_reg_upperDay6')],

                  [types.InlineKeyboardButton("ПН", callback_data='525_reg_lowerDay1'),
                   types.InlineKeyboardButton("ВТ", callback_data='525_reg_lowerDay2'),
                   types.InlineKeyboardButton("СР", callback_data='525_reg_lowerDay3'),
                   types.InlineKeyboardButton("ЧТ", callback_data='525_reg_lowerDay4'),
                   types.InlineKeyboardButton("ПТ", callback_data='525_reg_lowerDay5'),
                   types.InlineKeyboardButton("СБ", callback_data='525_reg_lowerDay6')],
                  [types.InlineKeyboardButton("Забронировать", callback_data='reg_day_append')],
                 ]

USER_REGISTER = [types.InlineKeyboardButton("Одобрить", callback_data='register_Y'),
                  types.InlineKeyboardButton("Отказать", callback_data='register_N')]

ROOM_REGISTER = [types.InlineKeyboardButton("525", callback_data='register_525'),
                  types.InlineKeyboardButton("529", callback_data='register_529')]