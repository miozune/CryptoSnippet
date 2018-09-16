# -*- coding: utf-8 -*-

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
import gmpy2
from rsa_wiener_attack.RSAwienerHacker import hack_RSA

from utils import common_modulus_attack
from utils import fermat_factor


public_key_path = 'locals/public-key.pem'
flag_path = 'locals/FLAG.encrypted'


with open(public_key_path, 'r') as f:
    public_key = RSA.importKey(f.read())
    n = public_key.n
    e = public_key.e
c = open(flag_path, 'rb').read()
print('n:', n)
print('e:', e)


def decrypt_from_d(d):
    keys = RSA.construct((n, e, d))
    return PKCS1_v1_5.new(keys).decrypt(c, '').decode().strip()


# here's some ways to get decrypt
# Ref. https://www.slideshare.net/sonickun/rsa-n-ssmjp
#
#
# 1. if n is too small, Full Attack
#
# for i in range(3, int(n**(1/2)+1), 2):
#     if n % i == 0:
#         p = i
#         q = n // p
#         d = gmpy2.invert(e, (p-1)*(q-1))
#         break
# print('flag:', decrypt_from_d(d))
#
#
# 2. if p or q is too small, Full Attack
#
# for i in range(3, 10**8, 2):
#     if n % i == 0:
#         p = i
#         q = n // p
#         d = gmpy2.invert(e, (p-1)*(q-1))
#         break
# print('flag:', decrypt_from_d(d))
#
#
# 3. if p and q are close, Fermat's Factorization Method
#
# p, q = fermat_factor(n, 10**5)
# d = gmpy2.invert(e, (p-1)*(q-1))
# print('flag:', decrypt_from_d(d))
#
#
# 4. Mersenne Prime
#
# mersenne_primes = [2**i-1 for i in [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217]]
# for prime in mersenne_primes:
#     if n % prime == 0:
#         p = prime
#         q = n // p
#         d = gmpy2.invert(e, (p-1)*(q-1))
#         break
# print('flag:', decrypt_from_d(d))
#
#
# 5. if p or q is reused, Common Factor Attack
#
# prev_n = None
# p = gmpy2.gcd(n, prev_n)
# q = n // p
# d = gmpy2.invert(e, (p-1)*(q-1))
# print('flag:', decrypt_from_d(d))
#
#
# 6. if e (typically 65537) is too small, Low Public Exponent Attack (m**e < n)
#
# print('flag:', bytes.fromhex(hex(gmpy2.root(c, e).__int__())[2:]).decode().strip())
#
#
# 7. if e (typically 65537) is too large, Wiener's Attack (q < p < 2*q, d < n**(1/4)/3)
# use module "rsa-wiener-attack" (https://github.com/pablocelayes/rsa-wiener-attack)
#
# d = hack_RSA(e, n)
# print('flag:', decrypt_from_d(d))
#
#
# 8. if given two ciphertext which encrypted the same plaintext with different e, Common Modulus Attack
#
# e_another = None
# c_another = None
# print('flag:', common_modulus_attack(c, c_another, e, e_another, n))
