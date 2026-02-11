import base64

def encode_b64():
    data = input("Text: ")
    encoded = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    print(f"\nBase64: {encoded}")


if __name__ == "__main__":
    encode_b64()