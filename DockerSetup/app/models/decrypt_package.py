import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import unencrypted_package
import encrypted_package
from DockerSetup.app.encryption import decrypt

def decrypt_package(encrypted_package):
    if not encrypted_package.past_unlock_time(encrypted_package):
        print(f"File is not ready for decryption. Unlock time is {encrypted_package.date} at {encrypted_package.time}")
        return None
    else:
        decrypted_message = encrypted_package.decrypt_data(encrypted_package.encrypted_message, decrypt.key)
        decrypted_image = decrypt.decrypt_data(encrypted_package.encrypted_image, decrypt.key)
        return unencrypted_package.UnencryptedPackage(decrypted_message, decrypted_image, encrypted_package.date, encrypted_package.time)