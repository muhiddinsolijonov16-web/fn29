import random

def son_topish(sirli_son):
    count = 0
    while 1:
        print("-"*50)
        count += 1
        son = int(input("son: "))
        if sirli_son == son:
            print(f"Tabriklayman {count} ta urunishda topdingiz !!!")
            break
        else:
            if son > sirli_son:
                print("kichikroq son kiriting")
            else:
                print("kattaroq son kiriting")
while 1:
    print("-"*50)
    print("       MENU\n1.O'ynash\n2.stop")
    tanlov = int(input("tanlov kiriting: "))
    if tanlov == 1:
        sirli_son = random.randint(1,100)
        son_topish(sirli_son)
    elif tanlov == 2:
        print("dastur yakunlandi")
        break
        

