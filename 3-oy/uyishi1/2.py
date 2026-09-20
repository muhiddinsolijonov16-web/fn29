def max_son(sonlar):
    max_num = sonlar[0]
    for i in sonlar:
        if max_num < i:
            max_num = i
    return max_num

def min_son(sonlar):
    min_num = sonlar[0]
    for i in sonlar:
        if min_num > i:
            min_num = i
    return min_num
    


tanlov = int(input("nechta son kiritmoqchisz: "))

sonlar = []

for i in range(1,tanlov+1):
    son = int(input(f"{i}-son: "))
    sonlar.append(son)

print(f"eng katta son {max_son(sonlar)}")
print(f"eng kichik son {min_son(sonlar)}")