student = open("student.txt", "w")
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

students = []
students.append(poojith)
students.append(surya)
students.append(renuka)

resultsHome = {}
resultsExam = {}
studentsName = []
Dict = {}
for eachItem in students:
    student.write(eachItem["name"] + "\n")
    studentsName.append(eachItem["name"])
    homeAvg = (sum(eachItem["homework"]) / len(eachItem["homework"]))
    student.write(f'The average homework score is : {homeAvg}' + "\n")
    examAvg = (sum(eachItem["exam"]) / len(eachItem["exam"]))
    student.write(f'The average exam score is : {examAvg}' +  "\n")
    result_homework_key = str(eachItem["name"])
    result_exam_key = str(eachItem["name"]) + '_exam_average_score'
    resultsHome.update({ result_homework_key : homeAvg})
    resultsExam.update({ result_exam_key : examAvg})


homeValues = list(resultsHome.values())
examValues = list(resultsExam.values())
maxScore = max(homeValues)
max_score_exam = max(examValues)
for everyNumber in homeValues:
    if maxScore == everyNumber:
        print("Student with best homework score is : "  "\n")
for everyNumber in examValues:
    if max_score_exam == everyNumber:
        print("Student with best exam score is : "  "\n")
