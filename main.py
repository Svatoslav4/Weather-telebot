import telebot
import requests
import json

bot = telebot.TeleBot("7985806779:AAECH7S44hWattalE25ypuSx3Mmbapkn5sQ")
api = "43723760989e623ad27b0bb45a714ff9"

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,"Привіт,напиши назву свого міста!")


@bot.message_handler(content_types=['text'])
def get_weathher(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message,f'Зараз погода: {data['main']['temp']} градусів')

bot.polling(none_stop=True)