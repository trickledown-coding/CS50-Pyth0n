
def main():
    while True:
        try:
            fuel_fraction = input("Fraction: ").split("/")

            fuel_percentage = (int(fuel_fraction[0]) / int(fuel_fraction[1]) * 100)

            if 99 < fuel_percentage < 100:
                print("F")
            elif 0 < fuel_percentage < 1:
                print("E")
            else:
                print(f"{int(fuel_percentage)}%")
                break

        except (ZeroDivisionError, ValueError):
            pass

main()
