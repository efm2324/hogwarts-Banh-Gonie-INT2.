import sys
from pathlib import Path

# Add the parent directory to sys.path so we can import utils (doesn't work without this)
sys.path.insert(0, str(Path(__file__).parent.parent))

from universe.character import init_character, display_character

def introduction():
    print(".")

def create_character():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    attributes = {
        "Courage": int(input("Enter your Courage level (1-10): ")),
        "Intelligence": int(input("Enter your Intelligence level (1-10): ")),
        "Loyalty": int(input("Enter your Loyalty level (1-10): ")),
        "Ambition": int(input("Enter your Ambition level (1-10): "))
    }
    character = init_character(last_name, first_name, attributes)
    display_character(character)
    return character
    