def isPrime(num):
    counter = abs(num) // 2
    if (counter == 1):
        return True
    while (counter > 1):
        if (num % counter == 0):
            return False
        counter -= 1
    return True


# print(isPrime(2))
# print(isPrime(1))
# print(isPrime(3))
# print(isPrime(4))
# print(isPrime(10))f
# print(isPrime(11))


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def fastMul(a, b, n):
    res = 1
    while b != 0:
        if b % 2 == 0:
            b = b / 2
            a = (a * a) % n
        elif b % 2 != 0:
            b = b - 1
            res = (res * a) % n
    return res


# def encrypt(m, publicKey):
#     n = publicKey[0]
#     e = publicKey[1]
#     c = fastMul(m, e, n)
#     return c
#
# def decrypt(c, privateKey):
#     n = privateKey[0]
#     d = privateKey[1]
#     m = fastMul(c, d, n)
#     return m

def gen_key(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)  # 710820
    e = 65537  # e меньше 710 тысяч, условие выполняется
    # print(fn)
    d = multiplicative_inverse(e, fi)
    if (d == 1):
        d += fi
    # print(d)
    return (n, e), (n, d)


# def encrypt(pk, plaintext):
#     # Unpack the key into it's components
#     key, n = pk
#     # Convert each letter in the plaintext to numbers based on the character using a^b mod m
#     cipher = [(ord(char) ** key) % n for char in plaintext]
#     # Return the array of bytes
#     return cipher
#
#
# def decrypt(pk, ciphertext):
#     # Unpack the key into its components
#     key, n = pk
#     # Generate the plaintext based on the ciphertext and key using a^b mod m
#     plain = [chr((char ** key) % n) for char in ciphertext]
#     # Return the array of bytes as a string
#     return ''.join(plain)

def enc(alphabet, msg, publkey):
    result = list()
    for l in msg:
        if not l.isalpha():  # skip if not letter
            result += l
            continue
        newindex = ((alphabet.index(l) ** publkey[1]) % publkey[0])
        result.append(newindex)
    return result
    # newWord += str((dict1.index(i) ** e) % n)


def dec(alphabet, msg, privkey):
    result = ""
    for l in msg:
        if type(l) is str:  # skip if not letter
            result += l
            continue
        oldindex = ((l ** privkey[1]) % privkey[0])
        # if (oldindex > len(alphabet)):
        #     oldindex = oldindex % 33 - 1
        result += alphabet[oldindex]
    return result


def main():
    print("Hello there!")
    # x = gen_primes()
    alp = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper())
    p = 719
    q = 991
    publickey, privatekey = gen_key(p, q)
    print("Your public key is ", publickey, " and your private key is ", privatekey)
    message = input("Enter a message to encrypt with someones public key: ").upper()
    encrypted_msg = enc(alp, message, publickey)
    print("Your encrypted message is: " + str(encrypted_msg))
    print("Receiver is decrypting message with private key ", privatekey, "...")
    print("Your message is:", str(dec(alp, encrypted_msg, privatekey)))


if __name__ == '__main__':
    main()
