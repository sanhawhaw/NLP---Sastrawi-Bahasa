# Python Sastrawi 

# # import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()# stemming process
sentence = 'mencoba-coba untuk melakukan pertumbuhan akar dalam menanan jagung adalah hal yang memudahkan kita untuk memanennya'
output   = stemmer.stem(sentence)
print(output)
# coba untuk laku tumbuh akar dalam nan jagung adalah hal yang mudah kita untuk panen 

#print(stemmer.stem('Mereka meniru-nirukannya'))
# # mereka tiru
