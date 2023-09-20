if __name__ == '__main__':
    n = int(input('Enter size N: '))
    arr=[]

    for i in range(n):
        comand, *value= input('enter comand: ').split()

        if comand=='insert':
            arr.insert(int(value[0]),int(value[1]))

        elif comand =='print':
            print(arr)

        elif comand =='pop':
            arr.pop()
        
        elif comand == 'append':
            arr.append(int(value[0]))

        elif comand == 'remove':
            if int(value[0]) in arr:
                arr.remove(int(value[0]))
            else: print(f'No value such {int(value[0])} to remove !')

        elif comand =='reverse':
            arr.reverse()
        elif comand =='sort':
            arr.sort()

        else: print('Comand not clear')


''' Sample input:
 12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''