def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        chars = char.lower()
        if chars in characters:
            characters[chars] += 1
        else:
            characters[chars] = 1
    return characters

def sort_characters(char_counts):
    items = list(char_counts.items())
    items.sort(reverse=True, key=get_count)
    return items

def get_count(item):
    return item[1]