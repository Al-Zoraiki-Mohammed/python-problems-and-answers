print('----'*25)
n = int(input('Enter n: '))
# for sure we can do it in one line  as the following line :)
# scores = sorted(list(set([int(i) for i in(input(f'input{n} numbers: ').split())])))[-2]
#One more shorter :)
# print(sorted(list(set([int(i) for i in(input(f'input{n} numbers: ').split())])))[-2])

# But to make it clear and readable we do the following:
scores = [int(i) for i in(input(f'Enter {n} numbers: ').split())]
scores=set(scores)
scores=list(scores)
scores.sort()
print(scores)

# Note:  - We can do it in low level way like C++ :)
