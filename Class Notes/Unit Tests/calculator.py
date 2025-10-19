def main():
    x = input("Whats x: ")
    print("x squared is", square(x))

def square(n):
    return n * n
#Make sure when you import a square function make sure main is not
#not automatically code
if __name__ == "__main__":
    main()