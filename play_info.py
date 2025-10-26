import re
from collections import Counter



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

def character_names(text, character_dict):
    lines = text if isinstance(text, list) else text.splitlines()

    collecting = False

    for line in lines:

        if not collecting and ("dramatis personæ" in line.lower() or "dramatis personae" in line.lower()):
            collecting = True
            continue

        if collecting and ("act i" in line.lower() or "act i" in line.lower()):
            break

        if collecting and line:
            clean_line = line.split(",", 1)[0].strip()
            if "CHORUS." in clean_line or "THE PROLOGUE" in clean_line:
                continue

            if clean_line.isupper():
                character_dict[clean_line] = {"full_title": line, "words_spoken": 0}


def top_spoken_words(text):
    lines = text if isinstance(text, list) else text.splitlines()
    character_name = re.compile(r"^[A-Z][A-Z .,'’\-]+\. *$")

    token_words = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")

    counts = Counter()
    collecting = False
    talking = False

    for line in lines:

        if not collecting and character_name.match(line):
            collecting = True
            talking = True
            continue

        if not talking:
            continue

        if collecting and ("*** END " in line):
            break

        if collecting and line and include_line(line):
            clean_line = re.sub(r"\[.*?", "", line)
            tokens = token_words.findall(clean_line)
            counts.update(word.lower() for word in tokens)

    return counts.most_common(20)

def include_line(line):
    act_scene = re.compile(r"^\s*(ACT|SCENE)\b", re.IGNORECASE)
    character_name = re.compile(r"^[A-Z][A-Z .,'’\-]+\. *$")

    if act_scene.match(line):
        return False

    if character_name.match(line):
        return False

    return True