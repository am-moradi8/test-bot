import telebot
# from googletrans import Translator
import os
# import logging
from telebot import types

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

API_TOKEN = os.environ.get('API_TOKEN')

# translator = Translator()

bot = telebot.TeleBot(API_TOKEN)

list_butten = ['Home' , 'b1' , 'b2' , 'b3']

# user_info = {

# }

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    btn1 = types.KeyboardButton('Home')
    btn2 = types.KeyboardButton('Contact')
    btn3 = types.KeyboardButton('About')
    markup.add(btn1 , btn2 , btn3)
    bot.reply_to(message , 'یکی از دکمه های زیر را انتخاب کنید' , reply_markup=markup)

def contact(message):
    bot.reply_to(message , 'متن contact')

def about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    for about in list_butten:
        markup.add(types.KeyboardButton(about))
    bot.reply_to(message , 'plasse in butten' , reply_markup=markup)
    


@bot.message_handler(func=lambda message: True)
def btn(message):
    if message.text == 'Home':
        start(message)
    elif message.text == 'Contact':
        contact(message)
    elif message.text == 'About':
        about(message)




# @bot.message_handler(commands=['start'])
# def start_bot(message):
#     bot.reply_to(message , 'نام و نام خانوادگی خود را وارد کنید')
#     bot.register_next_step_handler(message , phone_number)

# def phone_number(message):
#     user_info['name'] = message.text
#     bot.reply_to(message , 'لظفا شماره خود را وارد کنید')
#     bot.register_next_step_handler(message , adres)

# def adres(message):
#     user_info['phone'] = message.text
#     bot.reply_to(message , 'لظفا ادرس خود را وارد کنید')
#     bot.register_next_step_handler(message , finish)

# def finish(message):
#     user_info['adres'] = message.text
#     print(user_info)
#     bot.reply_to(message , 'ثبت نام شما با موفقیت به پایان رسید')
    # with open("./info.txt" , "a") as file:
    #     for key in user_info:
    #         file.write(user_info[key]+"\n")










# @bot.message_handler(func=lambda message:True)
# def wellcome_messege(messege):
#     translated_text = translator.translate(messege.text , src='en' , dest='fa')
#     bot.reply_to(messege , translated_text.text)




bot.infinity_polling()