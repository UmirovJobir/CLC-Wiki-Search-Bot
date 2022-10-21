from urllib import response
from telegram.bot import Bot
from telegram.user import User
from telegram.update import Update
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler, Filters
import settings
import requests  
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


# bot = Bot(token="5552099898:AAGrWUcDRf0-Fg5sD5G6HZsS4EYZQLK-DYc")
# user : User = bot.get_me()


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! Vikipediadan ma'lumot qidiruvchi botga xush kelibsiz!" 
                                "Ma'lumot izlash uchun /search va teks yozing. Misol uchun /search Amir Temur")
    # context.bot.send_message(chat_id=update.message.chat_id, text='Salom yana bir bor')

def search(update: Update, context: CallbackContext):
    args = context.args

    logging.info('checking args length')

    if len(args)==0:
        update.message.reply_text("/search kamandasidan so'ng diqirmoqchi bo'lgan ma'lumotingizni yozing!")
    else:
        search_text = ' '.join(args)

        logging.info('send request to Wikipedia API')

        response = requests.get('https://uz.wikipedia.org/w/api.php',{
            'action':'opensearch',
            'search':search_text,
            'limit':1,
            'namespace':0,
            'format':'json',
        })

        logging.info('result from Wikipedia API')

        result = response.json()
        link = result[3]

        if len(link):
            update.message.reply_text("Sizning so'rovingiz bo'yicha havola:" + link[0])
        else:
            update.message.reply_text("Sizning so'rovingiz bo'yicha hech narsa yo'q")

updater = Updater(token=settings.TOKEN)

dipatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("search", search))
updater.dispatcher.add_handler(MessageHandler(Filters.all,start))



updater.start_polling()
updater.idle()
