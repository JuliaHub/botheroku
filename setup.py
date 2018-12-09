import telebot
from telebot.types import Message


TOKEN = '702156751:AAEBEQyrkY-wwvOuEileZ02CxmfMKG4RHCU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.reply_to(message, 'help command helpi')  

@bot.message_handler(content_types=['text'])
def message_handler(message: Message):
    bot.reply_to(message, 'test reply newwwwwww')

  
bot.polling()