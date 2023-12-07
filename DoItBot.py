import telebot
import requests
import traceback
import random

bot = telebot.TeleBot('6546598143:AAG45SEGEIpoaLZtv3auXOmpgjNHx8Vms2o') 

# Чтение с тхт файла цитат
def read_motivational_quotes():
    file_path = 'motivational_quotes.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            quotes = file.read().splitlines()
        return quotes
    except FileNotFoundError:
        print("Файл 'motivational_quotes.txt' не найден. Убедитесь, что файл существует.")
        return []

# Функция для получения случайной мотивирующей фразы
def get_random_motivational_quote():
    quotes = read_motivational_quotes()
    if quotes:
        return random.choice(quotes)
    else:
        return "Не удалось получить мотивационную цитату. Попробуйте еще раз."

@bot.message_handler(commands=['motivation'])
def handle_motivation(message):
    quote = get_random_motivational_quote()
    bot.send_message(message.chat.id, quote)

# Отслеживание команды
@bot.message_handler(commands=['start'])
def start(message):
    # from user собеседнику с фирст - имя, ласт - фамилия
    mess = f'<b>Супер {message.from_user.first_name} Теперь ты подключен к своему ежедневному дозированному заряду мотивации. 🌟 Каждый день я буду присылать тебе вдохновляющие цитаты, короткие задания и вопросы для саморефлексии. Готов начать свой первый мотивационный день?</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    response = "Доступные команды:\n"
    response += "/start - Начать взаимодействие с ботом\n"
    response += "/help - Показать список доступных команд\n"
    response += "/motivation - Получить вдохновляющую цитату"
    bot.send_message(message.chat.id, response)

# Любые текстовые команды от человека
@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == "привет" and message.text != "Привет":
        bot.send_message(message.chat.id, "Привет только с заглавной буквы, попробуйте еще раз!")
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "Привет!")
    else:
        bot.send_message(message.chat.id, "Не понял, напиши /help для доступных команд :)", parse_mode='html')

# Работа бота на постоянной основе
bot.polling(none_stop=True)