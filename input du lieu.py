s = int(input("Input somthing: "))
print ("your input: ", s)
print (type(s))

def StrToBool(s):
    return s.lower() in ("true", "t", "1", "yes")
x = input ("true or false: ")
x = StrToBool(x)
print (x)