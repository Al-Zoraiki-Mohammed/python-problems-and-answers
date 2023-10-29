hours = 0.5
distance = int(input("Enter the number of miles: "))
while not 0 <= distance:    #checking for correct numeric input
    print("Enter the correct value")
    distance = int(input("Enter the number of miles: "))
 
if distance/hours > 45:
    print("The driver violated the traffic rules")
else:
    print("The driver didn't violate the traffic rules")