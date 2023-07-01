from util import *

# Add your import statements here




class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		retrieved = 0
		rel = 0
		for docID in query_doc_IDs_ordered:
			retrieved+= 1			#	count of retrived documents
			if docID in true_doc_IDs:
				rel += 1			#	count of relavant documents
			if retrieved == k:			
				break
		precision = (rel/retrieved)
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		prec_sum  = 0
		count = 0
		for i,query_doc_IDs_ordered in enumerate(doc_IDs_ordered):
            
			true_doc_IDs = []
            
			while int(qrels[count]["query_num"]) == query_ids[i]:
				true_doc_IDs.append(int(qrels[count]["id"]))	# getting the relavant documents for each query
				count += 1
				if count == len(qrels):
					break
				
			prec = self.queryPrecision(query_doc_IDs_ordered, query_ids[i], true_doc_IDs, k)	# calculating precision for each query
			prec_sum += prec

		meanPrecision = prec_sum/len(query_ids)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1
		#Fill in code here
		retrieved_rel = 0
		retr = 0
		relevant = len(true_doc_IDs)
		for docID in query_doc_IDs_ordered:
			retr +=1				#	count of retrived documents
			if docID in true_doc_IDs:
				retrieved_rel +=1	#	count of relavant documents
			if retr == k:
				break
		recall = (retrieved_rel/relevant)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""
		meanRecall = -1
		#Fill in code here
		recall_sum  = 0
		count = 0
		for i,query_doc_IDs_ordered in enumerate(doc_IDs_ordered):
			
			true_doc_IDs = []
			while int(qrels[count]["query_num"]) == query_ids[i]:
				true_doc_IDs.append(int(qrels[count]["id"]))	# getting the relavant documents for each query
				count += 1
				
				if count == len(qrels):
					break
				
			rec = self.queryRecall(query_doc_IDs_ordered, query_ids[i], true_doc_IDs, k)	# calculating recall for each query
			recall_sum += rec
		
		meanRecall = recall_sum/len(query_ids)
		
		return meanRecall

	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		a = 0.5 #alpha
		p = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k) # calculating precision
		r = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)    # calculating recall
		if p*r == 0:
			fscore = 0
		else:
			fscore = 1/(a*(1/p)+(1-a)*(1/r))

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		fscore_sum  = 0
		count = 0
		for i,query_doc_IDs_ordered in enumerate(doc_IDs_ordered):
			true_doc_IDs = []
			while int(qrels[count]["query_num"]) == query_ids[i]:
				true_doc_IDs.append(int(qrels[count]["id"]))		# collecting relavant documents of the query
				count += 1			
				if count == len(qrels):
					break
				
			fscore_sum  += self.queryFscore(query_doc_IDs_ordered, query_ids[i], true_doc_IDs, k)	# Calculating Fscore for each query
		meanFscore = fscore_sum/len(query_ids)
		return meanFscore

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The dictionary of tru docIDs with their relavance measure of the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here
		relevance = list(range(k))
		true_doc_IDs_proxy = [x for x,_ in true_doc_IDs]
		true_relevance_proxy = [y for _,y in true_doc_IDs]

		for i,docID in enumerate(query_doc_IDs_ordered):
			try:
				index = true_doc_IDs_proxy.index(docID)			# storing the relavant retreived document
				relevance[i] = true_relevance_proxy[index]		# and its relavance measure
			except:
				relevance[i] = 0
			if i == k-1:
				break
				
		DCG  = 0
		for i,rel in enumerate(relevance):
			DCG += rel/math.log((i+2),2)  # formula: summation over relavance/i+1   
		
		IDCG = 0  # Ideal DCG which is calculated with relevance array sorted 
		
		relevance_sort = list(sorted(true_relevance_proxy, reverse=True))
		
		for i,rel in enumerate(relevance_sort):
			if rel == 0:
				break
			IDCG += rel/math.log((i+2),2) 	#	calculating the ideal measure using the true documents
			if i == k-1:
				break

		if DCG == 0:
			nDCG = 0
		else: 
			nDCG = DCG/IDCG
		return nDCG



	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		NDCG_sum  = 0
		count = 0
		for i,query_doc_IDs_ordered in enumerate(doc_IDs_ordered):
			
			true_doc_IDs = []
			
			while int(qrels[count]["query_num"]) == query_ids[i]:
				true_doc_IDs.append((int(qrels[count]["id"]), 5-int(qrels[count]["position"])))
				count += 1		# getting queries tru documents and their measure of relavance
				if count == len(qrels):
					break
				
			nDCG = self.queryNDCG(query_doc_IDs_ordered, query_ids[i], true_doc_IDs, k)	# calculating the nDCG measure for each query
			NDCG_sum += nDCG
		
		meanNDCG = NDCG_sum/len(query_ids)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		retrieved = 0
		relavant = 0
		precisions = []
		
		for docID in query_doc_IDs_ordered:
			retrieved+= 1		# count of retrieved documents
			
			if docID in true_doc_IDs:
				relavant += 1	# count of relavant documents
				precisions.append(relavant/retrieved)	
			
			if retrieved == k:                                       
				break
		if relavant == 0:
			avgPrecision = 0
		else:    	# avg precison is sum of precision at each retrived document
			avgPrecision = sum(precisions)/relavant

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		AP_sum  = 0
		count = 0
		for i,query_doc_IDs_ordered in enumerate(doc_IDs_ordered):
			
			true_doc_IDs = []
			
			while int(q_rels[count]["query_num"]) == query_ids[i]:
				true_doc_IDs.append(int(q_rels[count]["id"]))
				count += 1
				if count == len(q_rels):	#collecting true documents for each query
					break
				
			avg_prec = self.queryAveragePrecision(query_doc_IDs_ordered, query_ids[i], true_doc_IDs, k)	#calculating MAP for each query
			AP_sum += avg_prec
		
		meanAveragePrecision = AP_sum/len(query_ids)
		return meanAveragePrecision


	def querySMC(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of SMC of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The Dictionary of documents relevant to the query and their relavance measure (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The SMC value as a number between 0 and 1
		"""

		SMC = -1

		#Fill in code here
		relevance = list(range(k))
		true_doc_IDs_proxy = [x for x,_ in true_doc_IDs]
		true_relevance_proxy = [y for _,y in true_doc_IDs]
		meanx = 0
		meany = 0

		for i,docID in enumerate(query_doc_IDs_ordered):
			try:
				index = true_doc_IDs_proxy.index(docID)
				relevance[i] = true_relevance_proxy[index]
				meanx += relevance[i]	# calculating the mean of the relavance measure of the retrieved documents
			except:
				relevance[i] = 0
			if i == k-1:
				break
		meanx = meanx/k
		
		relevance_sort = list(sorted(true_relevance_proxy, reverse=True))
		
		for i,rel in enumerate(relevance_sort):
			if rel == 0:
				break
			meany += rel
			if i == k-1:	# calculating the mean of the relavance measure of the true documents
				break
		meany = meany/k

		sigmanum = 0
		sigmax = 0			# calculating the SMC measures each summation
		sigmay = 0
		for i, rel in enumerate(relevance):
			x = rel
			if i < len(relevance_sort):
				y = relevance_sort[i]
			else:
				y = 0
			sigmanum += (x-meanx)*(y-meany)
			sigmax += (x-meanx)*(x-meanx)
			sigmay += (y-meany)*(y-meany)

		if sigmax == 0 or sigmay == 0:
			SMC = 0
		else:
			SMC = sigmanum/((sigmax*sigmay)**0.5)
		return SMC



	def meanSMC(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of SMC of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean SMC value as a number between 0 and 1
		"""

		meanSMC = -1

		#Fill in code here
		SMC_sum  = 0
		count = 0
		for i,query_doc_IDs_ordered in enumerate(doc_IDs_ordered):
			
			true_doc_IDs = []
			
			while int(qrels[count]["query_num"]) == query_ids[i]:
				true_doc_IDs.append((int(qrels[count]["id"]), 5-int(qrels[count]["position"])))
				count += 1		#collecting the true relavant documents of the query
				if count == len(qrels):
					break
				
			SMC = self.querySMC(query_doc_IDs_ordered, query_ids[i], true_doc_IDs, k)	# calculating the SMC measure for each query
			SMC_sum += SMC
	
		meanSMC = SMC_sum/len(query_ids)
		return meanSMC