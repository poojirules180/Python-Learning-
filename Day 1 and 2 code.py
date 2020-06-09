msg = "hello world"
for x in range(6):
    print(msg)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

color = ["red", "blue", "green"]
for x in color:
    if x == "blue":
        continue
    print(color)


g = input("enter your name: ")
print (g)

p = input("enter a value that is higher than one and less than or equal to 6: ")
if int(p) >= 1 and int(p) <= 6:
    if int(p) >= 1:
        print("1")
    if int(p) >= 2:
        print("2")
    if int(p) >= 3:
        print("3")
    if int(p) >= 4:
        print("4")
    if int(p) >= 5:
        print("5")
    if int(p) >= 6:
        print("6")