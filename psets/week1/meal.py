def main():
    time = input("What time is it? ")
    T = convert(time)

    print(T)



def convert(time):
    hour, min = time.split(":")
    return float(hour) + (float(min) / 60)


main()