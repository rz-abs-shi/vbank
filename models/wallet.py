import peewee

from crypto.aes import AESCipher
from crypto.rsa import new_keys, import_key
from models import BaseModel


class Wallet(BaseModel):

    private_key_encrypted = peewee.CharField(max_length=2048)

    public_key = None
    private_key = None

    def decrypt(self, password):
        cipher = AESCipher(password)

        try:
            private_key_str = cipher.decrypt(self.private_key_encrypted)

            if not private_key_str.startswith('-----BEGIN RSA PRIVATE KEY-----'):
                raise Exception('Password was invalid to decode private key')

            self.private_key = import_key(private_key_str)
            self.public_key = self.private_key.publickey()

        except UnicodeDecodeError:
            raise Exception('Password was invalid to decode private key')

    @staticmethod
    def create_wallet(password):
        wallet = Wallet()
        public_key, private_key = new_keys(1024)
        private_key_as_str = private_key.export_key().decode()

        cipher = AESCipher(password)
        wallet.private_key_encrypted = cipher.encrypt(private_key_as_str)
        wallet.save()

        return wallet
