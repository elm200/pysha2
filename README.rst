======
pysha2
======

License
=======

This software is distributed under the
`MIT License <https://choosealicense.com/licenses/mit/>`_.

About
=====

pysha2 is a pure Python implementation of the FIPS 180-2 secure hash
standard.

It is originally written by Thomas Dixon. Eiji Sakai modified it
so that it can run on Python 3.5+. He also made some changes on
its API.

Usage
=====

A quick example of hashing a string::

    import pysha2

    print(pysha2.sha256.hexdigest('Can you keep a secret?'))

Testing
=======

To run the included unit tests, execute::

    pip install green
    green test -vv
