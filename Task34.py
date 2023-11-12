
grades = input("Enter all grades with single space between them: ").split()
 
for grade in sorted(set(grades)):
    print(f"Number of ratings {grade} = {grades.count(grade)}")