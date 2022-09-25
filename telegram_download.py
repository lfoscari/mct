from telethon import TelegramClient
from text_normalizer import normalize

def telegram_download(user: str, limit: int, api_id: str, api_hash: str) -> list[str]:
	client = TelegramClient('downloader', api_id, api_hash)
	client.start()

	texts = []

	for message in client.iter_messages(user, limit=limit, from_user=user):
		if message.message is not None and message.media is None:
			texts.append(normalize(message.message))

	return texts

def save_texts(user: str, limit: int, api_id: str, api_hash: str):
	texts = telegram_download(user, limit, api_id, api_hash)
	with open(f"{user}.texts", "w") as save:
		save.write(str(texts))