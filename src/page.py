#Unit harga
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

#Input jumlah buah
nApel= int(input("Input jumlah apel:"))
nJeruk= int(input("Input jumlah jeruk:"))
nAnggur= int(input("Input jumlah jeruk:"))

#Hitung harga per buah
priceApel = nApel*priceApel
priceJeruk = nJeruk*priceJeruk
priceAnggur = nAnggur*priceAnggur

#Hitung harga total
PriceTotal= priceApel + priceAnggur + priceJeruk

#show answer
print(
    f'''
Detail Belanja

Apel    : {nApel} x {priceApel}
Jeruk   : {nJeruk} x {priceJeruk}
Anggur  : {nAnggur} x {priceAnggur}
Total   : {PriceTotal}   
'''
)