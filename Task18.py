def mutate_string(string, position, character):
    s_m= list(string)
    s_m[position]=character
    s_new = ''.join(s_m)   

    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Alternative sulotion:
''' string ='akmed'
string = string[:1] + "h" + string[2:]
print(string)'''