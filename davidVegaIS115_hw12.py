## David Vega
## Course Number And Section: IS 115 Section 1004
## Date Of Completion: 5/9/2019
## Time Of Completion : 5 Hours
## Brief Explanation Of The Program: Utilizing try/catch method for valid input, using arrys and the information
##                                                                     stored in them to modularize our program while using functions 

## Function to display student info entered
def studentInfo(firstName, middleInitial, lastName, gpa, students): 
    for x in range (0, students):
        print (firstName[x], middleInitial[x], lastName[x], "-" "%.2f" % gpa[x])

## Function to display student emails
def studentEmail(firstName, lastName, students):
    for x in range (0, students):
        schoolEmail = firstName[x] + "." + lastName[x] + "@csn.edu"
        print (schoolEmail)

## Function to return average gpa
def avgGPA(gpa, students):   
    total = 0
    for x in range (0, students):
        total = total + gpa[x]
    avg = total / students
    return avg

## Function to return the student name with the highest gpa
def highGPA(firstName, gpa, students):
    high = gpa[0]
    highIndex = 0
    for x in range (1, students):
        if gpa[x] > high:
            high = gpa[x]
            highIndex = x
    return firstName[highIndex]

## Function to create a file and write the info entered to it
def writeFile(firstName, middleInitial, lastName, gpa, students):
    fileName = str(input("What do you want to name the file to write to? "))
    outfile = open(fileName, "w")
    for x in range (0, students):
        outfile.write(firstName[x] + " " + middleInitial[x] + " " + lastName[x] + "-" "%.2f" % gpa[x] + "\n")
    print ("I just wrote to the file ", fileName) ## Displays message to inform user that the file was written to
    outfile.close() ## Closes and saves file 


def main():
 ## Try/catch method used to accept only whole numbers
## and does not accept decimal or character values as input 

    students = 0
    while students == 0:
        try:
            students = int(input("How many students do you want to process? "))
            while students <= 0:
                print ("Invalid entry, enter a number greater than 0")
                students = int(input("How many students do you want to process? "))
        except ValueError:
            print ("Enter only whole numbers, decimal or character values are not allowed")
            students = 0

    print (students, "students were entered to be processed")
    
## Defines array with the input of students entered
    firstName = [""] * students
    middleInitial = [""] * students
    lastName = [""] * students
    gpa = [0] * students

## Data that will be entered into array
    for x in range (0, students):
        firstName[x] = (str(input("Enter the students first name: ")))
        middleInitial[x] = (str(input("Enter the students middle initital : ")))
        lastName[x] = (str(input("Enter the students last name : ")))
        gpa[x] = (float(input("Enter the students gpa: ")))

    print ("Student data that was entered: ")
    studentInfo(firstName, middleInitial, lastName, gpa, students)
    print ("Student emails are: ")
    studentEmail(firstName, lastName, students)
    print ("The average gpa is: ", "%.2f" % avgGPA(gpa, students))
    print ("The student with the highest gpa is: ", highGPA(firstName, gpa, students))
    writeFile(firstName, middleInitial, lastName, gpa, students)

main() ## Calls the main function to begin the program








