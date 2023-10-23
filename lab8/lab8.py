# Роботу почав тім лід Михайловський Олексій
students_data = { "Іванов Іван Іванович": {
                    "Група": " 101",
                    "ПІБ": "Іванов Іван Іванович",
                    "Курс": 2,
                    "Предмети та оцінки": {
                        "Математика": 85,
                        "Фізика": 78,
                        "Програмування": 92
                    }
                },
                "Петров Петро Петрович": {
                    "Група": "102",
                    "ПІБ": "Петров Петро Петрович",
                    "Курс": 1,
                    "Предмети та оцінки": {
                        "Математика": 92,
                        "Фізика": 85,
                        "Програмування": 78
                    }
                },
                "Сидорова Анна Олександрівна": {
                    "Група": " 103",
                    "ПІБ": "Сидорова Анна Олександрівна",
                    "Курс": 2,
                    "Предмети та оцінки": {
                        "Математика": 78,
                        "Фізика": 82,
                        "Програмування": 90
                    }
                },
                "Коваленко Марина Сергіївна": {
                    "Група": " 106",
                    "ПІБ": "Коваленко Марина Сергіївна",
                    "Курс": 3,
                    "Предмети та оцінки": {
                        "Математика": 88,
                        "Фізика": 90,
                        "Програмування": 95
                    }
                },
                "Михайленко Олексій Олександрович": {
                    "Група": " 105",
                    "ПІБ": "Михайленко Олексій Олександрович",
                    "Курс": 1,
                    "Предмети та оцінки": {
                        "Математика": 75,
                        "Фізика": 82,
                        "Програмування": 88
                    }
                }}

def add_student_data():
    full_name = input("Введіть ПІБ студента: ")
    group = input("Введіть групу студента: ")
    course = int(input("Введіть курс студента: "))
    subjects_and_grades = {}

    num_subjects = int(input("Введіть кількість предметів: "))
    for i in range(num_subjects):
        subject = input(f"Введіть назву предмету {i + 1}: ")
        grade = int(input(f"Введіть оцінку за предмет {subject}: "))
        subjects_and_grades[subject] = grade

    students_data[full_name] = {
        "Група": group,
        "ПІБ": full_name,
        "Курс": course,
        "Предмети та оцінки": subjects_and_grades
    }
    print(f"Інформація про {full_name} успішно додана до словника.")


def display_all():
    for full_name, data in students_data.items():
        print(f"{full_name} - Група: {data['Група']} - Курс: {data['Курс']}")
        print("Предмети та оцінки:")
        for subject, grade in data["Предмети та оцінки"].items():
            print(f"  {subject}: {grade}")
def delete_student():
  print ("Empty function")
def find_key():#Пошук студентів за курсом
    find=False
    kurs=int(input("Введіть номер шуканого курса: "))
    while kurs<=0:
        print("Курс не може бути від'ємним числом")
        kurs=int(input("Введіть номер шуканого курса: "))
    for full_name, data in students_data.items():
        if data['Курс']==kurs:
            find=True
            print(f"{full_name} - Група: {data['Група']} - Курс: {data['Курс']}")
            print("Предмети та оцінки:")
            for subject, grade in data["Предмети та оцінки"].items():
                print(f"  {subject}: {grade}")
      
          
    if find is False:
        print("Даного курса не знайдено")
          
def sort():
  sorted_students = sorted(students_data.items(), key=lambda x: int(x[1]["Група"]))

  for full_name, data in sorted_students:
      print(f"{full_name} - Група: {data['Група']} - Курс: {data['Курс']}")
      print("Предмети та оцінки:")
      for subject, grade in data["Предмети та оцінки"].items():
          print(f"  {subject}: {grade}")
while True:
    choice = int(input("\n1. Додати дані про студента\n2. Вивести всіх студентів\n3. Пошук студентів за курсом\n4. Видалення інформацію про студента\n5. Сортування по групам\n6. Вийти\nВибір: "))

    if choice == 1:
        add_student_data()#Виконав  Михайловський Олексій
    elif choice == 2:
        display_all()# Виконав Боднар Степан
    elif choice == 3:
        find_key()#Виконав Шамрай Максим
    elif choice == 4:
        delete_student() #Виконує Шевченко Вадим
    elif choice == 5:
        sort() #Виконав Охріменко Антон
    elif choice == 6:
        print("Ви успішно вийшли з програми. До побачення!")
        break
    else:
        print("Невірний вибір!")
