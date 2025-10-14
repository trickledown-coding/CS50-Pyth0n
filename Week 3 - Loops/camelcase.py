file = input("camelCase: ")

new_string = ""

for i in file:
    if i.islower():
        new_string += i
    elif i.isupper():
        new_string += "_" + i.lower()

print(new_string)