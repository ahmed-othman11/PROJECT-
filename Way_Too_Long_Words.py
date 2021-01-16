# defnination function
def name():
    name = input('Enter name: ')      # variable to Receive the input
    if len(name) <= 10:           # if condetion to check len of name 
        return name
    else:
        return name[0] + str(len(name[1:-2])) + name[-1]
        
# ptint fun        
print(name())     
