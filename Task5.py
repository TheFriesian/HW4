import string

text = "This is some text.here are sentences! and different punctuations signs? and also digits 284."

sentences = text.split('. ')
capitalized_sentences = [sentence.capitalize() for sentence in sentences]
capitalized_text = '. '.join(capitalized_sentences)

digits_count = sum(char.isdigit() for char in text)

punctuation_count = sum(char in string.punctuation for char in text)

exclamation_count = text.count('!')

print("Capitalized text:", capitalized_text)
print("Digits count:", digits_count)
print("Count punctuation signs:", punctuation_count)
print("Count exclamation signs:", exclamation_count)
