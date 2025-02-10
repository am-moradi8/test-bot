import telebot
import os
from telebot import types

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('btn1' , callback_data='btn1')
    b2 = types.InlineKeyboardButton('btn2' , callback_data='btn2')
    markup.add(b1 , b2)
    bot.reply_to(message , 'متن دلخواه' , reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'btn1')
def run(call):
    message = call.message
    bot.answer_callback_query(call.id , 'amirrrrrr')
    bot.send_message(message.chat.id , 'متن')

@bot.callback_query_handler(func=lambda call: call.data == 'btn2')
def run2(call):
    message = call.message
    bot.answer_callback_query(call.id , '22222222')
    bot.send_message(message.chat.id , 'عکس')






bot.infinity_polling()