import base64

def decode_b64():
    data = input("Base64: ")
    decoded = base64.b64decode(data).decode('utf-8')
    print(f"\nDecoded: {decoded}")


if __name__ == "__main__":
    decode_b64()