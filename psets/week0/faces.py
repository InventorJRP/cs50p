def main():
    emoticon = input("Input your emoticon: ")
    print(convert(emoticon))

def convert(emoticon):
    return emoticon.replace(':)', '🙂').replace(':(', '🙁')


main()