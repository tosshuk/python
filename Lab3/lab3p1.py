symbol = str(input("Введіть слово: "))

if len(symbol) >= 3:  # перевірка достатньої довжини слова
    result = symbol[:-2] + symbol[-1]  
    print(f"Результат після зрізу: {result}")
else:
    print("Довжина слова недостатня для виконання операції зрізу.")
  
print (f"Зрізаний передостанній символ:{symbol[-2]}")
