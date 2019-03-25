# MSGoverHASH
Allows encyrption and decryption of messages using a one-way hasing algorim. It's fully written in Python3. 


## Getting Started
 1. Choose a secure password/encrytionkey/salt, you will need this when both encryption and decryption. Try to choose one that is at least 10 characters to fully prevent brute-forcing. 
 2. Encrypt a message using the `encode.py`. The script will ask for the message and the encryption key (from step 1).
 3. To decrypt the message you will need to create a "rainbow table". Do this using the `rainbow.py` script. This script will ask for the encryption key. This proces can take a *looong* time if you set the blobsize higher (more about that under the configuration header). After this is done, a file will apear called [encryption key].db (needs to be changed later).
 4.  Now let's decrypt the message! Run the `decode.py` script. This script will ask for the encrypted message (step 2) and the encryption key (to find the the rainbow table database file). Depending on the size of the message and the blobsize the decryption time will vary (way shorter than step 3). After the proces is done you can see the decrypted message! Of cource it is also possible to send the encrypted message over the internet. Anyone that knows the encryption key can decode the message using this tool!

## Dependencies
To run this tool you need to install:
 - Python 3, Tested on 3.5.2. ( python.org )
 - apsw, used to improve SQLite3 DB speed. ( `pip install apsw` ) 
 - mmh3, MurMurHash 3 is used to hash the msg, mainly because of the speed. More hashing algoritmes will be available later. ( `pip install mmh3` )

## Configuration
The configuration is stored in `CONFIGURATION.py`. It is not needed to edit this but if you want you can change:
- `blobsize`, set this to 4 or 5. Higher is more secure but takes longer to calculate.
- `algoritm`, reserved untill I add more algoritm's. Does nothing for now.

## Issue's
Please report bugs, any issue's or security issue's using the GH issue's.

### License
Licensed under the `Apache License 2.0`
