from telebot import TeleBot
from config import token
from stock import Stock


def telegram_bot(token):
    bot = TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        hello_mess = f'Привет, {message.from_user.first_name} введи тикер акции и какую информацию хотите получить.\n' \
                     f'info - информация об акции\nhistory - график рыночных данных\ndiv - дивиденды\n' \
                     f'Например: aapl history'
        bot.send_message(message.chat.id, hello_mess)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        x = (str(message.text)).split()
        if x[1] in ['info', 'history', 'div']:
            try:
                msg = Stock(x[0])
                if x[1].lower() == 'info':
                    bot.send_message(message.chat.id, msg.info())
                if x[1].lower() == 'history':
                    msg.info()
                    msg.plot()
                    img = open('saved_figure.png', 'rb')
                    bot.send_photo(message.chat.id, img)
                if x[1].lower() == 'div':
                    bot.send_message(message.chat.id, f'{msg.div()}')
            except Exception:
                bot.send_message(message.chat.id, 'Введи корректный тикер')
        else:
            bot.send_message(
                message.chat.id,
                "Введи корректную команду"
            )

    bot.polling(none_stop=True)


if __name__ == '__main__':
    telegram_bot(token)
