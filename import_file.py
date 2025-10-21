import sys
from pathlib import Path

def check_file_path():

    drama_file_path = Path()

    while True:
        print("Enter exit to quit")
        print("Enter back to return to main menu")
        drama_file_path_holder = input("Enter path to drama file (.txt only): ").strip()

        if drama_file_path_holder == "exit":
            print("\nThank you, the program will now exit.")
            sys.exit()

        if drama_file_path_holder == "back":
            print("\nThank you, the program will now return to menu.")
            break
        if not drama_file_path_holder:
            print("Please enter a valid path.")
            return None

        drama_file_path = Path(drama_file_path_holder)

        if drama_file_path.suffix.lower() != ".txt":
            print("Only .txt files are supported.")
            continue

        if not drama_file_path.exists():
            print("File not found: " + drama_file_path.as_posix())
            continue

        print("File found: " + drama_file_path.as_posix())
        break
    return drama_file_path

def read_file_contents(file_path: Path):
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
        return content
    except Exception as e:
        print(" Error reading file: " + e)
        return ""