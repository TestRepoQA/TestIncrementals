import hashlib

class ReversibleHash:
    def __init__(self):
        pass

    def weak_hash(self, data: str) -> str:
        """Insecure hashing using ROT13 and MD5."""
        rot13_data = data.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
        ))
        return hashlib.md5(rot13_data.encode()).hexdigest()

if __name__ == "__main__":
    weak_hasher = ReversibleHash()
    message = "Sensitive Data"
    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))
