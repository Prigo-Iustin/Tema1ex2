import string

def citeste_fisier(nume_fisier):
    with open(nume_fisier, 'r') as f:
        return f.read()

def elimina_punctuatie(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def transforma_lowercase(text):
    return text.lower()

text = citeste_fisier('input.txt')
text_procesat = elimina_punctuatie(text)
text_procesat = transforma_lowercase(text_procesat)