# -*- coding: utf-8 -*-

import codecs
import gmpy2


def hex_decode(sentence):
    return codecs.decode(sentence, 'hex_codec').decode()


def rot13(sentence):
    return codecs.decode(sentence, 'rot13')


def fermat_factor(n, tries):
    # original source: http://kataware.hatenablog.jp/entry/2018/01/03/161926

    x = gmpy2.isqrt(n) + 1
    y = gmpy2.isqrt(x*x - n)
    for _ in range(tries):
        w = x*x - n - y*y
        if w == 0:
            return x+y, x-y
        elif w > 0:
            y += 1
        else:
            x += 1
    return None, None

# assert fermat_factor(0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F, 10**5) == (9733382803370256893136109840971590971460094779242334919432347801491641617443615856221168611138933576118196795282443503609663168324106758595642231987246769, 9733382803370256893136109840971590971460094779242334919432347801491641617443615856221168611138933576118196795282443503609663168324106758595642231987245583)


def common_modulus_attack(c1, c2, e1, e2, n):
    # original source: http://inaz2.hatenablog.com/entry/2016/01/15/011138

    gcd, s1, s2 = gmpy2.gcdext(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = gmpy2.invert(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = gmpy2.invert(c2, n)
    v = pow(c1, s1, n)
    w = pow(c2, s2, n)
    m = (v * w) % n
    return m


