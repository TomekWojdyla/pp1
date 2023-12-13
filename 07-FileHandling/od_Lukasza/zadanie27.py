import re

text = "To be, or not to be, that is the question"


# slowa = re.findall(" ", text)
# nie oddaje liczby slow, tylko liczbe spacji, a przy przecinku sie to psuje
# trzeba skorzystac z "\S+"

slowa = re.findall('\S+', text)

print(len(slowa))