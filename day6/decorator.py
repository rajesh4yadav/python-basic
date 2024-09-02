def hash(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper

def star(func):
    def wrapper():
        print("#"*10)
        func()
        print("#"*10)
    return wrapper
@star
@hash
def hello():
    print("hello")

@hash
def world():
    print("world")

hello()
world()



    

            