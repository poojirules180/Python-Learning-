test_dict = {"idli" : "breakfast","poori" : "breakfast","chapathi" : "dinner","rice" : "lunch","maggie" : "lunch"}
new_dict = {} 
finalDict = {}
#I replaced keys with value and value with keys
for key, value in test_dict.items(): 
   if value in new_dict: 
#making the value into a key
       new_dict[value].append(key) 
   else: 
       new_dict[value]=[key] 
#print key and key value
for i in new_dict: 
    print(i + ":" + new_dict[i])


return_dict = { "breakfast" : ["idli", "poori"],"lunch" : ["rice", "maggie"], "dinner" : ["chapathi"]}