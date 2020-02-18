# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
    )

def greet_user(bot, update):
    text = 'Вызван /start' 
    logging.info('Vyzvan /start')
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = f'Привет {update.message.chat.first_name}! Ты написал {update.message.text}'
    print(user_text)
    # print(update.message)
    logging.info('User: {}, chat id: {}, message {} '.format(update.message.chat.username,
                                                             update.message.chat.id,
                                                             update.message.text
                                                             ))
    update.message.reply_text(user_text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    astana_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Bot started')
    dp = astana_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    astana_bot.start_polling()
    astana_bot.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()

