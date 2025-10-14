def main():

    total = 50
    
    while total > 0:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            total -= coin
        else:
            print("Not a real coin")

        if total > 0:
            print(f"Amount Due {total} cents")
        elif total < 0:
            print(f"Change Due {0 - total}")
        else:
            print("Change Due: 0")

main()
    
