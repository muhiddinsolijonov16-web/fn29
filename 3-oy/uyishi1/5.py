def takrorlanmas_sonlar(sonlar):
    nums = []
    for i in sonlar:
        if i not in nums:
            nums.append(i)
    return nums



sonlar = [2, 5, 2, 8, 5, 9, 2, 8, 10, 5]

print(takrorlanmas_sonlar(sonlar))