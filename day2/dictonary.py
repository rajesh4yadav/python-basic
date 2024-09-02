#mutable
person ={
    "name":'rajesh',
    
    "hobbies": ['playing', 'cycling', 'coding'],
    
    'friends':[ 
        {
        
        'name':'ram',
        
        'hobbies':['playing football','guitar']
    }
        ]
    
    
    
    
}

friend = person['friends'][0]  # Unpacking the first (and only) item in the list
print( friend['name'], friend['hobbies'])


print(person['friends'][0]['name'])
print(person['friends'][0]['hobbies'])
print(person['friends'][0]['hobbies'][1])
print(person['friends'][0]['hobbies'][1][3])
print(person['friends'][0]['name'], person['friends'][0]['hobbies'][1][3])#sinle code for all above 4 line

person["name"] = "ravi"
print(person)#chainging the person name
person['friends'][0]['name'] = 'shyam'
print(person)#chainging the friends name



#print(person['hobbies'])#printing the dictonary
#print(person['name'])#printing the dictonary with indexing
#print(person(friends('name')))#printing the dictonary with indexing
#print(type(person))#printing the dictonary