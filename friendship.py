import telebot
import telebot.types as tt

def get_name(message : tt.Message, bot : telebot.TeleBot, users : dict):
    uid = message.from_user.id
    if uid in users.keys():
        bot.send_message(message.chat.id, "А я тебя знаю. Ты же " + users[uid]["name"] + " " + users[uid]["sname"])
    else:
        if message.text == "Ахилес":
            bot.send_message(message.chat.id, "Ахилес? Я помню это имя")
        else:
            if message.text == message.from_user.first_name or message.text == (message.from_user.first_name + " " + message.from_user.last_name):
                    users[message.from_user.id] = {"name" : message.from_user.first_name, "sname" : message.from_user.last_name}
                    updateUsers(users)
                    bot.send_message(message.chat.id, "Будем знакомы!")
            else:
                users[message.from_user.id] = {"name" : "Чел", "sname" : ""}
                updateUsers(users)
                bot.send_message(message.chat.id, "В профиле указано другое имя. Я буду называть тебя Чел")


def updateUsers(users : dict):
    with open("Users.txt", "w") as file:
        for key in users.keys():
            file.write("{}:{}:{}\n".format(key, users[key]["name"], users[key]["sname"]))
