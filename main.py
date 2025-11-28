
from utils.input_utils import ask_text

def main():
    name = ask_text("Please enter your name: ")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
