def statistika(oquvchilar):
    count_59 = 0
    count_61 = 0
    print("Imtihondan otgan oquvchilar")
    for key,value in oquvchilar.items():
        if value >= 60:
            
            print(key)
            count_61 += 1
    print(f"soni {count_61} ta")
    print("-"*50)

    print("imtihondan ota olmagan oquvchilar")
    for key,value in oquvchilar.items():
            if value < 60:
                
                print(key)
                count_59 += 1
    print(f"soni {count_59} ta")
    print("-"*50)

    max_grade = 0
    for key,value in oquvchilar.items():
         if max_grade < value:
              max_grade = value
    print(f"eng yuqor ball: {max_grade}")
    print("-"*50)

    min_grade = 101
    for key,value in oquvchilar.items():
        if min_grade > value:
            min_grade = value
    print(f"eng past ball: {min_grade}")
    print("-"*50)
    

    sum_grade = 0
    for key,value in oquvchilar.items():
         sum_grade += value
    print("ortacha ball")
    print(sum_grade / len(oquvchilar))
    print("-"*50)
         



oquvchilar = {
    "Ali": 85,
    "Vali": 45,
    "Hasan": 72,
    "Husan": 58,
    "Sardor": 91,
    "Jasur": 63
}

statistika(oquvchilar)



    
