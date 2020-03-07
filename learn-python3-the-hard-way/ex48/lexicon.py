def scan(input):
    words = input.split()
    result = []
    for word in words:
        if word in ["north", "south", "west", "east"]:
            result.append(('direction', word))
        elif word in ["go", "kill", "eat"]:
            result.append(('verb', word))
        elif word in ["the", "in", "of"]:
            result.append(('stop', word))
        elif word in ["bear", "princess"]:
            result.append(('noun', word))
        elif convert_number(word):
            result.append(('number', convert_number(word)))
        else:
            result.append(('error', word))

    return result


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
