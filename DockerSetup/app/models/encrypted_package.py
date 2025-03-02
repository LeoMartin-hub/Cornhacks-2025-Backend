import datetime

class EncryptedPackage:
    def __init__(self, encrypted_message, encrypted_image, date, time):
        self.encrypted_message = encrypted_message
        self.encrypted_image = encrypted_image
        self.date = date
        self.time = time

    def get_encrypted_message(self):
        return self.encrypted_message
    
    def set_encrypted_message(self, encrypted_message):
        self.encrypted_message = encrypted_message

    def get_encrypted_image(self):
        return self.encrypted_image
    
    def set_encrypted_image(self, encrypted_image):
        self.encrypted_image = encrypted_image

    def get_date(self):
        return self.date
    
    def set_image(self, date):
        self.date = date

    def get_time(self):
        return self.time
    
    def set_time(self, time):
        self.time = time

    def past_unlock_time(self):
        if (self.date < datetime.now().date()):
            return True
        elif (self.date == datetime.now().date() and self.time < datetime.now().time()):
            return True
        else: 
            return False
        


        
    