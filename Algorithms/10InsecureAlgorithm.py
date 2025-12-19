import hashlib

class WeakShiftXORHash:
    def __init__(self):
        pass

    def weak_hash22(self, data: str) -> str:
        """Insecure hashing using shift XOR and MD5."""
        xor_result = ''.join(chr((ord(c) << 1) ^ 0x55) for c in data)  # Weak transformation
        return hashlib.md5(xor_result.encode()).hexdigest()

if __name__ == "__main__":
    weak_hasher22 = ShiftXORHash()
    message = "Sensitive Data"
    print("Original:", message)
    print("Weak Hash:", weak_hasher.weak_hash(message))
