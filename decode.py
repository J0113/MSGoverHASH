import apsw
from os import path
from time import time
from CONFIGURATION import *

print("\nEnter encrypted text:\n\n")
hashedinput = input()
print("\nEnter the encrytion key:\n\n")
securecode = input()

if path.isfile(securecode + ".db"):
    starttime = time()
    encryptedmsg = hashedinput.split()
    conn=apsw.Connection(":memory:")
    diskdb = apsw.Connection(securecode + ".db")
    with conn.backup("main", diskdb, "main") as backup:
        backup.step()
    diskdb.close()
    c = conn.cursor()
    msg = ""
    for x in encryptedmsg:
        c.execute("SELECT value FROM tb WHERE hash=?", (x,))
        group = c.fetchone()
        if group:
            msg = msg + str(group[0])
        pass
    endtime = time()
    timeused = endtime-starttime
    print("\n\n\n\n\n\n--------------------------------------------")
    if timeused>60:
        if timeused>3600:
            print("Time: " + str(round((timeused/3600),2)) + " hours")
        else:
            print("Time: " + str(round((timeused/60),2)) + " min")
    else:
        print("Time: " + str(round((timeused), 4)) + " sec")
    print("Message:\n\n\n")
    print(msg)
    print("\n\n\n--------------------------------------------\n\n")
    c.close()
    conn.close()
    pass
else:
    print("No DB for this code has been made yet, create one using the rainbow.py generator.")

#t = (hash,)
#c.execute('SELECT * FROM tb WHERE hash=?', t)
#print (c.fetchone())
