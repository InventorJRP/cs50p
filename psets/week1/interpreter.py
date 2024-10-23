def main():
    x, y, z = input("Expression: ").split(" ")

    print(math(float(x), y, float(z)))

def math(x, y, z):
    match y:
        case '+':
            return x + z
        case '-':
            return x - z
        case '*':
            return x * z
        case '/':
            return x / z
        
main()