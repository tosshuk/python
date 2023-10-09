a = 5
b = 80

squares = 0

for i in range (a, b + 1):
    squares += i**2

average = squares / (b - a + 1)

print("Середнє арифметичне квадратів чисел від а (= 5) до b (= 80), дорівнює: ", average)