import import_file
import sys

# Global variables
drama_file_path = ""
drama_info = ""

def menu_options():
    print("\nSelect an option:")
    print("1. Import a drama from a text file.")
    print("2. Print a summary report.")
    print("3. Output the summary report to a text file.")
    print("4. View details of drama act.")
    print("5. Search inside a drama scene.")
    print("6. Exit\n")


def main():
    print("Drama Analysis System")

    while True:
        menu_options()
        choice = input("Enter your choice (1–6): ").strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        if choice == "1":
            option_1()

        elif choice == "2":
            print("Printing a summary report...")
        elif choice == "3":
            print("Outputting the summary report to a text file...")
        elif choice == "4":
            print("Viewing details of drama act...")
        elif choice == "5":
            print("Searching inside a drama scene...")
        elif choice == "6":
            print("\nThank you, the program will now exit.")
            sys.exit()
        else:
            print("\n Invalid choice. Please enter a number between 1 and 6.")


def option_1():
    global drama_file_path, drama_info

    print("Importing a drama from a text file...")
    path = import_file.check_file_path()

    if path:
        drama_file_path = path
        drama_info = import_file.read_file_contents(drama_file_path)

    if drama_info:
        print("Successfully imported drama from text file: " + drama_file_path.as_posix())
    else:
        print("File was empty or could not be read: " + drama_file_path.as_posix())

if __name__ == "__main__":
    main()