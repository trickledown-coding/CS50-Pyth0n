def main():
    mass = int(input("m: "))
    print(convert(mass))

def convert(m):
    c = 300000000 
    return m * (c * c)

main()