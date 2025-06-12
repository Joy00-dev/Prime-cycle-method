import math

def genera_sequenza(limit):
    finali = [7, 1, 3, 7, 9, 3, 9, 1]
    candidati = []
    i = 0
    n = 7
    while n <= limit:
        if int(str(n)[-1]) == finali[i % len(finali)]:
            candidati.append(n)
            i += 1
        n += 2  # salto i pari perché non primi (tranne 2)
    return candidati

def is_primo(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def filtra_primi(lista):
    return [n for n in lista if is_primo(n)]

def main():
    limite = 10000  # Modifica qui il limite massimo
    print(f"Generazione numeri fino a {limite} con sequenza...")
    candidati = genera_sequenza(limite)
    print(f"Numeri candidati generati: {len(candidati)}")
    
    primi = filtra_primi(candidati)
    print(f"Numeri primi trovati: {len(primi)}")
    print(primi)

if __name__ == "__main__":
    main()
