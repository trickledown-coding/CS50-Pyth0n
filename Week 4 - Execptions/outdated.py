calendar = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Date: ")
if "/" in date:
    date = date.split("/")
    print(f"{date[2]}-{calendar[int(date[0])]}-{calendar[int(1)]:1f}")



if date in calendar:
    print(calendar.index(date) + 1)

