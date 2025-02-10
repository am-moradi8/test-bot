import telebot
import os
from telebot import *
# from telebot import types
# from telebot import InlineKeyboardMarkup
# from telebot import InlineKeyboardButton

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

user_info = {}

list_btn = ['Back']

list_Season = {
    'Spring': ['ccna' , 'lpic' , 'django', "icdl"],
    'Summer': ['mcsa' , 'ccnp'],
    'Autumn': ['python' , 'photoshop' , 'C#'],
    'Winter': ['django2' , 'python' ' net +'],

}

@bot.message_handler(commands=['start'])
def Start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    start_btn1 = types.KeyboardButton('Courses')
    start_btn2 = types.KeyboardButton('Back')
    start_btn3 = types.KeyboardButton('Information')
    markup.add(start_btn1 , start_btn2 , start_btn3)
    bot.reply_to(message , 'Choose one of the options below.' , reply_markup=markup)
    user_info = {}



def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
    bot.reply_to(message , 'School contact number')
    for info in list_btn:
        markup.add(types.KeyboardButton(info))
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


def spring_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in list_Season["Spring"]:
        markup.add(types.InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)
def summer_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in list_Season["Summer"]:
        markup.add(types.InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)
def autumn_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in list_Season["Autumn"]:
        markup.add(types.InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)
def winter_courses(message):
    markup = types.InlineKeyboardMarkup()
    for cr in list_Season["Winter"]:
        markup.add(types.InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True )
def handle_register_course(call):
    user_info["course"] = call.data
    message = call.message
    text = """
    please insert your name and family
"""
    bot.reply_to(message, text )
    bot.register_next_step_handler(message, insert_basic_info)#
def insert_basic_info(message):
    user_info["info"] = message.text
    text = """
    please insert your phone number
    """
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, insert_phone_number)#
def insert_phone_number(message):
    user_info["phone"] = message.text
    text = """
    pre_register complete successfully
"""
    bot.reply_to(message, text)
    with open("./export/register.txt", "a") as file:
        file.write(
            f"{user_info['season']}\n=============\n{user_info['info']}\n=============\n{user_info['phone']}\n=============\n{user_info['course']}\n***********************\n"
            )
    Start_bot(message)







def show_Cour(message):
    Seasons = message.text.lower()
    courses = list_Season.get(Seasons , [])
    markup = types.InlineKeyboardMarkup()
    for course in courses:
        markup.add(types.InlineKeyboardMarkup(course, callback_data=course))
    bot.reply_to(message, 'Courses to register for:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message = call.message
    bot.reply_to(message , 'نام و نام خانوادگی خود را وارد کنید:')
    user_info['course'] = call.data
    bot.register_next_step_handler(message , get_name)


def get_name(message):
    user_info['name'] = message.text
    bot.reply_to(message , 'شماره تلفن خود را وارد کنید')
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    phone_number = message.text
    if phone_number.isdigit():
        user_info['phone'] = phone_number
        bot.reply_to(message , 'پیش ثبت نام شما با موفقیت انجام شد')
        bot.reply_to(message , 'منتظر تماس ما برای آغاز کلاس ها باشید')
        with open('./info.text' , 'r') as file:
            for key in user_info:
                file.write(user_info[key])


@bot.message_handler(func=lambda message: True)
def btn(message):
    if message.text == 'Back':
        Start_bot(message)
    elif message.text == 'Information':
        info(message)
    elif message.text == 'Courses':
        cour(message)
    elif message.text in list_Season:
        show_Cour(message)
    elif message.text == "Spring":
        user_info['Season'] = message.text
    elif message.text == 'Summer':
        user_info['Summer'] = message.text
    elif message.text =='Autumn':
        user_info['Autumn'] = message.text
    elif message.text =='Winter':
        user_info['Winter'] = message.text


bot.infinity_polling()