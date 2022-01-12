name= "Joyo"
greeting= f"Hello, {name}"

print (f"Hello, {name}")

name= "Jinmeiyo"

print(f"Hello, {name}")

name= "Jojo"
greeting= "Hello, {}"
with_name= greeting.format(name)
with_name= greeting.format("Kuwabara")

print(with_name)

longer_phrase= "Hello, {}. Today is {}."

formatted= longer_phrase.format("Jojo", "Monday")
print(formatted)

x= 24521.24982753

print(f"{x:f}")          #f-string version
print("{:.7}".format(x))  #format method version

#separators
x = 23500224
print(f"{x:,}") # 23,500,224
print(f"{x:_}") # 23_500_224

x = 24521.24982753
print(f"{x:,.3f}")
print(f"{x:_f}")

#percentages
questions= 30
correct_answers= 25

print(f"You got {correct_answers/questions:.2%} correct!")