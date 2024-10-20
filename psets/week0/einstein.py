def main():
    mass = int(input("m: "))
    print("E:", energy(mass))

def energy(mass):
    return mass * (300000000 ** 2)


main()