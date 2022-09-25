# 1. Download all text examples belonging to specified user
# 2. Tokenize the text (couples, triplets, ...)
# 3. Learn a Markov chain

import os
import sys
import pandas as pd
from dotenv import load_dotenv

from telegram_download import telegram_download, save_texts
from speech_generate import speech_learn

def main():
	load_dotenv()
	api_id = os.getenv("TELEGRAM_API_ID")
	api_hash = os.getenv("TELEGRAM_API_HASH")

	user = sys.argv[1]
	messages = telegram_download(user, None, api_id, api_hash)
	# messages = eval(open(f"{user}.texts", "r").readline())
	speech_patterns = speech_learn(messages, None)


	# messages = pd.DataFrame([word for sentence in messages for word in sentence])
	# messages.value_counts().to_csv(f"{user}.csv", header=False)

if __name__ == "__main__":
	main()