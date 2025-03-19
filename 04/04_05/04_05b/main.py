def has_unique_characters(data):
    character_list = str(data).split()
    character_set = set([character_list])
    if len(character_list) != len(character_set):
        return True
    return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
