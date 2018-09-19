def unicStrings(str, l, r):
    if l == r:
        print(''.join(str), end=", ")
    else:
        for i in range(l, r + 1):
            str[l], str[i] = str[i], str[l]
            unicStrings(str, l + 1, r)
            str[l], str[i] = str[i], str[l]


strIn = input("enter string: ")
str = []
for i in range(len(strIn)):
    str.append(strIn[i])
unicStrings(str, 0, len(str) - 1)
