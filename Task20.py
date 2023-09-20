if __name__ == '__main__':
    s = input('Enter String: ')
    d={'alnum':False,'alpha':False,'digit':False,'lower':False,'upper':False}
    for c in s:
        if c.isalnum():
            d['alnum']=True
        if c.isalpha():
            d['alpha']=True
        if c.isdigit():
            d['digit']=True
        if c.islower():
            d['lower']=True
        if c.isupper():
            d['upper']=True

    for key,value in d.items():
        print(value)


        

# my_dict.get('a', 'Key not found')