# This program gets two numbers and an operator from the user, performs the specified operation
# on the numbers, and prints the result. It also checks that the user entered an allowed
# operator (+,-,*,/) and does not allow division by 0.

# Get the two numbers and an operator.
# Set DIVIDEBY0 to False as a flag. Change to True if the user divides by 0.
number1 = float(input('Enter your first number: '))
number2 = float(input('Enter your second number: '))
operator = input('Enter your operator (+, -, *, /): ')
DIVIDEBY0 = False



#Check to see if the user entered an operator.
if not (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
    print ("You did not enter an operator. Your calculation can not be completed.")
    
#Valid operator was entered.
#Determine the operator, do the corresponding math, and store the result in a variable named result
else:
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    else:
        #check to see if the second number is 0 since you can't divide by zero
        #set DIVIDEBY0 = True if the second number is 0
        if number2 == 0.0:  
            print ("You can't divide by 0. Your calculation can not be completed.")
            DIVIDEBY0 = True
        else:
            result = number1 / number2

    #print the results if DIVDEBY0 == False, format decimal numbers to 2 places
    if DIVIDEBY0 == False:
        print("\nYou entered:", format(number1, ',.2f'),operator,format(number2, ',.2f'))
        print("The solution is:", format(result, ',.2f'))
