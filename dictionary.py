# name={
#     'name':'qaisar',
#     'age' : 78,
#     'Deptt':'cs'
# }
# print(name['name'])
# print(name.get('name'))
# name1=input("enter a name:")
# print(f"my name is {name1} and  i am belong to Hangu ")
#we can easliy create dictionary with dict constructor
# class1=dict(name='ali',age=445,course='pyhton')
# print(class1)


#below methods are for access the items
# print(name.keys())
# print(name.values())
# print(name.items())
# name['name']='ali khan'  #it update the value through key
# print(name)

# if 'salary' in name:
#     print("it is available")
# else:
#     print("not present")    

#below methods for chande items  in dictionary

# name.update({'name':'MUHAMMAD'})
# print(name)

# name.update({'salary':8800 ,'university':'UET PESHWAR'})  # HERE I ADD the keys,values pairs in dictionry
# print(name)


#below are removes the values from dictionary
# name.pop('name')
# name.popitem()
# del name['Deptt']
# name.clear()


#below used loop in dictionary
# for i in name.items():
#     print(i) 


# for i in name.keys():
#     print(i) 

# for i in name.values():
#     print(i) 
# for i,j in name.items():
#     print(i,j)
# print(name)
# mydic=dict(name)
# print(mydic)
name={
    'name':'qaisar',
    'age' : 78,
    'Deptt':'cs'
}
a=list(name.items())
print(a)
print(type(a))
