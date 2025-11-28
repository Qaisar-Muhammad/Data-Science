print("***************************WEEKLY DASHES IN EACH DAYS IS BELOW***************")
menu={
    'Monday':{'Moring':['Tea','sherpo parata','gabin'],'Evening':['lobai','dal chana','acher gost'],'Night':['mota chawal']},
    'Tuestday':{'Moring':['Tea','parata','mali'],'Evening':['chekan handi','dal mash','sabzeei'],'Night':['chekan rice']},
    'Wednesday':{'Moring':['Tea','mali parata','anda'],'Evening':['rice','lobai','acher gost'],'Night':['banu chawal']},
    'Thursday':{'Moring':['Tea','mali parata','anda'],'Evening':['rice','lobai','acher gost'],'Night':['banu chawal']},
    'Friday':{'Moring':['Tea','sherpo parata','gabin'],'Evening':['lobai','dal chana','acher gost'],'Night':['mota chawal']},
    'saturday':{'Moring':['Tea','parata','mali'],'Evening':['chekan handi','dal mash','sabzeei'],'Night':['chekan rice']},
    'sunday':{'Moring':['Tea','mali parata','anda'],'Evening':['rice','lobai','acher gost'],'Night':['banu chawal']},
}

for i,j in menu.items():
    print(f"Days menu in dashes : {i}")
    for key,value in j.items():
        print(f"  {key.capitalize()} : {value}")