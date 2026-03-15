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
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        avg_grade = self.get_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        """Получить среднюю оценку за лекции"""
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


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
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


# Функция для подсчета средней оценки за домашние задания по курсу
def average_hw_grade(students_list, course_name):
    """
    Подсчитывает среднюю оценку за домашние задания
    по всем студентам в рамках конкретного курса
    """
    total_grades = []
    for student in students_list:
        if (isinstance(student, Student)
                and course_name in student.grades):
            total_grades.extend(student.grades[course_name])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# Функция для подсчета средней оценки за лекции по курсу
def average_lecture_grade(lecturers_list, course_name):
    """
    Подсчитывает среднюю оценку за лекции
    всех лекторов в рамках конкретного курса
    """
    total_grades = []
    for lecturer in lecturers_list:
        if (isinstance(lecturer, Lecturer)
                and course_name in lecturer.grades):
            total_grades.extend(lecturer.grades[course_name])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# Создание экземпляров классов (по 2 каждого)
print("=== СОЗДАНИЕ ЭКЗЕМПЛЯРОВ КЛАССОВ ===\n")

# Студенты
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress.extend(['Python', 'Git'])
student1.finished_courses.append('Введение в программирование')

student2 = Student('Alice', 'Smith', 'female')
student2.courses_in_progress.extend(['Python', 'Java'])
student2.finished_courses.append('Основы алгоритмов')

print("Созданы студенты:")
print(f"1. {student1.name} {student1.surname}")
print(f"2. {student2.name} {student2.surname}\n")

# Проверяющие
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached.extend(['Python', 'Git'])

reviewer2 = Reviewer('Jane', 'Johnson')
reviewer2.courses_attached.extend(['Python', 'Java'])

print("Созданы проверяющие:")
print(f"1. {reviewer1.name} {reviewer1.surname}")
print(f"2. {reviewer2.name} {reviewer2.surname}\n")

# Лекторы
lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached.extend(['Python', 'Git'])

lecturer2 = Lecturer('Bob', 'Wilson')
lecturer2.courses_attached.extend(['Python', 'Java'])

print("Созданы лекторы:")
print(f"1. {lecturer1.name} {lecturer1.surname}")
print(f"2. {lecturer2.name} {lecturer2.surname}\n")

# Выставление оценок студентам
print("=== ВЫСТАВЛЕНИЕ ОЦЕНОК ===\n")

# Reviewer1 оценивает студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 6)

# Reviewer2 оценивает студентов
reviewer2.rate_hw(student2, 'Java', 9)
reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Java', 10)

print("Оценки студентов после проверки:")
print(f"{student1.name} {student1.surname}: {student1.grades}")
print(f"{student2.name} {student2.surname}: {student2.grades}\n")

# Выставление оценок лекторам
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Git', 9)
student1.rate_lecturer(lecturer1, 'Git', 8)

student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Java', 8)
student2.rate_lecturer(lecturer2, 'Java', 9)

print("Оценки лекторов от студентов:")
print(f"{lecturer1.name} {lecturer1.surname}: {lecturer1.grades}")
print(f"{lecturer2.name} {lecturer2.surname}: {lecturer2.grades}\n")

# Вызов методов __str__
print("=== ИНФОРМАЦИЯ ОБ ОБЪЕКТАХ (__str__) ===\n")

print("Проверяющие:")
print(reviewer1)
print()
print(reviewer2)
print()

print("Лекторы:")
print(lecturer1)
print()
print(lecturer2)
print()

print("Студенты:")
print(student1)
print()
print(student2)
print()

# Сравнение студентов и лекторов
print("=== СРАВНЕНИЕ ===\n")

print(f"student1 > student2: {student1 > student2}")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 == student2: {student1 == student2}")
print()

print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
print()

# Использование функций для подсчета средних оценок
print("=== ПОДСЧЕТ СРЕДНИХ ОЦЕНОК ===\n")

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

# Средние оценки за домашние задания по курсам
print("Средние оценки за домашние задания:")
python_hw_avg = average_hw_grade(students_list, 'Python')
git_hw_avg = average_hw_grade(students_list, 'Git')
java_hw_avg = average_hw_grade(students_list, 'Java')

print(f"По курсу Python: {python_hw_avg:.2f}")
print(f"По курсу Git: {git_hw_avg:.2f}")
print(f"По курсу Java: {java_hw_avg:.2f}")
print()

# Средние оценки за лекции по курсам
print("Средние оценки за лекции:")
python_lecture_avg = average_lecture_grade(lecturers_list, 'Python')
git_lecture_avg = average_lecture_grade(lecturers_list, 'Git')
java_lecture_avg = average_lecture_grade(lecturers_list, 'Java')

print(f"По курсу Python: {python_lecture_avg:.2f}")
print(f"По курсу Git: {git_lecture_avg:.2f}")
print(f"По курсу Java: {java_lecture_avg:.2f}")