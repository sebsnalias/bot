from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging # ALmacena cada proceso para una posterior revision (fallas, errores, ...)
import web

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'brawlbot',
    user = 'brawlbot1',
    pw = 'brawlbot.2019',
    port = 3306
    )

#Token de AlexAndreOso_bot 
token = '717181120:AAHHYsp1ucHcP0XjJwiy9AOrNY0PAbRvxRo'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username # Almacena el nombre del usuario de Telegram
    update.message.reply_text('Hola {}¿Descrube cual es tu jugador introduciendo tu dia de nacimiento?\nUsa el comando:\n/numero dia #dia_de_nacimiento'.format(username))

def help(bot, update):
    username = update.message.from_user.username # Almacena el nombre del usuario de Telegram
    update.message.reply_text('Hola {}¿Descrube cual es tu jugador introduciendo tu dia de nacimiento?\nUsa el comando:\n/numero dia #dia_de_nacimiento'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        numero = int(text[1]) # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(numero)
        result = db.select('jugadores', where='numero=$numero', vars=locals())[0]
        print result
        respuesta =  "Nombre: " + str(result.nombre) + "\nPais: " + str(result.pais) + "\nPosicion: " + str(result.posicion) + "\nEquipo: " + str(result.equipo)
        update.message.reply_text('Hey {}\nEste es tu jugador relacionado:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(numero))

def info(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'COMITBOT init token'
        
        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'COMITBOT init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("numero", info))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'COMICBOT ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
