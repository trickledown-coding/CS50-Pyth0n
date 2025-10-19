import sys
import re


b_day = input("Birthdate: ")
if re.search(r"[0-2]\d\d\d-+\d{2}-+\d{2}", b_day):
    print(b_day)
else:
    print("Wrong date format")