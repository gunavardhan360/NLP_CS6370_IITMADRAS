from util import *
# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []

		stop_words = set(stopwords.words('english')).union(set(string_lib.punctuation))
		#Fill in code here
		for string in text:
			filteredtext = [word for word in string if not word in stop_words]
			stopwordRemovedText.append(filteredtext) 

		return stopwordRemovedText	