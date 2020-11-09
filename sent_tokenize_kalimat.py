# Tokenizing kalimat
# # impor sent_tokenize dari modul nltk
import nltk
from nltk.tokenize import sent_tokenize
kalimat = "makan nasi padang adalah panggilan jiwaku untuk bertahan dari kelaparan. Ketika kesedihan melanda negeri dongeng."
 
tokens = nltk.tokenize.sent_tokenize(kalimat)
print(tokens)
# # ouput
# # ['makan nasi padang adalah panggilan jiwaku untuk bertahan dari kelaparan.', 'Ketika kesedihan melanda negeri dongeng.']
