
print(f' The maximum number is: {max}')

def find_max():
    numbers = int(input('how many numbers to compare? : '))
    max = int(input('Type number 0: '))
    for i in range(numbers -1):
        number = int(input(f'Type number {i + 1}: '))
        if number > max:
            max = number
    print(max)

if __name__ == '__main__':
    find_max()
    
#Note:
# We can use a list to store all numbers then use built in max() function.