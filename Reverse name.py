def reverse(s):
    reversedName = ""
    for x in s:
        reversedName = x + reversedName
    return reversedName
s = input("What is your name? : ")
print ("my name in reverse is : " + reverse(s))