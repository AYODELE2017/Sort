def remove_duplicates(string):
    if isinstance(string, int):
        return TypeError
    else:
        k = set(string)
        x = len(string) - len(set(string))
        return ''.join(sorted(k)), x
print(remove_duplicates("thelexash"))



