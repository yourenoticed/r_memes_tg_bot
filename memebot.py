import os
import telebot
from service import Service
import texts

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def welcome_message(message):
    send_help(message)
    bot.reply_to(
        message, "Sup! What memes do you want today? (give a subreddit name)")


@bot.message_handler(commands=["search", "find"])
def search(message):
    msg = message.text.split()
    service = Service()
    search_result = None
    while not verify_download(search_result):
        search_result = service.get_search(msg[1])
    if search_result:
        names = "\n".join(search_result)
        bot.send_message(message.chat.id, names,
                         reply_to_message_id=message.id)


@bot.message_handler(commands=['best'])
def send_best(message):
    msg = message.text.split()
    service = Service(msg[1])
    memes = None
    if len(msg) > 2 and msg[2].isdigit():
        while not verify_download(memes):
            memes = service.get_best_memes(msg[2])
    else:
        while not verify_download(memes):
            memes = service.get_best_memes()
    if memes:
        for meme in memes:
            bot.send_photo(message.chat.id, meme,
                           reply_to_message_id=message.id)


@bot.message_handler(commands=['hot'])
def send_hot(message):
    msg = message.text.split()
    service = Service(msg[1])
    memes = None
    if len(msg) > 2 and msg[2].isdigit():
        while not verify_download(memes):
            memes = service.get_hot_memes(msg[2])
    else:
        while not verify_download(memes):
            memes = service.get_hot_memes()
    if memes:
        for meme in memes:
            bot.send_photo(message.chat.id, meme,
                           reply_to_message_id=message.id)


@bot.message_handler(commands=['new'])
def send_new(message):
    msg = message.text.split()
    service = Service(msg[1])
    memes = None
    if len(msg) > 2 and msg[2].isdigit():
        while not verify_download(memes):
            memes = service.get_new_memes(msg[2])
    else:
        while not verify_download(memes):
            memes = service.get_new_memes()
    if memes:
        for meme in memes:
            bot.send_photo(message.chat.id, meme,
                           reply_to_message_id=message.id)


@bot.message_handler(commands=["memes", "help"])
def send_help(message):
    bot.send_message(message.chat.id, texts.HELP,
                     reply_to_message_id=message.id)


@bot.message_handler(commands=["commands"])
def send_commands(message):
    bot.send_message(message.chat.id, texts.COMMANDS,
                     reply_to_message_id=message.id)


@bot.message_handler(func=lambda message: len(message.text.split()) == 2)
def send_random_n(message):
    msg = message.text.split()
    service = Service(msg[0])
    for _ in range(int(msg[1])):
        meme = None
        while not verify_download(meme):
            meme = service.get_random_meme()
        bot.send_photo(message.chat.id, meme, reply_to_message_id=message.id)


@bot.message_handler(func=lambda message: True)
def send_random(message):
    service = Service(message.text)
    meme = None
    while not verify_download(meme):
        meme = service.get_random_meme()
    bot.send_photo(message.chat.id, meme, reply_to_message_id=message.id)


def verify_download(meme):
    return meme is not None and len(meme) > 0


if __name__ == "__main__":
    bot.infinity_polling()
