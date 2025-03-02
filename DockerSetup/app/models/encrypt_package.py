import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import unencrypted_package
import encrypted_package
from DockerSetup.app.encryption import encrypt

def encrypt_package(unencrypted_package):
    encrypted_message = encrypt.encrypt_data(unencrypted_package.message.encode(), encrypt.key)
    with open(unencrypted_package.image, "rb") as img_file:
        image_data = img_file.read()
    encrypted_image = encrypt.encrypt_data(image_data, encrypt.key)
    return encrypted_package.EncryptedPackage(encrypted_message, encrypted_image, unencrypted_package.date, unencrypted_package.time)
    
    
package = unencrypted_package.UnencryptedPackage("Hello, World!", "app/storage/uploaded/example_uploaded.jpeg", "2021-01-01", "12:00:00")
key = encrypt.key
encrypted_package = encrypt_package(package)
print(encrypted_package.get_encrypted_message())
print(encrypted_package.get_encrypted_image())
print(key)