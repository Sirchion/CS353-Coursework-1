import import_file
import sys
import re

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
            option_2()
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


def option_2():
    global drama_file_path, drama_info

    if not drama_info:
        print("No drama has been imported yet. Please import a file first.")
        return

    text = "\n".join(drama_info) if isinstance(drama_info, list) else str(drama_info)
    num_acts = scene_act_counter(text, "act")
    print("Number of acts: " + str(num_acts))

    num_scenes = scene_act_counter(text, "scene")
    print("Number of scenes: " + str(num_scenes))



def scene_act_counter(text, word):
    lines = text if isinstance(text, list) else text.splitlines()

    collecting = False
    count = 0

    for line in lines:
        lower_line = line.lower().strip()

        if not collecting and "contents" in lower_line:
            collecting = True
            continue

        if collecting and ("dramatis personæ" in lower_line or "dramatis personae" in lower_line):
            break

        if collecting and lower_line.startswith(word):
            count += 1

    return count



if __name__ == "__main__":
    main()