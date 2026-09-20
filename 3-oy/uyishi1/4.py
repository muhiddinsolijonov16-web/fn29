def grades_fanc(baholar):
    for key , value in baholar.items():
        if value >= 60:
            print(key,"-",value,"O'tdi")
        else:
            print(key,"-",value,"Yiqlidi")

baholar = {
    "Ali": 78,
    "Vali": 45,
    "Hasan": 91,
    "Husan": 56,
    "Sardor": 67
}
grades_fanc(baholar)
