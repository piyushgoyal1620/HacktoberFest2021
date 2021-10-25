import pyttsx3    #used for converting text to speech
import random      #used to generate random numbers between a specific range.
import operator     #special symbols used for performing opeation on one or more operand.
import speech_recognition as sr   #used for converting our speech to text
import datetime    #used for extracting time and date
import webbrowser   #used to launch a browser for seraching or having some content
import os        #used for interacting with os
import winshell   #provide basic functionalities in directories like copy, rename and delete
import time      #for stopping or pausing the compiler
import sqlite3   #database
import requests  #sends requests to have some information through the internet
import shutil     #used for operating the file within directories.
import json       #used json module for recieving the weather info in json format
import account_data    #program for creating the table in the database
from twilio.rest import Client   #used for sendng otp
from urllib.request import urlopen  #used for fetching URLs 


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("\nGood Morning!\n")
        speak("Good Morning...!")
  
    elif hour>= 12 and hour<18:
        print("\nGood Afternoon!\n")
        speak("Good Afternoon...!")
  
    else:
        print("\nGood Evening!\n")
        speak("Good Evening...!")
  
    print("\nWelcome to Voice Automated ATM\n")
    speak("Welcome to Voice Automated ATM...I am your Assistant for this ATM")
    

def remove(var):
    return var.replace(" ","")


def account():
    while True:
        c=0
        while c<3:
            print("\nPlease say your account number\n")
            speak("Please say your account number")
            global uacc_no
            uacc_no=takeCommand()
            if uacc_no.isdigit():
                break
            else:
                c+=1
                print("Invalid input\n")
                speak("Invalid input")
        if c==3:
            print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
            speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
            exit()
        
        try:
            con=sqlite3.connect('account.db')
            cur=con.cursor()
            cursor=cur.execute("SELECT acc_phone FROM DATA where acc_no="+uacc_no)
            for row in cursor:
                s=str(row[0])
            con.close()
        except Exception as e:
            print("Server down...please try again later\n")
            speak("Server down...please try again later")
            exit()
        
        reciever="+91" + s
        otp=random.randint(1000,9999)
        account_sid='ACdaf3c5de76e84f542fbc9bdb9c3accd4'
        auth_token= '292c0c146fbf95a97a97d70651d1f70a'
        client=Client(account_sid,auth_token)

        message=client.messages\
                      .create(body="Your OTP is="+str(otp),
                              from_='+19705192187',
                              to=reciever
                              )
        break

    c=0   
    while c<3:
        print("Please say the OTP received on your phone\n")
        speak("Please say the OTP received on your phone")
        time.sleep(1)
        req_otp=takeCommand()
        if str(req_otp) == str(otp):
            con=sqlite3.connect('account.db')
            cur=con.cursor()
            cursor=cur.execute("SELECT acc_name FROM DATA where acc_no="+uacc_no)
            for row in cursor:
                t=row[0]
            con.close()
            uname=t
            break
        else:
            c+=1
            print("Incorrect OTP, Please Re-enter\n")
            speak("Incorrect OTP, Please Re-enter")

    if c == 3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()
    print("Welcome "+uname+" to Voice Automated ATM\n")
    speak("Welcome "+uname+"...to Voice Automated ATM")
    time.sleep(1)
    print("What would you like to have from the following:\n")
    speak("What would you like to have from the following:")
    time.sleep(1)
    print("Withdraw Money\n")
    speak("Withdraw Money")
    time.sleep(1)
    print("Deposit Money\n")
    speak("Deposit Money")
    time.sleep(1)
    print("Check Balance\n")
    speak("Check Balance")
    time.sleep(1)
    print("Create a new account\n")
    speak("Create a new account")
    time.sleep(1)
    print("Link Aadhar card to your account\n")
    speak("Link Aadhar card to your account")


