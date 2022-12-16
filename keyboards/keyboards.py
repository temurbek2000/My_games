from connections.connect import *
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup


lang_keyboard = ReplyKeyboardMarkup([['Uz','Ru'],['◀Orqaga Uz']], resize_keyboard=True)
buy_keyboard = ReplyKeyboardMarkup([['Sotib olish'],['◀Orqaga Uz']], resize_keyboard=True)




def package_keyboard(g_name):
    packages=[]
    game = get_game_by_name(g_name)
    if game:
        data = get_packages_by_game_id(game[0][0])
        for i in range(0, len(data)):
            a = []
            a.append(str(data[i][2]))
            packages.append(a)

    packages.append(['Ortga'])
    return packages