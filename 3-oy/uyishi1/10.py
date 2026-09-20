def mahsulotlarni_korsatish(mahsulotlar):
    for key,value in mahsulotlar.items():
        print(key ,"-->",value)

def savatga_qoshish(mahsulotlar, savat):
    maxsulot_nomi = input("maxsulot nomini kiriting: ")
    for i in mahsulotlar:
        if maxsulot_nomi == i:
            savat[i] = mahsulotlar[i]
            return "savatga qoshildi"
            
    else:
        return "bunday maxsulot mavjud emas"

def savatni_korsatish(savat):
    print("Savatdagi maxsulotlar:")
    for key,value in savat.items():
        print(key ,"-->",value)
    

def umumiy_narx(savat):
    sum_narx = 0
    print("Savatdagi maxsulotlar umumiy narxi:")
    for key,value in savat.items():
        sum_narx += value
    print(sum_narx)

    

mahsulotlar = {
    "olma": 12000,
    "banan": 18000,
    "apelsin": 15000,
    "uzum": 20000,
    "anor": 25000
}
savat = {}
while 1:
    print("1. Mahsulotlarni korish\n2. Savatga mahsulot qoshish\n3. Savatni korish\n4. Umumiy narxni korish\n5. Dasturdan chiqish")
    tanlov = int(input("tanlov: "))

    if tanlov == 1:
        mahsulotlarni_korsatish(mahsulotlar)

    elif tanlov == 2:
        print(savatga_qoshish(mahsulotlar,savat))

    elif tanlov == 3:
        savatni_korsatish(savat)

    elif tanlov == 4:
        umumiy_narx(savat)

    elif tanlov == 5:
        print("dastur yakunlandi")
        break

    else:
        print("Xato")    
