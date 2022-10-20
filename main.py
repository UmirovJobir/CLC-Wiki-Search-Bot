from telegram.bot import Bot
from telegram.user import User
from telegram.update import Update
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
import settings


# bot = Bot(token="5552099898:AAGrWUcDRf0-Fg5sD5G6HZsS4EYZQLK-DYc")
# user : User = bot.get_me()


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom')
    context.bot.send_message(chat_id=update.message.chat_id, text='Salom yana bir bor')


updater = Updater(token=settings.TOKEN)

dipatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler("start", start))


updater.start_polling()
updater.idle()
