def savat_hisobla(mahsulotlar):
    summa_narx = 0
    while 1:
        mahsulot = input("kiriting: ")
        if mahsulot.lower() == "stop":
            break
        for key , value in mahsulotlar.items():
            if key == mahsulot.lower():
                summa_narx += value
                print("qabul qilindi")
                break
        else: 
            print("bunday maxsulot mavjud emas")
    return summa_narx
                
mahsulotlar = {
    "non": 4000,
    "sut": 10000,
    "shakar": 14000,
    "guruch": 16000,
    "yog'": 18000
}

print("jami:",savat_hisobla(mahsulotlar),"som")