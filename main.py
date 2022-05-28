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
rakamlar=(["", "BİR", "İKİ", "ÜÇ", "DÖRT", "BEŞ", "ALTI", "YEDİ", "SEKİZ", "DOKUZ"])
onluk=(["", "ON", "YİRMİ", "OTUZ", "KIRK", "ELLİ", "ALTMIŞ", "YETMİŞ", "SEKSEN", "DOKSAN"])
binlik=(["", "BİN", "MİLYON", "MİLYAR", "TRİLYON", "KATRİLYON","çok"])
###
yazi=[]

def sayidanyaziya(sayi):
    
    uzunluk=len(sayi)
    binindex=int((uzunluk-1)//3)
    basamak=uzunluk % 3
    if basamak==0: basamak=3
    sayac=0
    for rakam in kelimeayraci(sayi):   
        if int(rakam)==1:
            if int(basamak) ==3:
                yazi.append("YÜZ")
            if int(basamak) ==2:
                yazi.append("ON")         
            if int(basamak) ==1:
                if int(binindex)!=1:
                    yazi.append("BİR")
        
        else:
           
            yazi.append(printci(basamak,int(rakam)))
            if int(basamak) ==3:
                if not int(rakam)==0:
                    yazi.append("YÜZ")


        basamak=basamak-1
        if int(rakam)==0:
            sayac=sayac+1
        else:
            sayac=0


        if (binindex>0):
            if basamak == 0:
                if(sayac<3):
                    yazi.append(str(binlik[binindex]))
                binindex=binindex-1
                basamak=basamak+3

    tekkelime=""
    for eleman in yazi:
        tekkelime=tekkelime+eleman
    yazi.clear()
    return(tekkelime)


sayi="1451"

print(sayidanyaziya(sayi))
#yazi.clear()


