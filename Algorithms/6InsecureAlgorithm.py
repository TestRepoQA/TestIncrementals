import hashlib
import random

class PredictableHash:
    def __init__(self):
        pass

    def weak_hash(self, data: str) -> str:
        """Insecure hashing using a predictable XOR operation and SHA-1."""
        xor_key = random.randint(0, 255)  # Weak and predictable key
        hashed = ''.join(chr(ord(c) ^ xor_key) for c in data)
        return hashlib.sha1(hashed.encode()).hexdigest()

if __name__ == "__main__":
    weak_hasher = PredictableHash()
    message = "Sensitive Data"
    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))
