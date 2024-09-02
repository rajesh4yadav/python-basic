Name=' rajesh '
print(len(Name))
print(Name.lower())
print(Name.upper())
print(Name.strip())
print(Name.split())

hi="this is example of split method for string"
R=hi.split()
print(R)
print(hi.split())
print(hi.center(100))

txt = "I love apples, apple are my favorite fruit my "

x = txt.count("my")

print(x)

txt = "banana is always yellow in color and it's price is {} and {} 1"
x = txt.center(10,'*')
print(x)

print(hi.encode())
print(txt.encode())
print(txt.endswith('1'))
print(txt.find('price'))
print(txt.format(20,40))
print(txt.index('price'))
print(txt.join('$'))
name=('raj','bus','car')
symbol='$'
print(symbol.join(name))

