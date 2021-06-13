def joinWords(words):
    sentence = ""
    for w in words:
        sentence = sentence + w
    return sentence

words = ["i", "eat", "three", "meals", "a", "day"]
a = joinWords(words)
print(a)
