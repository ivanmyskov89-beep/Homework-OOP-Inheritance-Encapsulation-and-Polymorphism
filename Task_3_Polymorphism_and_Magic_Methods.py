class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Метод для выставления оценок лекторам"""
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        """Получить среднюю оценку за домашние задания"""
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        """Магический метод для строкового представления студента"""
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        avg_grade = self.get_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        """Метод для сравнения 'меньше' (по средней оценке)"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        """Метод для сравнения 'меньше или равно'"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        """Метод для сравнения 'равно'"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # оценки за лекции

    def get_average_grade(self):
        """Получить среднюю оценку за лекции"""
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        """Магический метод для строкового представления лектора"""
        avg_grade = self.get_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade}')

    def __lt__(self, other):
        """Метод для сравнения 'меньше' (по средней оценке)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        """Метод для сравнения 'меньше или равно'"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        """Метод для сравнения 'равно'"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Метод для выставления оценок студентам за домашние задания"""
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Магический метод для строкового представления проверяющего"""
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


# Создание объектов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student.courses_in_progress.append('Git')
best_student.finished_courses.append('Введение в программирование')

second_student = Student('Alice', 'Smith', 'female')
second_student.courses_in_progress.append('Python')
second_student.finished_courses.append('Введение в программирование')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached.append('Python')

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached.append('Python')

second_lecturer = Lecturer('Jane', 'Brown')
second_lecturer.courses_attached.append('Python')

# Проверяющий выставляет оценки студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

cool_reviewer.rate_hw(second_student, 'Python', 7)
cool_reviewer.rate_hw(second_student, 'Python', 8)
cool_reviewer.rate_hw(second_student, 'Python', 6)

# Студенты выставляют оценки лекторам
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)

second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 10)

# Демонстрация работы __str__
print('=== Проверяющий ===')
print(cool_reviewer)
print()

print('=== Лекторы ===')
print(cool_lecturer)
print()
print(second_lecturer)
print()

print('=== Студенты ===')
print(best_student)
print()
print(second_student)
print()

# Демонстрация сравнения
print('=== Сравнение студентов ===')
print(f"best_student > second_student: {best_student > second_student}")
print(f"best_student < second_student: {best_student < second_student}")
print(f"best_student == second_student: {best_student == second_student}")
print()

print('=== Сравнение лекторов ===')
print(f"cool_lecturer > second_lecturer: {cool_lecturer > second_lecturer}")
print(f"cool_lecturer < second_lecturer: {cool_lecturer < second_lecturer}")
print(f"cool_lecturer == second_lecturer: {cool_lecturer == second_lecturer}")