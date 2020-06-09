# Opening file
readFile = open("poojith.txt", "r")

# running a loop for every line in the file
for line in readFile:
    #You can use the len method to find how many chracters there are.
    #lengthofLine = len(str(line))
    #print(lengthofLine) 
    if 'Python' in line:
        #using the replace method I was able to replace the word Python with Java Script.
        print (line.replace('Python', "Java Script"))