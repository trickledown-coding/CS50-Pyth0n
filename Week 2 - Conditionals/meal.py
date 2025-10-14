def main():
    time = int(input("What time is it? ").replace(":", ""))
    convert_24(time)

def convert_24(time):
    if 700 <= time <= 800:
        print("Breakfast Time")
    elif 1200 <= time <= 1300:
        print("Lunch Time")
    elif 1800 <= time <= 1900:
        print("Dinner Time")

main()