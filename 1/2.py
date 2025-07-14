DC = 20000
S = 30000
M = 45000
L = 50000
XL = 65000
PW = 5000

print("Python Project Shipping Cost Calculator")
print("Document = 20,000 Kip")
print("Small Size (10cmx20cmx30cm) = 30,000 Kip")
print("Medium Size (15cmx25cmx40cm) = 45,000 Kip")
print("Large Size (25cmx30cmx50cm) = 50,000 Kip")
print("Extar Large Size (30cmx45cmx70cm) = 65,000 Kip")
print("Weight = 5000Kib per Kilogram")
while True:
   SB = str(input("Choose Size DC,S,M,L,XL ="))
   W = float(input("Enter Weight (KG)="))

   print("BOX Sizs Is", SB, "Weight IS", W,"KG")
   if SB =="DC" or SB=="dc" or SB=="Dc" or SB=="dC":
      PT = PW * W + DC
      print("Total Price",PT,"Kip")

   elif SB =="S" or SB=="s":
      PT = PW * W + S
      print("Total Price",PT,"Kip")
   elif SB=="M" or SB=="m":
      PT = PW * W + M
      print("Total Price",PT,"Kip")
   elif SB=="L" or SB=="l":
      PT = PW * W + L
      print("Total Price",PT,"Kip")
   elif SB=="XL" or SB=="xl" or SB=="xL" or SB=="Xl" :
      PT = PW * W + XL
      print("Total Price",PT,"Kip")
   else:
      print("Wrong Size")
      print("Please Insert It Again")
   Q = input("Would You Like To Use The Service Again? (yes/no)")
   if Q == "no":

      print("=====================")
      print("Thanks")
   break