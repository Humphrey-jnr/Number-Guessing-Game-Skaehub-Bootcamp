from numberGameOOP import check
import random
import re
import os
from time import sleep
from twilio.rest import Client
from colorama import Fore, Back, Style

score_normal=10
score_repeat=5
score_fail=0



#function to clear the console
def clear():
    os.system('clear')

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
        try:
            u_guess=input("Enter your guess between 1 and 100 : ")
            global guess
            guess=int(u_guess)
            if guess>0 and guess<100:
                    diff=number-guess
                    print("Difference between actual number and guess is :"+str(diff))
                    print("You entered :"+str(guess))
                    return guess
            else:
                print("Your guess is out of range,Enter a number within the given range!")
                user_guess()
                return 'error'
        except:
             print("Enter a valid number of type int:")
             user_guess()
             return guess
            

#function that checks for the right score
def check():       
    if guess==number:
        print("Your score is :"+str(score_normal))
        message(score_normal)
        return True
    else:
        print("\nYou got it wrong")
        print("Try again")
        for i in range(1):
            multiple_check()
            hint()
            user_guess()
            repeat_check()
        return False

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
    phone_number=str(input("Enter your Phone number: "))
    sleep(2)
    clear()
    phone_check = re.match(r'^[+][0-9]', phone_number)
    if bool(phone_check)==True and len(phone_number)==13:
        print(phone_number)
        return phone_number
    else:
        print("Enter a valid Phone number")
        enter_phone()
        return phone_number
#function to send the message
def message(score):
    client = Client("ACc57459795cd42b520978ecf3b5413641", "32d4a914d0bbe4daeae97d9b282a99ac")
    client.messages.create(to=f"{phone_number}", 
                       from_="+15097403668", 
                       body="Your game score is"+str(score))
                       
if __name__=="__main__":
    number=random.randrange(1,101)
    print(Back.LIGHTCYAN_EX+Fore.BLACK+"\n*********NUMBER_GUESSING_GAME*********"+Back.RESET+Fore.RESET)
    enter_phone()
    hint()
    user_guess()
    check()


    