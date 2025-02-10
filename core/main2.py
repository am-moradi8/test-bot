import telebot
import os
from telebot import *
import sqlite3


API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

user_image_database = {}
user_id_list = []

connection = sqlite3.connect("commercial_users.sqlite3", check_same_thread=False)
cursor = connection.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
   cursor.execute("""
                  CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  chat_id TEXT NOT NULL,
                  user_name TEXT);
                  """)
   cursor.execute("""
                   INSERT INTO user (chat_id, user_name) VALUES (?, ?);
                   """, [message.chat.id,message.from_user.username])
   connection.commit()
   bot.send_message(message.chat.id, "<b><i>WELCOME TO MY BOT</i></b>", parse_mode="HTML")


@bot.message_handler(commands=['amir0123'])
def start_message(message):
   users = cursor.execute("SELECT * FROM user")
   for user in users:
       bot.send_message(user[1], "<b>تخفیف ویژه فصل زمستان</b>", parse_mode="HTML")



# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.reply_to(message , 'hi\nwellcome to my bot')


# @bot.message_handler(commands=['send'])
# def send_photo(message):
#    bot.reply_to(message, """ 
#                 please send your photo for me
#                 after you send your photo , i will send for you unique photo id
#                 please note it because for recover your photo you will need it
#                 """)
#    bot.register_next_step_handler(message , send_from_user)

# def send_from_user(message):
#     if message.content_type == 'photo':
#         user_id = message.chat.id
#         file_id = message.photo[-1].file_id
#         bot.send_message(message.chat.id, "note this image code 📝")
#         bot.send_message(message.chat.id , file_id)
#         if user_id not in user_id_list:
#             user_id_list.append(user_id)
#             for user in user_id_list:
#                 if user not in user_image_database:
#                     user_image_database[user] = []
#                 else:
#                     user_image_database[user].append(file_id)
#             else:
#                 user_image_database[user_id].append(file_id)
#         print(user_image_database)


# @bot.message_handler(commands=['take'])
# def start_message(message):
#    bot.reply_to(message, """
#                 please insert your image unique id
#                 """)
#    bot.register_next_step_handler(message, send_image_for_user)#


# def send_image_for_user(message):
#    user_id = message.chat.id
#    image_id = message.text
#    if user_id in user_image_database:
#        for id in user_image_database[user_id]:
#            if image_id == id:
#                file_info = bot.get_file(image_id)
#                file = bot.download_file(file_info.file_path)
#                bot.send_photo(user_id, file)
#                break
#        else:
#            bot.send_message(user_id, "you have not any file in my database")
#    else:
#        user_image_database[user_id] = []
#        bot.send_message(user_id, "you have not any file in my database")



# @bot.message_handler(commands=['send_photo'])
# def send_photo_file(message):
#     photo = open(r'C:\Users\AMIR\OneDrive\Pictures\amir.jpg' , 'rb')
#     bot.send_photo(message.chat.id , photo)


# @bot.message_handler(commands=['send_video'])
# def send_video_file(message):
#     video = open(r'مسیر ویدیو مد نظر' , 'rb')
#     bot.send_video(message.chat.id , video)


# @bot.message_handler(commands=['send_audio'])
# def send_audio_file(message):
#     audio = open(r'مسیر فایل مد نظر' , 'rb')
#     bot.send_audio(message.chat.id , audio)


# @bot.message_handler(commands=['send_gift'])
# def send_gift_file(message):
#     gift = open(r'مسیر فایل مد نظر' , 'rb')
#     bot.send_gift(message.chat.id , gift)


# @bot.message_handler(commands=['send_sticker'])
# def send_sticker_file(message):
#     sticker = open(r'مسیر فایل مد نظر' , 'rb')
#     bot.send_sticker(message.chat.id , sticker)


# @bot.message_handler(commands=['send_document'])
# def send_ducument_file(message):
#     document = open(r'مسیر فایل مد نظر' , 'rb')
#     bot.send_document(message.chat.id , document)

# @bot.message_handler(content_types=['photo'])
# def photo_message(message):
#     photo_id = message.photo[-1].file_id
#     file_link = bot.get_file(photo_id)
#     picture = bot.download_file(file_link.file_path)
#     with open('./picture.jpg' , 'wb') as f:
#         f.write(picture)
#         bot.send_message(message.chat.id , 'Your file was saved successfully!...')
#     bot.send_photo(message.chat.id , picture)



bot.infinity_polling()