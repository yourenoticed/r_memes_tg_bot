import os
import telebot
from service import Service

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def welcome_message(message):
    send_help(message)
    bot.reply_to(message, "Sup! What memes do you want today? (give a subreddit name)")
    
@bot.message_handler(commands=['hot'])
def send_hot(message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = service.get_hot_memes(msg[2])
    else:
        memes = service.get_hot_memes()
    
    if verify_download(memes):
        for meme in memes:
            bot.send_photo(message.chat.id, meme) 

@bot.message_handler(commands=['new'])
def send_new(message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = None
        while not verify_download(memes):
            memes = service.get_new_memes(msg[2])
    else:
        memes = None
        while not verify_download(memes):
            memes = service.get_new_memes()
            
    if verify_download(memes):
        for meme in memes:
            bot.send_photo(message.chat.id, meme)

@bot.message_handler(commands=["memes", "help"])
def send_help(message):
    bot.send_message(message.chat.id, "You can get a random meme from a subreddit you send")
    bot.send_message(message.chat.id, "Meme subreddits I personally enjoy are \"memes\", \"memes_of_the_dank\", \"dank\", \"wholesomememes\", \"programmingmemes\", \"dankmemes\", \"dank_memes\"")

@bot.message_handler(func=lambda message: len(message.text.split()) == 2)
def send_random_n(message):
    msg = message.text.split()
    service = Service(msg[0])
    for _ in range(int(msg[1])):
        meme = None
        while not verify_download(meme):
            meme = service.get_random_meme()
        bot.send_photo(message.chat.id, meme)

@bot.message_handler(func=lambda message: True)
def send_random(message):
    service = Service(message.text)
    meme = None
    while not verify_download(meme):
        meme = service.get_random_meme()
    bot.send_photo(message.chat.id, meme)
        
# # /schedule testgroup dank 50
# @bot.message_handler(commands=["schedule"])
# def schedule_memes(message):
#     msg = message.split()
#     channel = bot.get_chat("@" + msg[1])
#     sub_r = msg[2]
#     if len(msg) > 3:
#         limit = msg[3]
#     else:
#         limit = 10
#     memes = None
#     service = Service(sub_r)
#     while not verify_download(memes):
#         memes = service.get_hot_memes(limit)
#     for meme in memes:
#         bot.send_photo(channel.id, meme)
        
def verify_download(meme):
    return meme is not None and len(meme) > 0
    
bot.infinity_polling()