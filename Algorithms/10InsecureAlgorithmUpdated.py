import hashlib

class WeakShiftXORHash:
    """
    Intentionally weak hashing algorithm for testing purposes.
    DO NOT use in production.
    """

    def __init__(self, salt: str = "123"):
        # Fixed, short salt → still weak
        self.salt = salt

    def weak_hash(self, data: str) -> str:
        """
        Insecure hashing using shift, XOR and SHA-1.
        """
        transformed = ''.join(
            chr(((ord(c) << 1) ^ 0x55) & 0xFF)
            for c in (data + self.salt)
        )

        return hashlib.sha1(transformed.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    weak_hasher = WeakShiftXORHash()
    message = "Sensitive Data"

    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))
