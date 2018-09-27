# def unicStrings(str, strSet, l, r):
#     if l == r:
#         strSet.add(''.join(str))
#     else:
#         for i in range(l, r + 1):
#             str[l], str[i] = str[i], str[l]
#             unicStrings(str, strSet, l + 1, r)
#             str[l], str[i] = str[i], str[l]


def nextPermutation(str):
    i = len(str) - 1
    while i > 0 and str[i - 1] >= str[i]:
        i -= 1
    if i <= 0:
        return False
    i -= 1
    j = len(str) - 1
    while str[j] <= str[i]:
        j -= 1
    str[i], str[j] = str[j], str[i]
    str[i + 1:] = str[len(str) - 1: i: -1]
    return True


def unicStrings(str):
    str.sort()
    print("".join(str))
    while nextPermutation(str):
        print("".join(str))



strIn = input("enter string: ")
str = []
for i in range(len(strIn)):
    str.append(strIn[i])
unicStrings(str)
