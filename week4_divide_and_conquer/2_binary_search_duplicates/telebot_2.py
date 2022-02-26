import os
import telebot
bot=telebot.TeleBot("2113880404:AAHpCyJmar7KS0O1AILmp6j6lmZqmPkYRwI")
@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.send_message(message,"Hey! Che gohi mikhori?")
bot.polling()