import hashlib

secret = "This is the password or document text"

bsecret = secret.encode()

m = hashlib.md5()

m.update(bsecret)

m.digest()
# b' \xf5\x06\xe6\xfc\x1c\xbe\x86\xddj\x96C\x10\x0f5E'
