'''This code solve the problem, and clean the spaces between words to one space,
 if we want to maintain the number of spaces between words,
 we should use split(' '), instead using default parameter split()'''

def solve(s):
    words=s.split() # s.split(' ') to  split for each single space.
    l=[]
    
    for word in words:
        l.append(word.capitalize())

    print(l)
    return ' '.join(l)


if __name__ == '__main__':
    full_name= input('enter your full name: ')
    
    print(solve(full_name))

