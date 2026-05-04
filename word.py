def count_words(sentence):
    return len(sentence.split())

text = input("Enter a sentence: ")
print("Word count:", count_words(text))