def check_bal():
    global uacc_no
    try:
        con=sqlite3.connect('account.db')
        cur=con.cursor()
        cursor=cur.execute("SELECT acc_amount FROM DATA where acc_no="+uacc_no)
        for row in cursor:
            bal=row[0]
        con.close
        print("Your balance is="+str(bal)+"\n")
        speak("Your balance is="+str(bal))
    except Exception as e:
        print("Server down...please try again later\n")
        speak("Server down...please try again later")
        exit()
    time.sleep(2)
    print("Thank you for using this ATM...Hope you have a good day ahead\n")
    speak("Thank you for using this ATM...Hope you have a good day ahead")
    exit()


def withdraw():
    global uacc_no
    try:
        con=sqlite3.connect('account.db')
        cur=con.cursor()
        cursor=cur.execute("SELECT acc_amount FROM DATA where acc_no="+uacc_no)
        for row in cursor:
            bal=row[0]
        print("Your Current Balance is="+str(bal)+"\n")
        speak("Your Current Balance is="+str(bal))
    except Exception as e:
        print(e)
        print("Server down...please try again later\n")
        speak("Server down...please try again later")
        exit()
    print("You can withdraw only ten thousand rupees at one time\n")
    speak("You can withdraw only ten thousand rupees at one time")
    c=0
    while c<3:
        print("How much money you want to withdaw from your account:\n")
        speak("How much money you want to withdaw from your account:")
        a=takeCommand()
        if a.isdigit() and int(a)<int(bal) and int(a)<10000:
            cursor=cur.execute("UPDATE DATA SET acc_amount=acc_amount-"+str(a)+" where acc_no="+uacc_no)
            con.commit()
            break
        else:
            c+=1
            print("Incorrect input, please say in digits\n")
            speak("Incorrect input, please say in digits")
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()
    print("Your Transaction is being processed...Wait for few seconds...\n")
    speak("Your Transaction is being processed...Wait for few seconds...")
    time.sleep(2)
    cursor=cur.execute("SELECT acc_amount FROM DATA where acc_no="+uacc_no)
    for row in cursor:
        print("Your Remaining balance is="+str(row[0])+"\n")
        speak("Your Remaining balance is="+str(row[0]))
    con.close()
    time.sleep(2)
    print("Thank you for using this ATM...Hope you have a good day ahead\n")
    speak("Thank you for using this ATM...Hope you have a good day ahead")
    exit()
    

def deposit():
    global uacc_no
    try:
        con=sqlite3.connect('account.db')
        cur=con.cursor()
        cursor=cur.execute("SELECT acc_amount FROM DATA where acc_no="+uacc_no)
        for row in cursor:
            bal=row[0]
        print("Your Current Balance is="+str(bal)+"\n")
        speak("Your Current Balance is="+str(bal))
    except Exception as e:
        print(e)
        print("Server down...please try again later\n")
        speak("Server down...please try again later")
        exit()
    print("You can deposit only ten thousand rupees at one time\n")
    speak("You can deposit only ten thousand rupees at one time")
    c=0
    while c<3:
        print("How much money you want to deposit into your account:\n")
        speak("How much money you want to deposit into your account:")
        a=takeCommand()
        if a.isdigit() and int(a)<10000:
            cursor=cur.execute("UPDATE DATA SET acc_amount=acc_amount+"+str(a)+" where acc_no="+uacc_no)
            con.commit()
            break
        else:
            c+=1
            print("Incorrect input, please say in digits\n")
            speak("Incorrect input, please say in digits")
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()
    print("Your Transaction is being processed...Wait for few seconds...\n")
    speak("Your Transaction is being processed...Wait for few seconds...")
    time.sleep(2)
    cursor=cur.execute("SELECT acc_amount FROM DATA where acc_no="+uacc_no)
    for row in cursor:
        print("Your New balance is="+str(row[0])+"\n")
        speak("Your New balance is="+str(row[0]))
    con.close()
    time.sleep(2)
    print("Thank you for using this ATM...Hope you have a good day ahead\n")
    speak("Thank you for using this ATM...Hope you have a good day ahead")
    exit()
    

