import json
import telebot
import requests
bot = telebot.TeleBot(TOKEN)

# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print("{} : {}".format(message.chat.id, message.text))
    answer = getAnswer(message.text, message.chat.id)
    print('bot : '+ answer)
    bot.send_message(message.from_user.id, answer)


def getAnswer(question, userId):
    url = 'https://aiproject.ru/api/'

    params = {'ask':question, 'userid': userId, 'key':''}
    jsonParams = json.dumps(params)

    postdata = {'userid':userId, 'query':jsonParams}

    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=postdata)
    response.encoding = 'utf-8'
    answer = response.json()['aiml']
    return answer

bot.polling(none_stop=True, interval=0)
