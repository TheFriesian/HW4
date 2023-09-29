# Keep prompting the user for input until a non-empty string is entered
while True:
    user_input = input("Please enter your string: ")

    if len(user_input) > 0:
        break
    else:
        print("You have entered an empty string. Please enter a valid string.")

print("Third character:", user_input[2])

print("Penultimate character:", user_input[-2])

print("First five characters:", user_input[:5])

print("All characters except the last two:", user_input[:-2])

print("Characters with even indexes:", user_input[::2])

print("Characters with odd indexes:", user_input[1::2])

print("All characters in reverse order:", user_input[::-1])

print("Every second character in reverse order:", user_input[::-2])

print("Length of the string:", len(user_input))
