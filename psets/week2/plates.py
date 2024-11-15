def main():
    
    plate = input("Plate: ")
    if isValid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def isValid(plate):
    
    if plate[0].isdigit() == True and plate[1].isdigit() == True:
        return False
    if len(plate) < 2 or len(plate) > 6:
        return False
    if ending(plate) == True:
        return False
    if isZeroFirst(plate) == True:
        return False
    if plate.isalnum() == False:
        return False
    
    return True


def ending(plate):
    if plate.isalpha() == True:
        return False
    elif plate[len(plate) - 1].isdigit() == False:
        return True


def isZeroFirst(plate):
    
    for char in plate:
        if char.isdigit() == True and char != '0':
            return False
        elif char == '0':
            return True


main()

#Working build... As far as I can tell