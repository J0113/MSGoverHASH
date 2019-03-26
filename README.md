# MSGoverHASH
Allows encyrption and decryption of messages using a one-way hasing algorim. It's fully written in Python3.


## Getting Started
#### Encoding
1. Choose a secure password/encrytionkey/salt, you will need this when both encryption and decryption. Try to choose one that is at least 10 characters to fully prevent brute-forcing.
2. Encrypt a message using the `encode.py`. The script will ask for the message and the encryption key.

#### Rainbowtable
_Creating a rainbow table is necessary for decrytion_
1. To decrypt the message you will need to create a "rainbow table". Do this using the `rainbow.py` script. This script will ask for the encryption key. This proces can take a *looong* time if you set the blobsize higher (more about that under the configuration header). After this is done, a file will apear called [encryption key].db (needs to be changed later).

#### Decoding
1. Now let's decrypt the message! Run the `decode.py` script. This script will ask for the encrypted message and the encryption key (to find the the rainbow table database file). Depending on the size of the message and the blobsize the decryption time will vary (but it is way shorter than creating a rainbowtable). After the proces is done you can see the decrypted message! Of cource it is also possible to send the encrypted message over the internet. Anyone that knows the settings and encryption key can decode the message using this tool!

## Configuration
The configuration is stored in `CONFIGURATION.py`.
- `blobsize`, set this to 4 or 5. Higher is more secure but takes longer to calculate. Can be any INT higher than 1, don't go higher than 6 unless you have a super computer, which you probably don't have.
- `algoritm`, set this to the hashing algoritm you want to use.
#### Available Hashing Algoritms:
Hashing Algoritm  |  Description
--        |  --
mmh3*     |  MurMurHash3 128bits, fast and secure enough
md5       |  Message Digest Algorithm 5, fast not super secure
sha1      |  Secure Hash Algorithm 1, fast insecure
sha256    |  Secure Hash Algorithm 256, slower SUPER secure
sha512    |  Secure Hash Algorithm 512, slower ULTRA secure
adler32   |  Adler-32, fast insecure
crc32     |  Cyclic Redundancy Check, fast insecure
xxhash32* |  xxHash 32bits version, claims to be the fastest and secure, looks to be faster for this usage
xxhash64* |  xxHash 64bits version, claims to be the fastest and secure

## Dependencies
To run this tool you need to install:
- Python 3, Tested on 3.5.2. ( python.org )
- apsw, used to improve SQLite3 DB speed. Will **not** work without this dependencie! ( `pip install apsw` )
- mmh3, MurMurHash3 is a hashing algoritm, only necessary if you're using mmh3 as algorim. ( `pip install mmh3` )
- pyhashxx, 32bits version of xxhash, an hashing algoritm, only necessary if you're using xxhash32 as algorim. ( `pip install pyhashxx` )
- xxhash, 64bits version of xxhash, an hashing algoritm, only necessary if you're using xxhash64 as algorim. ( `pip install xxhash` )

## How it works
#### Encryption
1. Split input into blobs of `blobsize`. (`hello world` would be `[hell] [o wor] [ld  ]` with a `blobsize` of 4).
2. Calculate hash for every blob + salt. (`[hell]` would be the hash of `hellsalt` with a salt being salt).

#### Rainbowtable
1. Create a rainbowtable of every possible combination with `[a-z] + space` (`aaaa`, `aaab`, `aaac`).
2. Calculate hash for every item from the rainbowtable with `[item]+[salt]` (Hash of `aaaasalt`, `aaabsalt`).
3. Save to a SQLite3 Database.

#### Decryption
1. Lookup every hash inside the rainbowtable using SQLite3.
2. Combine the results to make it readable.

## Issue's
Please report **bugs**, any **issue's** or **security issue's** using the GH issue's.

### License
Licensed under the `Apache License 2.0`
