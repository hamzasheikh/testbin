import os
from os.path import basename

import keyring
import keyrings

service = "testbin"  # Change this value based on your requirements


class EncryptedKeyring_(keyrings.alt.file.EncryptedKeyring):
    def _unlock(self):
        """
        Unlock this keyring by getting the password for the keyring from an environment variable.

        Overriding function because original requires interactive input for password to unlock file.
        """
        # Begin override
        # Change the env var name to use based on your requirements
        self.keyring_key = os.environ["TESTBIN_SENSITIVE_KEY"]
        # End override
        try:
            ref_pw = self.get_password('keyring-setting', 'password reference')
            assert ref_pw == 'password reference value'
        except AssertionError:
            self._lock()
            raise ValueError("Incorrect Password")


class Keyring():
    def __init__(self, filepath):
        encrypted_keyring = EncryptedKeyring_()
        encrypted_keyring.filename = basename(filepath)
        encrypted_keyring.file_path = filepath

        self.keyring = keyring.set_keyring(encrypted_keyring)

    def get(key):
        return self.keyring.get_password(service, key)

    def add(key, value):
        return self.keyring.set_password(service, key, value)

    def remove(key):
        return self.keyring.delete_password(service, key)
