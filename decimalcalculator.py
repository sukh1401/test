print("Enter the two numbers")

first = "{:.2f}".format(float(input("first number is:  ")))
second = "{:.2f}".format(float(input("Second number is :  ")))

first= float(first)
second=float (second)

multiplication = (first*second)
division= (first/second)
addittion = (first+second)
subtraction= (first-second)

print(f" the result for their multiplication is {multiplication} \n their division is {division} \n their addition is {addittion} \n and their subtraction is {subtraction}")