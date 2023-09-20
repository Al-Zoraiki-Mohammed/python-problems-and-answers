n= int(input('Enter the number of stamps: '))
s=set()
for i in range(n):
    s.add(input(f'Enter country {i} name:  '))

print(len(s))
#print(f' number of distict countries is {len(s)} {s}')