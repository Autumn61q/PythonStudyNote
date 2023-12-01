import random
set1={"fvrev","fwr","qioxm","wqdo","dccqio"}
word=list(random.choice(set1))
list_guess=list()
for ele in word:
    list_guess.append("_")
print("welcome to hangman game!I am thinking a word,can you guess it")
guess=input("Try to guess:")
incorrect_guesses=0
while True:
    list_guess_before=list_guess[:]
    i=0
    while i<len(word):
        if guess==word[i]:
            list_guess[i]=guess
        i+=1
    if list_guess_before==list_guess:
        incorrect_guesses+=1
    print("word:",end='')
    for ele in list_guess:
        print(ele,end=' ')
    print(f"incorrect number :{incorrect_guesses}")
    if list_guess==word:
        break
    guess=input("Try again: ")
print("You are right!")