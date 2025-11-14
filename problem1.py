Set = {"Seb":"Apple", "kela":"Banana",
       "Aam":"Mango", "Santara":"Orange", "Anar":"Pomegranate"}
usrin = (input ("Provide the Hindi word of any from 'Seb','Kela','Aam','Santara','Anar': "))

print("The English word for", usrin, "is", Set[usrin] if usrin in Set else "not found in the set")