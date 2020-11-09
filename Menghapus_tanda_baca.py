# Menghapus tanda baca
import string 
kalimat = "Ini &adalah Tanda Titik (.) Tanda Koma (,) Tanda Titik Koma (;) Tanda Titik Dua (:) Tanda Tanya (?) Tanda Seru (!)  Tanda Elipsis ..."
kalimat = kalimat.replace('“','').replace('”','')
hasil = kalimat.translate(str.maketrans("","",string.punctuation))
print(hasil)
# # output
# # Ini adalah Tanda Titik  Tanda Koma  Tanda Titik Koma  Tanda Titik Dua  Tanda Tanya  Tanda Seru   Tanda Elipsis
