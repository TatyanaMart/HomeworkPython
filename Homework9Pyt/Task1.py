# Задача 1. Добавьте telegram-боту возможность вычислять выражения:
# 1 + 4 * 2 -> 9
# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда
# игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
from random import randint

count = False
play = False
number = None
steps = 1

bot = telebot.TeleBot(
    "5925252982:AAGNGfYeZagrB4t3_xrOx7Q4TdzpYHjfuYs", parse_mode=None)

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, " + message.from_user.first_name)
    bot.send_message(message.chat.id, f"\nХочешь поиграть? Жми -> /play \nХочешь посчитать? Жми -> /count")

@bot.message_handler(commands=['play'])
def send_welcome(message):
    global play
    global number
    play = True
    number = randint(1, 1001)
    print(number)
    bot.send_message(message.chat.id, f"Я загадал число от 1 до 1000, попробуй его отгадать. Введи число.")

@bot.message_handler(commands=['count'])
def send_welcome(message):
    global count
    count = True
    bot.send_message(message.chat.id, "Напиши, что хочешь посчитать")

@bot.message_handler(content_types=['text'])
def hello_user(message):
    global play
    global count
    global steps
    if play:
        if message.text.isdigit():
            input_number = int(message.text)
            if input_number == number:
                play = False
                bot.send_message(message.chat.id,
                                 f'Ты выиграл! Я загадал число {number}. Ты угадал за {steps} шагов')
                steps = 1
            elif input_number > number:
                bot.send_message(message.chat.id, 'Меньше!')
            elif input_number < number:
                bot.send_message(message.chat.id, 'Больше!')
            steps += 1
    elif count:
        if '+' in message.text or '*' in message.text or '/' in message.text or '-' in message.text:
            do = str(eval(str(message.text)))
            bot.send_message(message.chat.id, f'Получилось: {do}')
        else:
            bot.send_message(message.chat.id, 'Некорректный ввод')
        count = False
    
bot.infinity_polling()
