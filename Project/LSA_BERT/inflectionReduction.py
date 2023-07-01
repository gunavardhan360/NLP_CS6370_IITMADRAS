from util import *

# Add your import statements here




class InflectionReduction:

	def reduce(self, text,method='lemmatisation'):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		#Fill in code here
		# Lemmatisation is best fit but comparision sake both are implemented and lemma is selected

		if (method=='lemmatisation'):
			lemmatizer = WordNetLemmatizer()
			for sentence in text:
				reducedSentence = []
				for word in sentence:
					reducedSentence.append(lemmatizer.lemmatize(word))
				reducedText.append(reducedSentence)

		else:
			ps = PorterStemmer() 

			for string in text:
				stemedtext = []
				for words in string:
					stemedtext.append(ps.stem(words))
				reducedText.append(stemedtext)

		
		return reducedText


