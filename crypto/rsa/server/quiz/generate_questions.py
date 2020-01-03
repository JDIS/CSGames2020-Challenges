import gmpy2
import math
import primefac
import random

from utils.Utils import generate_prime_number
from functools import reduce


def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def generate_q1():
    print('Q1: ==========================')
    p = generate_prime_number()
    q = generate_prime_number()

    print('Given p, q, generate n')
    n = p * q

    print('Values')
    print('p: {}'.format(p))
    print('q: {}'.format(q))

    print('Answers')
    print('n: {}'.format(n))


def generate_q2():
    print('Q2: ==========================')
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q

    print('Given p, n, generate q')
    q_p = n // p
    assert(q_p == q)

    print('Values')
    print('p: {}'.format(p))
    print('n: {}'.format(n))

    print('Answers')
    print('q: {}'.format(q_p))


def generate_q3():
    print('Q3: ==========================')

    p = generate_prime_number()
    q = generate_prime_number()
    e = 65537
    m = generate_prime_number(256)

    print('Given p, q, e, m , generate c')
    n = p * q
    c = pow(m, e, n)

    print('Values')
    print('p: {}'.format(p))
    print('q: {}'.format(q))
    print('e: {}'.format(e))
    print('m: {}'.format(m))

    print('Answers')
    print('c: {}'.format(c))


def generate_q4():
    print('Q4: ==========================')
    p = generate_prime_number()
    q = generate_prime_number()
    e = 65537
    m = generate_prime_number(256)

    print('Given c, d, n, generate m')
    # First, encrypt
    n = p * q
    c = pow(m, e, n)

    # Then, decrpyt
    phi = (p-1) * (q-1)
    d = getModInverse(e, phi)
    m_p = pow(c, d, n)

    assert(m_p == m)
    assert(pow(m, e*d, n) == m)

    print('Values')
    print('c: {}'.format(c))
    print('d: {}'.format(d))
    print('n: {}'.format(n))

    print('Answers')
    print('m: {}'.format(m))


def generate_q5():
    print('Q5: ==========================')
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q

    assert(n // q == p)

    print('Given n, q, generate phi')
    phi = (p-1) * (q-1)

    print('Values')
    print('n: {}'.format(n))
    print('q: {}'.format(q))

    print('Answer')
    print('phi: {}'.format(phi))


def generate_q6():
    print('Q6: ==========================')
    p = generate_prime_number()
    q = generate_prime_number()
    m = generate_prime_number(256)
    e = 65537

    n = p * q

    c = pow(m, e, n)

    print('Given p, n, e, c generate m')
    # First, encrypt
    n = p * q
    c = pow(m, e, n)

    # Then, decrpyt
    phi = (p-1) * (q-1)
    d = getModInverse(e, phi)
    m_p = pow(c, d, n)

    assert(m_p == m)
    assert(pow(m, e*d, n) == m)

    print('Values')
    print('p: {}'.format(p))
    print('n: {}'.format(n))
    print('e: {}'.format(e))
    print('c: {}'.format(c))

    print('Answers')
    print('m: {}'.format(m))


def generate_q7():
    print('Q7: ==========================')
    p = generate_prime_number()
    q = generate_prime_number()
    m = generate_prime_number(256)

    n = p * q
    e = 3

    c = pow(m, e, n)
    print('Given n, e, c, generate m')
    # The trick here is that e is so small you can just
    # get the (cubic root of c) % n  to get m
    gc = gmpy2.mpz(c)
    gn = gmpy2.mpz(n)
    ge = gmpy2.mpz(e)

    root, _ = gmpy2.iroot(gc, ge)
    m_p = gmpy2.t_mod(root, gn)

    assert(m_p == m)

    print('Values')
    print('n: {}'.format(n))
    print('e: {}'.format(e))
    print('c: {}'.format(c))

    print('Answer')
    print('m: {}'.format(m))


def generate_q8():
    print('Q8: ==========================')
    n = 25735664145190389285057703686192800899705919152576441463391134729007771965919846923127428578522061398506987280139163802365132867371555016059630770918319052361574038129434461641589247193942274761931612037853509472630757167158051628233272586365739584359583565563288057330271262509882524468563142934008187343454761865753388775613752888169560816991
    # prime factorize n
    e = 65537
    m = int('JDIS-{RSA_B3-C4R3FUL-86123112}'.encode('utf-8').hex(), 16)

    # First, encrypt
    c = pow(m, e, n)

    print('Given n, e, c generate m')
   # Then, decrpyt
    ps = list(primefac.primefac(n))
    phi = 1
    for i in ps:
        phi *= (i-1)

    n_p = reduce((lambda x, y: x * y), ps)
    assert n_p == n, (n_p, n)
    # phi = reduce((lambda x, y: (x-1) * y), ps)

    d = getModInverse(e, phi)
    m_p = pow(c, d, n)

    assert m_p == m, (m_p, m)
    assert(pow(m, e*d, n) == m)

    print('Values')
    print('n: {}'.format(n))
    print('e: {}'.format(e))
    print('c: {}'.format(c))

    print('Answer')
    print('m: {}'.format(m))

    print('Flag: ')
    print(bytearray.fromhex(format(m, 'x')).decode())


if __name__ == '__main__':
    generate_q1()
    generate_q2()
    generate_q3()
    generate_q4()
    generate_q5()
    generate_q6()
    generate_q7()
    generate_q8()
