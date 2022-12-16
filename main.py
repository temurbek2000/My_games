from telegram.ext import Updater,CallbackQueryHandler,CommandHandler,MessageHandler,Filters, ConversationHandler

from constants.constants import BOT_TOKEN
from functions.functions import *

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            'main': [MessageHandler(Filters.text,enter_name)],
            'phone': [
                MessageHandler(Filters.text, phone_send)
            ],
            'menu': [
                MessageHandler(Filters.contact, menu)
            ],
            'menu_select': [
                MessageHandler(Filters.text, menu_select)
            ],
            'contact': [
                MessageHandler(Filters.text, contact)
            ],
            'change': [
                MessageHandler(Filters.text, change)
            ],
            'lang_change': [
                MessageHandler(Filters.text, lang_change)
            ],
            'phone_change': [
                MessageHandler(Filters.text, phone_change)
            ],
            'game_select': [
                MessageHandler(Filters.text,game_select)
            ],
            'package_select': [
                MessageHandler(Filters.text,package_select)
            ],
            'buy_select': [
                MessageHandler(Filters.text,buy_select)
            ],
            # 'product': [
            #     CallbackQueryHandler(classess)
            # ],
            # 'selected': [
            #     CallbackQueryHandler(Selected)
            # ],
            # 'tasdiq': [
            #     MessageHandler(Filters.photo, photo_handler)
            # ],

        },
        fallbacks=[
            CommandHandler('start', start)
        ]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


main()
