# answer version_1 using if_else statements
year = int(input("Enter the year (positive value and less than 10000): "))
while not 0 <= year < 10000:
    print("Enter the correct value")
    year = int(input("Enter the year (positive value and less than 10000): "))
 
k = year % 12
if k == 0:
    year_animal = "Monkey"
elif k == 1:
    year_animal = "Rooster"
elif k == 2:
    year_animal = "Dog"
elif k == 3:
    year_animal = "Pig"
elif k == 4:
    year_animal = "Rat"
elif k == 5:
    year_animal = "Ox"
elif k == 6:
    year_animal = "Tiger"
elif k == 7:
    year_animal = "Rabbit"
elif k == 8:
    year_animal = "Dragon"
elif k == 9:
    year_animal = "Snake"
elif k == 10:
    year_animal = "Horse"
elif k == 11:
    year_animal = "Goat"
 
print("{} - The year of the {}.".format(year, year_animal))