name= input("what's your name? ")

print(f"your name is {name}")

size_input= input("How big is your house (in square feet): ")
size_meters= int(size_input)/10.8
print(f"{size_input} feet is {size_meters:.2f} meters.")