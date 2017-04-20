def is_isogram(word):
    if isinstance(word, str):
        if word == " " or "":
            return word, False
        w = word
        return word, len(w) == len(set(w)) if word else False
    else:
        raise TypeError("Argument should be a string")
print(is_isogram("abolishment"))
print(is_isogram("alphabet"))
print(is_isogram(" "))
print(is_isogram(2))