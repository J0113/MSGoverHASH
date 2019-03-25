# ------------------- #
#  CONFIGURATION FOR  #
#                     #
#    HASH POWERED     #
# ENCRYPTED MESSAGING #
#     Version r1.0    #
# ------------------- #

# Blob Size (Message will be split every x caracters)
# Set this to either 4 or 5. higher = more secure (but more calculations).
# Has to be an int between 1 ~ 7 (Going higher that 7 will probebly take years to calculate even on high end PC's)
blobsize = 4

# Hashing Algoritm
algoritm = "mmh3" #(only murmurhash is currently available; it's fast and secure enough as long as you use a good security code/ salt)
