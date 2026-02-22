import string
import re

def citeste_fisier(nume_fisier):
    with open(nume_fisier, 'r') as f:
        return f.read()

def elimina_punctuatie(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def transforma_lowercase(text):
    return text.lower()

def elimina_spatii_multiple(text):
    return re.sub(r'\s+', ' ', text).strip()

# Fluxul de executie
text = citeste_fisier('input.txt')
text_procesat = elimina_punctuatie(text)
text_procesat = transforma_lowercase(text_procesat)
text_final = elimina_spatii_multiple(text_procesat)

# Afisare la consola
print(text_final)