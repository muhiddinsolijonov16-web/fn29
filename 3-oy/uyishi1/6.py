def kontakt_qidir(kontaktlar, ism):
    for key,value in kontaktlar.items():
        if key == ism:
            print("kontakt mavjud\n",key,value)
            break
    else:
        print("bunday kontakt mavjud emas")


son = int(input("nechta kontakt kiritmoqchisz: "))

kontaktlar = {}

for i in range(0,son):
    ism = input("ism: ")
    phone = input("phone: ")
    kontaktlar[ism] = phone

ism = input("qidiruv uchun ism: ")

kontakt_qidir(kontaktlar,ism)

    
