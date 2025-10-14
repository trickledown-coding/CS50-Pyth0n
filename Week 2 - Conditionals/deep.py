def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    check(answer)

def check(data):
    if data == "42" or data == "forty-two" or data == "forty two":
        print("Yes")
    else:
        print("No")


main()