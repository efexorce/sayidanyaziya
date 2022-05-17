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
yazi=[]

def sayidanyaziya(sayi):
    
    uzunluk=len(sayi)
    binindex=int((uzunluk-1)//3)
    basamak=uzunluk % 3
    if basamak==0: basamak=3

    for rakam in kelimeayraci(sayi):   
        if int(rakam)==1:
            if int(basamak) ==3:
                yazi.append("yüz")
            if int(basamak) ==2:
                yazi.append("on")         
            if int(basamak) ==1:
                yazi.append("bir")
        
        else:
           
            yazi.append(printci(basamak,int(rakam)))
            if int(basamak) ==3:
                if not int(rakam)==0:
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


sayi=input()
sayidanyaziya(sayi)
yazi.clear()
sayi=input()
sayidanyaziya(sayi)
yazi.clear()
sayi=input()
sayidanyaziya(sayi)
yazi.clear()
sayi=input()
sayidanyaziya(sayi)
yazi.clear()


