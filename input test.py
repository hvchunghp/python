var1 = input("input a: ")
var2 = input("input b: ")

try: 
   a = int(var1)
   b = int(var2)
   sum = a + b
   print("sum of a and b: ", sum)
except: 
   print("invalid input!")