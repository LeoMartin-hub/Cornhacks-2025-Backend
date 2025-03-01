class EncryptedPackage:
    def _init_(self, encrypted_message, encrypted_image, date, time):
        self.encrypted_message = encrypted_message
        self.encrypted_image = encrypted_image
        self.date = date
        self.time = time