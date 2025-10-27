import sys

import import_file
import play_info
import act_info
import scene_info

# Global variables
drama_file_path = ""
drama_info = ""
character_dict = {}

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
            option_3()

        elif choice == "4":
            option_4()

        elif choice == "5":
            option_5()
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
    global drama_file_path, drama_info, character_dict

    character_dict.clear()

    if not drama_info:
        print("No drama has been imported yet. Please import a file first.")
        return

    print("\nPrinting summary report...")

    text = "\n".join(drama_info) if isinstance(drama_info, list) else str(drama_info)
    num_acts = play_info.scene_act_counter(text, "act")
    print("Number of acts: " + str(num_acts))

    num_scenes = play_info.scene_act_counter(text, "scene")
    print("Number of scenes: " + str(num_scenes))

    play_info.character_names(text, character_dict)
    print("\nCharacter names:")
    name_counter = 1
    for name, info in character_dict.items():
        print(str(name_counter) + ". " + info["full_title"])
        name_counter += 1

    top_20 = play_info.top_spoken_words(text)
    print("\nTop 20 words:")
    word_counter = 1
    for word, count in top_20:
        print(str(word_counter) + ". " + word + ": " + str(count))
        word_counter += 1

    print("\nPress Enter to go back to main menu.")
    input()

def option_3():
    global drama_file_path, drama_info, character_dict

    character_dict.clear()

    lines = []

    if not drama_info:
        print("No drama has been imported yet. Please import a file first.")
        return

    lines.append("Report of " + str(drama_file_path))

    text = "\n".join(drama_info) if isinstance(drama_info, list) else str(drama_info)
    num_acts = play_info.scene_act_counter(text, "act")
    lines.append("\nNumber of acts: " + str(num_acts))

    num_scenes = play_info.scene_act_counter(text, "scene")
    lines.append("\nNumber of scenes: " + str(num_scenes))

    play_info.character_names(text, character_dict)
    lines.append("\nCharacter names:")
    name_counter = 1
    for name, info in character_dict.items():
        lines.append(str(name_counter) + ". " + info["full_title"])
        name_counter += 1

    top_20 = play_info.top_spoken_words(text)
    lines.append("\nTop 20 words:")
    word_counter = 1
    for word, count in top_20:
        lines.append(str(word_counter) + ". " + word + ": " + str(count))
        word_counter += 1

    with open("summary_drama.txt", "w") as drama_summary:
        drama_summary.write("\n".join(lines))

    print("\nFile successfully created")
    print("\nPress Enter to go back to main menu.")
    input()

def option_4():
    global drama_file_path, drama_info, character_dict

    if not drama_info:
        print("No drama has been imported yet. Please import a file first.")
        return

    text = "\n".join(drama_info) if isinstance(drama_info, list) else str(drama_info)
    print("\nSummary report of act")
    num_acts = play_info.scene_act_counter(text, "act")

    while True:
        act_number = input("\nEnter the act number: ")

        if act_number.isdigit():
            act_number_int = int(act_number)
            if act_number_int <= num_acts:
                act_number = act_number_int
                break
            else:
                print("\nInvalid act number. Please try again.")
        else:
            print("\nInvalid input. Please enter a number.")


    num_words = act_info.number_of_words(drama_info, act_number)
    print("Number of words: " + str(num_words))

    num_utterances = act_info.number_utterances(drama_info, act_number)
    print("Number of utterances: " + str(num_utterances))

    character_most_spoken = act_info.character_spoke_count(text, act_number)
    print("\nCharacter who speaks the most: " + str(character_most_spoken))

    character_least_spoken = act_info.character_spoke_least(drama_info, act_number)
    print("Character who speaks the least: " + str(character_least_spoken))

    store_name_of_scenes = act_info.name_of_scenes(text, act_number)
    scene_counter = 1
    print("\nNumber of scenes: ")
    for scene in store_name_of_scenes:
        print(str(scene_counter) + ": " + scene)
        scene_counter += 1

    print("\nPress Enter to go back to main menu.")
    input()

def option_5():
    global drama_file_path, drama_info, character_dict

    if not drama_info:
        print("No drama has been imported yet. Please import a file first.")
        return

    text = "\n".join(drama_info) if isinstance(drama_info, list) else str(drama_info)
    print("\nSummary report of scene")


    num_acts = play_info.scene_act_counter(text, "act")

    while True:
        act_number = input("\nEnter the act number: ")

        if act_number.isdigit():
            act_number_int = int(act_number)
            if act_number_int <= num_acts:
                act_number = act_number_int
                break
            else:
                print("\nInvalid act number. Please try again.")
        else:
            print("\nInvalid input. Please enter a number.")

    num_scenes = act_info.name_of_scenes(text, act_number)

    while True:
        scene_number = input("\nEnter the scene number: ")

        if scene_number.isdigit():
            scene_number_int = int(scene_number)
            if scene_number_int <= len(num_scenes):
                scene_number = scene_number_int
                break
            else:
                print("\nInvalid scene number. Please try again.")
        else:
            print("\nInvalid input. Please enter a number.")

    while True:
        search_phrase = input("\nEnter phrase: ").strip()
        if search_phrase:
            break
        else:
            print("Invalid input. Please enter a phrase.")

    count_phrase = scene_info.phrase_counter(text, act_number, scene_number, search_phrase)
    print("Found: " + str(count_phrase)  + " occurrences:")
    phrase = scene_info.phrase_list(text, act_number, scene_number, search_phrase)
    phrase_counter = 1
    for name in phrase:
        print(str(phrase_counter) + ". " + name)
        phrase_counter += 1

    while True:
        character_name = input("\nEnter character name: ").strip()
        if character_name:
            break
        else:
            print("Invalid input. Please enter a phrase.")


    print("\nPress Enter to go back to main menu.")
    input()

if __name__ == "__main__":
    main()