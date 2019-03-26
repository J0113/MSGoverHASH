from CONFIGURATION import *

# MurMurHash3
if (algoritm == "mmh3"):

    from mmh3 import hash128

    def hash(input):
        return str(hash128(input))
        pass

    pass


# MD5
if (algoritm == "md5"):

    from hashlib import md5

    def hash(input):
        return md5(input.encode('utf-8')).hexdigest()
        pass

    pass


# SHA1
if (algoritm == "sha1"):

    from hashlib import sha1

    def hash(input):
        return sha1(input.encode('utf-8')).hexdigest()
        pass

    pass


# SHA256
if (algoritm == "sha256"):

    from hashlib import sha256

    def hash(input):
        return sha256(input.encode('utf-8')).hexdigest()
        pass

    pass


# SHA512
if (algoritm == "sha512"):

    from hashlib import sha512

    def hash(input):
        return sha512(input.encode('utf-8')).hexdigest()
        pass

    pass

# adler32
if (algoritm == "adler32"):

    from zlib import adler32

    def hash(input):
        return adler32(input.encode('utf-8'))
        pass

    pass


# crc32
if (algoritm == "crc32"):

    from zlib import crc32

    def hash(input):
        return crc32(input.encode('utf-8'))
        pass

    pass

# xxhash 32 bits version
if (algoritm == "xxhash32"):

    from pyhashxx import hashxx

    def hash(input):
        return hashxx(input.encode(), seed=0)
        pass

    pass


# xxhash 64 bits version
if (algoritm == "xxhash64"):

    from xxhash import xxh64

    def hash(input):
        return xxh64(input.encode(), seed=0).hexdigest()
        pass

    pass
