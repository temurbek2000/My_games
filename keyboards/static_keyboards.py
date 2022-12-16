from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup([['Games'], ['Settings', 'Contacts']], resize_keyboard=True)
settings_keyboard = ReplyKeyboardMarkup([['Change Language'], ['Change Phone'],['◀Orqaga Uz']], resize_keyboard=True)
phone_keyboard = ReplyKeyboardMarkup([[KeyboardButton('Share contact', request_contact=True)]], resize_keyboard=True)
ortga = ReplyKeyboardMarkup([['◀Orqaga Uz']], resize_keyboard=True)
confirm_keyboard = ReplyKeyboardMarkup([['✅  TASDIQLASH']], resize_keyboard=True)