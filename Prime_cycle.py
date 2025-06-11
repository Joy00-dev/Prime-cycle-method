# prime_cycle.py

# This script generates prime candidates based on a final-digit cycle
# and eliminates false positives that are products of other primes.

def generate_candidates(limit):
    cycle = [7, 1, 3, 7, 9, 3, 9, 1]
    candidates = []
    num = 0
    i = 0
    while num < limit:
        num += 1
        if int(str(num)[-1]) == cycle[i % len(cycle)]:
            candidates.append(num)
            i += 1
    return candidates

def remove_false_positives(candidates):
    cleaned = candidates[:]
    for a in candidates:
        for b in candidates:
            prod = a * b
            if prod in cleaned:
                cleaned.remove(prod)
    return cleaned

if __name__ == "__main__":
    limit = 200
    raw = generate_candidates(limit)
    primes = remove_false_positives(raw)
    print("Filtered primes:", primes)
