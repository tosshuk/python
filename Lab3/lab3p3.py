def find_non_repeat_words (sentence):
  words = sentence.split()
  unique_words = []

  for word in words:
        word_lower = word.lower()
        if words.count(word_lower) == 1:
            unique_words.append(word)
    
  return unique_words

sentence = str(input("Введіть речення: "))
unique_words = find_non_repeat_words(sentence)

print("Слова, які зустрічаються тільки один раз:")
for word in unique_words:
    print(word)
