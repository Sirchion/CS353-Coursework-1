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
            number_utterances_counter += 1

    return number_utterances_counter

def character_spoke_count(text, act_number):
    lines = text if isinstance(text, list) else text.splitlines()
    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman

    act_number2_roman = roman.toRoman(int(int(act_number) + 1)).lower()
    next_act = "act " + act_number2_roman

    counts = {}
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
            name = line.strip().rstrip(".")
            if name in counts:
                counts[name] += 1
            else:
                counts[name] = 1

    most_spoken = ""
    most_spoken_count = 0
    for name, count in counts.items():
        if count > most_spoken_count:
            most_spoken = name
            most_spoken_count = count

    return most_spoken


def character_spoke_least(text, act_number):
    lines = text if isinstance(text, list) else text.splitlines()
    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman

    act_number2_roman = roman.toRoman(int(act_number) + 1).lower()
    next_act = "act " + act_number2_roman

    counts = {}
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
            name = line.strip().rstrip(".")
            if name in counts:
                counts[name] += 1
            else:
                counts[name] = 1

    least_spoken = ""
    least_spoken_count = float('inf')
    for name, count in counts.items():
        if count < least_spoken_count:
            least_spoken = name
            least_spoken_count = count

    return least_spoken

def name_of_scenes(text, act_number):
    lines = text if isinstance(text, list) else text.splitlines()
    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman

    act_number2_roman = roman.toRoman(int(act_number) + 1).lower()
    next_act = "act " + act_number2_roman

    store_name_of_scenes = []
    found_dramatis = False
    collecting = False

    scene_re = re.compile(r"^SCENE\s+[IVXLCDM]+\.\s+.+$", re.IGNORECASE)

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

        if scene_re.match(line.strip()):
            store_name_of_scenes.append(line.strip())

    return store_name_of_scenes


def include_line(line):
    act_scene = re.compile(r"^\s*(ACT|SCENE)\b", re.IGNORECASE)
    character_name = re.compile(r"^[A-Z][A-Z .,'’\-]+\. *$")

    if act_scene.match(line):
        return False

    if character_name.match(line):
        return False

    return True