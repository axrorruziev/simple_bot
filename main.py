import Telebot
import buttons

bot = telebot.Telebot('6777841195:AAHITPyMYgYI5baFPImB0mzDekDprr0GKcw')


@bot.message_handler(commands == ['start'])
def start(message):
    bot.send.message(message.chat.id, f'привет,{message.from_user.first_name}{message.from_user.last_name},'
                                      'пожалуйста зарегистрируйтесь 😉')


def get_name(message):
    user_id = message.from_user.id

    username = message.text

    bot.send_message(user_id, 'отправте свое имя')
    bot.register_next_step_handler(message, get_number, username)


def get_number(message):
    user_id = message.from_user.id

    username = message.text

    bot.send_message(user_id, f'{message.from_user.first_name}{message.from_user.last_name} отправте номер телефона',
                     reply_markup=buttons.number_buttons())
    print(f'поздравляем {message.from_user.first_name}{message.from_user.last_name} вы успешно зарегистрировались')
    bot.register_next_step_handler(message, username)


bot.infinity_pooling()
