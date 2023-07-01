from util import *
# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Stop word removal from the library of stopwords

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

		# stop_words = set(stopwords.words('english')).union(set(string_lib.punctuation))
		stop_words = set(stopwords.words('english'))
		#Fill in code here
		for string in text:
			filteredtext = [word for word in string if not word in stop_words]
			stopwordRemovedText.append(filteredtext) 

		return stopwordRemovedText	