import hashlib

class TrivialHash:
    def __init__(self):
        pass

    def weak_hash(self, data: str) -> str:
        """Insecure hashing using character sum and SHA-1."""
        char_sum = sum(ord(c) for c in data)  # Predictable sum of characters
        return hashlib.sha1(str(char_sum).encode()).hexdigest()

if __name__ == "__main__":
    weak_hasher = TrivialHash()
    message = "Sensitive Data"
    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))