import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '').split()] # give channel id with seperate space. Ex : ('0')

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6769575529:AAEvaEvd-em2ThrbVum3zfxhhmTPWHLEG-E")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://madarazbotz:Dy1i2Ap8RR6AGpGc@cluster0.my7zhtd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
