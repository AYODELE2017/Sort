def is_isogram(word):
    if isinstance(word, str):
        if word == '' or ' ' or " " or "":
            return word, False
        else:
            if len(word) == len(set(word)):
                return word, True
            return word, False
    else:
        raise TypeError('Argument should be a string')
print(is_isogram("abolishment"))
print(is_isogram("alphabet"))
print(is_isogram(" "))
print(is_isogram(2))