input = input("Input: ")

for char in input:
    lwrChar = char.lower()
    if lwrChar == 'a' or lwrChar == 'e' or lwrChar == 'i' or lwrChar == 'o' or lwrChar == 'u':
        first, last = input.split(char, 1)
        input = first + last

print(input)

#Working build