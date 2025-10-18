import sys
import pyfiglet
import random

def main():
    if len(sys.argv) == 2:
        print("Too Few Arguments")
        sys.exit(0)


    string = input("Input: ")

    if len(sys.argv) == 1:
        figlet_fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(figlet_fonts)

        f = pyfiglet.Figlet(font=random_font)
        print(f.renderText(string))

    elif len(sys.argv) == 3:
        f = pyfiglet.Figlet(font=sys.argv[2])
        print(f.renderText(string))

if __name__ == "__main__":
    main()



