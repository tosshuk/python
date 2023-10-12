import math
from mod import sum_of_squares

def calculate_z (x, y):
  z = math.cos(2 * x) + math.sin(2 * y)
  return z


x = float(input("Введіть значення х: "))
y = float(input("Введіть значення y: "))

z = calculate_z(x, y)

print(f"Значення z = {z}")

print("\nТепер перейдемо до іншої функції.")

N = int(input("Введіть значення N: "))
while (N <= 0):
  N = int(input("Введіть значення N(Ви допустили помилку у ОДЗ введіть значення більше 0): ")) 
  
result = sum_of_squares(N)
print(f"Сума квадратів від 1 до {N} = {result}")