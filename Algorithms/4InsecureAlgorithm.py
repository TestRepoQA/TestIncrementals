import hashlib

class WeakChecksum:
    def __init__(self):
        pass

    def checksum(self, data: str) -> int:
        """Weak checksum using simple character sum."""
        return sum(ord(c) for c in data) % 256

    def hash_md5(self, data: str) -> str:
        """Insecure hashing using MD5."""
        return hashlib.md5(data.encode()).hexdigest()

if __name__ == "__main__":
    weak_checksum = WeakChecksum()
    message = "Sensitive Data"
    print("Original:", message)
    print("Checksum (Weak):", weak_checksum.checksum(message))
    print("MD5 Hash:", weak_checksum.hash_md5(message))
