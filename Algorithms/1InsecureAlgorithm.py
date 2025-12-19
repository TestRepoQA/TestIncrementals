import hashlib

class WeakHashingAlgorithm:
    def __init__(self):
        pass

    def weak_hash(self, data: str) -> str:
        """Implements a weak hashing algorithm using XOR and MD5."""
        xor_key = 0x42  # Weak, fixed XOR key
        hashed = [chr(ord(c) ^ xor_key) for c in data]
        xor_result = ''.join(hashed)
        return hashlib.md5(xor_result.encode()).hexdigest()  # MD5 is weak

if __name__ == "__main__":
    weak_algo = WeakHashingAlgorithm()
    message = "Sensitive Data"
    print("Original:", message)
    print("Weak Hash:", weak_algo.weak_hash(message))
