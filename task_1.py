# 1. Користувач вводить рядок з клавіатури.
# Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)

user_input=input('Please enter your record: ')

letters_count = 0
digits_count = 0
others_count = 0

for char in user_input:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
    else:
        others_count += 1
    
print("There are ", letters_count, " letters in the input string")
print("There are ", digits_count, " digits in the input string")
print("There are ", others_count, " unrecognizable values")