#2. Користувач вводить з клавіатури рядок та символ для пошуку.
#Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.


user_input = input("Enter a record: ")

symbol_to_search = input("Enter a symbol to search: ")

if len(symbol_to_search) != 1:
    print("Please, enter only one symbol")
else:
    count = user_input.count(symbol_to_search)

print("Symbol '{}' was found {} time(s) in the record.".format(symbol_to_search, count))