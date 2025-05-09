num = 1 != 3    
num00 = 4 != 4   
num01 = 1 != 1  
num02 = 0 != 0
num03 = 0 != 3
print(num or num00 > 50) # True
print( num00 and num01 > 20) # False
print(num03 and num < 70) # True
print(num02 or num > 30) # False
print( num00 and num01 > 12) # False