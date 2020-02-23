from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, 
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start' 
    logging.info('Vyzvan /start')
    print(text)
    update.message.reply_text('Пользователь, Вы нажали старт. Поехали:)')


def talk_to_me(bot, update): 
    user_text = f'Привет {update.message.chat.first_name}! Ты написал {update.message.text}'
    print(user_text)
    # update.message - содержит служебную информацию и сообщение пользователя
    # print(update.message)
    logging.info('User: {}, chat id: {}, message {} '.format(update.message.chat.username,
                                                             update.message.chat.id,
                                                             update.message.text
                                                             ))
    update.message.reply_text(user_text)


def return_planet_constellation(bot, update):
    planet_name = update.message.text.split()[1].capitalize()
    print(planet_name)
    update.message.reply_text(f'Планета: {planet_name}')
    now = datetime.datetime.today()
    formated_now = '%d/%02d/%02d' % (now.year, now.month, now.day)
    if planet_name == 'Mercury':
        location = ephem.Mercury(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
    if planet_name == 'Venus':
        location = ephem.Venus(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
    if planet_name == 'Mars':
        location = ephem.Mars(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
    if planet_name == 'Jupiter':
        location = ephem.Jupiter(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
    if planet_name == 'Saturn':
        location = ephem.Saturn(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
    if planet_name == 'Uranus':
        location = ephem.Uranus(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
    if planet_name == 'Neptune':
        location = ephem.Neptune(formated_now)
        constellation = ephem.constellation(location)
        update.message.reply_text(f'Созвездие: {constellation}')
        print(constellation)
   


def main():
    astana_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Bot started')

    dp = astana_bot.dispatcher 
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', return_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    astana_bot.start_polling()
    astana_bot.idle()

main()