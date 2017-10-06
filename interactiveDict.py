import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead? Y/N: ".format(get_close_matches(word, data.keys())[0]))
        
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does note exist.  Please check the spelling"
        else:
            return "We didn't understand your entry"

    return "Could not find the word.  Please check the spelling"

word = input("What word would you like to find the defintion(s) for: ").lower()

output = definition(word)

if type(output) == list:
    for item in output:
         print(item)
else:
    print(output)
