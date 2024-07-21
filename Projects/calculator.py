def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not and integer")


def main():
    X = get_int("X: ")
    Y = get_int("Y: ")

    print(X + Y)

main()