import heapq
import os
from collections import Counter, namedtuple


encoded_huffman = dict()


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def encode_huffman(file_in, file_out):
    chars = {}

    for s in file_in:
        s = s.split('\n')
        s = s[0]
        for i in s:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1

    h = []
    for ch, freq in Counter(chars).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    if h:
        [(_freq, _count, root)] = h
        root.walk(encoded_huffman, "")
    encoded = "".join(encoded_huffman[ch] for ch in s)
    file_out.write(encoded)


def decode_huffman(file_in, file_out):
    sx = []
    enc_ch = ""
    for s in file_in:
        s = s.split('\n')
        s = s[0]
        for ch in s:
            enc_ch += ch
            for dec_ch in encoded_huffman:
                if encoded_huffman.get(dec_ch) == enc_ch:
                    sx.append(dec_ch)
                    enc_ch = ""
                    break
    encoded = "".join(sx)
    file_out.write(encoded)


encoded_lz = []
encoded_dictionary_lz = []


def encode_lz(file_in, file_out):

    for char in file_in:
        char = char.split('\n')
        char = char[0]
        for s in char:
            if s in encoded_dictionary_lz:
                continue
            else:
                encoded_dictionary_lz.append(s)
        next_char = ""
        for s in char:
            a = next_char + s
            if a in encoded_dictionary_lz:
                next_char = a
            else:
                next_char = a[len(a)-1]
                dictionary_word = a[0:len(a)-1]
                encoded_dictionary_lz.append(a)
                encoded_lz.append(encoded_dictionary_lz.index(dictionary_word))
        encoded_lz.append(encoded_dictionary_lz.index(next_char))

    i = 0
    while i != len(encoded_lz):
        file_out.write(str(encoded_lz[i]))
        i += 1


def decode_lz(file_in, file_out):
    dictionary = []

    for char in file_in:
        char = char.split('\n')
        char = char[0]
        for s in char:
            if s in dictionary:
                continue
            else:
                dictionary.append(s)
        next_char = ""
        for s in char:
            a = next_char + s
            if a in dictionary:
                next_char = a
            else:
                next_char = a[len(a) - 1]
                dictionary.append(a)
    x = ""
    for i in encoded_lz:
        x = x + encoded_dictionary_lz[i]
    file_out.write(x)


def get_compression_ratio(input_data, output_data):
    initial_data = os.stat(input_data).st_size
    total_data = os.stat(output_data).st_size
    return float(initial_data / total_data)


input_file = open("fileIn.txt", "r")
output_file = open("fileOut.txt", "w")
encode_lz(input_file, output_file)
output_file = open("fileOut.txt", "r")
compression_ratio = get_compression_ratio("fileIn.txt", "fileOut.txt")
print("Compression ration for LZ Algorithm: ", compression_ratio)
input_file.close()
output_file.close()

input_file = open("fileOut.txt", "r")
output_file = open("fileOut2.txt", "w")
decode_lz(input_file, output_file)
input_file.close()
output_file.close()

input_file = open("fileIn.txt", "r")
output_file = open("fileOut.txt", "w")
encode_huffman(input_file, output_file)
output_file = open("fileOut.txt", "r")
compression_ratio = get_compression_ratio("fileIn.txt", "fileOut.txt")
print("Compression ration for Huffman Algorithm: ", compression_ratio)
input_file.close()
output_file.close()

input_file = open("fileOut.txt", "r")
output_file = open("fileOut2.txt", "w")
decode_huffman(input_file, output_file)
input_file.close()
output_file.close()
