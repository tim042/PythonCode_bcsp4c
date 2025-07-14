def Out_Of_Town():

    Name = str(input("Enter You Name="))
    Num = int(input("Telephone Number="))
    To = str(input("Delivery To Name="))
    ToNum = int(input("Number="))
    print('''
              ========== Province ===========
              1. Vientiane
              2. Luangprabang
              3. Bolikhamxay
              4. Xayabury
              5. Xaysomboon
              6. Xiengkhuang
              7. Khammuane
              8. Huaphanh
              9. Savannakhet
              10. Oudomxay
              11. Saravane
              12. Bokeo
              13. Luangnamtha
              14. Phongsaly
              15. Sekong
              16. Champasack
              17. Attapeu               
              ''')

    choice = int(input('Enter Choice: '))
    if choice == 1:
        print("Vientiane")
    elif choice == 2:
        print("Luangprabang")
    elif choice == 3:
        print("Bolikhamxay")
    elif choice == 4:
        print("Xayabury")
    elif choice == 5:
        print("Xaysomboon")
    elif choice == 6:
        print("Xiengkhuang")
    elif choice == 7:
        print("Khammuane")
    elif choice == 8:
        print("Huaphanh")
    elif choice == 9:
        print("Savannakhet")
    elif choice == 10:
        print("Oudomxay")
    elif choice == 11:
        print("Saravane")
    elif choice == 12:
        print("Bokeo")
    elif choice == 13:
        print("Luangnamtha")
    elif choice == 14:
        print("Phongsaly")
    elif choice == 15:
        print("Sekong")
    elif choice == 16:
        print(" Champasack")
    elif choice == 17:
        print("Attapeu")

    DC = 5000
    S = 8000
    M = 10000
    L = 12000
    XL = 15000
    PW = 8000

    SB = str(input("Choose Size DC,S,M,L,XL ="))
    W = float(input("Enter Weight (KG)="))

    print("BOX Sizs Is", SB, "Weight IS", W, "KG")
    if SB == "DC" or SB == "dc" or SB == "Dc" or SB == "dC":
        PT = PW * W + DC
        print("Name:::",Name," AND Number:::",Num)
        print("=============To===========")
        print("Name:::",To," AND Number:::",ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "S" or SB == "s":
        PT = PW * W + S
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "M" or SB == "m":
        PT = PW * W + M
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "L" or SB == "l":
        PT = PW * W + L
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "XL" or SB == "xl" or SB == "xL" or SB == "Xl":
        PT = PW * W + XL
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    else:
        print("Wrong Size")
        print("Please Insert It Again")
    Q = input("Would You Like To Use The Service Again? (yes/no)")
    if Q == "no":
        print("=====================")
        print("Thanks")


def In_capital():

    Name = str(input("Enter You Name="))
    Num = int(input("Telephone Number="))
    To = str(input("Delivery To Name="))
    ToNum = int(input("Number="))

    DC = 1000
    S = 2000
    M = 3000
    L = 5000
    XL = 7000
    PW = 3000
    SB = str(input("Choose Size DC,S,M,L,XL ="))
    W = float(input("Enter Weight (KG)="))

    print("BOX Sizs Is", SB, "Weight IS", W, "KG")
    if SB == "DC" or SB == "dc" or SB == "Dc" or SB == "dC":
        PT = PW * W + DC
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "S" or SB == "s":
        PT = PW * W + S
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "M" or SB == "m":
        PT = PW * W + M
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "L" or SB == "l":
        PT = PW * W + L
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    elif SB == "XL" or SB == "xl" or SB == "xL" or SB == "Xl":
        PT = PW * W + XL
        print("Name:::", Name, " AND Number:::", Num)
        print("=============To===========")
        print("Name:::", To, " AND Number:::", ToNum)
        print("=============================")
        print("=============================")
        print("=============================")
        print("Total Price", PT, "Kip")
    else:
        print("Wrong Size")
        print("Please Insert It Again")
    Q = input("Would You Like To Use The Service Again? (yes/no)")
    if Q == "no":
        print("=====================")
        print("Thanks")

while True:
    print('''
          ========== MENU ===========
          1. Out of Town
          2. In Capital
          3. Exit''')

    choice = int(input('Enter Choice: '))
    if choice == 1:
        print()
        Out_Of_Town()
    elif choice == 2:
        print()
        In_capital()
    elif choice == 3:
        print('Goodbye')
        exit()