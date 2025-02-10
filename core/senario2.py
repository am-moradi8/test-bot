import telebot
import os
from telebot import *

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

list_btn = ['Back']




@bot.message_handler(commands=['start'])
def Start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    start_btn1 = types.KeyboardButton('Courses')
    start_btn2 = types.KeyboardButton('Back')
    start_btn3 = types.KeyboardButton('Information')
    markup.add(start_btn1 , start_btn2 , start_btn3)
    bot.reply_to(message , 'Choose one of the options below.' , reply_markup=markup)


# def information(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
#     bot.reply_to(message , 'School contact number')
#     for info in list_btn:
#         markup.add(types.KeyboardButton(information))
#     bot.reply_to(message , 'در صورت نیاز با این شماره\n**08612345**\n   تماس بگیرید' , reply_markup=markup)

@bot.message_handler(commands=['Information'])
def information(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
    for info in list_btn:
        markup.add(types.KeyboardButton(information))
    bot.reply_to(message , 'در صورت نیاز با این شماره\n**08612345**\n   تماس بگیرید' , reply_markup=markup)


def cour(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=4)
    bot.reply_to(message , 'Choose one of the options below.')
    btn_cour1 = types.KeyboardButton('Spring')
    btn_cour2 = types.KeyboardButton('Summer')
    btn_cour3 = types.KeyboardButton('Autumn')
    btn_cour4 = types.KeyboardButton('Winter')
    btn_cour5 = types.KeyboardButton('Back')
    markup.add(btn_cour1 , btn_cour2 , btn_cour3 , btn_cour4 , btn_cour5)
    bot.reply_to(message , 'Choose a season' , reply_markup=markup)










@bot.message_handler(func=lambda message: True)
def btn(message):
    if message.text == 'Back':
        Start_message(message)
    elif message.text == 'Information':
        information(message)
    elif message.text == 'Courses':
        cour(message)
    # elif message.text in list_Season:
    #     show_Cour(message)
    # elif message.text == "Spring":
    #     user_info['Season'] = message.text
    # elif message.text == 'Summer':
    #     user_info['Summer'] = message.text
    # elif message.text =='Autumn':
    #     user_info['Autumn'] = message.text
    # elif message.text =='Winter':
    #     user_info['Winter'] = message.text


bot.infinity_polling()