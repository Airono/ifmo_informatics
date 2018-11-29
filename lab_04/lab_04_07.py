class Row:
    cnt = 0

    def __init__(self, collection, value):
        self.id = Row.cnt
        Row.cnt += 1
        self.collection = collection
        self.value = int(value)


class Table:
    def __init__(self, rows_num):
        self.rowsNum = rows_num
        self.rows = list()

    def add_row(self, row):
        check = True
        for i in range(0, len(self.rows)):
            if row.id == self.rows[i].id:
                check = False
        if check:
            self.rows.append(row)

    def set_row(self, row):
        check = False
        for el in self.rows:
            if el.id == row.id:
                check = True

        if check:
            row_id = 0
            for i in range(0, len(self.rows)):
                if self.rows[i] == row:
                    row_id = i
            self.rows[row_id].collection = row.collection
            self.rows[row_id].value = row.value
        else:
            print("Ошибка")

    def get_row(self, row_id):
        for el in self.rows:
            if el.id == row_id:
                return el

    def display(self):
        basest = "id"
        for i in range(1, len(self.rows[0].collection)+1):
            basest += "  x{}".format(i)
        basest += "   f(x)"
        print(basest)
        for el in self.rows:
            st = " "
            st += str(el.id)
            for i in range(0, len(el.collection)):
                st += "   {}".format(el.collection[i])
            st += "  |  "
            st += str(el.value)
            print(st)


def search_dif(a, b):
    cnt = 0
    for i in range(0, len(a[1])):
        if a[1][i] != b[1][i]:
            cnt += 1
    return cnt


def search_ab(table):
    l = []
    for i in range(0, len(table) - 1):
        for j in range(i + 1, len(table)):
            if search_dif(table[i], table[j]) == 1:
                l.append(table[i])
                l.append(table[j])
                break
    return l


def make_new_row(a, b):
    collection = []
    new_id = []

    new_id.extend(a[0])

    for i in range(0, len(b[0])):
        check = True
        for j in range(0, len(a[0])):
            if b[0][i] == a[0][j]:
                check = False
        if check:
            new_id.append(b[0][i])
    for i in range(0, len(a[1])):
        if a[1][i] == b[1][i]:
            collection.append(a[1][i])
        else:
            collection.append('*')

    new_row = [new_id, collection]
    return new_row


def make_new_table(table):
    new_table = []
    l = search_ab(table)
    for el in table:
        if el != l[0] and el != l[1]:
            new_table.append(el)
    new_table.append(make_new_row(l[0], l[1]))
    return new_table


class LogicFunction:
    def __init__(self, variables_num, table):
        self.variablesNum = variables_num
        self.table = table

    def get_expression(self):
        st = ""
        new_table = list()
        cnt = 1
        for i in range(0, len(self.table.rows)):
            if self.table.rows[i].value == 1:
                d = list()
                d.append(cnt)
                new_table.append([d, self.table.rows[i].collection])
                cnt += 1
        end = False
        while not end:
            if len(new_table) > 1:
                if search_ab(new_table) != []:
                    new_table = make_new_table(new_table)
                else:
                    end = True
            else:
                end = True

        for el in new_table:
            for i in range(0, len(el[1])):
                if el[1][i] == '1':
                    st += "X{}*".format(i+1)
                else:
                    if el[1][i] == '0':
                        st += "!X{}*".format(i+1)
            st = st[:-1]
            st += "+"
        st = st[:-1]
        return st

    def get_table(self):
        return self.table

    def print_table(self):
        self.table.display()


print("Введите кол-во переменных в функции:")
variableNums = int(input())
print("Введите кол-во строк:")
rowsNum = int(input())

table = Table(rowsNum)

for i in range(0, rowsNum):
    a = []
    print("Введите ряд:")
    for j in range(0, variableNums):
        a.append(input())
    print("Введите значение функции:")
    f = input()
    b = Row(a, f)
    table.add_row(b)

lf = LogicFunction(variableNums, table)
print(lf.print_table())
print(lf.get_expression())



