from hashlib import sha1

f = open("data.txt", 'w')
for i in range(10000000, 20000000):
    hash = str(i) + "salt_for_you"
    for j in range(500):
        hash = sha1(hash.encode("UTF-8")).hexdigest()
    f.write(str(i) + " : " + hash + "\n")
f.close()