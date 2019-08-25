##David Vega
##Course Number And Section: IS 115 Section 1004
##Date Of Completion: 4/19/19
##Time Of Completion: 3 Hours
##Brief Explanation Of The Program: Utilized Python to handle exceptions in a 
##                                  temperature conversion, calculates total and  
##                                  average tempeatures, and create/write results to file 

tempRead = 0 ## Primer for loop to catch errors being entered 
while tempRead == 0: 
    try:
        tempRead = int(input("How many temperature readings do you want to convert? "))
        ## tempRead checks  for characters, decimals, and negative numbers
        ## If tempRead has characters in it - will go to the except segment
        ## If tempRead has no decimals or characters, will go to next segment and check if entry is a negative number
        ## If tempRead is greater than 0, loop is exited
        ## A print statment is displayed when tempRead is greater than 0

        while tempRead <= 0: ## Checks entry, does not allow for it to be less than or equal to 0
            print ("Invalid entry, enter a number greater than 0")
            tempRead = int(input("How many temperature readings do you want to convert? "))
    except ValueError:
        print("Enter only whole numbers, decimal or character values are not allowed")
        tempRead = 0               ## tempRead is set back to 0 due to error encountered. Loop will continue until valid entry is entered. 

print (tempRead, "temperature readings were entered to be converted")
x = 0                               ## Tracks valid temperature input
fahrenheitTotal = 0
celsiusTotal= 0
while tempRead > 0: ## Loop to input temperature readings 
    fahrenheit = float(input("Enter degrees in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8                         ## Converts fahrenheit temperature into celsius 
    while fahrenheit < -100 or fahrenheit > 100: ## Loop that will display an error message if temperature is outside of range
        fahrenheit = float(input("Re-enter the degree in Fahrenheit, must be between -100 and 100: "))
        celsius = (fahrenheit - 32) / 1.8
    print (fahrenheit, "degrees Fahrenheit converts to" , "%.2f" % celsius, "degrees Celsius") 
    fahrenheitTotal = fahrenheitTotal + fahrenheit ## Keeps running total for fahrenheitTotal 
    celsiusTotal = celsiusTotal + celsius          ## Keeps running total for celsiusTotal 
    tempRead = tempRead - 1 ## Loop counter for outer loop 
    x = x + 1                                      ## Used to calculate average of temperatures 
avgFahrenheit = fahrenheitTotal / x ## Calculates average temperature of fahrenheit
avgCelsius = celsiusTotal / x ## Calculates average temperature of celsius
print ("Total temperature in degrees Fahrenheit = ", "%.2f" % fahrenheitTotal)
print ("Total temperature in degrees Celsius = ", "%.2f" % celsiusTotal)
print ("Average temperature in degrees Fahrenheit = ", "%.2f" % avgFahrenheit)
print ("Average temperature in degrees Celsius = ", "%.2f" % avgCelsius)

fileName = str(input("What is the name of the file to write to? ")) ## Input from user for the filename
outfile = open(fileName, "w") ## Creates and writes to the file entered by the user
outfile.write("Total temperature in degrees Fahrenheit = " "%.2f" % fahrenheitTotal + "\n")     
outfile.write("Total temperature in degrees Celsius = " "%.2f" % celsiusTotal + "\n")                  
outfile.write("Average temperature in degrees Fahrenheit = " "%.2f" % avgFahrenheit + "\n") 
outfile.write("Average temperature in degrees Celsius = " "%.2f" %avgCelsius + "\n")               
print("I just wrote to the file " , fileName)                                                                                                        ## Displays message to inform user that the file was written to
outfile.close() ## Closes and saves file 



