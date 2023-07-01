from util import *
# Add your import statements here




class SpellCheck():

	def fromList(self, text):
		# """
		# SpellChecker using pyspellchecker library

		# Parameters
		# ----------
		# arg1 : list
		# 	A list of lists where each sub-list is a sequence of tokens
		# 	representing a sentence

		# Returns
		# -------
		# list
		# 	A list of lists where each sub-list is a sequence of tokens
		# 	representing a sentence with words spellchecked and belong to dictionay
		# """


		spellCheckedText = []

		spell = SpellChecker()
		
		#Fill in code here
		for string in text:
			filteredtext = []
			for word in string:
				if word in spell.unknown([word]):
					word = spell.correction(word)
				filteredtext.append(word)
			spellCheckedText.append(filteredtext) 

		return spellCheckedText	
