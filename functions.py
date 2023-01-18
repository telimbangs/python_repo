#function for checking the divisibility
#notice the identation after function declaration
# and if else statements
def checkdivisibility (a,b):
    if a % b==0:
       print(a,"is divisible by",b)
    else:
       print(a,"is not divisible by",b)
#Driver program to test the above function
checkdivisibility(5,2)