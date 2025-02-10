import telebot
import os
from telebot import types

API_TOKEN = os.environ.get('API_TOKENN')
bot = telebot.TeleBot(API_TOKEN)

user_info = {}

glass = {
    'spring': ['ccna', 'lpic', 'django', 'icdl'],
    'summer': ['mcsa', 'ccnp'],
    'autumn': ['python', 'photoshop', 'C#'],
    'winter': ['django2', 'python', 'net+'],
}

list_butten = ['Back']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Contact')
    btn2 = types.KeyboardButton('Call_number')
    markup.add(btn1, btn2)
    bot.reply_to(message, 'یکی از دکمه های زیر را انتخاب کنید', reply_markup=markup)

@bot.message_handler(commands=['Call_number'])
def about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Back')
    markup.add(btn1)
    bot.reply_to(message, 'در صورت نیاز با شماره\n08612345\nتماس بگیرید', reply_markup=markup)

@bot.message_handler(commands=['Contact'])
def contact(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn1 = types.KeyboardButton('spring')
    btn2 = types.KeyboardButton('summer')
    btn3 = types.KeyboardButton('autumn')
    btn4 = types.KeyboardButton('winter')
    btn5 = types.KeyboardButton('Back')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.reply_to(message, 'یکی از فصل های زیر را انتخاب کنید', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def btn(message):
    if message.text == 'Back':
        start(message)
    elif message.text == 'Contact':
        contact(message)
    elif message.text == 'Call_number':
        about(message)
    elif message.text in glass:
        show_courses(message)

def show_courses(message):
    season = message.text.lower()
    courses = glass.get(season, [])
    markup = types.InlineKeyboardMarkup()
    for course in courses:
        markup.add(types.InlineKeyboardButton(course, callback_data=course))
    bot.reply_to(message, 'دوره ها:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message = call.message
    bot.reply_to(message, 'نام خود را وارد کنید')
    user_info['course'] = call.data
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_info['name'] = message.text
    bot.reply_to(message, 'شماره خود را وارد کنید')
    bot.register_next_step_handler(message, get_phone)
# def get_name(message):
#     user_info['name'] = message.text
#     bot.reply_to(message, 'شماره خود را وارد کنید')
#     bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    phone_number = message.text
    if phone_number.isdigit():
        user_info["phone"]=phone_number
        bot.reply_to(message, 'پیش ثبت نام شما انجام شد👌')
        with open("./info.txt", "a") as file:
          for key in user_info:
            file.write(f"{key}: {user_info[key]}\n")
    else:
        bot.reply_to(message,"لطفا فقط عدد وارد کنید ")
        bot.register_next_step_handler(message,get_phone)
bot.infinity_polling()