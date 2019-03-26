import apsw
from time import time
from itertools import product
from CONFIGURATION import *
from hasher import *

letter = "abcdefghijklmnopqrstuvwxyz "

print("\nCreating New Rainbow Table\n\nEnter Security Code:")
securecode = input()

memdb = apsw.Connection(":memory:")
memdbc = memdb.cursor()
memdbc.execute("CREATE TABLE IF NOT EXISTS tb (hash text, value text)")

print("\n\n\nStaring now.\n\n")
starttime = time()
print("[1/3] Creating Rainbowtable")
rainbowtable = [''.join(i) for i in product(letter, repeat = blobsize)]
print("[1/3] Done Creating Rainbowtable")

print("[2/3] Hashing")
starttimeblob = time()
for i in rainbowtable[:100000]:
    memdbc.execute('INSERT INTO tb VALUES (?,?)', (hash(i+securecode),i))
endtimeblob = time()
timeusedblob = endtimeblob-starttimeblob
print("Estemated Solve Time: " + str(round(timeusedblob/100000*(pow(len(letter),blobsize)))) + " seconds")

for i in rainbowtable[100000:]:
    memdbc.execute('INSERT INTO tb VALUES (?,?)', (hash(i+securecode),i))
print("[2/3] Hashing Done")

print("[3/3] Exporting to file")
diskdb = apsw.Connection(securecode + ".db")
with diskdb.backup("main", memdb, "main") as backup:
    backup.step() # copy whole database in one go
print("[3/3] Exported")

memdbc.close()
memdb.close()
endtime = time()
timeused = endtime-starttime
totalhashes = pow(len(letter),blobsize)

# Display Result
print("\n\n\n\n\n\n--------------------------------------------")
print("Procces Completed")
print("Hashes Calcuated: " + str(totalhashes))
print("Speed: " + str(round(totalhashes/timeused)) + " per second")
if timeused>60:
    if timeused>3600:
        print("Time: " + str(round((timeused/3600),2)) + " hours")
    else:
        print("Time: " + str(round((timeused/60),2)) + " min")
else:
    print("Time: " + str(round((timeused), 4)) + " sec")
print("--------------------------------------------\n\n\n")
