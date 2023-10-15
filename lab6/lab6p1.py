def insert_element(lst, element):
  for i in range(0, len(lst) * 2, 2):
      lst.insert(i, element)
  return lst

A = list(map(int, input("Enter a list: ").split()))
B = int(input("Enter a new element: "))
result = insert_element(A, B)
print("The new list is:", result)