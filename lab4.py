# Частина роботи виконана тім лідом групи Михайловським Олексієм
str="Python is popular for a variety of reasons, the most important of which is its ease of learning. Python is a simple language to learn. This is primarily due to its linguistic similarities to English. The syntax of Python is characterized by a small number of rules and special situations. It’s safe to say that the focus in Python is on what you want to do with the code rather than on the language’s complexities. Python is simple to learn and master."
print(str.split(" "))# Розділяє рядок за вказаним роздільником і повертає список
print(str.title())#Перетворює перший символ кожного слова на верхній регістр
print(str.upper())#Перетворює рядок у верхній регістр
# Інший студент Шамрай Максим реалізує такі функції : lower(),replace(),split()
# Частина роботи виконана Шамраєм Максимом
print()
print(str.lower())#Перетворює рядок у нижній регістр
print(str.replace("a","d"))#Повертає рядок, де вказане значення замінено на вказане значення
print(str.split(". "))# Розділяє рядок за вказаним роздільником і повертає список
# Інший студент Боднар Степан реалізує такі функції : isalpha(), isalnum(), split()
# Частина роботи виконана Боднаром Степаном
print()
print(str.isalpha())#Повертає true, якщо всі символи в рядку знаходяться в алфавіті
print(str.isalnum())#Повертає true, якщо всі символи в рядку буквено-цифрові
print(str.split(","))#Розділяє рядок за вказаним роздільником і повертає список
# Інший студент Гриб Павло реалізує такі функції : strip(), zfill(), rjust()
# Інший студент Охріменко Антон реалізує такі функції : isnumeric(), strip(), 
print (str.isnumeric()) #Повертає true, якщо всі символи в рядку є числами
print(str.strip()) #Повертає скорочену версію рядка
print(str.swapcase()) #Міняє регістр всіх літер у рядку