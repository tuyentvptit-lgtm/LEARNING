def capitalize_words(sentence: str) -> str:
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

input_sentence = input()
output_sentence = capitalize_words(input_sentence)
print(output_sentence)