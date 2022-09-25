# 1. Download all text examples belonging to specified user
# 2. Tokenize the text (couples, triplets, ...)
# 3. Learn a Markov chain

import os
import sys
from dotenv import load_dotenv

from telethon import TelegramClient
from text_normalizer import normalize

import pandas as pd

def telegram_download(user: str, limit: int, api_id: str, api_hash: str) -> list[str]:
	client = TelegramClient('downloader', api_id, api_hash)
	client.start()

	texts = []

	for message in client.iter_messages(user, limit=limit, from_user=user):
		if message.message is not None and message.media is None:
			texts.extend(normalize(message.message))

	return texts

def main():
	load_dotenv()
	api_id = os.getenv("TELEGRAM_API_ID")
	api_hash = os.getenv("TELEGRAM_API_HASH")

	user = sys.argv[1]
	messages = telegram_download(user, 100, api_id, api_hash)
	
	messages = pd.DataFrame(messages)
	messages.value_counts().to_csv(f"{user}.csv", header=False)

if __name__ == "__main__":
	main()