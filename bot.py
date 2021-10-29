# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('2073322401:AAGzJ012KdUOs2tiesV9K3h6gNBvai5wSg0')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == 'Привет':
        # Пишем приветствие
        bot.send_message(message.from_user.id, 'Привет, это курс валют')
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик
        key_usd = types.InlineKeyboardButton(text='Доллар США', callback_data='key_usd')
        # И добавляем кнопку на экран
        keyboard.add(key_usd)
        key_eur = types.InlineKeyboardButton(text='Евро', callback_data='key_eur')
        keyboard.add(key_eur)
        key_rub = types.InlineKeyboardButton(text='Российский рубль', callback_data='key_rub')
        keyboard.add(key_rub)
        key_uah = types.InlineKeyboardButton(text='Гривна', callback_data='key_uah')
        keyboard.add(key_uah)
        key_pln = types.InlineKeyboardButton(text='Польский злотый', callback_data='key_pln')
        keyboard.add(key_pln)
        key_cny = types.InlineKeyboardButton(text='Китайский юань', callback_data='key_cny')
        keyboard.add(key_cny)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери интересующую тебя валюту', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши Привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 6 кнопок — выводим действие

    if call.data == 'key_usd':
        bot.send_message(call.message.chat.id, '1 $  =  2.43 руб')

    elif call.data == 'key_eur':
        bot.send_message(call.message.chat.id, '1 €  =  2.81 руб')

    elif call.data == 'key_rub':
        bot.send_message(call.message.chat.id, '100 ₽  =  3,44 руб')

    elif call.data == 'key_uah':
        bot.send_message(call.message.chat.id, '100 ₴  =  9,22 руб')

    elif call.data == 'key_pln':
        bot.send_message(call.message.chat.id, '10 Zł  =  6,08 руб')

    elif call.data == 'key_cny':
        bot.send_message(call.message.chat.id, '10 ¥  =  3,79 руб')

# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)