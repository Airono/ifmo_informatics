num = int(input("enter number: "), 16)
if num < 0:
    num = (1 << 8) + num
num = format(num, "08b")
print(num)
