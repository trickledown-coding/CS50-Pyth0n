def main():
    grocery_list = []

    while True:
        try:
            item = input()
            grocery_list.append(item)

        except EOFError:
            print(grocery_list)
            break
            


main()