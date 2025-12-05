def count_words(text):
    return len(text.split())
    
def count_characters(text):
    character_counts = {}
    for character in text:
        character_as_lower = character.lower()
        if character_as_lower in character_counts:
            character_counts[character_as_lower] += 1
        else:
            character_counts[character_as_lower] = 1
    
    return character_counts
    
def sort_on(items):
    return items["num"]
    
def sort_character_counts(character_counts):
    unsorted_list = []
    for key in character_counts:
        unsorted_list.append({"char": key, "num": character_counts[key]})
    
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list