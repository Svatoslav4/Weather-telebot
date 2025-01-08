import requests
import json
import telebot

bot = telebot.TeleBot('7985806779:AAECH7S44hWattalE25ypuSx3Mmbapkn5sQ')
api = '43723760989e623ad27b0bb45a714ff9'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привіт напиши назву свого міста 😁")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    data = json.loads(res.text)

    if res.status_code == 200:
        # Якщо місто знайдено, виводимо температуру
        bot.reply_to(message, f'Зараз погода в місті {city.capitalize()}: {data["main"]["temp"]} градусів')
    else:
        # Якщо місто не знайдено або інша помилка
        bot.reply_to(message, f'Не вдалося знайти місто "{city.capitalize()}". Будь ласка, перевірте правильність введеного назви 😒w')


bot.polling(non_stop=True)
