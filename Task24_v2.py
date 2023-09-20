# short answer for Task24 using built-in function bin(),hex() and oct()
def print_formatted(n):
    padding = len(bin(n))-2
    for i in range (n):
        decimal = i+1
        hexa = hex(decimal).upper()
        hexa = hexa[2:]
        octal = oct(decimal)[2:]
        binary = bin(decimal)[2:]

        print(f'{decimal:>{padding}}',
               f'{octal:>{padding}}', 
               f'{hexa:>{padding}}', 
               f'{binary:>{padding}}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
