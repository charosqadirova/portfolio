import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Men haqimda")
    btn2 = types.KeyboardButton("Loyihalarim")
    btn3 = types.KeyboardButton("Bog'lanish")
    btn4 = types.KeyboardButton("Qobiliyatlarim")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    text = "telegram botiga xush kelibsiz! Quyidagi tugmalardan birini tanlang:"

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def aboutme_handler(message):
    text = "O'quvchi"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Loyihalarim")
def projects_handler(message):
    text = "Bu qism tez orada qo'shiladi"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Bog'lanish")
def contact_handler(message):
    text = "Bog'lanish ma'lumotlari"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Qobiliyatlarim")
def skills_handler(message):
    text = "Qobiliyatlarim haqida ma'lumot"
    
    bot.send_message(message.chat.id, text)

bot.infinity_polling()