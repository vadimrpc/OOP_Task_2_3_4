class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n" + \
            f" Средняя оценка за домашние задания: {self.average_grade()}\n" + \
            f" Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" + \
            f" Завершенные курсы: {''.join(self.finished_courses)}"

    def average_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n" + \
            f" Средняя оценка за лекции: {self.average_grade()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruby', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Git', 9.8)
cool_reviewer.rate_hw(best_student, 'Git', 9.8)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_lecturer = Lecturer('Bob', 'Silver')
cool_lecturer.courses_attached += ['Python', 'Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 9.9)
best_student.rate_lecturer(cool_lecturer, 'Git', 9.9)

print(best_student.grades)
print(cool_lecturer.grades)
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
