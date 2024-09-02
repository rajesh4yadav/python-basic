try:
    f = open("demofile.txt",)
    f.close()

except FileNotFoundError:
    print("hello")
    


    