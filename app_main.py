#!/usr/bin/env python
# -*- coding: utf-8 -*-

#imports
import telebot
from telebot import types, util
from decouple import config
from datetime import datetime

#Token
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

#config 
#SUDO = config('ID_SUDO')
#print(SUDO)
#print(BOT_TOKEN)

chatmsg = {
    'hi':["hello", "hi", "Hi", "Hello"],
    'hru':["how are you", "h r u", "hru"]
}

#methods
#starting command method ::: /stsrt, /help
@bot.message_handler(commands=["start","help"])
def welcome(message):
    print(f"{datetime.now()} :: /start :::: welcome")
    bot.send_message(message.chat.id,"welcome to billy bot just a bot to have fun building it")

#small method
@bot.message_handler(func=lambda m:True)
def some(message):
    chat_id = message.chat.id
    words = message.text.split()
    if words[0] in chatmsg["hi"] :
        bot.send_message(chat_id, text="hello")
        print(f"{datetime.now()} ::: hello")
    elif words[0] in chatmsg["hru"] :
        bot.send_message(chat_id, text="im great, WAU?")   
        print(f"{datetime.now()} ::: hru/ im great")

#polling
print(f"\n {datetime.now()} :: Bot is running \n")
bot.infinity_polling(allowed_updates=util.update_types)