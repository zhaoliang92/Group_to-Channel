import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters


def procesar_mensajes(update, context):

    text = update.message.text

    if str(text).__contains__("#canal"):
        # enviar el mensaje
        context.bot.send_message(
            chat_id="@dojo_en_tv",
            text=str(text).replace("#canal", "")
        )


if __name__ == '__main__':

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp =updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=procesar_mensajes))
    updater.start_polling()

    print('Bot is polling')

    updater.idle()