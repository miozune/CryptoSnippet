# CryptoSnippet

## Usage
- RSA Attack
    1. Full Attack by n
    2. Full Attack by p
    3. Fermat's Factorization Method
    4. Mersenne Prime
    5. Common Factor Attack
    6. Low Public Exponent Attack
    7. Wiener's Attack
    8. Common Modulus Attack
- Decodes
    1. Decode by hex
    2. Decode by rot13

## Requirements
- Python3==3.6
- gmpy2==2.0.8
- PyCrypto==2.6.1
- [pablocelayes/rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack)
    - run `git clone https://github.com/pablocelayes/rsa-wiener-attack`
    - rename folder to `rsa_wiener_attack`
    - place folder in `CryptoSnippet/`
    - change description
    ```python:RSAwienerHacker.py
    # RSAwienerHacker.py line 7
    from . import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
    ```
    ```python:RSAvulnerableKeyGenerator.py
    # RSAvulnerableKeyGenerator.py line 38
    import random
    from . import MillerRabin, Arithmetic
    ```
