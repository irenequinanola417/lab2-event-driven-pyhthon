print("Welcome to Lab 2 Event-Driven App")

import json
import os

# Load config from the same folder as main.py
def load_config():
    folder = os.path.dirname(os.path.realpath(__file__))  # folder where main.py is
    config_path = os.path.join(folder, "config.json")
    with open(config_path, "r") as file:
        return json.load(file)

def show_menu():
    print("\n=== Main Menu ===")
    print("1. Show App Name")
    print("2. Show Version")
    print("3. Exit")

def main():
    config = load_config()

    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()
        choice = choice.replace(".", "")

        if choice == "1":
            print("App Name:", config.get("app_name", "Unknown"))
        elif choice == "2":
            print("Version:", config.get("version", "Unknown"))
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    print("Welcome to Lab 2 Event-Driven App")
    main()