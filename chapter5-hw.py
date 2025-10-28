# This Python program that calculates student grades using multiple functions.
#It asks for the user to enter the number of students they plan to enter grades for.
#It asks for 4 grades for each student.
#It will print the student's name, grades, entered, numberic average, and letter grade.



def main():

    #BEGIN MAIN PROGRAM
    
    print("\n=== GRADE CALCULATOR ===")
    print("========================\n")
    
    #Get how many students the user wants to enter grades for.
    num_students = int(input('How many sudents would you like to enter grades for? '))

    #loop through the number of students the user wants to enter data for
    for count_students in range(num_students):

        #Set flags to true for each grade and for the first name and last name user check.
        #Once a positive numbergrade is entered, flag is set to false.
        #Once user approves what they entered for the name (yes), set flag to false.
        grade1_check = True
        grade2_check = True
        grade3_check = True
        grade4_check = True
        first_check = True
        last_check = True

        #ask user for student's name and 4 grades
        
        #ask for first name and check allow user to check enter
        while first_check == True:
            first_name = input("\nPlease enter the student's first name: ")
            print("You entered:", first_name)
            namecheck1 = input('Is that correct? Please enter Y for yes and N for no.')
            #If no, allow user to enter the name again
            if namecheck1 == "n" or namecheck1 == "N" or namecheck1 == "No" or namecheck1 == "NO" or namecheck1 == "no":
                print ("\nPlease try again.")
            else:
                #change flag to False and leave the loop
                first_check = False

        #ask for last name and check allow user to check enter
        while last_check == True:
            last_name = input("\nPlease enter the student's last name: ")
            print("You entered:", last_name)
            namecheck2 = input('Is that correct? Please enter Y for yes and N for no.')
            #If no, allow user to enter the name again
            if namecheck2 == "n" or namecheck2 == "N" or namecheck2 == "No" or namecheck2 == "NO" or namecheck2 == "no":
                print ("\nPlease try again.")
            else:
                #change flag to False and leave the loop
                last_check = False

        #concatenate the names        
        name = first_name + " " + last_name

    
        #set flag for each grade entry checking for a negative number. Once positive grade
        #is entered, change flag to false and proceed to the next grade
        while grade1_check == True:
            grade1 = float(input('Please enter the first number grade: '))
            if grade1 < 0.0:
                print("Error: Grade can't be negative. Enter a new grade.")
            else:
                grade1_check = False

        while grade2_check == True:
            grade2 = float(input('Please enter the second number grade: '))
            if grade2 < 0.0:
                print("Error: Grade can't be negative. Enter a new grade.")
            else:
                grade2_check = False

        while grade3_check == True:
            grade3 = float(input('Please enter the third number grade: '))
            if grade3 < 0.0:
                print("Error: Grade can't be negative. Enter a new grade.")
            else:
                grade3_check = False

        while grade4_check == True:
            grade4 = float(input('Please enter the fourth number grade: '))
            if grade4 < 0.0:
                print("Error: Grade can't be negative. Enter a new grade.")
            else:
                grade4_check = False

        
        #call the function to find the grade average and assign the average to
        #the average variable
        average = calculate_average(grade1, grade2, grade3, grade4)

        #call the function to determine the letter grade based on the average
        letter_grade = determine_letter_grade(average)

        
        #formatting to separate student's printed information
        print("\n========================\n")
        print("STUDENT", count_students+1)
        
        #call function to print each student's name, average, and letter grade
        display_grade_info(name, average, letter_grade)

    #END MESSAGE
    print("\nThank you for using the Grade Calculator Program.")

        

# The calculate average function takes in 4 grades,
#computes the average, and returns the average
def calculate_average(grade1, grade2, grade3, grade4):
    # Calculate the average
    grades_sum = grade1 + grade2 + grade3 + grade4
    average = grades_sum/4


    # Return the average
    return average


#This function determines the letter grade by
#taking in the numerica average and defining a letter grade
#based on predetermined values. It then returns the letter grade.
def determine_letter_grade(average):
    if average >= 90:
        letter_grade = "A"
    elif average >=80:
        letter_grade = "B"
    elif average >=70:
        letter_grade = "C"
    elif average >=60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    #return the letter grade    
    return (letter_grade)
        

#print the student's name, average, and letter grade
def display_grade_info(name, average, letter_grade):

    print("Student's Name:", name)
    print("Student's Average:", average)
    print("Student's Letter Grade:", letter_grade)

    

# Call the main function.
main()
