
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np 


#load file
filename = 'poe.txt'
file = open(filename, 'rt')
text = file.read()
file.close()


# split file 
words = text.split()
words = [word.lower() for word in words]


#remove punctuation 
no_punctuation_list = [w.translate(str.maketrans('','', string.punctuation)) for w in words]

#remove stop words 
stop_words = stopwords.words('english')
no_stop_words = [word for word in no_punctuation_list if word not in stop_words]


#remove non-alphabetic characters
clean_words = [word for word in no_stop_words if word.isalpha()]
print(clean_words[:10])

#bag of words 