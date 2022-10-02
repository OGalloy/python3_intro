from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5423252479:AAHtStPn6tyZLQWPQQqu5IyqE4MF8WE-yTk')
updater = Updater(token='5423252479:AAHtStPn6tyZLQWPQQqu5IyqE4MF8WE-yTk')
dispatcher = updater.dispatcher


def message(update, context):
    user_message = update.message.text.split(" ")
    text = ""
    for word in user_message:
        if not "абв" in word:
            text += f" {word}"
            print(text)
    context.bot.send_message(update.effective_chat.id, f'{text}')


message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c