#loop to loop 6 times for 6 guesses
for guess_num in range(1, 7):
  guess = input(f"\nGuess {guess_num}: ").upper()#get user input

#test if the user's guess is the same (==) as 'SNAKE'
  if guess == "SNAKE":
    print("Correct")
    break
  else:
    print("Wrong")
    for snake_letter, crane_letter in zip("SNAKE", guess):
      if snake_letter == crane_letter:
        print(snake_letter)
