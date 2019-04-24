#%%
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer



#load file
filename = 'poe.txt'
file = open(filename, 'rt')
text = file.read()
file.close()


# split file 
split_text = text.split('*')

document = [work for work in split_text]

print(document[:10])

# #remove punctuation 
# no_punctuation_list = [w.translate(str.maketrans('','', string.punctuation)) for w in words]

# # #remove stop words 
# stop_words = stopwords.words('english')
# no_stop_words = [word for word in no_punctuation_list if word not in stop_words]


# # #remove non-alphabetic characters
# clean_words = [word for word in no_stop_words if word.isalpha()]