# 1. Download all text examples belonging to specified user
# 2. Tokenize the text (couples, triplets, ...)
# 3. Learn a Markov chain

import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, sync

def telegram_download():
	api_id = os.getenv("TELEGRAM_API_ID")
	api_hash = os.getenv("TELEGRAM_API_HASH")

	client = TelegramClient('downloader', api_id, api_hash)
	client.start()

	# TODO: iter_message prende il parametro filter per avere solo alcuni messaggi, fai in modo di avere solo i messaggi di solo testo
	for message in client.iter_messages('aripizz', limit=100):
		print(message.message)

if __name__ == "__main__":
	load_dotenv()

	telegram_download()
