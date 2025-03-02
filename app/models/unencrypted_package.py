import encrypted_package
import encrypt

class UnencryptedPackage:
    def _init_(self, message, image, date, time):
        self.message = message
        self.image = image
        self.date = date
        self.time = time

    def get_message(self):
        return self.message
    
    def set_message(self, message):
        self.message = message

    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image

    def get_date(self):
        return self.date
    
    def set_image(self, date):
        self.date = date

    def get_time(self):
        return self.time
    
    def set_time(self, time):
        self.time = time

    def encrypt_package(self, key):
        encrypted_message = encrypt.encrypt_data(self.message, key)
        encrypted_image = encrypt.encrypt_data(self.image, key)
        return encrypted_package.EncryptedPackage(encrypted_message, encrypted_image, self.date, self.time)