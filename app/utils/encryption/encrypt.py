from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()
    
message = "Hello, World!"
encrypted_message = encrypt_data(message.encode(), key)

print(encrypted_message)