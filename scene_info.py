import re
import roman

def phrase_counter(text, act_number, scene_number, phrase):
    lines = text if isinstance(text, list) else text.splitlines()
    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman

    scene_number_roman = roman.toRoman(int(scene_number)).lower()
    full_scene = "scene " + scene_number_roman

    scene_number2_roman = roman.toRoman(int(scene_number + 1)).lower()
    next_scene = "scene " + scene_number2_roman


    found_dramatis = False
    found_act = False
    collecting = False

    phrase_counter_scene = 0

    for line in lines:

        if not found_dramatis:
            if "dramatis personæ" in line.lower() or "dramatis personae" in line.lower():
                found_dramatis = True
            continue

        if not found_act and line.lower().startswith(full_act):
            found_act = True
            continue

        if not collecting and line.lower().startswith(full_scene):
            collecting = True
            continue

        if  found_act and collecting and line.lower().startswith(next_scene):
            break

        if not collecting:
            continue

        if phrase in line.lower():
            phrase_counter_scene += 1

    return phrase_counter_scene

def phrase_list(text, act_number, scene_number, phrase):
    lines = text if isinstance(text, list) else text.splitlines()
    act_number_roman = roman.toRoman(int(act_number)).lower()
    full_act = "act " + act_number_roman

    scene_number_roman = roman.toRoman(int(scene_number)).lower()
    full_scene = "scene " + scene_number_roman

    scene_number2_roman = roman.toRoman(int(scene_number + 1)).lower()
    next_scene = "scene " + scene_number2_roman

    results = []
    found_dramatis = False
    found_act = False
    collecting = False

    for line in lines:

        if not found_dramatis:
            if "dramatis personæ" in line.lower() or "dramatis personae" in line.lower():
                found_dramatis = True
            continue

        if not found_act and line.lower().startswith(full_act):
            found_act = True
            continue

        if not collecting and line.lower().startswith(full_scene):
            collecting = True
            continue

        if  found_act and collecting and line.lower().startswith(next_scene):
            break

        if not collecting:
            continue

        if re.search(rf"\b{re.escape(phrase)}\b", line, re.IGNORECASE):
            results.append(line)

    return results