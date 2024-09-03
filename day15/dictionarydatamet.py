places={
    'District':'ktm',
    'hi':"guys",
    
    'city': [  'lahan',
        'Dharan',
        "Illam",
        "lalitpur"],
    'alphabet':['a','b','c'],
    'person':{
        'name':'ram',
        'hobbies':['playing','dancing','sleeping']
        
    }
    }

# print(len(places))
# print(places.keys())
# print(places.values())
# print(places.items())
# print(places.get('District'))
# print(places.get('hi'))
# print(places.pop('hi'))

country={
    'Nepal':"Asia",
    'Germany':'Europe'
}
print(places.update(country))
print(places)
print(places.keys())