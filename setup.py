import telebot
from telebot.types import Message
import os 

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.reply_to(message, 'help command helpi token heroku')  

@bot.message_handler(content_types=['text'])
def message_handler(message: Message):
    bot.reply_to(message, 'test reply newwwwwww  token heroku')

  
bot.polling()