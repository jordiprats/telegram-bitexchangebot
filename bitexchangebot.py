from telegram.ext import Updater
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('bitexchangebot.config')

BOT_TOKEN = config.get('bot', 'token')

updater = Updater(token=BOT_TOKEN)

#https://blockchain.info/ticker
