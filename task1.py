'''
Task 1:
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
'''



def A():
    print("Hello")
def B():
    print("How are you")
def C():
    print("Hi")

picked = input("Please choose a letter from A to C: ")

if picked == 'A':
        A()
if picked == 'B':
        B()
if picked == 'C':
        C()
