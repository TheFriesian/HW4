'''
3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
'''

user_input = input("Please enter your string: ")

search_word = input("Please enter the word to search for: ")

replace_word = input("Please enter the word to replace it with: ")

modified_string = user_input.replace(search_word, replace_word)

print("The modified string is:", modified_string)
