class HammingEncoder:
    def __init__(self, data_bits):
        self.data_bits = data_bits
        control_bits = 0
        while control_bits + data_bits + 1 > pow(2, control_bits):
            control_bits += 1
        self.control_bits = control_bits

    def encode(self, string):
        n = self.data_bits + self.control_bits
        transformation_matrix = [[0] * (n + 1) for i in range(self.control_bits + 1)]
        cnt = 0
        for i in range(1, n + 1):
            check = True
            for j in range(0, self.control_bits + 1):
                if i == pow(2, j):
                    check = False
            if check:
                transformation_matrix[0][i] = int(string[cnt])
                cnt += 1

        for i in range(1, n + 1):
            a = [0] * (self.control_bits + 1)
            j = int(i)
            counter = self.control_bits
            b = pow(2, self.control_bits)
            while j > 0:
                if j >= b:
                    a[counter] = 1
                    j -= b

                counter -= 1
                b /= 2

            for k in range(0, self.control_bits):
                transformation_matrix[k + 1][i] = a[k]

        for i in range(1, self.control_bits + 1):
            sum = 0
            for j in range(1, n + 1):
                sum += transformation_matrix[i][j] * transformation_matrix[0][j]
            sum %= 2
            transformation_matrix[i][0] = sum

        encoded = ""
        for i in range(1, self.control_bits + 1):
            transformation_matrix[0][pow(2, i - 1)] = transformation_matrix[i][0]
        for i in range(1, n + 1):
             encoded += str(transformation_matrix[0][i])

        return encoded

    def decode(self, string):
        n = self.data_bits + self.control_bits
        transformation_matrix = [[0] * (n + 1) for i in range(self.control_bits + 1)]
        for i in range(1, n + 1):
            transformation_matrix[0][i] = int(string[i - 1])

        for i in range(1, n + 1):
            a = [0] * (self.control_bits + 1)
            j = int(i)
            counter = self.control_bits
            b = pow(2, self.control_bits)
            while j > 0:
                if j >= b:
                    a[counter] = 1
                    j -= b

                counter -= 1
                b /= 2

            for k in range(0, self.control_bits):
                transformation_matrix[k + 1][i] = a[k]

        for i in range(1, self.control_bits + 1):
            sum = 0
            for j in range(1, n + 1):
                sum += transformation_matrix[i][j] * transformation_matrix[0][j]
            sum %= 2
            transformation_matrix[i][0] = sum

        decoded = 0
        for i in range(1, self.control_bits + 1):
            decoded += transformation_matrix[i][0] * pow(2, i - 1)

        return decoded


string = "110010010010"
he = HammingEncoder(len(string))
print(he.encode(string))
print(he.decode("00110001100100100"))
