def find_repeated_symbols(text):
  count = {}

  for i in text:
      i = i.lower()
      if i.isalpha():
          if i in count:
              count[i] += 1
          else:
              count[i] = 1

  repeated = []
  for letter, count in count.items():
      if count >= 2:
          repeated.append(letter)
  return repeated

text = input("Enter a text: ")
result = find_repeated_symbols(text)
print(f"Repeated symbols: {result}")