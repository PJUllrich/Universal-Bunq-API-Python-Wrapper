import base64
import json
import copy
import requests
import uuid

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from config import Controller


class ApiClient:

    __version_api = 1
    __version = '0.0.1'
    __uri = f"https://api.bunq.com/v{__version_api}"

    def __init__(self):
        self.config = Controller()

    def get(self, endpoint, verify=False):
        pass

    def post(self, endpoint, payload):
        action = 'POST /v%d/%s' % (self.__version_api, endpoint)
        msg = self.create_message(action, payload)

        headers_all = copy.deepcopy(self.headers)

        if self.privkey is not None:
            headers_all['X-Bunq-Client-Signature'] = self.sign(msg)
        print(self.sign(msg))
        url = '%s/%s' % (self.__uri, endpoint)

        print(json.dumps(headers_all, indent=4))
        print(msg)

        return requests.request('POST', url, headers=headers_all, json=payload)

    def create_message(self, action, payload):
        headers_as_text = '\n'.join(['%s: %s' % (k, v) for k, v in sorted(
                self.headers.items())])
        msg = '%s\n%s\n\n' % (action, headers_as_text)

        if payload:
            msg += json.dumps(payload)

        return msg

    def sign(self, msg):
        """Create signature for message
        Taken from https://github.com/madeddie/python-bunq - Thanks!

        :param msg: data to be signed, usually action, headers and body
        :type msg: str

        """
        return base64.b64encode(
            self.privkey_pem.sign(
                msg.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        ).decode()

    def verify(self, res):
        """Verify response from server
        Taken from https://github.com/madeddie/python-bunq - Thanks!

        :param res: request to be verified
        :type res: requests.models.Response

        """
        if not self.server_pubkey:
            print('No server public key defined, skipping verification')
            return

        serv_headers = [
            'X-Bunq-Client-Request-Id',
            'X-Bunq-Client-Response-Id'
        ]

        msg = '%s\n%s\n\n%s' % (
            res.status_code,
            '\n'.join(
                ['%s: %s' % (k, v) for k, v in sorted(
                    res.headers.items()
                ) if k in serv_headers]
            ),
            res.text
        )

        signature = base64.b64decode(res.headers['X-Bunq-Server-Signature'])

        try:
            self.server_pubkey.verify(
                signature,
                msg.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except InvalidSignature:
            print('Message failed verification, data might be tampered with')
            return False
        else:
            return True

    @property
    def headers(self):
        request_id = str(uuid.uuid1())
        headers = {
            'Cache-Control': 'no-cache',
            'User-Agent': 'universal-bunq-api-python/' + self.__version,
            'X-Bunq-Client-Request-Id': request_id,
            'X-Bunq-Geolocation': '0 0 0 0 NL',
            'X-Bunq-Language': 'en_US',
            'X-Bunq-Region': 'en_US'
        }
        if self.user_token is not None:
            headers['X-Bunq-Client-Authentication'] = self.user_token

        return headers

    @property
    def user_token(self):
        return self.config.get('user_token')

    @property
    def server_token(self):
        return self.config.get('server_token')

    @property
    def pubkey(self):
        return self.config.get('key_public')

    @property
    def privkey(self):
        return self.config.get('key_private')

    @property
    def privkey_pem(self):
        key = self.privkey

        if not isinstance(key, bytes):
            key = key.encode()

        return serialization.load_pem_private_key(
            key,
            password=None,
            backend=default_backend()
        )

    @property
    def api_key(self):
        return self.config.get('api_key')

    @property
    def server_pubkey(self):
        return self.config.get('server_pubkey')


