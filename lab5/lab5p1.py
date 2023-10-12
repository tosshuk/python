N = int(input("Введіть кількість елементів масиву: "))
while N <= 0:
    print("Введіть число більше за 0")
    N = int(input("Введіть кількість елементів масиву: "))

array = []
for i in range(N):
    element = float(input(f"Введіть {i + 1}-й елемент масиву: "))
    array.append(element)

positive_numbers = []

for num in array:
    if num > 0:
        positive_numbers.append(num)
      
if positive_numbers:
    result = min(positive_numbers)
    print(f"Найменший додатній елемент масиву = {result}")
else:
    print("У масиві немає додатніх чисел.")