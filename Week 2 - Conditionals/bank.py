def main():
    greeting = input("Greeting: ").lower()
    check(greeting)


def check(greeting):
    if "hello" in greeting:
        print("$0")
    elif greeting[0] == "h" and "hello" not in greeting:
        print("$20")
    else:
        print("$100")

main()