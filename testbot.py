import os
import telebot
import telebot.types as tt
import friendship

users = {}

with open("Users.txt", "r") as file:
    for line in file:
        data = line.split(':')
        users[int(data[0])] = {"name" : data[1], "sname" : data[2]}

token = ""

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message: tt.Message):
    uid = message.from_user.id
    if uid in users.keys():
        bot.send_message(message.chat.id, "Салам алейкум, " + users[uid]["name"] + ". Мир твоему дому.")
    else:
        bot.reply_to(message, "Прииииииииивет")

@bot.message_handler(commands=['friendship'])
def echo_all(message):
    sm = bot.send_message(message.chat.id, "Как тебя зовут?", reply_to_message_id=message.id)
    bot.register_next_step_handler(sm, friendship.get_name, bot, users)

    # bot.send_message(message.chat.id, "[Парень](tg://user?id=<ididididi>)", parse_mode="Markdown")

@bot.message_handler(commands=['whoi'])
def echo_all(message):
    if message.from_user.username == "username":
        bot.send_message(message.chat.id, "Властелин")
    else:
        bot.send_message(message.chat.id, "не властелин")

@bot.message_handler(commands=['peterparker'])
def echo_all(message):
    bot.send_message(message.chat.id, "Дружелюбный сосед, человек-паук!")


# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, "Сформулируй свою мысль и попробуй еще разок.")


bot.infinity_polling()
