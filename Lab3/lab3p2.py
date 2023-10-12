word = str(input("Введіть слово: "))
f = filter(str.isalpha, word)
word1 = "".join(f)
print(f"Після видалення усіх символів, що не є буквами отримаємо: {word1} ")
