#!usr/bin/env python

import hashlib

st = raw_input("Enter string : ")
md5st = hashlib.md5(st.encode())
sha1st = hashlib.sha1(str(md5st).encode())
sha256st = hashlib.sha256(str(sha1st).encode())
print sha256st.hexdigest()
