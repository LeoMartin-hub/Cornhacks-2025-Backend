from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from . import encrypt  # Ensure the correct relative import

key = get_random_bytes(16)

def decrypt_data(encrypted_data, key):
    data = base64.b64decode(encrypted_data)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()