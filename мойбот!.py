import telebot
from telebot import types
import random
#import sqlite3



#Keyboard-кнопки Такие кнопки можно увидеть в большом количестве ботов,
# таких как Дайвинчик и тому подобные. Пишутся они довольно просто,
# с помощью метода ReplyKeyboardMarkup. Для примера сделаем кнопку выбора языка
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, 'Что случилось?')

#еще есть варик где можно вместо текста поставить message, оно типо данные о чате и пользователе даст, но у меня не дает((((((

#<b>слово/b> - жирное слово, <em>слово</em> - курсив, <u>слово</u> подчеркнуто (parse_mode = 'html')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1= types.KeyboardButton('👋Привет')
    markup.add(btn1)
    bot.send_message(message.from_user.id, '👋Привет!', reply_markup=markup)


#Inline-кнопки Для создания таких кнопок используется метод InlineKeyboardMarkup,
#например, сделаем кнопку, которая ведет на сайт Хабра


#@bot.message_handler(commands = ['start'])
#def url(message):
#markup = types.InlineKeyboardMarkup()
#btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
#markup.add(btn1)
#bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)

# еще есть методы bot.send_video/audio

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '👋Привет':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('О нас')
        btn2 = types.KeyboardButton('FAQ')
        btn3 = types.KeyboardButton('Поддержка')
        btn4 = types.KeyboardButton('Профиль')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Что обсудим🤔', reply_markup=markup)

    elif message.text == 'О нас':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://factorings.ru/company/19/')
        markup.add(btn1)
        file = open('./photo.png', 'rb')
        bot.send_photo(message.from_user.id, photo=file)
        bot.send_message(message.from_user.id, "Мы - факторинговая компания, посредник, между поставщиком и получателем в международных транзакциях. О нас вы можете узнать подробнее:", reply_markup = markup)


    elif message.text == 'FAQ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Что такое факторинг?')
        btn2 = types.KeyboardButton('Чем факторинг отличается от кредита?')
        btn3 = types.KeyboardButton('Какие документы нужны для оформления факторинга?')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Часто задаваемые вопросы🧐:', reply_markup=markup)

    elif message.text == 'Что такое факторинг?':
        bot.send_message(message.from_user.id, '''Факторинг - это финансовая услуга для компаний, которые продают товары или услуги с отсрочкой платежа.
Факторинговая компания выкупает дебиторскую задолженность поставщика и выплачивает ему большую часть суммы сразу, а остаток — после оплаты покупателем, за вычетом комиссии. 
Это помогает бизнесу получать деньги быстрее и не зависеть от сроков оплаты клиентов.''')


    elif message.text == 'Чем факторинг отличается от кредита?':
        bot.send_message(message.from_user.id,'''При кредите компания получает деньги под залог или поручительство и 
обязана их вернуть независимо от ситуации. При факторинге финансирование связано с конкретной поставкой: деньги 
выдаются под уступку денежного требования к покупателю. Кроме того, факторинг часто включает дополнительные сервисы:
управление дебиторской задолженностью, контроль платежей, оценку рисков по покупателям.''')

    elif message.text == 'Какие документы нужны для оформления факторинга?':
        bot.send_message(message.from_user.id,'''Стандартный пакет включает: учредительные документы компании, бухгалтерскую 
отчётность (баланс, отчёт о прибылях и убытках), договоры с покупателями, накладные и счета-фактуры по поставкам,
карточку счёта, сведения о кредитной истории. Конкретный перечень зависит от политики компании и специфики сделки.''')

    elif message.text == 'Профиль':
        username = message.from_user.username
        bot.send_message(message.from_user.id, f'''Name:{username}
balance:{random.randint(1,1200)}$''')

    elif message.text == 'Поддержка':
        bot.send_message(message.from_user.id, 'Переключаю вас на оператора.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'К вам подключится певрый освобовишийся оператор!', reply_markup=markup)
    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('О нас')
        btn2 = types.KeyboardButton('FAQ')
        btn3 = types.KeyboardButton('Поддержка')
        btn4 = types.KeyboardButton('Профиль')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Что обсудим🤔', reply_markup=markup)

    else:
        bot.send_message(message.from_user.id, 'Не знаю о чем ты говоришь, выбери команду из предложенных.')

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
