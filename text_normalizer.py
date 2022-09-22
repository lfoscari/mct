import re
import string
import unidecode
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import gensim.downloader as api

"""
Text Normalization for NLP
- removes extra whitespace within text
- removes numbers
- removes urls
- converts unicode to ascii
- converts to lowercase
- remove leading or trailing whitespace
- tokenizes sentences and words
- removes punctuation
- lemmatizes words
- removes stopwords

Credits: https://gist.github.com/lvngd/3695aac64461de2cfb9d50bb11d5fbb3
"""

class TextNormalizer:
	def __init__(self):
		self.lemmatizer = WordNetLemmatizer()
		self.punctuation_table = str.maketrans('', '', string.punctuation)
		self.stop_words = set(stopwords.words('english')) | set(stopwords.words('italian'))

	def normalize_text(self, text):
		normalized_sentences = []
		text = re.sub(' +',' ', text)
		text = re.sub('\d+',' ', text)
		text = re.sub('http\S+', '', text)
		text = unidecode.unidecode(text)
		text = text.lower()
		sentences = sent_tokenize(text)

		for sentence in sentences:
			# remove punctuation
			sentence = sentence.translate(self.punctuation_table)

			# strip leading/trailing whitespace
			sentence = sentence.strip()
			words = word_tokenize(sentence)

			# remove stopwords
			filtered = [word for word in words if word not in self.stop_words]
			new_sentence = ' '.join(filtered)
			normalized_sentences.append(new_sentence)
		
		return normalized_sentences