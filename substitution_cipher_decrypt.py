
from collections import Counter

ciphertext = (
    "jgrmqoyghmvbj wrwqfpw hgf fdqgfpfzr kbeebjizq qo cibzk. "
    "lfafgqvfzfww, eog wopf gfhwol phlr lolfdmfgqw blwbwq ol "
    "kfwbylbly lfs fljgrmqbol wjvfpfw qvhq wffp qo qvfp qo cf "
    "pogf wfjigf qvhl hlr oqvfg wjvfpf ol fhgqv. qvf ileogqilhqf "
    "qgiqv vosfafg bw qvhq wijv wjvfpfw hgf iwihzzr qgbabhz qo cgfhx."
)


substitution_map = {
    'a': 'v', 'b': 'i', 'c': 'b', 'd': 'x', 'e': 'f', 'f': 'e', 'g': 'r',
    'h': 'a', 'i': 'u', 'j': 'c', 'k': 'd', 'l': 'n', 'm': 'p', 'o': 'o',
    'p': 'm', 'q': 't', 'r': 'y', 's': 'w', 'v': 'h', 'w': 's', 'x': 'k',
    'y': 'g', 'z': 'l',
}


def decrypt_substitution(text: str, mapping: dict) -> str:
    """Replace every cipher letter with its mapped plaintext letter,
    preserving case, spacing and punctuation."""
    result = []
    for ch in text:
        if ch.isalpha():
            lower = ch.lower()
            plain = mapping.get(lower, lower)  # unmapped letters pass through
            result.append(plain.upper() if ch.isupper() else plain)
        else:
            result.append(ch)
    return "".join(result)


def letter_frequency(text: str) -> Counter:
    """Count how often each letter appears in the ciphertext -
    this is the FIRST clue Proma used (E and T are usually the most
    frequent letters in English, so the most common cipher letters
    are likely to map to them)."""
    letters = [c.lower() for c in text if c.isalpha()]
    return Counter(letters)


if __name__ == "__main__":
    print("=== Step 1: Letter Frequency Analysis ===")
    freq = letter_frequency(ciphertext)
    for letter, count in freq.most_common():
        print(f"  '{letter}' -> {count} times")

    print("\n=== Step 2: Recovered Plaintext ===")
    plaintext = decrypt_substitution(ciphertext, substitution_map)
    print(plaintext)