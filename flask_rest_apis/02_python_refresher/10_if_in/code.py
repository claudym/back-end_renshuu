# movies_watched= {"The Matrix", "Broly", "K-Pax"}
# user_movie= input("Movie you've watched recently? ")

# if user_movie in movies_watched:
#   print(f"I've watched {user_movie} too!!!")
# else:
#   print("I haven't watched that yet yo!")

number= 7
user_input= input("Enter 'y' if you wanna play a game: ")

if user_input == "y":
  #game
  user_number= int(input("Guess the number: "))
  if user_number == number:
    print("You've guessed it!!!")
  # elif number - user_number in (-1, 1):
  elif abs(number - user_number) == 1:
    print("You were off by 1")
  else:
    print("Que feo TT")
else:
  print("Gameover from the start xD!")