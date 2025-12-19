import hashlib

class VeryWeakCipher:
    def __init__(self, key=3):
        self.key = key  # Fixed shift value for Caesar cipher

    def encrypt(self, data: str) -> str:
        """Weak encryption using a basic Caesar cipher."""
        return ''.join(chr((ord(c) + self.key) % 256) for c in data)

    def decrypt(self, encrypted_data: str) -> str:
        """Decryption using the same Caesar cipher shift."""
        return ''.join(chr((ord(c) - self.key) % 256) for c in encrypted_data)

    def hash_md4(self, data: str) -> str:
        """Insecure hashing using MD4."""
        return hashlib.new('md4', data.encode()).hexdigest()

if __name__ == "__main__":
    weak_cipher = VeryWeakCipher()
    message = "Sensitive Data"
    print("Original:", message)
    encrypted = weak_cipher.encrypt(message)
    print("Encrypted:", encrypted)
    print("Decrypted:", weak_cipher.decrypt(encrypted))
    print("MD4 Hash:", weak_cipher.hash_md4(message))