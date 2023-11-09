def is_vowel(char):
  vowels = "aeiouAEIOU"
  return char in vowels

def create_file(filename):
  with open(filename, 'w') as file:
      file.write("Hello world!\nMy name is Anton\nPython programming is fun.\nHave a great day.\nI study at group IT-21")

def process_file(input_filename, output_filename):
  try:
      with open(input_filename, 'r') as input_file:
          content = input_file.read().split()
          starting_with_vowel = [word for word in content if is_vowel(word[0])]

          with open(output_filename, 'w') as output_file:
              output_file.write('\n'.join(starting_with_vowel))

  except FileNotFoundError:
      print(f"Файл {input_filename} не знайдений.")
  except Exception as e:
      print(f"Сталася помилка: {e}")

def print_file(filename):
  try:
      with open(filename, 'r') as file:
          content = file.read()
          print(content)
  except FileNotFoundError:
      print(f"Файл {filename} не знайдений.")
  except Exception as e:
      print(f"Сталася помилка: {e}")

# а) Створити файл TF16_1
create_file("TF16_1.txt")

# б) Обробити файл TF16_1 та записати результат у TF16_2
process_file("TF16_1.txt", "TF16_2.txt")

# в) Вивести вміст файлу TF16_2
print_file("TF16_2.txt")