def weather():
    api_key = "710b77ea5bbb36db632ef38fc75b2858"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Delhi"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url) 
 
    if response.status_code==200:
        data=response.json()
        main=data['main']
        temperature=main['temp']
        temperature=int(temperature-273)
        print(f"Temperature: {temperature}\n")
        speak("The Temperature here is " + str(temperature) + "degree celsius")
    else:
        print("Unable to fetch Weather Update")

    
def create_acc():
    c=0
    n=0
    while c<3:
        print("What you want to have your account number?\n")
        speak("What you want to have your account number?")
        anum=takeCommand()
        var=anum
        anum=remove(var)
        try:
            con=sqlite3.connect('account.db')
            cur=con.cursor()
            cursor=cur.execute("SELECT acc_no FROM DATA where acc_no="+anum)
            for row in cursor:
                n=row[0]
            con.close()
            if str(n) == anum:
                c+=1
                print("This account number already exists...Please choose another account number\n")
                speak("This account number already exists...Please choose another account number")
            else:
                break
        except Exception as e:
            print(e)
            print("Invalid input...Please try again...\n")
            speak("Invalid input...Please try again...")
            exit()
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts,...Goodbye hope you have a good day")
        exit()

    c=0
    while c<3:
        print("What is your full name?\n")
        speak("What is your full name?")
        aname=takeCommand()
        if aname.isdigit():
            c+=1
            print("Invalid input\n")
            speak("Invalid input")
        else:
            break
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()

    c=0
    while c<3:
        print("What is your phone number?\n")
        speak("What is your phone number?")
        aphone=takeCommand()
        var=aphone
        aphone=remove(var)
        if aphone.isdigit() and len(aphone)==10:
            break
        else:
            c+=1
            print("Invalid input\n")
            speak("Invalid input")
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()
    
    
    c=0
    reciever="+91" + aphone
    otp=random.randint(1000,9999)
    account_sid='ACdaf3c5de76e84f542fbc9bdb9c3accd4'
    auth_token= '292c0c146fbf95a97a97d70651d1f70a'
    client=Client(account_sid,auth_token)

    message=client.messages\
                  .create(body="Your OTP is="+str(otp),
                          from_='+19705192187',
                          to=reciever
                          )

    while c<3:
        print("Please say the OTP received on your phone\n")
        speak("Please say the OTP received on your phone")
        time.sleep(1)
        req_otp=takeCommand()
        if str(req_otp) == str(otp):
            print("OK")
            break
        else:
            c+=1
            print("Incorrect OTP, Please Re-enter\n")
            speak("Incorrect OTP, Please Re-enter")
            
    if c == 3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()


    c=0
    while c<3:
        print("Which account type do you want: Current Account, Savings Account, Fixed Deposit Account\n")    
        speak("Which account type do you want: Current Account, Savings Account, Fixed Deposit Account")
        atype=takeCommand()
        if atype.isdigit():
            c+=1
            print("Invalid input\n")
            speak("Invalid input")
        else:
            break
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()


    c=0
    while c<3:
        print("Do you also want to deposit money in your account? YES or NO\n")
        speak("Do you also want to deposit money in your account? YES or NO")
        adeposit=takeCommand()
        if adeposit.isdigit():
            c+=1
            print("Invalid input")
            speak("Invalid input")
        else:
            break
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()

    
    if adeposit == 'YES' or adeposit == 'yes':
        c=0
        while c<3:
            print("You can only deposit ten thousand at one time...How much money you want to deposit speak in digits?\n")
            speak("You can only deposit ten thousand at one time...How much money you want to deposit speak in digits?")
            aamount=takeCommand()
            if aamount.isdigit() and int(aamount)<10000:
                break
            else:
                c+=1
                print("Invalid input, Please try again\n")
                speak("Invalid input, Please try again")
        if c==3:
            print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
            speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
            exit()
    elif adeposit == 'NO' or adeposit == 'no':
        aamount=0
        print("It's OK\n")
        speak("It's OK")


    c=0
    while c<3:
        print("What is your Aadhar Number?\n")
        speak("What is your Aadhar Number?")
        aadhar=takeCommand()
        var=aadhar
        aadhar=remove(var)
        if aadhar.isdigit() and len(aadhar)==12:
            break
        else:
            c+=1
            print("Invalid input, Please try again\n")
            speak("Invalid input, Please try again")
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()
    
                
    try:
        con=sqlite3.connect('account.db')
        cur=con.cursor()
        cur.execute("INSERT INTO DATA(acc_no,acc_name,acc_phone,acc_type,acc_amount,acc_aadhar) VALUES(?,?,?,?,?,?)",(anum,aname,aphone,atype,aamount,aadhar))
        con.commit()
        print("Your Account is being created...Wait for few seconds...\n")
        speak("Your Account is being created...Wait for few seconds...")
        time.sleep(2)
        print("Congratulations...Your Account has been created...Thank you for using this ATM...Hope you have a good day ahead\n")
        speak("Congratulations...Your Account has been created...Thank you for using this ATM...Hope you have a good day ahead")
        con.close()
        exit()
    except Exception as e:
        print("Server is down, please try again later.\n")
        speak("Server is down, please try again later.")
        exit()


