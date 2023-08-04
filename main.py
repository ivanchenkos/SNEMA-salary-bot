import os
import telebot
from dotenv import load_dotenv
from telebot.util import quick_markup

load_dotenv() # take environment variables from .env.
bot = telebot.TeleBot(os.environ['token'])

markup = quick_markup({
    'Twitter': {'url': 'https://twitter.com'},
    'Facebook': {'url': 'https://facebook.com'},
    'Back': {'callback_data': 'whatever'}
}, row_width=2)
# returns an InlineKeyboardMarkup with two buttons in a row, one leading to Twitter, the other to facebook
# and a back button below

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, os.environ['test_phrase'])

bot.infinity_polling()