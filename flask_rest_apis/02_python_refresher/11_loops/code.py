# number= 7

# user_input=input("Do you wanna play a game? (Y/n) ")
# while user_input != 'n':
#   user_number= int(input("Guess the number: "))
#   if user_number == number:
#     print("You've guessed it!!!")
#   # elif number - user_number in (-1, 1):
#   elif abs(number - user_number) == 1:
#     print("You were off by 1")
#   else:
#     print("Que feo TT")
#   user_input=input("Do you wanna again? (Y/n) ")

# friends= ["Rodolfo", "Jenny", "Bobby", "Anne-Marie"]

# for friend in friends:
#   print(f"{friend} is my friend")

# grades= [35, 67, 98, 100, 100]
# total= sum(grades)
# amount= len(grades)

# print(total/amount)

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
  if number%2 == 0:
    evens.append(number)
# print(evens)


# # -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
  print("Add")
elif user_input == "q":
  print("Quit")