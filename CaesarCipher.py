import sys

def caesarEncryption(str, shift):
    encrypted=""
    for i in range(len(str)):
        letter=str[i]
        if letter.isupper():
            encrypted+=chr((ord(letter)+shift-65)%26+65)
        else:
            encrypted+=chr((ord(letter)+shift-97)%26+97)
    
    return encrypted


def caesarDecryption(str, shift):
    decrypted=""
    for i in str:
        if i.isupper():
            decrypted+=chr((ord(i)-shift-65)%26+65)
        else:
            decrypted+=chr((ord(i)-shift-97)%26+97)
    return decrypted

def main():
    if len(sys.argv)!=3:
        print("EXECUTE LIKE THIS: python3 CaesarCipher.py <your_string> <shift_value>")
        return
    
    str=sys.argv[1]
    shift=int(sys.argv[2])
    print(caesarDecryption(str, shift))

if __name__=="__main__":
    main()
    
