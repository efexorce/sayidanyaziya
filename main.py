def kelimeayraci(kelime):
    return [karakter for karakter in kelime]

def printci(basamak,rakam):
    if basamak==1:
        return str(rakamlar[rakam])
    if basamak==2:
        return str(onluk[rakam])
    if basamak==3:
        return str(rakamlar[rakam])
###
rakamlar=(["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"])
onluk=(["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"])
binlik=(["", "bin", "milyon", "milyar", "trilyon", "katrilyon","çok"])
###
sayi=input()
uzunluk=len(sayi)
binindex=int((uzunluk-1)//3)
basamak=uzunluk % 3
if basamak==0: basamak=3
yazi=[]

for rakam in kelimeayraci(sayi):    
    yazi.append(printci(basamak,int(rakam)))
    if basamak == 3:
        yazi.append("yüz")
    basamak=basamak-1
    if binindex>0:
        if basamak == 0:
            yazi.append(str(binlik[binindex]))
            binindex=binindex-1
            basamak=basamak+3
tekkelime=""
for eleman in yazi:
    tekkelime=tekkelime+eleman
print(tekkelime)
