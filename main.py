import telebot
bot = telebot.TeleBot("7403880282:AAHB97YpbXUCjAY9Tk7IbHeuBAu2WCs8zyg")
@bot.message_handler(commands=["yes"])
def yes_handler(message):
    bot.send_message(message.chat.id, "Отлично!Начни прокачивать своё мышление!")
@bot.message_handler(commands=["how"])
def how_handler(message):
    bot.send_message(message.chat.id, "Подкасты!!!")
@bot.message_handler(commands=["go"])
def go_handler(message):
    bot.send_message(message.chat.id, "[Сумасшедший подкаст для саморазвития](https://youtu.be/llHB8_93rKs?si=vaXZELTT00IkW1MU)")
bot.infinity_polling()