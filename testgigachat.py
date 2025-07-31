poem = """

"""

def parse_poem(poem):
    res = {}
    animal = None
    for line in poem.split('\n'):
        if not line:
            continue

        if animal is None:
            animal = line.split(' ')[0]
        elif line.startswith('-'):
            phrase = (line.replace('-', '').replace('!', '').split(',')[0].strip())
            res[animal] = phrase
            animal = None
    return res


