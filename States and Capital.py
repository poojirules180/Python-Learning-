from operator import itemgetter
startCapital = [["AP", "Amaravathi"], ["Telangana", "Hyderabad"],["Karnataka" , "Bangalore"],["TamilNadu", "Chennai"],["Maharastra", "Mumbai"]]
sortedByState = sorted(startCapital,key=itemgetter(0))
sortedByCapital = sorted(startCapital,key=itemgetter(1))
print (startCapital)
print (sortedByState)
print (sortedByCapital)