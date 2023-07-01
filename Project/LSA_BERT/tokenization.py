from util import *

# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		for sentence in text:
			tokenizedSentence = []
			for word in sentence.split(' '):		#Based on the fact that words are separated by spaces
				if len(word.strip())>0: tokenizedSentence.append(word.strip())
			tokenizedText.append(tokenizedSentence)

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []

		#Fill in code here
		tokenizer = treebank.TreebankWordTokenizer()
		for string in text:
			tokenizedText.append(tokenizer.tokenize(string))

		return tokenizedText