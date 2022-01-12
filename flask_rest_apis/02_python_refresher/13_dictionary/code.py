# friend_ages= {"Rodolfo": 24, "Adam": 30, "Anne": 27}
# # print(friend_ages["Adam"])

# print(friend_ages)
# friends= [
#   {"name": "Rolf", "age": 24},
#   {"name": "Adam", "age": 30},
#   {"name": "Anne", "age": 27}
# ]

# print(friends[1]['name'])

student_attendance= {"Rolf": 96, "Bob": 80, "Anne":100}

# for student in student_attendance:
#   print(f"{student}: {student_attendance[student]}")

# for student, attendance in student_attendance.items():
#   print(f"{student}: {attendance}")
# if "Bob" in student_attendance:
#   print("el Bob")

attendance_val= student_attendance.values()
print(sum(attendance_val)/len(attendance_val))