def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def ask_number(message, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number >= {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Please enter a number <= {max_value}.")
            continue
        return value
    


    
    
    
    courage_lv = int(input(message))
    while courage_lv < min_value or courage_lv > max_value:
        print(f"Please enter a number between {min_value} and {max_value}.")
        courage_lv = int(input(message))
    return courage_lv

    

if __name__ == "__main__":
    # demo / manual test only — won't run on import
    lvl = ask_number("Enter courage level (1-10): ", 1, 10)
    print(f"Courage level set to {lvl}")