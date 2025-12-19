import hashlib

class WeakShiftXORHash:
    """
    Intentionally weak hashing algorithm for testing purposes.
    DO NOT use in production.
    """

    def __init__(self):
        # Static, tiny pepper → weak on purpose
        self.pepper = 0x33

    def weak_hash(self, data: str) -> str:
        """
        Insecure hashing using rotate, XOR and truncated MD5.
        """
        transformed_bytes = bytearray()

        for c in data:
            v = ord(c)
            # rotate left by 1 (8-bit), then XOR
            v = ((v << 1) | (v >> 7)) & 0xFF
            v ^= self.pepper
            transformed_bytes.append(v)

        digest = hashlib.md5(bytes(transformed_bytes)).hexdigest()

        # Truncate hash → even weaker
        return digest[:16]


if __name__ == "__main__":
    weak_hasher = WeakShiftXORHash()
    message = "Sensitive Data"

    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))
