import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import unencrypted_package
import encrypted_package
from app.utils.encryption import decrypt

def decrypt_package(encrypted_package):
    decrypted_message = encrypted_package.decrypt_data(encrypted_package.encrypted_message, decrypt.key)
    decrypted_image = decrypt.decrypt_data(encrypted_package.encrypted_image, decrypt.key)
    return unencrypted_package.UnencryptedPackage(decrypted_message, decrypted_image, encrypted_package.date, encrypted_package.time)