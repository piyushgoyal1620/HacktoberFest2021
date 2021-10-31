import random #importing random library for generating random value late in the program
def toss(): #the function 'toss' is defined
    k=1
    while k==1: #this condition is for endless game
        a=['Heads','Tails','Heads','Tails','Heads','Tails']
        x=random.choice(a) #here x takes a random value from the List 'a' which contains Heads and Tails
        Player=input('Enter Heads or Tails') #here the player inputs their choice
        if Player==x:
            print('Congratulations!! You\'ve won the toss') #winning condition
        else:
            print('Sorry you\'ve lost the toss') #losing condition


toss() #the function is called
            
    
