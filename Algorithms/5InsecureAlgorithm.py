import hashlib

class ObsoleteHash:
    def __init__(self):
        pass

    def weak_hash(self, data: str) -> str:
        """Insecure hashing using CRC32 and MD4."""
        crc32_hash = format(hashlib.crc32(data.encode()), 'x')
        md4_hash = hashlib.new('md4', data.encode()).hexdigest()
        return f"CRC32: {crc32_hash}, MD4: {md4_hash}"

if __name__ == "__main__":
    weak_hasher = ObsoleteHash()
    message = "Sensitive Data"
    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))
