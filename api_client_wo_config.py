from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from api_client import ApiClient


class ApiClientWOConfig(ApiClient):

    def __init__(self, privkey_pem, token='', servkey_pem='', api_key=''):
        super().__init__()
        self.__privkey_pem = privkey_pem
        self.__token = token
        self.__servkey_pem = servkey_pem
        self.__api_key = api_key

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
        privkey_pem_bytes = self.privkey_pem
        if not isinstance(privkey_pem_bytes, bytes):
            privkey_pem_bytes = privkey_pem_bytes.encode()

        return serialization.load_pem_private_key(
            privkey_pem_bytes,
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
