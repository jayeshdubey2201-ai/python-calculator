# Simple calculator

def calculator(num1,operator,num2):

    if operator=="+":
        result= num1+num2

    elif operator=="-":
        result= num1-num2

    elif operator=="*":
        result= num1*num2

    elif operator=="/":
        if num2==0:
            result ="cannot divide by zero"

        else:
            result= num1/num2

    elif operator=="%":
        result= num1% num2

    elif operator=="**":
        result=num1**num2


    else:
        result ="Invalid operator"

    return result

while True:
        
# Taking input from the user
        num1= float(input("Entre first number:"))
        operator =input("Entre operator(+,-,*,/,%,**):")
        num2= float (input("Entre second number:"))

#Calling the function
        answer = calculator(num1, operator, num2)

#display the result
        print("Result", answer) 
# Ask weather to reapeat or not
        again = input("do you wantyr to calculate again ? (yes/no): ")
        if again. lower () != "yes":
            break