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
for eachItem in students:
    print(eachItem["name"])
    homeAvg = (sum(eachItem["homework"]) / len(eachItem["homework"]))
    print((homeAvg))
    examAvg = (sum(eachItem["exam"]) / len(eachItem["exam"]))
    print(examAvg)
    dictionary = {}
    dictionary.update({"poojith": homeAvg})
    dictionary.update({"surya": homeAvg})
    dictionary.update({"renuka": homeAvg})
print(dictionary[0:1])