# Opening file
readFile = open("poojith.txt", "r")
#number of words
data = readFile.read()
#using data.split, It will help me dissect each word in the file.
words = data.split()
print('Number of words in text file :', len(words))
#code for number of lines
lines = 0
with open("poojith.txt", 'r') as f:
    for line in f:
        lines += 1
print("Total number of lines is:", lines)
#total number of spaces in the files
spaces=0
for spacesinText in data:
    #isspace method will bascially see if there are any spaces in the file, it will say either true and false. If it says yes, It will add 1 to spaces.
    if (spacesinText.isspace()) == True:
        spaces += 1
print("The number of blank spaces is: ",spaces)
#total number of characters in the file
characters = 0
for line in data:
    #You can use the len method to find how many chracters there are.
    characters = characters + len(line)
print("Number of characters in the file: ", characters)
#total number of times Python is mentioned in the file
pythoninText = 0
#It is checking each word to see if it says "python" and then it will add 1 everytime it sees the word "Python".
for line in words:
    if 'Python' in line:
        pythoninText = pythoninText + 1
print("Number of times Python was mentioned: ", pythoninText)