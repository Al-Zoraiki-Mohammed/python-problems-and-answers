if __name__ == '__main__':
    n = int(input('Enter number of students: '))
    student_marks = {}
    for i in range(n):
        name, *str_scores = input(f'Enter Student name {i+1} followed by scores: ').split()
        scores = [float(item) for item in str_scores]
        student_marks[name] = scores
    query_name = input()
    s=0
    for mark in student_marks[query_name]:
        s+=mark
    average = s/len(student_marks[query_name])

    print(f'{average:.2f}')

    '''
    2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
    '''
