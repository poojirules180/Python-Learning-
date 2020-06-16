# Opening file
readFile = open("poojith.txt", "r")
#number of words
data = readFile.read()
#using data.split, It will help me dissect each word in the file.
words = data.split()
numberOfword = ('Number of words in text file :', str(len(words)) + "\n")
print(numberOfword)
w = " ".join(numberOfword)
#code for number of lines
lines = 0
with open("poojith.txt", 'r') as f:
    for line in f:
        lines += 1
numberOflines = ("Total number of lines is:", str(lines) + "\n")
print(numberOflines)
l = " ".join(numberOflines)
#total number of spaces in the files
spaces=0
for spacesinText in data:
    #isspace method will bascially see if there are any spaces in the file, it will say either true and false. If it says yes, It will add 1 to spaces.
    if (spacesinText.isspace()) == True:
        spaces += 1
numberOfspaces = ("The number of blank spaces is: ",str(spaces) + "\n")
print(numberOfspaces)
s = " ".join(numberOfspaces)
#total number of characters in the file
characters = 0
for line in data:
    #You can use the len method to find how many chracters there are.
    characters = characters + len(line)
numberOfchar = ("Number of characters in the file: ", str(characters) + "\n")
print(numberOfchar)
c = " ".join(numberOfchar)
#total number of times Python is mentioned in the file
pythoninText = 0
#It is checking each word to see if it says "python" and then it will add 1 everytime it sees the word "Python".
for line in words:
    if 'Python' in line:
        pythoninText = pythoninText + 1
numberOfpython = ("Number of times Python was mentioned: ", str(pythoninText) + "\n")
print(numberOfpython)
p = " ".join(numberOfpython)
file1 = open("results.txt", "w")
file1.write(w)
file1.write(l)
file1.write(s)
file1.write(c)
file1.write(p)
file1.close()
