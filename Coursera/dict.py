sally = "sally sells sea shells by the sea shore"
characters = {}
for l in sally:
    if l in characters.keys():
        characters[l] += 1
    else:
        characters[l] = 1




list(characters.values()).index(max(characters.values()))

list(characters.keys())[0]

best_char = characters.keys()[characters.values().index(max(characters.values()))]

[1, 2, 3][1]
