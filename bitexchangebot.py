from telegram.ext import Updater
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('bitexchangebot.config')

BOT_TOKEN = config.get('bot', 'token')

updater = Updater(token=BOT_TOKEN)

#https://blockchain.info/ticker


# MACD = EMA12 – EMA26

# La fórmula:
#
# EMA(t) = EMA(t – 1) + K*[Precio(t) – EMA(t – 1)]
#
# Donde
#
# t=valor actual
#
# t-1=valor previo
#
# K= 2 / (n + 1) (n=periodo elegido para EMA)
