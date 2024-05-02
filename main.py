
import requests
import json
from telebot import telebot,TeleBot
from telebot.types import *
from telebot.util import user_link
#from runForever import keepAlive

#keepAlive()

markup = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
markup.add(group,channel)

bot = telebot.TeleBot("6978250041:AAEzindZxm3xaexCXbm6-4nwnl6tLP8yAYM",parse_mode="HTML")

@bot.message_handler(commands=["start"])
def greet(msg):
    user = f"{user_link(msg.from_user)}"
    bot.reply_to(msg,f"""Hello {user}This is random quote generator bot.to get a quote send /getquote to get a quote""",reply_markup=markup)

@bot.message_handler(func=lambda m:True)
def generateQuote(msg):
    link = "https://api.quotable.io/random"
    header = {"User-Agent":"Generic user agent"}
    request = requests.get(url=link,headers=header)
    data = json.loads(request.text)
    quote = data['content']
    author = data['author']
    content = f""" ```{quote} \n BY {author}```"""
    print(content)

    if "/getquote" in msg.text:
        bot.send_message(msg.chat.id,content,reply_markup=markup,parse_mode="MarkdownV2")


bot.infinity_polling()
