first_week = sum([int(number) for number in input(
    "Enter the number of tickets sold during the first week (for each day): ",
).split()])
second_week = sum([int(number) for number in input(
    "Enter the number of tickets sold during the second week (for each day): ",
).split()])
price = int(input("Enter the ticket price: "))
 
print("{} tickets were sold during the first week".format(first_week))
print("{} tickets were sold during the second week".format(second_week))
 
if first_week < second_week:
    print(
        "In the second week, the cinema sold {} more tickets than in the first one.".format(
            second_week - first_week,
        ),
    )
elif first_week > second_week:
    print(
        "In the first week, the cinema sold {} more tickets than in the second one.".format(
            first_week - second_week,
        ),
    )
else:
    print(
        "The cinema sold the same number of tickets in the first week as in the second week."
    )
print("The total cinema's revenue for two weeks was ${}.".format(
    (second_week + first_week)*price
))