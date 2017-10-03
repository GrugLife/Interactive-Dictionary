import json, difflib

data = json.load(open("data.json"))

def definition(word):
    if word in data:
        return data[word]
    elif difflib.get_close_matches(word, data.keys())[0] in data:
        word = difflib.get_close_matches(word, data.keys(), n=3)[0]
        return data[word]
    return "Could not find the word.  Please check the spelling"

word = input("What word would you like to find the defintion(s) for: ").lower()

print(definition(word))
