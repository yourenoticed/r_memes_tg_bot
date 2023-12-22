import os
import telebot
from service import Service

BOT_TOKEN = os.environ.get("BOT_TOKEN")
DB_URI = os.environ.get("DB_URI")

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def welcome_message(message: str):
    bot.reply_to(message, "Sup! What memes do you want today? (give a subreddit name)")
    
@bot.message_handler(commands=['hot'])
def send_hot(message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = service.get_hot_memes(msg[2])
    else:
        memes = service.get_hot_memes()
        
    for meme in memes:
        bot.send_photo(message.chat.id, meme)

@bot.message_handler(commands=['new'])
def send_new(message):
    msg = message.text.split()
    service = Service(msg[1])
    if len(msg) > 2 and msg[2].isdigit():
        memes = service.get_new_memes(msg[2])
    else:
        memes = service.get_new_memes()
        
    for meme in memes:
        bot.send_photo(message.chat.id, meme)

@bot.message_handler(func=lambda msg: True)
def send_random(message):
    service = Service(message.text)
    bot.send_photo(message.chat.id, service.get_random_meme())
    
bot.infinity_polling()