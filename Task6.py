
def is_leap(year):
    
    '''	The year can be evenly divided by 4, is a leap year, unless:
	The year can be evenly divided by 100, it is NOT a leap year, unless:
	The year is also evenly divisible by 400. Then it is a leap year.
    example: 
    2000 and 2400 are leap years
    1800, 1900, 2100, 2200, 2300 and 2500  are not leap years
'''
    leap = False
     
    if  (year % 4 ==0 ):
        if (year % 100 ==0) and (year %400 !=0):
            #leap = False
            return leap
        leap = True
    
    #else: 
        #leap = False
        
    return leap

year = int(input())
print(is_leap(year))