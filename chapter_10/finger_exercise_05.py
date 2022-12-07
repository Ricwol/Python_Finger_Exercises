# Finger exercise, p.227
# Add to Grades a generator that meets the specification
from person import Grad, UG, grade_report


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

    def get_students(self):
        """Return the students in the grade book one at a time in alphabetical
           order
        """
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for student in self._students:
            yield student

    # Finger exercise: add generator that meets the specification
    def get_students_above(self, grade):
        """Return the students above mean grade > g one at a time"""
        for student in self.get_students():
            grades = self.get_grades(student)
            try:
                mean_grade = sum(grades) / len(grades)
            except ZeroDivisionError:
                mean_grade = 0.0
            if mean_grade > grade:
                yield student


if __name__ == "__main__":
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

    print(grade_report(six_hundred))

    mean = 75
    print(f"\nThe following students have a grade above mean {mean}")
    for a_students in six_hundred.get_students_above(mean):
        print(a_students)
