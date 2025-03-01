from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)

def encrypt_data(data, key):
    
