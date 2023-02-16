some_text = input().split()
even_length_word = [word for word in some_text if len(word) % 2 == 0]
for word in even_length_word:
    print(word)