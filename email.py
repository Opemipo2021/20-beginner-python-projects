import re
import numpy


file = open("email_text.txt", "r")

for line in file:
    s = line.strip()

    reg = re.findall(r"[A-za-z0-9._%+-]+"
                     r"@[A-Za-z0-9.-]+"
                     r"\.[A-Za-z]{2,4}", s)
    print(reg)