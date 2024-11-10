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
    
    return True

main()

#WIP build