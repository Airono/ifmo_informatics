import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(acc + "0")
        self.right.walk(acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def encodeHuffman(fileIn, fileOut):
    fileIn = open("fileIn.txt", "r")
    h = []
    for ch, freq in Counter(fileIn).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = dict()
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    fileOut = open("fileOut.txt", "w")
    fileOut.write("".join(code[ch] for ch in fileIn))


def decodeHuffman(fileIn, fileOut):

