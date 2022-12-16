from telegram import ReplyKeyboardMarkup

from connections.connect import get_languages, get_games, get_payments


def language_keyboard():
    languages = []
    data = get_languages()
    if len(data)%2==0:
        for i in range(0, len(data), 2):
            a = [f'{data[i][1]}',f'{data[i+1][1]}']
            languages.append(a)
    else:
        for i in range(0, len(data)-1, 2):

            a = [f'{data[i][1]}',f'{data[i+1][1]}']
            languages.append(a)

        languages.append([
            str(data[len(data)-1][1])
        ])

    return  languages


def games_keyboard():
    games=[]
    data = get_games()
    for i in range(0, len(data)):
        a = [f'{data[i][0]}']
        games.append(a)
    games.append(['Ortga'])
    return games

def payment_keyboards():
    data = get_payments()
    payments = []
    for i in range(0, len(data)):
        a = [f'{data[i][1]}']
        payments.append(a)
    payments.append(['Ortga'])
    return payments

