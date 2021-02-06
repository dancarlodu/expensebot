from config import bot
import config
from time import sleep
import re
import logic


#########################################################

# Aquí vendrá la implementación de la lógica del bot

#El saludo inicial: comando /start
@bot.message_handler(commands=['start'])
def on_command_start(message):
    pass


#La ayuda: comando /help
@bot.message_handler(commands=['help'])
def on_command_help(message):
    pass

    #Procesar los “demás mensajes”
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.reply_to (
        message,
        "\U0001F63F Ups, no entendí lo que me dijiste. Intenta de nuevo")

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)

#########################################################