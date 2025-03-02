from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

#Generates 16-byte AES key
key = get_random_bytes(16)

#Takes in data as a byte sequence and encrypts it using AES in GCM mode
#Returns the encrypted data as a base64 encoded string
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()


    


