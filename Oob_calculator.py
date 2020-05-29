class Hesapmakinesi():
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def toplama(self):
        toplami = self.sayi1 + self.sayi2
        print("{} ile {}'nin Toplamı {} Eder".format(self.sayi1,self.sayi2,toplami))

    def cikarma(self):
        cikan = self.sayi1 - self.sayi2
        print("{} ile {}'nin Çıkarsa {} Kalır.".format(self.sayi1,self.sayi2,cikan))

    def carpma(self):
        carpilan = self.sayi1 * self.sayi2
        print("{} ile {}'nin Çarpılırsa {} Eder.".format(self.sayi1,self.sayi2,carpilan))

    def bolme(self):
        bolum = self.sayi1 / self.sayi2
        print("{} ile {}'nin Bölünürse {} Kalır.".format(self.sayi1,self.sayi2,bolum))

print("""**********************************
* BlackJack35 OOP Hesap Makinesi *
* işlemler :                     *
* 1-) Toplama                    *
* 2-) Çıkarma                    *
* 3-) Çarpma                     *
* 4-) Bölme                      *
**********************************
Programdan çıkmak için "q" ya Basınız.""")

işlem = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz :")
if işlem == "q":
    print("BlackJack35 İyi Günler Diler.")
    exit()
sayi1 = int(input("Birinci Sayıyı Giriniz :"))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))
deger = Hesapmakinesi(sayi1,sayi2)


if (işlem == "1"):
  sonuc = deger.toplama()

elif (işlem == "2"):
   sonuc = deger.cikarma()

elif (işlem == "3"):
   sonuc = deger.carpma()

elif (işlem == "4"):
   sonuc = deger.bolme()

