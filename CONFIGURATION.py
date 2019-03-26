# ------------------- #
#  CONFIGURATION FOR  #
#                     #
#    HASH POWERED     #
# ENCRYPTED MESSAGING #
#     Version r2.0    #
# ------------------- #

# Blob Size (Message will be split every x caracters)
# Set this to either 4 or 5. higher = more secure (but more calculations).
# Has to be an int between 1 ~ 7 (Going higher that 7 will probebly take years to calculate even on high end PC's)
blobsize = 4

# Hashing Algoritm
algoritm = "sha256"

# Available Hashing Algoritms:
#  mmh3     -->  MurMurHash3 128bits, fast and secure enough
#  md5      -->  Message Digest Algorithm 5, fast not super secure
#  sha1     -->  Secure Hash Algorithm 1, fast insecure
#  sha256   -->  Secure Hash Algorithm 256, slower SUPER secure
#  sha512   -->  Secure Hash Algorithm 512, slower ULTRA secure
#  adler32  -->  Adler-32, fast insecure
#  crc32    -->  Cyclic Redundancy Check, fast insecure
#  xxhash32 -->  xxHash 32bits version, claims to be the fastest and secure, looks to be faster for this usage
#  xxhash64 -->  xxHash 64bits version, claims to be the fastest and secure
