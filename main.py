# 1. Download all text examples belonging to specified user
# 2. Tokenize the text (couples, triplets, ...)
# 3. Learn a Markov chain

import os
import sys
from dotenv import load_dotenv

from telethon import TelegramClient
from text_normalizer import TextNormalizer

import pandas as pd

def tokenize(text: str) -> list[str]:
	normalized = TextNormalizer().normalize_text(text)
	return [word for sentence in normalized for word in sentence.split()]

def telegram_download(user: str, api_id: str, api_hash: str) -> list[str]:
	client = TelegramClient('downloader', api_id, api_hash)
	client.start()

	texts = []

	for message in client.iter_messages(user, limit=1000, from_user=user):
		if message.message is not None and message.media is None:
			texts.extend(tokenize(message.message))

	return texts

if __name__ == "__main__":
	load_dotenv()
	api_id = os.getenv("TELEGRAM_API_ID")
	api_hash = os.getenv("TELEGRAM_API_HASH")

	messages = telegram_download(sys.argv[1], api_id, api_hash)
	
	messages = pd.DataFrame(messages)
	messages.value_counts().to_csv(f"{sys.argv[1]}.csv")
