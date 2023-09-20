def swap_case(s):
    s_m=''
    for litter in s:
        if(litter==litter.upper()):
            s_m += litter.lower()
        else: 
            s_m += litter.upper()
    return s_m

if __name__ == '__main__':
    s=input()
    print(swap_case(s))