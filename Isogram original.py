def is_isogram(word):
    if word == " " or "":
        return word, False
    if isinstance(word, str):
        w = word
        return word, len(w) == len(set(w)) if word else False
    return TypeError("Argument should be a string")
print(is_isogram("abolishment"))
print(is_isogram("alphabet"))
print(is_isogram(" "))
print(is_isogram(2))
