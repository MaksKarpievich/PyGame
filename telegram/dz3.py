#5274147483:AAETJwzy751jD0hRi030E6l2ao9qAeeun8o

import telebot
from telebot import types

token = '5348280418:AAEmryot8he5y-ppYCCNKYs0GJ4p4k-k9lI'
bot  =telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    bmw_1 = types.InlineKeyboardButton(text='BMW', callback_data='1')
    mercedes_1 = types.InlineKeyboardButton(text='Mercedes', callback_data='2')
    audi_1= types.InlineKeyboardButton(text='Audi', callback_data='3')
    toyota_1 = types.InlineKeyboardButton(text='Toyota', callback_data='4')
    porshe_1 = types.InlineKeyboardButton(text='Porshe', callback_data='5')

    keyboard.add(bmw_1)
    keyboard.add(mercedes_1)
    keyboard.add(audi_1)
    keyboard.add(toyota_1)
    keyboard.add(porshe_1)

    return keyboard
@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день! выберите авто',
        reply_markup=keyboard
    )
marka=''
model=''
@bot.message_handler(content_types=['text'])
def markaavto(message):
    if message.text=='/reg':
        bot.send_message(message.from_user.id, 'Здравствуйте. Какая машина нужна?')
        bot.register_next_step_handler(message,marka_1)
    else:
        bot.send_message(message.from_user.id, 'напиши /reg')
def marka_1(message):
    global marka
    marka=message.text
    if message.text=='Bmw' or message.text=='Mercedes' or message.text=='Audi' or message.text=='Toyota' or message.text=='Porshe':
        bot.send_message(message.from_user.id, 'Хорошо. Какая модель')
        bot.register_next_step_handler(message,model_1)
def model_1(message):
    global model
    model=message.text
    bot.send_message(message.from_user.id,'Вы хотите машину марки ' + str(marka) + ' модели ' + str(model) + ' ?')
    bot.register_next_step_handler(message, okon)

def okon(message):
    keyboard = create_keyboard()
    if message.text=='Да':
        bot.send_message(message.from_user.id, 'Сейчас подберу', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Сейчас исправим',
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard=create_keyboard()
    if call.message:
        if call.data=='1':
            bot.send_message(
                call.message.chat.id, 'Эта машина яркая и энергичная. Если хотите её, напишите /reg',
                reply_markup=keyboard)
        if call.data=='2':
            bot.send_message(
                call.message.chat.id, 'Эта машина быстрая и мощная. Если хотите её, напишите /reg',
                reply_markup=keyboard)

        if call.data=='3':
            bot.send_message(
                call.message.chat.id, 'Эта машина привлекательная и дорогая. Если хотите её, напишите /reg',
                reply_markup=keyboard)

        if call.data=='4':
            bot.send_message(
                call.message.chat.id, 'Эта машина надёжная и быстрая. Если хотите её, напишите /reg',
                reply_markup=keyboard)

        if call.data=='5':
            bot.send_message(
                call.message.chat.id, 'Эта машина сногшибательная и мощная. Если хотите её, напишите /reg',
                reply_markup=keyboard)
if __name__=='__main__':
    bot.polling(none_stop=True)
