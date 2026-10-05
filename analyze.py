"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    lines = f.readlines()

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)
    math_grades = []
    python_grades = []
    english_grades = []
    students_averages = {}
    for line in lines:
        line = line.strip("\n")
        line = line.split(",")
        grades = line[1:]
        grades = [int(grade) for grade in grades]

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент
        math_grades.append(grades[0])
        total_math_grades = sum(math_grades)
        python_grades.append(grades[1])
        total_python_grades = sum(python_grades)
        english_grades.append(grades[2])
        total_english_grades = sum(english_grades)
        students = len(math_grades)
        students_averages[line[0]] = round(sum(grades) / len(grades), 1)
    best_student = sorted(students_averages.items(), key=lambda student: student[1], reverse=True)[0]

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)
    average_math_grades = round(total_math_grades / students, 1)
    average_python_grades = round(total_python_grades / students, 1)
    average_english_grades = round(total_english_grades / students, 1)

# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(f"Середній бал по класу:\n")
    f.write(f"math: {average_math_grades}\n")
    f.write(f"python: {average_python_grades}\n")
    f.write(f"english: {average_english_grades}\n")
    f.write("\n")
    f.write(f"Найкращий студент: {best_student[0]} ({best_student[1]})\n")

    print("Середній бал по класу:")
    print(f"math: {average_math_grades}")
    print(f"python: {average_python_grades}")
    print(f"english: {average_english_grades}")
    print("")
    print(f"Найкращий студент: {best_student[0]} ({best_student[1]})")

# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
