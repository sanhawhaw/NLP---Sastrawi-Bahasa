# Tokenizing kata

# # impor word_tokenize dari modul nltk
import nltk
import string
from nltk.tokenize import word_tokenize 
 
kalimat = "makan nasi padang adalah panggilan jiwaku untuk bertahan dari kelaparan."
 
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
 
tokens = nltk.tokenize.word_tokenize(kalimat)
print(tokens)
# # ouput 
# # ['makan', 'nasi', 'padang', 'adalah', 'panggilan', 'jiwaku', 'untuk', 'bertahan', 'dari', 'kelaparan']
