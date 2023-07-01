This folder contains the additional files required for Part 2 of the assignment, involving building a search engine application. Note that this code works for both Python 2 and Python 3. 

The following files have been added:
informationRetrieval.py and evaluation.py - Implement the corresponding tasks inside the functions in these files.

main.py - The main module that contains the outline of the Search Engine.
util.py - An extra file where we added any additional processing or utility functions that are needed for the sub-tasks mentioned below.
sentenceSegmentation.py - Code to perform a sentence segmentation
tokenization.py - Code to perform sentence tokenization
inflectionReduction.py - Code to perform lemmatisation
stopwordRemoval.py - Code performing the stop word removal operation
spellChecker.py - Code to perform the spellcheck on every word
informationRetrieval.py - this code contains the buildindex and ranking using the VSM, LSA model
evaluation.py - contains functions of evaluation metrics such as precision, recall, nDCG, F-score, MAP, spearmansorrelation

To run our code, run main.py as before with the appropriate arguments.
Usage: main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
               [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 

When the -custom flag is passed, the system will take a query from the user as input. For example:
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
This will print the IDs of the five most relevant documents to the query to standard output.

When the flag is not passed, all the queries in the Cranfield dataset are considered and precision@k, recall@k, f-score@k, nDCG@k and the Mean Average Precision are computed.

In both the cases, *queries.txt files and *docs.txt files will be generated in the OUTPUT FOLDER after each stage of preprocessing of the documents and queries.