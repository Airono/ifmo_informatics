num = int(input("enter number: "), 16)
numBin = bin(num)
numBin = list(numBin)
if num >= 0:
    numBin.pop(0)
    numBin.pop(0)
else:
    numBin.pop(0)
    numBin.pop(0)
    numBin.pop(0)
for i in range(len(numBin)):
    if numBin[i] == "0":
        numBin[i] = "1"
    else:
        numBin[i] = "0"
while len(numBin) < 8:
    numBin.insert(0, "0")
if num < 0:
    numBin[0] = "1"
num = "".join(numBin)
num = int(num, 2)
num += 1
numBin = bin(num)
numBin.replace("0b", "")
print(numBin)


# num2.remove("0")
# num2.remove("b")
# for i in range(len(num2)):
#     if num2[i] == "0":
#         num2[i] = "1"
#     else:
#         num2[i] = "0"
# num3 = "".join(num2)
# print(num3)
# num4 = int(num3)
# print(num4)


# p = int(input("enter number:"), 16)
# print(p)
# if p < 0:
#     p = bin(p)
# print(p)
# list = list(p)
# del list[0]
# print(list)
# if len(list)<10:
#     del list[0]
#     del list[1]
# listC = list.copy()
# del list
# list = list('1b')
# listC.reverse()
# d = 8 - len(list)
# for j in range (0, d-1):
#     listC.append('0')
#     listC.reverse()
#     list.extend(listC)
# print(list)
# i = 2
# for i in range (2, len(list)):
#     if list[i] == ('0'):
#         list[i] = ('1')
#     else:
#         list[i] = ('0')
# print(list)
# i = len(list)-1
# while i > 0:
#     if list[i] == ('0'):
#         list[i] = ('1')
#         i = 0
#     else:
#     list[i] = ('0')
#     i -= 1
# print(list)
# if len(list)>10:
#     k = len(list)-8
#     print(list[0], end="")
#     print(list[1], end="")
#     for i in range (k, len(list)):
#         print(list[i], end="")
# else:
#     for i in range (0, len(list)):
#         print(list[i], end="")
#     else:
#         p = bin(p)
#         print(p)
# list = list(p)
# if len(list)>10:
#     k = len(list)-8
#     print(list[0], end="")
#     print(list[1], end="")
#     for i in range (k, len(list)):
#         print(list[i], end="")
# else:
#     for i in range (0, len(list)):
#         print(list[i], end="")
