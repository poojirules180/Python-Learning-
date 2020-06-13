student = open("student.txt", "a")
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

results = {}

for eachItem in students:
    student.write(eachItem["name"] + "\n")
    homeAvg = (sum(eachItem["homework"]) / len(eachItem["homework"]))
    student.write(f'The average homework score is : {homeAvg}' + "\n")
    examAvg = (sum(eachItem["exam"]) / len(eachItem["exam"]))
    student.write(f'The average exam score is : {examAvg}' +  "\n")
    result_homework_key = str(eachItem["name"]) + '_homework_average_score'
    result_exam_key = str(eachItem["name"]) + '_exam_average_score'
    results.update({ result_homework_key : homeAvg  })
    results.update({ result_exam_key : examAvg})

homeMax = max(results["poojith_homework_average_score"], results["surya_homework_average_score"], results["renuka_homework_average_score"])
if homeMax == results["poojith_homework_average_score"]:
    student.write("Student with best homework score is : Poojith" + "\n")

if homeMax == results["surya_homework_average_score"]:
    student.write("Student with best homework score is : Surya" + "\n")

if homeMax == results["renuka_homework_average_score"]:
    student.write("Student with best homework score is : Renuka" + "\n")


examMax = max(results["poojith_exam_average_score"], results["surya_exam_average_score"], results["renuka_exam_average_score"])

if examMax == results["poojith_exam_average_score"]:
    student.write("Student with best Exam score is : Poojith" + "\n")

if examMax == results["surya_exam_average_score"]:
    student.write("Student with best Exam score is : Surya" + "\n")

if examMax == results["renuka_exam_average_score"]:
    student.write("Student with best Exam score is : Renuka" + "\n")
        
