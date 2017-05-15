from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from .api_client import ApiClient


class ApiClientWOConfig(ApiClient):

    def __init__(self, privkey_pem='', token='', servkey_pem='', API_key=''):
        super().__init__()
        self.__privkey_pem = privkey_pem
        self.__token = token
        self.__servkey_pem = servkey_pem
        self.__api_key = API_key

    @property
    def user_token(self):
        return None

    @property
    def server_token(self):
        return serialization.load_pem_public_key(
            self.__servkey_pem,
            backend=default_backend()
        )

    @property
    def session_token(self):
        return self.__token

    @property
    def pubkey(self):
        return self.privkey_pem.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @property
    def privkey(self):
        if not isinstance(self.__privkey_pem, bytes):
            self.__privkey_pem = self.__privkey_pem.encode()
        print(type(self.__privkey_pem))
        return serialization.load_pem_private_key(
            self.__privkey_pem,
            password=None,
            backend=default_backend()
        )

    @property
    def privkey_pem(self):
        return self.__privkey_pem

    @property
    def api_key(self):
        return self.__api_key

    @property
    def server_pubkey(self):
        return serialization.load_pem_public_key(
            self.server_pubkey_pem,
            backend=default_backend()
        )

    @property
    def server_pubkey_pem(self):
        return self.__servkey_pem
