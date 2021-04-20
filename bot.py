import config
import random
import telebot


bot = telebot.TeleBot(config.TOKEN)
help_string = 'Якщо не можеш визначитися, загадай питання і потруси магічну кулю'
list_of_answers = ["Це точно.", "Жодного сумніву, так.", "Ніяких сумнівів.", "Так - однозначно.",
                    "Можеш покластися на це.", "Як я бачу, так.", "Швидше за все.", "Шанси хороші.", "Так.",
                    "Знаки вказують, що так і буде.", "Відповідь туманна, спробуйте ще раз.", "Запитай ще раз пізніше.",
                   "Краще не говорити вам зараз.", "Неможливо передбачити зараз.", "Зосередься і запитай ще раз.",
                   "Не розраховуй на це.", "Моя відповідь - ні.", "Мої джерела стверджують, що ні.",
                   "Ти геть з глузду з'їхав? Звичайно, ні", "Дуже сумнівно."]


def get_the_answer():
        answer = random.choice(list_of_answers)
        return answer


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  # This is our keyboard
    key_get_answer = telebot.types.InlineKeyboardButton(text='Трусити Магічну Кулю', callback_data='get_answer')
    keyboard.add(key_get_answer)
    bot.send_message(message.from_user.id, text=help_string, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'get_answer':
        bot.send_message(call.from_user.id, get_the_answer())
        bot.send_message(call.from_user.id, 'Натисни /start щоб запитати знову')


bot.polling(none_stop=True, interval=0)