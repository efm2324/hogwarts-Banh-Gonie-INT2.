def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def ask_number(message, min_value=None, max_value=None):
    courage_lv = int(input(message))
    while courage_lv < min_value or courage_lv > max_value:
        print(f"Please enter a number between {min_value} and {max_value}.")
        courage_lv = int(input(message))
    return courage_lv

def ask_choice(message, option):
    print(message)
    for i, option in enumerate(option, start=1):
        print(f"{i}. {option}")

    choice = ask_number("Your choice: ", 1, len(option))
    return option[choice - 1]

ask_choice("dotou want to continue?", ["yes", "no"])