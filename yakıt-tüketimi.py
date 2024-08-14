benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

ortalamaYakitTuketimi = float(input("100 kmdeki ortalama  yakıt tüketimi :   "))
gidilecekYol = float(input("gidilen mesafe :  "))
yakitTipi = input("Yakıt Tipi :  ")


toplamYakitUcreti = 0
toplamTakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi/100)
if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamTakitTuketimi
    
elif(yakitTipi == "dizel"):
    toplamTakitTuketimi = dizelFiyat * toplamTakitTuketimi
elif(yakitTipi == "lpg"):
    toplamTakitTuketimi = lpgFiyat * toplamTakitTuketimi
else:
    print("yanlış yakıt tipi ")

if(toplamYakitUcreti != 0):
    print(toplamYakitUcreti)
