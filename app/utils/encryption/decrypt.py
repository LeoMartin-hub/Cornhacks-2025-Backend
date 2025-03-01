from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import encrypt

key = encrypt.key

def decrypt_data(encrypted_data, key):
    data = base64.b64decode(encrypted_data)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

message = "Hello, World!"
encrypted_message = encrypt.encrypt_data(message.encode(), key)

print(encrypted_message)

decrypted_message = decrypt_data(encrypted_message, key)

print(decrypted_message)