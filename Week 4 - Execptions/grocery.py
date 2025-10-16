def main():
    grocery_list = {}

    while True:
        try:
            item = input()
            if item not in grocery_list:
                grocery_list[item] = 1
            elif item in grocery_list:
                grocery_list[item] += 1
                 
        except KeyError:
            pass           
        except EOFError:
            print("\n"*5)
            print("-------------------------")
            print("       Grocery List      ")
            print("-------------------------")
            for key in grocery_list:
                print("Item: ", end='')
                print(f"{grocery_list[key]} x ", end='')
                print(f"{key}", end='\n')
            break
            


main()