def Out_Of_Town():

    Name = str(input("Enter Your Name="))
    Num = int(input("Telephone Number="))
    To = str(input("Consignee="))
    ToNum = int(input("Telephone Number="))
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
        print("Viengchan(Phonehong)Tel:2095422671")
    elif choice == 2:
        print("Luangprabang (Nakhonluangprabang) Tel:2095422672")
    elif choice == 3:
        print("Bolikhamxay(parkzun)Tel:2095422673")
    elif choice == 4:
        print("Xayabury(Xayyabury)Tel:2095422674")
    elif choice == 5:
        print("Xaysomboon(Anouvong)Tel:2095422675")
    elif choice == 6:
        print("Xiengkhuang(Phonsavanh) Tel:2095422676")
    elif choice == 7:
        print("Khammuane(Thakheak)Tel:2095422677")
    elif choice == 8:
        print("Huaphanh(Samneua)Tel:2095422678")
    elif choice == 9:
        print("Savannakhet(Nakonkaison phomvihan)Tel:2095422679")
    elif choice == 10:
        print("Oudomxay(Houn)Tel:2095422670")
    elif choice == 11:
        print("Saravane(Tah Aoi)Tel:2095422611")
    elif choice == 12:
        print("Bokeo(Houayxay)Tel:2095422612")
    elif choice == 13:
        print("Luangnamtha(Sing)Tel:2095422613")
    elif choice == 14:
        print("Phongsaly(Yod AU)Tel:2095422614")
    elif choice == 15:
        print("Sekong(Darkjueng) Tel:2095422615")
    elif choice == 16:
        print(" Champasack(Nakhon pakse) Tel:2095422616")
    elif choice == 17:
        print("Attapeu(sanamxay) Tel:2095422617")

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
    Q = input("Go to Menu (Yes/Y)")
    if Q == "Yes" or "y" or "Y":
        print("=====================")
        print("Thanks")

def In_capital():

    Name = str(input("Enter Your Name="))
    Num = int(input("Telephone Number="))
    To = str(input("Consignee="))
    ToNum = int(input("Telephone Number="))


    print('''
                  ========== BRANCH ===========
                  1. Wattai
                  2. Thatluang
                  3. Dongdok
                  ''')

    choice = int(input('Enter Choice: '))
    if choice == 1:
        print("Wattai Tel 58131411")
    elif choice == 2:
        print("Thatluang Tel 58131412")
    elif choice == 3:
        print("Dongdok Tel 58131413")

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
    Q = input("Go to Menu (Yes/Y)")
    if Q == "Yes" or "y" or "Y":
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
        Out_Of_Town()
    elif choice == 2:
        In_capital()
    elif choice == 3:
        print("Goodbye")
        exit()