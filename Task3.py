# We can write our code under the if statement below to 
#.. to allow runnig the code only from the current file 
#-- this mean the code can not be ran when we import this 
#.. file and run it in other external files :)
if __name__ == '__main__':
    # Read a and b from the keyboard/user
    a = int(input('input a:'))
    b = int(input('input b:'))

    #  math operations:
    c= a+b # additon 
    print(c)
    c= a-b # additon
    print(c)
    c= a*b # additon
    print(c)

    print('----'*25) # To print line 
    ''' We can perfom math operations inside '()' of the 'print'
     function and it will print the result directly as the following:
    '''
    
    print(a+b)
    print(a-b)
    print(a*b)