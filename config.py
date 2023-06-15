from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

deck = [rank+suit for suit in [str(n) for n in range(6,11)]+list("JQKA") for rank in "♠ ♣ ♦ ♥".split()]

TOKEN_API = "6253605508:AAHhbR56X-wkVtrJiSGwVG848T3P-EsFgFA"
hello = "<i><b>Вітаю!</b> Дякую що користуєтесь мною.<b>\n(П.С.Убийте мене!)</b></i>"

HELP_COMAND = """
<em><b>/help</b> - Список команд.</em>
<em><b>/start</b> - Привітання.</em>
<em><b>/stiker_pak</b> - Список стикерів.</em>
<em><b>/mem</b> - Забавна картинка.</em>
<em><b>/durack</b> - Гра у крти.</em>
<em><b>/sport</b> - Гіфка зі спортиком.</em>
<em><b>/links</b> - Посилання на соц иережі.</em>
<em><b>Якесь слово</b> - Озвучка українською.</em>
<em><b>Вова криворуке чмо тому будь ласка без спаму!</b></em>
"""
stickers ={"/Pofig":     "CAACAgIAAxkBAAEJI9NkdGPYL8zXvlnrbU_ADR37D16c6QACxSUAAt96wEp8QesJp_LSuy8E",
           "/Death":     "CAACAgIAAxkBAAEJI9lkdGSWpWh5XIxvZxpIvcw3t7f4vQACIiwAAvw6wEraQYjvJty_3y8E",
           "/Rat":       "CAACAgIAAxkBAAEJI-ZkdGZgY0Riu120DuInYQOdfQWHkAACDiwAAvqqwErJjEgOuayc1y8E",
           "/Homeless":  "CAACAgIAAxkBAAEJI-hkdGaHmX-nXTexgAE4y-qh3umj7QACIysAAoUjwUqleWsCg75n0C8E",
           "/Bitch":     "CAACAgIAAxkBAAEJI-pkdGa5VaUFcrjI8O1xFuFoA5Jh2gACqiMAAjzfwEqj2uFR8ikYcS8E",
           "/To_factory":"CAACAgIAAxkBAAEJI-xkdGbOyZnHAfD_z6CO6oClyaUoMgACoicAAmoywEo11yGuVxRJzS8E",
           "/Tracking":  "CAACAgIAAxkBAAEJI-5kdGbhM8dMmcE4JjjYLD2iT89qVAACmCYAArytwErXyhviyke6ky8E",
           "/Salty":     "CAACAgIAAxkBAAEJI_BkdGbzGRNHvqxa4rfUepVErHA2UgACOygAAuMLCEu3WpH_lHheTS8E",
           "/Humanitari":"CAACAgIAAxkBAAEJI_JkdGcQ6Z7E-kcHKVobY2i96NGduQACNycAAlaHCUtt_jD9fA6d3C8E",
           "/Fear":      "CAACAgIAAxkBAAEJI_RkdGc3hoOjJfF71BvNMh3re-YDHwACVCkAAmAW0UoMeGSGw8_Hvi8E",
           "/Search":    "CAACAgIAAxkBAAEJI_ZkdGdGfwUZ5FW_fYO2m8JutXghtgACWh8AAmgByErstOmzEjh6YS8E",
           "/Borov":     "CAACAgIAAxkBAAEJI_hkdGdcIh-LjlBSmBHNk6EzjA1oOQACtiIAAs5xwEqKC0D8dN8UsS8E",
           "/Pennywise": "CAACAgIAAxkBAAEJI_pkdGd7Ijm7d163MKNn7hD6eCD-ngACkygAAlKGKUuvxRL7oWEvli8E",
           "/Clown":     "CAACAgIAAxkBAAEJI_xkdGi-9gn5_OC3cJ-ghZvjLMomKwACLS8AAvhmqEvv9EHk3XeECS8E"}

def start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(KeyboardButton("/start"),KeyboardButton("/help"),KeyboardButton("/links"))
    kb.row(KeyboardButton("/stiker_pak"),KeyboardButton("/mem"),KeyboardButton("/durack"))
    return kb

def links_ikb():
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='GitHub',url="https://github.com/Vervol03")
    ib2 = InlineKeyboardButton(text='Telegram',url="https://t.me/Veres_VR")
    ikb.add(ib1,ib2)
    return ikb

def card_kb(player):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(player)-len(player)%3, 3):
        kb.row(KeyboardButton(player[i]),KeyboardButton(player[i+1]),KeyboardButton(player[i+2]))
    if len(player)%3==2: kb.row(KeyboardButton(player[-2]),KeyboardButton(player[-1]))
    if len(player)%3==1: kb.row(KeyboardButton(player[-1]))
    return kb

def card_kb_P(player):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(player)-len(player)%3, 3):
        kb.row(KeyboardButton(player[i]),KeyboardButton(player[i+1]),KeyboardButton(player[i+2]))
    if len(player)%3==2: kb.row(KeyboardButton(player[-2]),KeyboardButton(player[-1]),KeyboardButton("Не підкидати"))
    if len(player)%3==1: kb.row(KeyboardButton(player[-1]),KeyboardButton("Не підкидати"))
    if len(player)%3==0: kb.row(KeyboardButton("Не підкидати"))
    return kb

def card_kb_Z(player):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(player)-len(player)%3, 3):
        kb.row(KeyboardButton(player[i]),KeyboardButton(player[i+1]),KeyboardButton(player[i+2]))
    if len(player)%3==2: kb.row(KeyboardButton(player[-2]),KeyboardButton(player[-1]),KeyboardButton("Забрати"))
    if len(player)%3==1: kb.row(KeyboardButton(player[-1]),KeyboardButton("Забрати"))
    if len(player)%3==0: kb.row(KeyboardButton("Забрати"))
    return kb