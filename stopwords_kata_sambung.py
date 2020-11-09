# # Filtering (Stopword Removal)
# # Filtering dengan NLTK

import nltk
import string

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
 
kalimat = "makan nasi padang adalah panggilan jiwaku untuk bertahan dari kelaparan. Ketika kesedihan melanda negeri dongeng."
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
 
tokens = word_tokenize(kalimat)
listStopword =  set(stopwords.words('indonesian'))
 
removed = []
for t in tokens:
    if t not in listStopword:
        removed.append(t)
 

print(removed)

# ouput
# # ['makan', 'nasi', 'padang', 'panggilan', 'jiwaku', 'bertahan', 'kelaparan', 'kesedihan', 'melanda', 'negeri', 'dongeng']
