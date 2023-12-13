import re


text = "To be, or not to be, that is the question"
vowels = re.findall("[aoeuiy]", text)
print(vowels)
print(f"Liczba samogłosek w tym tekście: {len(vowels)}")