def main():
    time = input("What time is it? ")
    T = convert(time)

    if 7 <= T <= 8:
        print("breakfast time")
    elif 12 <= T <= 13:
        print("lunch time")
    elif 18 <= T <= 19:
        print("dinner time")



def convert(time):
    hour, min = time.split(":")
    return float(hour) + (float(min) / 60)


main()