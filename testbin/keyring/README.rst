Keyring
=======

This module uses
`keyring <https://pypi.python.org/pypi/keyring>`_ and
`keyrings.alt <https://pypi.python.org/pypi/keyrings.alt>`_
to manage the keyring. It builds on top for these reasons:

* Use an encrypted file for storage that can be added to source control repo
* Better handling of programmatic use cases (such as in scripts)

How to Use
----------

Create an environment variable ``TESTBIN_SENSITIVE_KEY`` that has the password
or passphrase to encrypt and decrypt data stored in the keyring.

Instantiate the ``Keyring`` class and provide a file that holds keyring data.
Then use the ``add``, ``get``, and ``remove`` methods to work with the stored
information.

Customize
---------

Look at the source code of keyring_.py for customizations for your uses.
