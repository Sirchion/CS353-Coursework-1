import re
from collections import Counter
import roman

def number_of_words(text, act_number):
    lines = text if isinstance(text, list) else text.splitlines()

    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman


    act_number2_roman = roman.toRoman(int(int(act_number) + 1)).lower()
    next_act = "act " + act_number2_roman

    token_words = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")

    counts = Counter()

    found_dramatis = False
    collecting = False

    for line in lines:

        lower_line = line.lower().strip()

        if not found_dramatis:
            if "dramatis personæ" in lower_line or "dramatis personae" in lower_line:
                found_dramatis = True
            continue

        if not collecting and lower_line.startswith(full_act):
            collecting = True
            continue

        if collecting and lower_line.startswith(next_act):
            break

        if not collecting:
            continue

        if not include_line(line):
            continue

        clean_line = re.sub(r"\[.*?|\(.*?\)", "", line)
        tokens = token_words.findall(clean_line)
        counts.update(word.lower() for word in tokens)

    return sum(counts.values())

def number_utterances(text, act_number):
    lines = text if isinstance(text, list) else text.splitlines()
    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman

    act_number2_roman = roman.toRoman(int(int(act_number) + 1)).lower()
    next_act = "act " + act_number2_roman

    number_utterances_counter = 0

    found_dramatis = False
    collecting = False

    character_name = re.compile(r"^[A-Z][A-Z .,'’\-]+\. *$")

    for line in lines:

        if not found_dramatis:
            if "dramatis personæ" in line.lower() or "dramatis personae" in line.lower():
                found_dramatis = True
            continue

        if not collecting and line.lower().startswith(full_act):
            collecting = True
            continue

        if collecting and line.lower().startswith(next_act):
            break

        if not collecting:
            continue


        if character_name.match(line.strip()):
            print(line.strip())
            number_utterances_counter += 1

    return number_utterances_counter



def include_line(line):
    act_scene = re.compile(r"^\s*(ACT|SCENE)\b", re.IGNORECASE)
    character_name = re.compile(r"^[A-Z][A-Z .,'’\-]+\. *$")

    if act_scene.match(line):
        return False

    if character_name.match(line):
        return False

    return True