n,m =[int(i) for i in (input('input n,m: ').strip().split())]

d=0
for i in range(n):
    if i< int(n/2):
        print('-'*(int(m/2-(2*i+1))-i)+ '.|.'*int((2*i+1))+  '-'*(int(m/2-(2*i+1)-i)))
    elif i== int(n/2):
        print('-'*int((m-len('WELCOME'))/2) + 'WELCOME' + '-'*int((m-len('WELCOME'))/2) )
    elif i> n/2:
        d += 2
        print('-'*int((m-((n-d)*3))/2) + '.|.'*int(n-d) +  '-'*int((m-((n-d)*3))/2))



# Anohter solutio :)

def another_solution():
    num = input('enter for another solution m,n: ').split(" ")
    n = int(num[0])
    m = int(num[1])
    row = (n-1)
    for i in range(0,row+1):
        character = ".|."
        if(i%2 != 0):
            character = character*i
            print(character.center(m,"-"))
        elif(i == row):
            print("welcome".upper().center(m,"-"))
        else:
            continue
    for i in range(row,0,-1):
        character = ".|."
        if(i%2 != 0):
            character = character*i
            print(character.center(m,"-"))
        else:
            continue

#another_solution()