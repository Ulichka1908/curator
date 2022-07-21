#19
from functools import*


def shag(h):
    a, b, c = h
    if c == 'ivleeva':
        return (a + 6, b, 'instasamka'), (a * 2, b, 'instasamka')
    if c == 'instasamka':
        return (a, b + 6, 'ivleeva'), (a, b * 2, 'ivleeva')


@lru_cache(None)
def igra(h):
    a, b, c = h
    if a + b >= 100:
        return 'pobeda'
    if any(igra(i) == 'pobeda' for i in shag(h)):
        return 'ivleeva1'
    if all(igra(i) == 'ivleeva1' for i in shag(h)):
        return 'instasamka1'
    if any(igra(i) == 'instasamka1' for i in shag(h)):
        return 'ivleeva2'
    if all(igra(i) == 'ivleeva1' or igra(i) == 'ivleeva2' for i in shag(h)):
        return 'instasamka1/2'


otvet = []
for s in range(1, 100):
    h = 17, s, 'ivleeva'
    if igra(h) == 'instasamka1':
        otvet.append(s)
print(min(otvet), max(otvet))
