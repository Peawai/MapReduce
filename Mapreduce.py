
def map(str):                                               #mapping
    with open(str, "r") as word_list:                       #opening text file
        return word_list.read().split()                     #read words from file and put them in a list

def reduce(words):                                          #reducing
    myD={}
    added=[]
    for elem in words:                                      #for each word of the list
        if(elem not in added):                              #if the word has not been added to the dictionary
            myD[elem]=1                                     #add it to the dictionary
            added.append(elem)                              #and add it to the already added words list

        else:
            myD[elem]+=1                                    #If the word is already in the dictionary, add one to its occurence value
    return myD                                              #And return it


fname=raw_input("Type the path of the text file you want to sort:") #ask for the path of the file



words=map(fname)            #mapping



print(reduce(words))        #reducing and printing





