#!usr/bin/env python

import hashlib

st = raw_input("string >> ")
md = hashlib.md5(st.encode())
print md
ss= md.hexdigest()
print ss
print repr(ss.digest())
