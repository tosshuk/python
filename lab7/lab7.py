people = {
         "Іванов": {"імя": "Іван", "зріст": 175, "стать": "чоловік"},
         "Петров": {"імя": "Петро", "зріст": 180, "стать": "чоловік"},
         "Сидоров": {"імя": "Микола", "зріст": 168, "стать": "чоловік"},
         "Коваленко": {"імя": "Олена", "зріст": 165, "стать": "жінка"},
         "Дмитрієва": {"імя": "Наталія", "зріст": 172, "стать": "жінка"},
         "Шевченко": {"імя": "Андрій", "зріст": 178, "стать": "чоловік"},
         "Мельник": {"імя": "Марія", "зріст": 160, "стать": "жінка"},
         "Бойко": {"імя": "Олександр", "зріст": 185, "стать": "чоловік"},
         "Кузьмін": {"імя": "Юрій", "зріст": 170, "стать": "чоловік"},
         "Павлюченко": {"імя": "Софія", "зріст": 163, "стать": "жінка"}
}

def main():
  while True:
    print("\nМеню:")
    print("1. Додати інформацію")
    print("2. Вивести інформацію")
    print("3. Середній зріст чоловіків")
    print("4. Видалити інформацію")
    print("5. Вийти")
    choice = input("Виберіть опцію: ")
    if choice == "1":
      add_info()
    elif choice == "2":
      show_info()
    elif choice == "3":
      average()
    elif choice == "4":
      delete_info()
    elif choice == "5":
      print ("Ви успішно вийшли з программи! До побачення!")
      break
    else:
      print("Невірний вибір. Будь ласка, спробуйте знову.")

def add_info():
  surname = input("Введіть прізвище: ")
  name = input("Введіть ім'я: ")
  height = int(input("Введіть зріст (у см): "))
  gender = input("Введіть стать: ")

  new_person = {"імя": name, "зріст": height, "стать": gender}
  people[surname] = new_person
  print("Інформацію про людину додано успішно.")

def show_info():
  for surname, person in people.items():
    print(f"Прізвище: {surname}, Ім'я: {person['імя']}, Зріст: {person['зріст']} см, Стать: {person['стать']}")

def delete_info():
    global people
    print("Список людей:")
    for i, (surname, person) in enumerate(people.items()):
        print(f"{i + 1}. Прізвище: {surname}, Ім'я: {person['імя']}, Зріст: {person['зріст']} см, Стать: {person['стать']}")

    surname = input("Введіть прізвище людини, яку ви хочете видалити: ")

    if surname in people:
        deleted_person = people.pop(surname)
        print(f"Інформацію про {surname} {deleted_person['імя']} було успішно видалено.")
    else:
        print("Невірне прізвище. Спробуйте ще раз.")

def average():
  total_height = 0
  count_male = 0

  for person in people.values():
    if person["стать"] == "чоловік":
      total_height += person["зріст"]
      count_male += 1

  if count_male > 0:
    average_height = total_height / count_male
    print(f"Середній зріст чоловіків: {average_height} см")
  else:
    print("Немає даних про чоловіків")

main()
