# Add your import statements here
from nltk.tokenize import punkt
from nltk.tokenize import treebank
from nltk.stem import PorterStemmer,WordNetLemmatizer 
from nltk.corpus import stopwords  
from spellchecker import SpellChecker
import re
import string as string_lib
import math
import numpy as np
from numpy import dot
from numpy.linalg import norm
import warnings
import operator
from scipy.linalg import svd
warnings.filterwarnings("ignore")




# Add any utility functions here