# Implementation of class Person, Figure 10-3, p.211

import datetime


class Person:

    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(" ")
        except ValueError:
            self._last_name = name
        else:
            self._last_name = name[last_blank+1:]
        self._birthday = None

    def get_name(self):
        """Returns self's full name"""
        return self._name

    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name

    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate
        """
        self._birthday = birthdate

    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday is None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """Assume other a Person
           Returns True if self precedes other in alphabetical order, False
           otherwise. Comparison is based on last names, but if these are the
           same full names are compared.
        """
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns self's name"""
        return self._name


def example_person():
    me = Person('Michael Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    print(him.get_last_name())  # prints Obama
    him.set_birthday(datetime.date(1961, 8, 4))
    her.set_birthday(datetime.date(1958, 8, 16))
    print(him.get_name(), 'is', him.get_age(), 'days old')

    pList = [me, him, her]
    for p in pList:
        print(p)
        # Prints person in the order entered into pList:
        # Michael Guttag
        # Barack Hussein Obama
        # Madonna

    # Sort list possible as __lt__ defined for Person()
    pList.sort()
    for p in pList:
        print(p)
        # Prints person in ascending order sorted by last name
        # Michael Guttag
        # Madonna
        # Barack Hussein Obama


# ------------------------------------------------
# Implementation of MIT Person, Figure 10-4, p.214
class MIT_person(Person):

    # Class variable, identification number
    _next_id_num = 0

    def __init__(self, name):
        super().__init__(name)
        # Call class variable
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def __lt__(self, other):
        return self._id_num < other._id_num

    def is_student(self):
        return isinstance(self, Student)


def example_mit_person():
    p1 = MIT_person("Barbara Beaver")
    print(p1, '\'s id number is ' + str(p1.get_id_num()))

    p1 = MIT_person('Mark Guttag')
    p2 = MIT_person('Billy Bob Beaver')
    p3 = MIT_person('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')

    print("p1 < p2 =", p1 < p2)  # True
    print("p3 < p2 =", p3 < p2)  # False
    print("p4 < p1 =", p4 < p1)  # True

    # '<' is shorthand for p1.__lt__(p4)
    # As __lt__ is defined in MIT_person with _id_num this wil cause an
    # AttributeError as 'Person' object has no attribute '_id_num'
    # print("p1 < p4 =", p1 < p4)
    return p3


# ------------------------------------------------
# Implement another couple of levels of inheritance, Figure 10-5, p.217
class Student(MIT_person):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year

    def get_class(self):
        return self._year


class Grad(Student):
    pass


def example_student(p3):
    p5 = Grad("Buzz Aldrin")
    p6 = UG("Billy Beaver", 1984)
    # print(p5, "is a graduate student is", type(p5) == Grad)
    # print(p5, "is an undergraduate student is", type(p5) == UG)

    # Can be rewritten using isinstance function
    print(p5, "is a graduate student is", isinstance(p5, Grad))
    print(p5, "is an undergraduate student is", isinstance(p5, UG))

    print(p5, "is a student is", p5.is_student())
    print(p6, "is a student is", p6.is_student())
    print(p3, "is a student is", p3.is_student())


class Transfer_student(Student):
    def __init__(self, name, from_school):
        super().__init__(name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school


def example_transfer():
    ts = Transfer_student("Brunni Busen", "Baumschule")
    print(ts, "is a student is", ts.is_student())


# ------------------------------------------------
# Implementation of Grades to keep track of the grades of a collection
# of students, Figure 10-6, p.220
class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book
        """
        if student in self._students:
            raise ValueError("Duplicate student")
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student
        """
        try:
            self._grades[student.get_id_num()].append(grade)
        except KeyError:
            raise ValueError("Student not in mapping")

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            # Return a copy of _grades for student
            return self._grades[student.get_id_num()][:]
        except KeyError:
            raise ValueError("Student not in mapping")

    # Implementation of get_students in Figure 10-6 inefficiently 
    # creates a copy of _students every time it gets called
    # def get_students(self):
    #     """Return a sorted list of the students in the grade book"""
    #     if not self._is_sorted:
    #         self._students.sort()
    #         self._is_sorted = True
    #     return self._students[:]

    # Implementation of get_students in Figure 10-9, p.226
    # using generator as return value
    def get_students(self):
        """Return the students in the grade book one at a time in alphabetical
           order
        """
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for student in self._students:
            yield student


# ------------------------------------------------
# Define grade_report using class Grades, Figure 10-7, p.222
def grade_report(course):
    """Assumes course is of type Grades"""
    report = ""
    for student in course.get_students():
        tot = 0.0
        num_grades = 0
        for grade in course.get_grades(student):
            tot += grade
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{student}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{student} has no grades"
    return report


def example_grade_book():
    ug1 = UG("Jane Doe", 2021)
    ug2 = UG("Pierce Addison", 2041)
    ug3 = UG("David Henry", 2003)
    g1 = Grad("Billy Buckner")
    g2 = Grad("Bucky F. Dent")

    # Create grade book for course six hundred
    six_hundred = Grades()

    # Add students to course
    six_hundred.add_student(ug1)
    six_hundred.add_student(ug2)
    six_hundred.add_student(g1)
    six_hundred.add_student(g2)

    for student in six_hundred.get_students():
        six_hundred.add_grade(student, 75)

    six_hundred.add_grade(g1, 25)
    six_hundred.add_grade(g2, 100)
    six_hundred.add_student(ug3)

    # Print grade report of the course
    print(grade_report(six_hundred))


if __name__ == "__main__":
    example_person()
    p3 = example_mit_person()
    example_student(p3)
    example_transfer()
    example_grade_book()
