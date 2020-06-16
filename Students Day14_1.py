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
Dict = {}
for eachItem in students:
    student.write(eachItem["name"] + "\n")
    homeAvg = (sum(eachItem["homework"]) / len(eachItem["homework"]))
    student.write(f'The average homework score is : {homeAvg}' + "\n")
    examAvg = (sum(eachItem["exam"]) / len(eachItem["exam"]))
    student.write(f'The average exam score is : {examAvg}' +  "\n")
    result_homework_key = str(eachItem["name"])
    result_exam_key = str(eachItem["name"])
    resultsHome.update({ result_homework_key : homeAvg})
    resultsExam.update({ result_exam_key : examAvg})

max_homework_score = 0
max_homework_student_name = "unknown"
for everyKey, everyValue in resultsHome.items():
    if everyValue > max_homework_score:
        max_homework_score = everyValue
        max_homework_student_name = everyKey
student.write(f'The student with the highest homework score is {max_homework_student_name}. Their score was {max_homework_score}' + '\n')
max_exam_score = 0
max_exam_student_name = "unknown"
for everyKey, everyValue in resultsExam.items():
    if everyValue > max_exam_score:
        max_exam_score = everyValue
        max_exam_student_name = everyKey
student.write(f'The student with the highest homework score is {max_exam_student_name}. Their score was {max_exam_score}')
