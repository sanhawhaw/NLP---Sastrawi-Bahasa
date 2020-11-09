# Filtering dengan sastrawi 2.0
import string
import nltk
import Sastrawi

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

kalimat = "makan nasi padang adalah panggilan jiwaku untuk bertahan dari kelaparan. Ketika kesedihan melanda negeri dongeng."
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()

stop = stopword.remove(kalimat)
tokens = nltk.tokenize.word_tokenize(stop)
print(tokens)
# # output
# # ['makan', 'nasi', 'padang', 'panggilan', 'jiwaku', 'bertahan', 'kelaparan', 'kesedihan', 'melanda', 'negeri', 'dongeng']
