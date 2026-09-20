def qimmat_mahsulotlar(mahsulotlar):
    for key,value in mahsulotlar.items():
        if value > 15000:
            print(key,"-",value)
mahsulotlar = {
    "non": 4000,
    "sut": 10000,
    "shakar": 14000,
    "yog'": 18000,
    "guruch": 16000
}
qimmat_mahsulotlar(mahsulotlar)