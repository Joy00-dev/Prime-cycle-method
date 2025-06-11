def genera_candidati(limit):
    finali = [7, 1, 3, 7, 9, 3, 9, 1]
    candidati = []
    n = 7
    i = 0
    while n <= limit:
        if int(str(n)[-1]) == finali[i % len(finali)]:
            candidati.append(n)
            i += 1
        n += 2
    return candidati

def elimina_falsi(candidati, limit):
    falsi = set()
    for i in range(len(candidati)):
        for j in range(i, len(candidati)):
            prod = candidati[i] * candidati[j]
            if prod <= limit:
                falsi.add(prod)
    return [n for n in candidati if n not in falsi]

def trova_primi(limit):
    candidati = genera_candidati(limit)
    return elimina_falsi(candidati, limit)

# Esempio d’uso
if __name__ == "__main__":
    print(trova_primi(34200))
