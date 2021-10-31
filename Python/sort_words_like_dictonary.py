def sort_words(): #defining the function for sorting the words.
    k=1
    while k==1: #this condition is used so that the porgram doesnt stop untill all the data has been fed
        word=input('Enter the word, leave blank if you want to stop')
        #'word' variable stores the word entered by the user 
        if word=='':
            break  #if the user want to stop entering the data, they can just press enter and the data entering phase will be over
        else:
            l.append(word)
    print('Enter the order in which you want the Words to be displayed')
    #message for the user
    order=input('Enter \'A\' for asscending order, \'B\' for decending order')
    #'A' is entered for alphabetical order and 'B' for the opposite
    
    if order=='A':
        l.sort() #Alphabatical sort
        print(l)
    if order=='B':
        l.sort(reverse=True) #Opposite sort
        print(l)
    
        
l=[] #the list that will store all the data is the variable 'l'
sort_words() #the function is called
