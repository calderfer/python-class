# This program prompts the user to enter their age, checks to make sure they
# entered a positive interger, and then groups them into defined categories
# The user then sees what category they are in. Finally the user is asked if
# they would like to enter another age.


# Set a flag to true. True means you should prompt the user for their age again.
PROMPT = True


# With the while loop, ask for the user's age until they enter no to leave the program.
while PROMPT == True:
    #reset error check flag to false each time the loop is run
    ERRORCATCH = False
    #ask for the user's age as a positive integer, but capture it as a float to avoid errors
    agecheck = float(input('\nPlease enter your age as a positive whole number: '))
    #convert the user entered age to an integer. It does not round up.
    age = int(agecheck)


    #check to see if they entered a positive integer and that the age is 125 or under
    if age >= 0 and age <= 125:
        print ("\nThe age you entered is:", age)
        #sort the ages and print the appropiate statement
        if age >= 19:
            print ("You are an adult. Choose your career path.")
        elif age >= 14 and age <= 18:
            print ("You are in High School.")
        elif age >= 11 and age <= 13:
            print ("You are in Middle School.")
        elif age >= 6 and age <= 10:
            print ("You are in Primary or Elementary School.")
        else:
            print ("You are too young for elementary school.")

       
            
    #User entered a negative number or entered an age over 125, so tell them the error.
    else:
        #User entered a negative number 
        if age < 0:
            print ("Oh no. You entered a negative number. Please try again. \n")
            #change flag to true so the user is prompted to enter a new age
            ERRORCATCH = True
        #User entered an age over 125
        else:
            print ("\nOver 125? That's amazing! Are you sure you entered the right age? \n")
            #Check to see if the entered age is what they wanted or enter a new age
            oldcheck = input('Please enter Y if this is the correct age or N if you need to re-enter your age.')
            #If age is correct, tell them they are an adult.
            if oldcheck == "y" or oldcheck == "Y" or oldcheck == "Yes" or oldcheck == "YES" or oldcheck == "yes":
                print ("You are an adult. Choose your career path.")
            else:
                #change flag to true so the user is prompted to enter a new age
                ERRORCATCH = True

    #Ask the user if they want to enter another age.
    #Skip this block if ERRORCATCH has been set to true
    #If no, change the flag to False to end the loop and exit the program.
    #Accept common entries for No
    #Any other input will be treated as a yes and ask for the age again.
    if ERRORCATCH == False:
        repeat = input('\nWould you like to enter another age? Enter Y for yes and N for no. ')
        if repeat == "n" or repeat == "N" or repeat == "No" or repeat == "NO" or repeat == "no":
            #Set flag to false to end while loop
            PROMPT = False
            print ("Thank you for using this program. Have a nice day.")

              
