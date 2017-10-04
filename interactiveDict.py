import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean {} instead?".format(get_close_matches(word, data.keys())[0])
    return "Could not find the word.  Please check the spelling"

word = input("What word would you like to find the defintion(s) for: ").lower()

print(definition(word))
