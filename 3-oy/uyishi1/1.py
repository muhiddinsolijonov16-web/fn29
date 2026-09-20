def juft_son(sonlar):
    juft_sonlar = []
    for i in sonlar:
        if i % 2 == 0:
            juft_sonlar.append(i) 
    return juft_sonlar

sonlar = [12, 7, 5, 18, 21, 30, 44, 9]

print(juft_son(sonlar))

