from telegram import InlineKeyboardMarkup, KeyboardButton

from keyboards.dynamic_keyboards import language_keyboard, games_keyboard
from keyboards.keyboards import *
from keyboards.static_keyboards import menu_keyboard, ortga, settings_keyboard, phone_keyboard, confirm_keyboard


def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tilni tanlang:",
                             reply_markup=ReplyKeyboardMarkup(language_keyboard(), resize_keyboard=True))
    return 'main'

def user_is_have(tg_id):
    data = get_data_users(tg_id)
    return data

def insert_user(language,tg_id):
    if len(user_is_have(tg_id))==0:
        add_data_user(language,tg_id)
def enter_name(update,context):
    message = update.message.text
    insert_user(message,update.message.from_user.id)
    if message=='Uz':
        my_text="Enter name Uz"
        previous = ReplyKeyboardMarkup([['◀Orqaga Uz']], resize_keyboard=True)
    elif message == "Ru":
        my_text="Enter name Ru"
        previous = ReplyKeyboardMarkup([['◀Orqaga Ru']], resize_keyboard=True)
    else:
        start(update,context)
    context.bot.send_message(chat_id=update.effective_chat.id, text=my_text,
                             reply_markup=previous)
    return 'phone'

def phone_send(update,context):
    message = update.message.text
    update_name(update.message.from_user.id,message)
    if message == '◀Orqaga Uz' or message == '◀Orqaga Ru':
        start(update,context)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Telefon raqamingizni yuboring:",
                                 reply_markup=phone_keyboard)
        return 'menu'

def menu(update,context):
    message = update.message.contact.phone_number
    update_phone(update.message.from_user.id,message)
    context.bot.send_message(chat_id=update.effective_chat.id, text="GamePin botga xush kelibsiz",
                                 reply_markup=menu_keyboard)
    return 'menu_select'

def menu_select(update,context):
    message = update.message.text
    if message == 'Contacts':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Agar sizda savollar bo'lsa bizga telefon qilishingiz mumkin: YY-XXX-XX-XX",
                                 reply_markup=ortga)

        return 'contact'
    elif message == "Settings":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Settings message",
                                 reply_markup=settings_keyboard)
        return 'change'
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Games",
                                 reply_markup=ReplyKeyboardMarkup(games_keyboard(),resize_keyboard=True))
        return 'game_select'


def contact(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="GamePin botga xush kelibsiz",
                             reply_markup=menu_keyboard)
    return "menu_select"

def change(update,context):
    message = update.message.text
    if message == '◀Orqaga Uz' or message == '◀Orqaga Ru':
        context.bot.send_message(chat_id=update.effective_chat.id, text="GamePin botga xush kelibsiz",
                                 reply_markup=menu_keyboard)
        return 'menu'
    elif message == "Change Language":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tilni tanlang:",
                                 reply_markup=lang_keyboard)
        return "lang_change"
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Telefon raqam yuboring:",
                                 reply_markup=phone_keyboard)
        return "phone_change"

def lang_change(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lang Saved!\n Select menu",
                             reply_markup=menu_keyboard)
    return "menu_select"

def phone_change(update,context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="Phone Saved!\n Select menu",
                             reply_markup=menu_keyboard)
    return "menu_select"

def game_select(update,context):
    message = update.message.text
    if message == "Ortga":
        menu(update,context)
        return 'menu_select'
    else:
        text = f"🎮 <{message}>\nQo'shimcha ma'lumotlar:\n1. <Paket nomi #1> - <Paket narxi #1>\n2. <Paket nomi #2> - <Paket narxi #2> "
        context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                                 reply_markup=ReplyKeyboardMarkup(package_keyboard(message), resize_keyboard=True))
        return "package_select"


def package_select(update,context):
    message = update.message.text
    if message == "Ortga":
        game_select(update,context)
    else:

        data = get_package_by_name(message)
        game_name = get_game_by_id(data[0][1])[0][0]
        add_product(get_game_by_name(game_name)[0][0],data[0][0],update.message.from_user.id,data[0][3])
        text = f"🎮 {game_name}\n" \
               f"📦 {message} \n" \
               f"💰 {data[0][3]} $"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                                 reply_markup=buy_keyboard)
        return 'buy_select'

def buy_select(update,context):
    message = update.message.text
    if message == "◀Orqaga Uz":
        game_select(update,context)
    else:
        tg_id = update.message.from_user.id
        product = get_products(tg_id)[-1]
        game_name = get_game_by_id(product[1])[0][0]
        package_name = get_package_by_id(product[2])[0][0]
        gamer_id = get_gamer_id_by_tg_id(tg_id)[0][0]
        text = f"Sizning buyurtmangiz:\n🎮 {game_name}\n" \
               f"📦 {package_name} \n" \
               f"💰 {product[4]} $\n " \
               f"🆔 {gamer_id} \n" \
               f"💻 1 \n" \
               f"Umumiy to'lov qiymati: {product[4]}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                                 reply_markup=confirm_keyboard)
        return 'confirm'




