import telebot
from telebot import TeleBot


bot = telebot.TeleBot('7042594009:AAGgaQtcRvbzVcO7nKlf8-hBNZOA_Li1bGs')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id4: [message.from_user.id]')
    


@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>',parse_mode='html')


bot.polling(none_stop=True)





