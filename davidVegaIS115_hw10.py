##David Vega
##Course Number And Section: IS 115 Section 1004
##Date Of Completion: 4/14/19
##Time Of Completion: 2 Hours and 30 Minutes 
##Brief Explanation Of The Program: Utlizing Python to write a bank check
##                                  fees processing fucntion, product total function, 
##                                  vowel checker functions  




def getFees(balance, checks): ## Function to calculate total bank fees due in a month 
    if balance <= 400:                    ## Condition that checks if balance is below or equal to 400
        fee = 15                          ## fee thats added to totalFees if balance is below 400
    else:
        fee = 0
    if checks > 0 and checks <= 19:
        totalChecks = checks *.10
    elif checks >= 20 and checks <= 39:
        totalChecks = checks * .08
    elif checks >= 40 and checks <= 59:
        totalChecks = checks * .06
    else:
        totalChecks = checks * .04

    totalFees= fee + totalChecks + 10 ## Calculates total bank fees due 
    return totalFees                                    ## Returns totalFees to bankFee of getFees function  

def getProduct(num1, num2, num3): ## Function will find product total of numbers entered
    
    if num1 > num2:                                     ## Condition checks and returns -999 error message 
        return -999
    else:
        total = 1
        while num1 <= num2:
            total = total * num1 
            num1 = num1 + num3                  ## Step increment decided by num3 that was entered 
    return total                                ## Returns total to getProduct function 

def vowelCheck(x): ## Function determines if character entered is vowel 
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"): 
        return "True"
    else:
        return "False"

        

def main(): ## Main function 
    balance = float(input("Enter your account balance: ")) ## Gets balance input for getFees function
    while balance <= 0: ## Condition test balance input , if  balance = 0 will ask to re-enter account balance 
            balance = float(input("Invalid account balance, Re-enter your account balance: "))
    checks = int(input("Enter the number of checks to process: ")) ## Gets checks input for getFees function
    while checks <= 0: ## Condition tests checks input, if checks = 0 will ask to re-enter checks to process 
        checks = int(input("Invalid number of checks entered, Re-enter your checks to process: "))
    bankFee = getFees(balance, checks) ## Calls getFees function
    print ("The bank fee due this month is: ", "%.2f"  % bankFee) 

    num1 = int(input("Enter the first number: "))       ## Gets first number input for getProduct function 
    num2 = int(input("Enter the second number: "))      ## Gets second number input for getProduct function 
    num3 = int(input("Enter the third number: "))       ## Gets third number input for getProduct function 
    total = getProduct(num1, num2, num3)                ## Calls the getProduct function 
    print("Total: ", total) 

    x = (input("Enter a character: "))    ## Gets input of character from user 
    if vowelCheck(x) == "True":           ## Displays character as a vowel if true
        print (x, "is a vowel")
    else:
        print (x, "is not a vowel")       ## Displays character as not a vowel if false 
              



main() ## Calls the main function to  begin the program 
    
    
    
