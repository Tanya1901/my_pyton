#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import requests
from bs4 import BeautifulSoup
import telebot
import random

#бот пока ничего не умеет, кроме приветствовать, повторять отправленный текст и реагировать на отправленную фотографию
answers=["То, что находится на этой картинке, похоже на моего кота", "Красота!!!!!", "Был бы у меня инстаграм, я бы поставил лайк два раза", "Картинка огонь, качество не очень", "Не вызывай у меня зависть такими шедеврами"]

bot = telebot.TeleBot('1144899408:AAHs9EuMWSCJE_TnCytKPrYtl40fHPfMv54')

def parse(search):
  #search=input("Введите понятие:   ")
  URL=f"https://ru.wikipedia.org/wiki/{search}"
  HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
  response=requests.get(URL, headers=HEADERS)
  soup=BeautifulSoup(response.content,'html.parser')
  items=soup.body('p',limit=1)
  return items

@bot.message_handler(commands=['start','help'])
def start_message(message):
  bot.send_message(message.chat.id, """Привет, я пока что просто цифровое пространство и ничего не умею делать, но скоро Таня и Тася научат меня многим крутым штукам!  """)


@bot.message_handler(content_types=['text'])
def term(message):
  a=parse(message.text)
  bot.send_message(message.chat.id, a)


#@bot.message_handler(content_types=['text'])
#def echo_message(message):
#    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['photo'])
def ph(message):
  bot.send_message(message.chat.id, random.choice(answers))


bot.polling()

