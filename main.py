def citeste_fisier(nume_fisier):
    with open(nume_fisier, 'r') as f:
        return f.read()

text = citeste_fisier('input.txt')