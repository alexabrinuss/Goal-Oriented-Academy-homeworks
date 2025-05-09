for i in range (20):
    print(i)
    if i % 2:
     print("even")
    else:
       print("odd")
num = 0
while num <= 19:
    if num % 2 == 0:
        print(f"{num} - even")
    else:
        print(f"{num} - odd")
    num += 1

name = "inga"
user_name = input("enter your name:")
if user_name == name:
   print("coincidence")
else:
   print("try again")

score = int(input("Score?:"))
if score >= 70:
   print("passed")
else:
   print("failed")

integer = int(input ("enter score:"))
if integer > 80:
   print("grade A")
elif integer > 60:
   print("grade B")
elif integer > 40:
   print("grade C")
elif integer > 20:
   print("grade D")
else: 
   print("grade F")