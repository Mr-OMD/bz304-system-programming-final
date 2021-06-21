#1030520259
#ÖMER MERT DEMİREL

#This program is some kind of calculator. User enters input that wants to calculate. Program writes it in a txt file then asks password.
#if user enter password correctly program read it from file and calculates with eval(). it prints result to both terminal and txt file.
import sys                          #to use in the future we add sys library
yazdir=input("Lütfen işleminizi aralarına işaretleri koyarak tek seferde giriniz: ")
f = open("hesap.txt","w")           #open file in write mode(if there is no file, it creates one)
f.write(yazdir)                     #write in it
f.close()                           #close file
sifre="sifrem123"                   #we set our password
print("İşlemi yapmak için şifreniz gerekmektedir...")
while True:                         #asks password until it entered correctly
    giris=input("Lütfen sifrenizi giriniz: ")
    if giris==sifre:
        print("Doğru şifre!")
        break                       #if entered correctly break the loop
    else:
        print("Yanlış şifre tekrar deneyin!")
f=open("hesap.txt", "r")            #opens file in read mode
hesap=f.read()                      #read its content and give it to variable "hesap"
f.close()                           #close file
try:
    sonuc=eval(hesap)               #evaluate the content
except:                             #if eval function cant evaluate the content, it means content given in wrong format
    print("Yanlış formatta işlem girdiniz, lütfen programı yeniden başlatarak deneyin.\nUygun format örneği: 2*3+4")
    quit()                          #catch the error and explain it to user, then quit
yazi="Hesaplamak istedğiniz işlem: {}\nSonucunuz: {}"
print(yazi.format(hesap,sonuc))     #print resul to terminal
f=open("hesap.txt", "a")            #open file in append mode which adds the given content at the end of file, without deleting older one
oldout=sys.stdout                     #this part is to show diffrent way to print into a file  
sys.stdout=f                          #we imported sys at the beginning so we can change the output direction
print(yazi.format(hesap,sonuc))       #it changed output direction from console to that file and write result
sys.stdout=oldout                     #then changed back to standart output direction
f.close()                             #close file

