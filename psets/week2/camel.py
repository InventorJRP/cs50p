camel = input(": ")

for char in camel:
    if char.isupper():
        first, last = camel.split(char)
        camel = first + '_' + char.lower() + last

print(camel)

#Working build