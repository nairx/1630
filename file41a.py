try:    
    # print(g)
    f = open("file.txt","r")
except NameError:
    print("Invalid Variable")
except FileNotFoundError:
    print("File does not exist")
else:
    print("Program completed")
finally:
    print("Do Something")
    
