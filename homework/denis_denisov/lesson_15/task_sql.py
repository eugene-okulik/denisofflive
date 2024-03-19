import mysql.connector as mysql

# Подключение к БД
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Добавление группы
add_new_group_sql = """
INSERT INTO
`groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
"""
# Параметры группы
new_group_values = 'AQA Engineers', 'march 2024', 'may 2024'

cursor.execute(add_new_group_sql, new_group_values)
group_id = cursor.lastrowid

# Добавление студента
add_new_student_sql = """
INSERT INTO students (name, second_name, group_id)
VALUES (%s, %s, %s)
"""
# Параметры студента
new_student_values = 'Denzel', 'Washington', group_id

cursor.execute(add_new_student_sql, new_student_values)
student_id = cursor.lastrowid

# Добавление книги
add_new_book_sql = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
# Параметры книги
add_new_book_value = ('Python для начинающих', student_id)
cursor.execute(add_new_book_sql, add_new_book_value)
book1_id = cursor.lastrowid

# Добавление книги
add_new_book_sql = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
# Параметры книги
insert_new_book_value = ('Python для продвинутых', student_id)
cursor.execute(add_new_book_sql, insert_new_book_value)
book2_id = cursor.lastrowid

# Добавление предмета
add_new_subject_sql = """
INSERT INTO subjets (title)
VALUES (%s)
"""
# Параметры предмета
add_new_subject_value = ('Ручное тестирование',)
cursor.execute(add_new_subject_sql, add_new_subject_value)
subject1_id = cursor.lastrowid

# Добавление предмета
add_new_subject_sql = """
INSERT INTO subjets (title)
VALUES (%s)
"""
# Параметры предмета
add_new_subject_value = ('Автоматизация тестирования',)
cursor.execute(add_new_subject_sql, add_new_subject_value)
subject2_id = cursor.lastrowid

# Добавление урока
add_new_lessons_sql = """
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
"""
# Параметры урока
add_new_lessons_value = ('Урок 1 Ручное тестирование', subject1_id)
cursor.execute(add_new_lessons_sql, add_new_lessons_value)
lesson1_id = cursor.lastrowid

# Добавление урока
add_new_lessons_sql = """
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
"""
# Параметры урока
add_new_lessons_value = ('Урок 2 Ручное тестирование', subject2_id)
cursor.execute(add_new_lessons_sql, add_new_lessons_value)
lesson2_id = cursor.lastrowid

# Добавление оценки
add_new_marks_sql = """
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)
"""
# Параметры оценки
add_new_marks_value = (5, lesson1_id, student_id)
cursor.execute(add_new_marks_sql, add_new_marks_value)

# Добавление оценки
add_new_marks_sql = """
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)"""
# Параметры оценки
add_new_marks_value = (4, lesson2_id, student_id)
cursor.execute(add_new_marks_sql, add_new_marks_value)

# Вывести всю информацию о студенте (книги, оценки с названиями занятий и предметов, используя Join)
all_info_student_sql = '''
SELECT *
FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons on marks.lesson_id = lessons.id
JOIN subjets on lessons.subject_id = subjets.id
WHERE students.id  = %s
'''

student_id_value = (student_id,)
cursor.execute(all_info_student_sql, student_id_value)
print(cursor.fetchall())

db.commit()
db.close()
