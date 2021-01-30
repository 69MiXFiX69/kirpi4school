fucking = "Fucking, fuck, fucker, fucked, Kirpi4"
for x in range(5):
    try:
        word = fucking[:fucking.index(',')+1]
        fucking = fucking[fucking.index(',')+1:]
        print(word)
    except ValueError:
        print(fucking)