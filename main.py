#get user input
guess = input("Guess a word: ").upper()
print(guess)

#test if the user's guess is the same (==) as 'SNAKE'
if guess == "SNAKE":
  print("Correct")
else:
  print("Wrong")