def link_aadhar():
    global uacc_no
    c=0
    while c<3:
        print("What is your Aadhar Number?\n")
        speak("What is your Aadhar Number?")
        aadhar=takeCommand()
        var=aadhar
        aadhar=remove(var)
        if aadhar.isdigit() and len(aadhar)==12:
            break
        else:
            c+=1
            print("Invalid input\n")
            speak("Invalid input")
    if c==3:
        print("Too many unsuccesfull attempts...Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts...Goodbye hope you have a good day")
        exit()

    try:
        con=sqlite3.connect('account.db')
        cur=con.cursor()
        cursor=cur.execute("UPDATE DATA SET acc_amount=acc_amount+"+str(aadhar)+" where acc_no="+uacc_no)
        con.commit()
    except Exception as e:
        print("Server down...please try again later\n")
        speak("Server down...please try again later")
        exit()
    print("Please wait while your Aadhar is being updated...\n")
    speak("Please wait while your Aadhar is being updated...")
    time.sleep(2)
    print("Your Aadhar is updated...Thank you for using this ATM...Hope you have a good day ahead...\n")
    speak("Your Aadhar is updated...Thank you for using this ATM...Hope you have a good day ahead...")
    exit()
    
def takeCommand():
     r = sr.Recognizer()

     with sr.Microphone() as source:
         print("\nListening...")
         r.pause_threshold = 1
         audio = r.listen(source)
  
     try:
         print("Recognizing...")    
         query = r.recognize_google(audio, language ='en-in')
         print(f"User said: {query}\n")
  
     except Exception as e:
         print(e)
         print("\nUnable to Recognize your voice. Please say again\n")
         speak("Unable to recognize your voice. Please say again")  
         return "None"

     return query

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    
    clear()
    wishMe()
    weather()
    c=0
    while c<1:
        print("\nDo you want to Login to your Account or Create a New Account?\n")
        speak("Do you want to Login to your Account or Create a New Account?")
        i=takeCommand().lower()
        if 'login' in i:
            account()
            break
        elif 'create' in i:
            create_acc()
        else:
            c+=1
            speak("Invalid input\n")
            print("Invalid input")
    if c==1:
        print("Too many unsuccesfull attempts,Goodbye hope you have a good day\n")
        speak("Too many unsuccesfull attempts,Goodbye hope you have a good day")
        exit()
     
    while True:
         
        query = takeCommand().lower()

        if 'new account' in query or 'create' in query:
            create_acc()
                

        elif 'deposit' in query:
            deposit()


        elif 'balance' in query:
            check_bal()


        elif 'withdraw' in query:
            withdraw()


        elif 'aadhar' in query or 'link' in query:
            link_aadhar()

        
        elif 'exit' in query or 'quit' in query or 'end' in query:
            print("\nThanks for using this ATM. Hope you have a good day ahead\n")
            speak("Thanks for using this ATM. Hope you have a good day ahead")
            exit()





        






    
