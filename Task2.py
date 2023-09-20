# To print '----' 25 times to make our fancy seperator line -------- :)
print("----"*25)

#Read the number from user into n variable
n = int(input('input number n: ').strip())

# We can use to conditions  when n is 'Weird' and 'Not Weird':
# The first condition when n is Weird.
if (n%2!=0) or ((n%2==0) and (n>=6) and (n<=20)):
    print('Weird')
    # The second condition when n is Not Weird.
elif ((n%2==0) and (n>=2) and (n<=5) or ((n%2==0)and(n>20))):
    print('Not Weird')