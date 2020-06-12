import collections
poojith = {
    "name" : "poojith",
    "homework" : [90, 99.7, 85, 70, 94],
    "exam" : [80, 78, 96, 87, 87],
}

surya = {
    "name2" : "surya",
    'homework2' : [65, 97, 80, 70, 64],
    "exam2" : [80, 98, 96, 87, 97],
}

renuka = {
    "name3" : "renuka",
    "homework3" : [86, 30, 99, 89, 94],
    "exam3" : [80, 88, 96, 97, 95],
}
#Combining the dictionaries into one list
chain = collections.ChainMap(poojith,surya,renuka)
if "name" in chain:
    name = print("Name = ", chain["name"])  
if "homework" in chain:
    homeAvg = sum(chain["homework"]) / len (chain["homework"])
    homework = (print("Homework = ", homeAvg))
if "exam" in chain:
    examAvg = sum(chain["exam"]) / len (chain["exam"])
    exam = print("Exam = ", examAvg)
if "name2" in chain:
    name2 = print("Name = ", chain["name2"])    
if "homework2" in chain:
    home2Avg = sum(chain["homework2"]) / len (chain["homework2"])
    homework2 = print("Homework = ", home2Avg)
if "exam2" in chain:
    exam2Avg = sum(chain["exam2"]) / len (chain["exam2"])
    exam2 = print("Exam = ",exam2Avg )
if "name3" in chain:
    name3 =print("Name = ", chain["name3"])    
if "homework3" in chain:
    home3Avg = sum(chain["homework3"]) / len (chain["homework3"])
    homework3 = print("Homework = ", home3Avg)
if "exam3" in chain:
    exam3Avg = sum(chain["exam3"]) / len (chain["exam3"])
    exam3 = print("Exam = ", exam3Avg)
#Finding the max Homework score
homeMax = max(homeAvg,home2Avg,home3Avg)
if homeMax == homeAvg:
    avg1 = print("Student with best homework score is : Poojith")
if homeMax == home2Avg:
    avg2 = print("Student with best homework score is : Surya")
if homeMax == home3Avg:
    avg3 = print("Student with best homework score is : Renuka")
#Finding the max Exam scores
examMax = max(examAvg,exam2Avg,exam3Avg)
if examMax == examAvg:
    examAvg1 = print("Student with best Exam score is : Poojith")
if examMax == exam2Avg:
    examAvg2 = print("Student with best Exam score is : Surya")
if examMax == exam3Avg:
    examAvg3 = print("Student with best Exam score is : Renuka")


