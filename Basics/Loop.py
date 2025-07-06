secret_word = "Wealth"
my_guess = ""
guess_count = 0
guess_limit = 3
Out_Of_Guess = False

while my_guess!=secret_word:
    if guess_count<=guess_limit:
        my_guess =input("guess your word :")
        guess_count +=1
    else:
        Out_Of_Guess = True    
    
print("You win")