numbers= [2, 3, 5]
doubled= [x * 2 for x in numbers]
print(doubled)

#regular approach (other languages)
# for num in numbers:
#   doubled.append(num*2)
# print(doubled)

friends= ["Rodolfo", "Sam", "Samantha", "Sara", "Jenny"]
starts_s= [friend for friend in friends if friend.startswith("S")]
# print(starts_s)

# for friend in friends:
#   if friend.startswith("S"):
#     starts_s.append(friend)
# print(starts_s)

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends(id):", id(friends), " starts_s:", id(starts_s))