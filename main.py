import string

def citeste_fisier(nume_fisier):
    with open(nume_fisier, 'r') as f:
        return f.read()

def elimina_punctuatie(text):
    return text.translate(str.maketrans('', '', string.punctuation))

text = citeste_fisier('input.txt')
text_procesat = elimina_punctuatie(text)