import random

words_list=['date', 'ocean', 'island', 'grape', 'house', 'cherry', 'elephant', 'fox', 'jungle', 'tree']
ChosenWordArray=[]
BlankWordArray=[]
hasUserGuessedWord=False #With this variable;User is going to continue the game unless it is not True


#Getting the random word and splitting into an array
ChosenWord=words_list[random.randint(0,len(words_list))]

#splitting the word into the array
for i in range(0,len(ChosenWord)):
    #splitting the word
    ChosenWordArray.append(ChosenWord[i])

    #Creating the blank word
    BlankWordArray.append("_"+" ")


while hasUserGuessedWord==False:
    print("".join(BlankWordArray))

    #Taking Input From user
    letterinput=input("Please enter the letter:")

    #Checking that letter exists in ChosenWordArray
    for i in range(0,len(ChosenWordArray)):
        if ChosenWordArray[i]==letterinput:
            BlankWordArray[i]=letterinput


        #If user has guessed all the letters;Finish the game
        if("_" not in "".join(BlankWordArray)):
            hasUserGuessedWord=True





print("Congratulations,You Are A Winner!")
