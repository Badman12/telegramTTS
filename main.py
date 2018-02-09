from telethon import TelegramClient
from resiver import resiver

api_id = 145771
api_hash = 'c088629faa58734606f27049dc06f3c8'

client = TelegramClient('session_name', api_id, api_hash, update_workers=4)
client.start()

resiver(client)

input('Press enter to stop this!')