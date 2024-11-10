import telebot, random
import time

A = ["🪨", "✂️", "📝"]

TOKEN = '7738805870:AAGk3ortTT3dQISXxDmhlJim0mpzVKxdM6Y'
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = telebot.types.KeyboardButton('Сыграть в 🪨✂️📝')
button_2 = telebot.types.KeyboardButton('Бросить кубик🎲')
keyboard.add(button_1, button_2)
#__________________________________________________________________________________________________________________

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Выберете действие снизу⬇️', reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text.strip().capitalize() == 'Сыграть в 🪨✂️📝')
def command(message: telebot.types.Message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton('🪨', callback_data="🪨")
    button_2 = telebot.types.InlineKeyboardButton('✂️', callback_data="✂️")
    button_3 = telebot.types.InlineKeyboardButton('📝', callback_data="📝")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выберете предмет', reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text.strip().capitalize() == 'Бросить кубик🎲')
def command1(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Бросаю куб для бота🤖')
    bot.send_dice(message.chat.id, '')
    bot.send_message(message.chat.id, f'Бросаю куб для {message.chat.username}👽')
    bot.send_dice(message.chat.id, '')



@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    if callback.data == '🪨':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        B = random.randint(0,2)
        bot.send_message(callback.message.chat.id, A[B])
        if B == 0:
            bot.send_message(callback.message.chat.id, 'Ничья', reply_markup=keyboard)
        elif B == 1:
            bot.send_message(callback.message.chat.id, 'Вы выиграли', reply_markup=keyboard)
        elif B == 2:
            bot.send_message(callback.message.chat.id, 'Вы проиграли', reply_markup=keyboard)
    elif callback.data == '✂️':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        B = random.randint(0,2)
        bot.send_message(callback.message.chat.id, A[B])
        if B == 1:
            bot.send_message(callback.message.chat.id, 'Ничья', reply_markup=keyboard)
        elif B == 2:
            bot.send_message(callback.message.chat.id, 'Вы выиграли', reply_markup=keyboard)
        elif B == 0:
            bot.send_message(callback.message.chat.id, 'Вы проиграли', reply_markup=keyboard)
    elif callback.data == '📝':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        B = random.randint(0,2)
        bot.send_message(callback.message.chat.id, A[B])
        if B == 2:
            bot.send_message(callback.message.chat.id, 'Ничья', reply_markup=keyboard)
        elif B == 0:
            bot.send_message(callback.message.chat.id, 'Вы выиграли', reply_markup=keyboard)
        elif B == 1:
            bot.send_message(callback.message.chat.id, 'Вы проиграли', reply_markup=keyboard)
    elif callback.data == "Сыграть в 🪨✂️📝":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('🪨', callback_data="🪨")
        button_2 = telebot.types.InlineKeyboardButton('✂️', callback_data="✂️")
        button_3 = telebot.types.InlineKeyboardButton('📝', callback_data="📝")
        keyboard.add(button_1, button_2, button_3)
        bot.send_message(callback.message.chat.id, 'Выберете предмет', reply_markup=keyboard)
    elif callback.data == "Бросить кубик🎲":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Сыграть в 🪨✂️📝', callback_data="Сыграть в 🪨✂️📝")
        button_2 = telebot.types.InlineKeyboardButton('Бросить кубик🎲', callback_data="Бросить кубик🎲")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, f'Бросаю куб для бота🤖')
        bot.send_dice(callback.message.chat.id, '')
        bot.send_message(callback.message.chat.id, f'Бросаю куб для {callback.message.chat.username}👽')
        bot.send_dice(callback.message.chat.id, '')


print("Сервер запущен!")        
bot.polling(
    non_stop=True,
    interval=1 
)