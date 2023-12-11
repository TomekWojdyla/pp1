# 13.	A program contains any defined dictionary, with any number of key-value pairs of information. Write a program that displays the number of pairs of information available in the dictionary.

movie = {
    "title":"Everest",
    "year": 2015,
    "director": "Baltasar Kormákur",
    "length": "140min",
    "actors":["Jason Clarke","Jake Gyllenhaal", "Emily Watson"],
}


for key,value in movie.items():
    print(f"{key}: {value}")
    
    