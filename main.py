import telebot
from telebot import types
import os
from dotenv import load_dotenv
from transliterate import to_cyrillic, to_latin

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  keyboard = types.ReplyKeyboardMarkup()
  button1 = types.KeyboardButton('Men haqimda')
  button2 = types.KeyboardButton('Loyihalarim')
  keyboard.add(button1, button2)
  text = "Assalom alaykum, botimizga xush kelibsiz \n quydagi tugmalardan birini tanlang"
  bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	print(message.text)
  if message.text == 'Men haqimda':
    bot.send_message(message.chat.id, "Men haqimda ma'lumot")
  elif message.text == 'Loyihalarim':
    bot.send_message(message.chat.id, "Loyihalarim haqida ma'lumot")
	
bot.infinity_polling()

# s = input()
# if s.isascii():
#     print(to_cyrillic(s))
# else:
#     print(to_latin(s))