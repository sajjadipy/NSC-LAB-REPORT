
import hashlib


def sha256_hash(message: str) -> str:
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def hex_to_bin(hex_str: str) -> str:
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def count_bit_difference(hash1: str, hash2: str) -> int:
    bin1, bin2 = hex_to_bin(hash1), hex_to_bin(hash2)
    return sum(b1 != b2 for b1, b2 in zip(bin1, bin2))


if __name__ == "__main__":
    original_message = "Byte Sentinels: Release notes v1.0 - build passed"

    hash1 = sha256_hash(original_message)
    hash2 = sha256_hash(original_message)

    print("Original Message :", original_message)
    print("Hash #1          :", hash1)
    print("Hash #2 (recheck):", hash2)
    print("Hashes Match?    :", hash1 == hash2)
    print()

    modified_message = "Byte Sentinels: Release notes v1.1 - build passed"
    hash_modified = sha256_hash(modified_message)

    print("Modified Message :", modified_message)
    print("Modified Hash    :", hash_modified)
    print()

    diff_bits = count_bit_difference(hash1, hash_modified)
    total_bits = len(hash1) * 4
    print(f"Bits changed: {diff_bits} / {total_bits} "
          f"({diff_bits / total_bits * 100:.2f}% of the hash changed)")
    print("This demonstrates the AVALANCHE EFFECT: changing just ONE")
    print("character in the input completely and unpredictably changes")
    print("the SHA-256 output, which is exactly what makes hashing")
    print("reliable for detecting tampering.")