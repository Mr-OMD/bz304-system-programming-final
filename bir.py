#1030520259
#ÖMER MERT DEMİREL

#This program prints the sum of first "r" natural numbers
sum = 0                 #Variable to store the sum
lisans="AA-OMD"         #Licance number is similar to password. it enables user to use a diffrent feature
r=input("Kaça kadar toplayalım? Giriniz: ")
try:                    #tries to catch an error early to prevent future errors
    r=int(r)            #if program gives ana error at this stage, it means input is in wrong format
except:
    print("Geçersiz format girildi! Lütfen doğal sayı giriniz! Çıkılıyor...")
    quit()              #it warns user and exits
if r>=100:
    kontrol=input("100`den sonrasını hesaplamak ücretlidir, devam etmek için lütfen lisans numaranızı giriniz: ")
    #Asks user to enter licance number. user enter anything but only if it is true(check later) it can reach a feature
# iterating over natural numbers using range()
for val in range(1, r):
    # calculating sum
    sum+=val
    if val>=100:                #to check licance, program waits until user needs to use thah premium future
        if kontrol==lisans:     #checks licance. if it is true than continues 
            continue
        else:                   #if it is wrong, then warns before quits
            print("Geçersiz lisans, gelecekte sorun yaşamamak için lütfen yöneticiden lisans anahtarı alın!\nProgramdan çıkılıyor...")
            quit()
else:
    # displaying sum of first "r" natural numbers
        uzunluk=len(str(sum))   #sometimes it gives an error while using len with other type of variables. So I converted it to Str 
        yazi="Sonucunuz {}, bir {} basamaklı sayıdır"
        print(yazi.format(sum,uzunluk))   #displays sum of first "r" natural numbers