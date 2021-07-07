import random
import re
from twilio.rest import Client
from colorama import Fore, Back, Style
import os
import time


score_normal=10
score_repeat=5
score_fail=0

#function to clear the console
def clear():
    os.system("clear")

#the  funtion that hints the user for input
def hint():
    if int(number/2)*2==number:
        print("""\nHint:
            \n"The number is even""")
        
    else:
        print("""\nHint:
            \n"The number is odd""")

#the function that asks the user for input
def user_guess():
    global u_guess
    u_guess=input("Enter your guess between 1 and 100 : ")
    user_guess_validation()

#check for valid input
def user_guess_validation():
    try:
        global guess
        guess=int(u_guess)
        print("Your guess is "+str(guess))
        guess_num_difference()
        return 'valid'
    except:
        clear()
        print("Enter a valid number of type int:")
        user_guess()
        return 'invalid'
   
def guess_num_difference():  
    if guess>0 and guess<100:
        if number>guess:
            diff=number-guess
        else:
            diff=guess-number

        print("Difference between the number and your guess is: "+str(diff))
    
  
#function that checks for the right score
def check():       
    if guess==number:
        print("Your score is :"+str(score_normal))
        message(score_normal)
    else:
        print("\nYou got it wrong")
        print("Try again")
        for i in range(1):
            multiple_check()
            hint()
            user_guess()
            repeat_check()

#function that does a repeat check if the user fails initial try
def repeat_check():
    if guess==number:
        print("\nYou got it right")
        print("Your score is  :"+str(score_repeat))
        message(score_repeat)
    else:
        print("\nYou got it wrong")
        print("Your score is  :" +str(score_fail))
            
#function that checks for multiples of the number
def multiple_check():
    number_list=[]
    for  i in range(2,101):
        if number>=i and i==number:
            if number%i==0:
                number_list.append(i)
                
        elif i>=number:
            if i%number==0:
                number_list.append(i)
                
    print("""\nEXTRA HINT
        \nIt's multiples are """+str(number_list) )

def enter_phone():
    global phone_number
    phone_number=input("\nEnter your Phone number: ")
    clear()
    phone_validation()
    
def phone_validation():
    global phone_check
    phone_check = re.match(r'^[+][0-9]', phone_number)
    if bool(phone_check)==True and len(phone_number)==13:
        print("Your phone number is"+phone_number)
        return True
    else:
        print("Enter a valid Phone number")
        enter_phone()
        return False

#function to send the message
def message(score):
    client = Client("ACc*****************", "************************")
    try:
        client.messages.create(to=f"{phone_number}", 
                            from_="+15097403668", 
                            body="Your game score is"+str(score))
        print("Your score has been sent to you")
    except:
        print("SMS Not Sent")
                       
if __name__=="__main__":
    number=random.randrange(1,101)
    print(Back.LIGHTCYAN_EX+Fore.BLACK+"*********NUMBER_GUESSING_GAME*********"+Back.RESET+Fore.RESET)
    print(Back.RED+Fore.LIGHTWHITE_EX+"""This a Number Guessing Game Where the system generates a random number and you have to guess the number!
    \nYou have only two tries,if you fail the first try your possible score reduces."""+Back.RESET+Fore.RESET)
    time.sleep(3)
    clear()
    enter_phone()
    hint()
    user_guess()
    check()


    
