poojith = {
    "name" : "poojith",
    "homework" : [90, 99.7, 85, 70, 94],
    "exam" : [80, 78, 96, 87, 87],
}

surya = {
    "name" : "surya",
    'homework' : [65, 97, 80, 70, 64],
    "exam" : [80, 98, 96, 87, 97],
}

renuka = {
    "name" : "renuka",
    "homework" : [86, 30, 99, 89, 94],
    "exam" : [80, 88, 96, 97, 95],
}
#Combining the Dictionaries into one Dictonary
def mergeStudents(poojith, surya,renuka):
    students = {**poojith, **surya, **renuka}
    for key, value in students.items():
        if key in poojith and key in surya and key in renuka:
            students[key] =  [poojith[key], surya[key],renuka[key]]
    return students
students = mergeStudents(poojith, surya, renuka)
#All names
if "name" in students:
    print(students["name"])
#Poojith's Avg Homework score
if "homework" in students:
    list = list(students.items())
    x = (list[1])
    y = x[1]
    poojithHome = y[0]
    homeAvg = sum(poojithHome) / len (poojithHome)
    homework = (print("Homework average of Poojith = ", homeAvg))
#Poojith's Avg Exam score
if "exam" in students:
    x = (list[2])
    y = x[1]
    poojithExam = y[0]
    examAvg = sum(poojithExam) / len (poojithExam)
    homework = (print("Exam average of Poojith = ", examAvg))
#Surya's Avg Homework score
if "homework" in students:
    x = (list[1])
    y = x[1]
    suryaHome = y[1]
    homeAvg = sum(suryaHome) / len (suryaHome)
    homework = (print("Homework average of Surya = ", homeAvg))
#Poojith's Avg Exam score
if "exam" in students:
    x = (list[2])
    y = x[1]
    suryaExam = y[1]
    examAvg = sum(suryaExam) / len (suryaExam)
    homework = (print("Exam average of Surya = ", examAvg))
#Renuka's Avg Homework score
if "homework" in students:
    x = (list[1])
    y = x[1]
    renukaHome = y[2]
    homeAvg = sum(renukaHome) / len (renukaHome)
    homework = (print("Homework average of Renuka = ", homeAvg))
#Poojith's Avg Exam score
if "exam" in students:
    x = (list[2])
    y = x[1]
    renukaExam = y[2]
    examAvg = sum(renukaExam) / len (renukaExam)
    homework = (print("Exam average of Renuka = ", examAvg))

#Finding the max Homework score
homeMax = max(poojithHome,suryaHome,renukaHome)
if homeMax == poojithHome:
    avg1 = print("Student with best homework score is : Poojith")
if homeMax == suryaHome:
    avg2 = print("Student with best homework score is : Surya")
if homeMax == renukaHome:
    avg3 = print("Student with best homework score is : Renuka")
#Finding the max Exam scores
examMax = max(poojithExam,suryaExam,renukaExam)
if examMax == poojithExam:
    examAvg1 = print("Student with best Exam score is : Poojith")
if examMax == suryaExam:
    examAvg2 = print("Student with best Exam score is : Surya")
if examMax == renukaExam:
    examAvg3 = print("Student with best Exam score is : Renuka")