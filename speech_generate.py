from nltk import ngrams

SEQUENCE_SIZE = 3 # n-grams

def generate_sequences(source: list[list[str]]):
	sequences = [ngram for sentence in source for ngram in ngrams(sentence, SEQUENCE_SIZE)]
	return [sequence for sequence in sequences if sequence != ()]

def speech_learn(source: list[list[str]], seed: list[str]):
	sequences = generate_sequences(source)
	speech_patterns = {}

	for index, sequence in enumerate(sequences):
		last = sequence[-SEQUENCE_SIZE+1:]

		for _index, _sequence in enumerate(sequences):
			if _sequence[:SEQUENCE_SIZE-1] == last and _index != index:
				if last not in speech_patterns:
					speech_patterns[last] = []
				speech_patterns[last].append(_sequence[-1])

	for seed, suggestions in list(speech_patterns.items()):
		if len(suggestions) == 1:
			del speech_patterns[seed]

	return speech_patterns

