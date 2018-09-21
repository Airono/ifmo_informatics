num = int(input("enter number in 12 notation: "), 12)
print(num)
newNum = ""
mod = ""
while num > 0:
    if num % 14 < 10:
        mod = str(num % 14)
    elif num % 14 == 10:
        mod = "A"
    elif num % 14 == 11:
        mod = "B"
    elif num % 14 == 12:
        mod = "C"
    else:
        mod = "D"
    newNum += mod
    num //= 14
print(newNum)
