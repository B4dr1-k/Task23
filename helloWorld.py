'''
Task 23 - Learn GIT
First fix - Adding comments and a line function
Second fix - adding a check to see if it is string
'''

def print_line():
    print("------------------------------------")

#Getting a string from the user and ensuring it is not empty
input = ''
while (input == ''):
    message = input("enter a string: ")
    #remove any empty strings
    input = input.strip()
    if input != '': 
        break
    elif input == '':
        continue
    
#Printing the input back to user
print_line()
print(message)
print_line()