'''This code converts number from one system to another from scratch,
 without using built-in function (bin(),hex(),etc.). which is in file Task24_v2
'''
print('New Run :)'.center(100,'-'))

# method for hexa conversion
def to_hexa(n):
    n = int(n)
    local_hexa =''
    if n <=9:
        local_hexa = n
    elif n in (10,11,12,13,14,15):
        if n ==10 : local_hexa='A'
        elif n ==11 : local_hexa='B'
        elif n ==12 : local_hexa='C'
        elif n ==13 : local_hexa='D'
        elif n ==14 : local_hexa='E'
        elif n ==15 : local_hexa='F'
    elif n>=16:
        d=''
        while (n>0):
            d += str(to_hexa(n % 16))
            n=int(n/16) 
        local_hexa = ''.join(reversed(d))
    return local_hexa

# method for octal conversion
def to_octal(n):
    l_octal =''
    if n <=7:
            l_octal = n
    else:
        d=''
        while (n>0):
            d += str(to_octal(n % 8))
            n=int(n/8) 
        l_octal= ''.join(reversed(d))

    return l_octal




    



def print_formatted(number):
    padding = len(bin(number))-2
    for i in range(number):
        decimal = i+1
        str_decimal =''
        octal = ''
        hexa = ''
        binary = ''
        d=decimal

        #To binary
        while (d>0):
            binary += str(d % 2)
            d = int(d /2)
        binary = ''.join(reversed(binary))
        #binary = reversed_string = binary[::-1]
        d=decimal
        #To Hexadecimal
        hexa = to_hexa(decimal)

        d=decimal

        #To Ocatal
        octal = to_octal(decimal)



    
        print(f'{decimal:>{padding}}', f'{octal:>{padding}}', f'{hexa:>{padding}}', f'{binary:>{padding}}')



    # your code goes here
if __name__ == '__main__':
    n = int(input('Enter number  n: '))
    print_formatted(n)

    





#file Task24_v2 solve the question using built-in function (bin(),hex(),etc.)

'''        deccimal = i+1
        octal = oct(deccimal)
        hexa = hex(deccimal)
        binary =  bin(deccimal) 
'''