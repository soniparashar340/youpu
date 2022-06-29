import os
import telebot
from config import API_KEY

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(command=['start'])
def start(message):
  bot.send_message(message, "hey hows it going?)
                   
bot.polling()
                   
