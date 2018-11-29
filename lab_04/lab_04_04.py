import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


class Encoder:

    def __init__(self):
        pass

    def encode(self, string):
        pass

    def decode(self, string):
        pass


class HuffmanEncoder(Encoder):

    def __init__(self):
        Encoder.__init__(self)
        self.compressionCoef = 1

    def encode(self, string):
        h = []
        for ch, freq in Counter(string).items():
            h.append((freq, len(h), Leaf(ch)))
        heapq.heapify(h)
        count = len(h)
        while len(h) > 1:
            freq1, _count1, left = heapq.heappop(h)
            freq2, _count2, right = heapq.heappop(h)
            heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
            count += 1
        code = {}
        if h:
            [(_freq, _count, root)] = h
            root.walk(code, "")
        encoded = "".join(code[ch] for ch in string)
        HuffmanEncoder.__setCompressionCoef__(self, string, encoded)
        print(encoded)

    def decode(self, string):
        l = list()
        l = string.split()
        encoded = l[len(l)-1]
        code = dict()
        i = 0
        while i != len(l) - 2:
            code[l[i]] = l[i + 1]
            i += 1
        sx = []
        enc_ch = ""
        for ch in encoded:
            enc_ch += ch
            for dec_ch in code:
                if code.get(dec_ch) == enc_ch:
                    sx.append(dec_ch)
                    enc_ch = ""
                    break
        print("".join(sx))

    def __setCompressionCoef__(self, string, encoded):
        self.st = string
        self.nd = encoded
        HuffmanEncoder.compressionCoef = len(self.nd) / len(self.st) * 100


    def getCompressionCoef(self):
        print("%.2f" % HuffmanEncoder.compressionCoef)

class LZEncoder(Encoder):

    def __init__(self):
        Encoder.__init__(self)
        self.compressionCoef = 1

    def encode(self, string):
        l = string
        i = 0
        d = dict()
        k = 1
        encoded = ''
        t = ''
        while i <= len(l)-1:
            t = t + l[i]
            if t in d and i == len(l)-1:
                encoded = encoded + str(d.get(t))
            if t in d:
                pass
            else:
                d[t] = k
                k+=1
                if len(t) == 1:
                    encoded = encoded + '0' + t
                else:
                    sy = t[0:-1]
                    sy1 = str(d.get(sy))
                    el = t[-1:]
                    encoded = encoded + sy1 + el
                t = ''
            i += 1
        LZEncoder.__setCompressionCoef__(self, string, encoded)
        print(encoded)

    def decode(self, string):
        l = string
        i = 0
        d = dict()
        ch = 0
        s =''
        k = 1
        decoded = ''
        while i < len(l) - 1:
            while ch != 1:
                if l[i]=='0'or l[i]=='1'or l[i]=='2'or l[i]=='3'or l[i]=='4'or l[i]=='5'or l[i]=='6'or l[i]=='7'or l[i]=='8'or l[i]=='9':
                    s = s + l[i]
                else:
                   s = s + l[i]
                   ch = 1
                i+=1
            if s[0:-1]=='0':
                d[str(k)] = s[-1:]
            else:
                d[str(k)] = d[s[0:-1]] + s[-1:]
            k+=1
            ch = 0
            s = ''
        for i in range(1, k):
            decoded += d[str(i)]
        if l[-1:] == '0' or l[-1:] == '1' or l[-1:] == '2' or l[-1:] == '3' or l[-1:] == '4' or l[-1:] == '5' or l[-1:] == '6' or l[-1:] == '7' or l[-1:] == '8' or l[-1:] == '9':
            decoded += d[str(l[-1:])]
        print(decoded)

    def __setCompressionCoef__(self, string, encoded):
        self.st = string
        self.nd = encoded
        LZEncoder.compressionCoef = len(self.nd) / len(self.st) * 100

    def getCompressionCoef(self):
        print("%.2f" % LZEncoder.compressionCoef)


t = HuffmanEncoder()
t.encode("Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.")
t.decode("a 01 b 10 c 11 0111111001")
t.getCompressionCoef()

t1 = LZEncoder()
t1.encode("Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.")
t1.decode("0a1b2a1")
t1.getCompressionCoef()
