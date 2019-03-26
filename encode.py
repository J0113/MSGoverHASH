import re
from CONFIGURATION import *
from hasher import *

print("\nWhat to encrypt? (Only lowercase letters and spaces)\n\n")
msg = input()
print("\nChoose a secure encrytion key: (min 8 caracters for security)\n\n")
securecode = input()
msg = msg.lower()
msg = re.sub(r'[^a-z ]', '', msg)

def splitter(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

while (len(msg)/4) != round(len(msg)/4):
    msg = msg + " "
    pass

print("Encrypting: " + msg)
print("Using encrytion key: " + securecode)

result = ""
for group in splitter(msg, blobsize):
    result = result + hash(group+securecode) + " "

print("\n\nEncrypted Message: \n\n" + result + "\n\n")
