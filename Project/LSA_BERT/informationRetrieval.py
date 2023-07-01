from util import *

# Add your import statements here


class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		
		index = None

		self.index = index
		self.docIDs = docIDs
		
		D = len(docs)
        
		list_of_words = []			#Intial step to get all the unique words from the dataset

		for document in docs:
			for sentence in document:
				for word in sentence:
					list_of_words.append(word)   #this can have repetition of words 

		self.list_unique = list(set(list_of_words))	#repetition of words is taken care using set
		
		df = np.zeros(len(self.list_unique)) # df(i) is number of docs containing term i, used for calculating IDF 
		
		TD_matrix = np.zeros([len(self.list_unique),len(docs)]) #term-document matrix initialised
        
        
		for j, doc in enumerate(docs):       # iterate over documents
			for k, sentence in enumerate(doc):  # iterate over sentences for a document
				for word in sentence:
					if word in self.list_unique:
						TD_matrix[self.list_unique.index(word),j] += 1	# count of words appearing in the same document (term frequency in document)
        
		df = np.sum(TD_matrix > 0, axis=1)

		self.IDF = np.zeros(len(self.list_unique))	# Initialising the IDF measure 

		for i in range(len(self.list_unique)):
			occ = np.where(TD_matrix[i,:] != 0)[0]
			self.IDF[i] = math.log(D*1.0/len(occ),10)		# Calculating measure based on total documents and documents in which the term appear


		self.doc_weights = np.zeros([len(self.list_unique),len(docs)])
        
		for i in range(len(self.list_unique)):
			self.doc_weights[i,:] = self.IDF[i]*TD_matrix[i,:]   # vector weights for each document, TFIDF matrix calclation
		
		index = {key: None for key in docIDs}  # initialize dictionary with keys as doc_IDs
       
		for j in range(len(docs)): 
			index[docIDs[j]] = self.doc_weights[:,j]   # update dict-values with weight vector for corresponding docIDs                
        
		self.index = index

	def rankVSM(self, queries):
		"""
		Rank the documents according to relevance for each query Vector space model

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []
		self.doc_weights = np.transpose(self.doc_weights)
		TQ_matrix = np.zeros([len(self.list_unique),len(queries)]) # term frequency matrix (for each query in list queries)
        
		for j, query in enumerate(queries):       # iterate over all queries
			for k, sentence in enumerate(query):  # iterate over sentences for a query
				for word in sentence:
					if word in self.list_unique:
						TQ_matrix[self.list_unique.index(word),j] += 1	# count of words appearing in the same query (term frequency in query)

		self.query_weights = np.zeros([len(self.list_unique),len(queries)])
        
		for i, unique_word in enumerate(self.list_unique):
			self.query_weights[i,:] = self.IDF[i]*TQ_matrix[i,:]  # vector weights for each query  
        
		self.query_weights = np.transpose(self.query_weights)	# Transposed to dot with documents weights

		cos_sim = np.dot(self.query_weights, np.transpose(self.doc_weights))

		for i in range(len(queries)):					# iterating over queries and documents 
			for j in range(len(self.doc_weights)):		# To normalise the dot product with their weights
				if np.linalg.norm(self.doc_weights[j]) == 0:	# To avoid division by zero
					cos_sim[i][j] = 0
				else:
					cos_sim[i][j] = cos_sim[i][j] * (1/np.linalg.norm(self.query_weights[i])) * (1/np.linalg.norm(self.doc_weights[j]))


		for i in cos_sim:				#	sorting the documents for each query based on the cosine measure and returning
			sorted_sim = np.argsort(i)[::-1]
			doc_IDs_ordered.append([self.docIDs[j] for j in sorted_sim])
        
		return doc_IDs_ordered

	def rankLSA(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		TQ_matrix = np.zeros([len(self.list_unique),len(queries)]) # term frequency matrix (for each query in list queries)
        
		for j, query in enumerate(queries):       # iterate over all queries
			for k, sentence in enumerate(query):  # iterate over sentences for a query
				for word in sentence:
					if word in self.list_unique:
						TQ_matrix[self.list_unique.index(word),j] += 1	# count of words appearing in the same query (term frequency in query)

		self.query_weights = np.zeros([len(self.list_unique),len(queries)])
        
		for i, unique_word in enumerate(self.list_unique):
			self.query_weights[i,:] = self.IDF[i]*TQ_matrix[i,:]  # vector weights for each query  

		id_docs = list(self.index.keys())
		self.doc_weights = np.transpose(self.doc_weights)		# LSA using the TFIDF matrix of term documents of the dataset
		A = self.doc_weights
		uu, ss, vvt = svd(A)						# SVD is performed on the TFIDF matrix
		s = ss**2
		total_variance = sum(s)
		k = 0
		variance_captured = 0
		for i in range(len(id_docs)):				# Criteria to calculate the cutoff count of principle components
			variance_captured += s[i]				# which is based on variance captured by first k components here 72% is taken as criteria
			if variance_captured/total_variance >= 0.72:
				k = i+1
				break
		print("principal components captured for variance of 72", k)
		U = uu[:, :k]; S = ss[:k]; 			# U is representative of latent terms matrix
		Vt = vvt[:k, :]   					# Vt is representative of latent documents matrix
		docs_rep = Vt.T
		W = uu[:, :k] @ np.diag(ss[:k])
		
		for j in range(len(queries)):		# iterating over the queries to order the documents based on relavence
			querytokns = np.where(self.query_weights[:,j] != 0)[0]		# Getting the latent term matrix for the words in the query
			q = np.dot(self.query_weights[querytokns,j], W[querytokns, :])	# Latent query matrix is mutiplied with TFIDF of measure of query to take into account term frequency
			dot = Vt.T @ q
			for i in range(len(id_docs)):	# normalising the dot product on each query and document
				dot[i] = dot[i]* (1/np.linalg.norm(q)) * (1/np.linalg.norm(docs_rep[i]))
			idx = np.argsort(dot)[::-1]		# sorting the documents for each query based on the cosine similarity measure and returning it
			doc_IDs_ordered.append([self.docIDs[i] for i in idx])
		
		return doc_IDs_ordered