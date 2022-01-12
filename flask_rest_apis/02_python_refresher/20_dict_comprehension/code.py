# users = [
#   (0, "Bobby", "password"),
#   (1, "Rodolfo", "b12345"),
#   (2, "Jose", "longypass"),
#   (3, "username", "12345")
# ]

# username_mapping= {user[1]: user for user in users}
# print(username_mapping)

# username_input= input("Enter your username: ")
# password_input= input("Enter your password: ")

# _, username, password= username_mapping[username_input]

# if password_input == password:
#   print("yo got it!")
# else:
#   print("you ain't got sh..!")


# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
  "name": "Jose",
  "school": "Computing",
  "grades": (66, 77, 88)
}
print(student)

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data["grades"]
    return sum(grades) / len(grades)
print(average_grade(student))

# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
  total = 0
  count = 0
  # for student in student_list:
  #   total += average_grade(student)
  #   count += 1
  total= sum(map(lambda list: sum(list["grades"])/len(list), student_list))
  # total= sum(map(average_grade, student_list))
  count= len(student_list)

  return total / count

student2 = {
  "name": "Jonas",
  "school": "Singig",
  "grades": (80, 80, 80)
}

print(average_grade_all_students([student, student2]))