def swap_list(list):
  swapped = list.copy()
  for i in range (0, len(list) - 1, 2):
    swapped[i], swapped[i + 1] = swapped [i + 1], swapped [i]
  return swapped
  
A = list(map(int, input("Enter a list: ").split()))
print(f"Маємо оригінальний список: {A}")
result = swap_list(A)
print(f"Змінений список: {result}")
