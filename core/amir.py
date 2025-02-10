import telebot
import os
from telebot.types import *

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

user = {}
course = {
    "spring": ["ccna", "mcsa", "python for beginner"],
    "summer": ["Sql Server", "MongoDB", "python for advanced"],
    "autumn": ["icdl", "seller", "photoshop"],
    "winter": ["photoshop", "c", "after effect", "3D max"],
}
@bot.message_handler(commands=["start"])
def start_message(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="please select one of our options")
    markup.add(
        KeyboardButton("Courses"),
        KeyboardButton("Home"),
        KeyboardButton("Call with Ac"),
    )
    user = {}
    bot.send_message(message.chat.id, 'select one Our options', reply_markup=markup)#
def see_course_season(message):
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="please select one season", row_width=4)
    markup.add(
        KeyboardButton("spring"),
        KeyboardButton("summer"),
        KeyboardButton("autumn"),
        KeyboardButton("winter"),
    )
    markup.add(
        KeyboardButton("Home"),
    )
    bot.send_message(message.chat.id, 'select one season', reply_markup=markup)#

def see_calling_and_info(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="for back to home press Home button")
    markup.add(
        KeyboardButton("Home"),
    )
    bot.send_message(message.chat.id, 'for call to Ac give This number\n**09123456789**\n', reply_markup=markup)#
def spring_courses(message):
    markup = InlineKeyboardMarkup()
    for cr in course["spring"]:
        markup.add(InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)#
def summer_courses(message):
    markup = InlineKeyboardMarkup()
    for cr in course["summer"]:
        markup.add(InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)#
def autumn_courses(message):
    markup = InlineKeyboardMarkup()
    for cr in course["autumn"]:
        markup.add(InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)#
def winter_courses(message):
    markup = InlineKeyboardMarkup()
    for cr in course["winter"]:
        markup.add(InlineKeyboardButton(cr, callback_data=cr))
    bot.send_message(message.chat.id, 'for register course click on it', reply_markup=markup)#
@bot.callback_query_handler(func=lambda call: True )
def handle_register_course(call):
    user["course"] = call.data
    message = call.message
    text = """
    please insert your name and family
"""
    bot.reply_to(message, text )
    bot.register_next_step_handler(message, insert_basic_info)#
def insert_basic_info(message):
    user["info"] = message.text
    text = """
    please insert your phone number
    """
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, insert_phone_number)#
def insert_phone_number(message):
    user["phone"] = message.text
    text = """
    pre_register complete successfully
"""
    bot.reply_to(message, text)
    with open("./export/register.txt", "a") as file:
        file.write(
            f"{user['season']}\n=============\n{user['info']}\n=============\n{user['phone']}\n=============\n{user['course']}\n***********************\n"
            )
    start_message(message)

@bot.message_handler(func=lambda message: True)
def other_message(message):
    if message.text == "Courses":
        see_course_season(message)
    elif message.text == "Home":
        start_message(message)
    elif message.text == "Call with Ac":
        see_calling_and_info(message)
    elif message.text == "spring":
        user["season"] = message.text
        spring_courses(message)
    elif message.text == "summer":
        user["season"] = message.text
        summer_courses(message)
    elif message.text == "autumn":
        user["season"] = message.text
        autumn_courses(message)
    elif message.text == "winter":
        user["season"] = message.text
        winter_courses(message)#


bot.infinity_polling()