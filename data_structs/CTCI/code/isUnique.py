def isUnique(words):
    n = set()
    for char in words:
        n.add(char)
    if len(n) == len(words):
        return True
    else:
        return False

# words = "potatoe" # returns False
words = "keyboard" # returns True
a = isUnique(words)
print(a)


def isUniqueArray(words):
    n = []
    for char in words:
        if char not in n:
            n.append(char)
    if len(n) == len(words):
        return True
    else:
        return False

wordsArray = "keyboard"
b = isUniqueArray(wordsArray)
print(b)
