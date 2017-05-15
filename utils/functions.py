"""
DISCLAIMER: This code was mostly taken from the example files in:

https://github.com/madeddie/python-bunq

Thanks for @madeddie for writing these examples and the API Wrapper
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from ..config import Controller
from ..api_client_wo_config import ApiClientWOConfig

config = Controller()
api_client = ApiClientWOConfig()


def create_new_key_pair():
    """Creates a new public/private key pair and saves them to the config file

    :return: Prints out a success message
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    private_key_decoded = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()

    public_key_decoded = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    config.set('key_private', private_key_decoded)
    config.set('key_public', public_key_decoded)

    print('New key pair created and saved to config.ini file.')


def register_key_pair():
    """Registers a public/private key pair with the Bunq API
    Ref: https://doc.bunq.com/api/1/call/installation/method/post

    Saves the installation (user) token and server public key to config

    KEY_PRIVATE needs to be set in the config for this method to run

    :return: Prints out either a success message or the Error message of the API
    """
    payload = {'client_public_key': api_client.pubkey}

    r = api_client.post('installation', payload)
    if r.status_code == 200:
        token_entry = [x for x in r.json()['Response'] if list(x)[0] == 'Token'][0]
        server_entry = [x for x in r.json()['Response'] if list(x)[0] == 'ServerPublicKey'][0]

        token_user = token_entry['Token']['token']
        server_public_key = server_entry['ServerPublicKey']['server_public_key']

        config.set('user_token', token_user)
        config.set('server_pubkey', server_public_key)

        print('Key pair was registered successfully.')
    else:
        print('Register Key Pair Error: ' + str(r.json()['Error'][0]))


def create_new_device_server():
    """Creates a new device server at the Bunq API
    Ref: https://doc.bunq.com/api/1/call/device-server/method/post

    API_KEY needs to be set in the config for this method to run

    :return: Prints out either a success message or the Error message of the API
    """
    payload = {'description': 'Castle', 'secret': api_client.api_key}

    r = api_client.post('device-server', payload)
    if r.status_code == 200:
        print('New device server was created successfully.')
    else:
        print('New Device Server Error: ' + str(r.json()['Error'][0]))


def create_new_session():
    """Creates a new session at the Bunq API
    Ref: https://doc.bunq.com/api/1/call/session-server/method/post

    Saves the session token to config

    API_KEY needs to be set in the config for this method to run

    :return: Prints out either a success message or the Error message of the API
    """

    r = api_client.post('session-server', {'secret': api_client.api_key})

    if r.status_code == 200:
        res = [x for x in r.json()['Response'] if list(x)[0] == 'Token'][0]
        session_token = res['Token']['token']
        config.set('session_token', session_token)
        print('New session was created successfully.')
    else:
        print('Create Session Error: ' + str(r.json()['Error'][0]))


def get_user_id():
    """Retrieves the id of the first user of an accounts from the Bunq API
    Saves the id to config

    :return: Prints out either a success message or the Error message of the API
    """
    r = api_client.get('user')
    if r.status_code == 200:
        res = [x for x in r.json()['Response'] if list(x)[0] == 'UserPerson'][0]
        user_id = res['UserPerson']['id']
        config.set('USER_ID', str(user_id))
        print('User id retrieved successfully.')
    else:
        print('Retrieve User ID Error: ' + str(r.json()['Error'][0]))
