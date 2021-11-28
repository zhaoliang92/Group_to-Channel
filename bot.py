import os
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

    updater = Updater(token=os.environ['TOKEN'], use_context=True)

    dp =updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=procesar_mensajes))
    updater.start_polling()

    print('Bot is polling')

    updater.idle()