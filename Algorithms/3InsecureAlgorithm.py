import hashlib
import base64

class WeakEncodingScheme:
    def __init__(self):
        pass

    def encode(self, data: str) -> str:
        """Weak encoding using base64 without encryption."""
        return base64.b64encode(data.encode()).decode()

    def decode(self, encoded_data: str) -> str:
        """Decoding base64."""
        return base64.b64decode(encoded_data.encode()).decode()

    def hash_sha1(self, data: str) -> str:
        """Insecure hashing using SHA-1."""
        return hashlib.sha1(data.encode()).hexdigest()

if __name__ == "__main__":
    weak_encoder = WeakEncodingScheme()
    message = "Sensitive Data"
    print("Original:", message)
    encoded = weak_encoder.encode(message)
    print("Encoded (Base64):", encoded)
    print("Decoded:", weak_encoder.decode(encoded))
    print("SHA-1 Hash:", weak_encoder.hash_sha1(message))
