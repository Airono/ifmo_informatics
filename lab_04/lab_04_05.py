class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display(self):
        print("First name: ", self.first_name)
        print("Last name: ", self.last_name)
        print("Age: ", self.age)


class Student(Person):

    count = 0

    def __init__(self, first_name, last_name, age):
        Person.__init__(self, first_name, last_name, age)
        Student.count += 1
        self.student_id = Student.count
        self.record_book = list()

    def display(self):
        print("First name: ", self.first_name)
        print("Last name: ", self.last_name)
        print("Age: ", self.age)
        print("StudentID: ", self.student_id)
        print("Record Book: ")
        print("Count of 2: ", self.record_book[0])
        print("Count of 3: ", self.record_book[1])
        print("Count of 4: ", self.record_book[2])
        print("Count of 5: ", self.record_book[3], "\n")

    def add_marks(self, count2, count3, count4, count5):
        self.record_book.append(count2)
        self.record_book.append(count3)
        self.record_book.append(count4)
        self.record_book.append(count5)


class Professor(Person):

    count = 0

    def __init__(self, first_name, last_name, age, degree):
        Person.__init__(self, first_name, last_name, age)
        Professor.count += 1
        self.professor_id = Professor.count
        self.degree = degree

    def display(self):
        print("First name: ", self.first_name)
        print("Last name: ", self.last_name)
        print("Age: ", self.age)
        print("ProfessorID: ", self.professor_id)
        print("Degree: ", self.degree, "\n")


student1 = Student("Vasya", "Vasin", 20)
student1.add_marks(3, 4, 5, 2)
student1.display()

student2 = Student("Petya", "Petin", 19)
student2.add_marks(2, 0, 2, 6)
student2.display()

student3 = Student("Vanya", "Vanin", 21)
student3.add_marks(8, 1, 2, 0)
student3.display()

professor1 = Professor("Vasiliy", "Vasin", 50, "krutoy")
professor1.display()

professor2 = Professor("Petr", "Petin", 49, "neoch")
professor2.display()

professor3 = Professor("Ivan", "Vanin", 51, "nu takoe")
professor3.display()
