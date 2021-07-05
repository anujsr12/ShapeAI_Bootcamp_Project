#!usr/bin/env python

import hashlib
#taking input as a string
st = raw_input("Enter string : ")

#converting the string into md5
md5st = hashlib.md5(st.encode())

#now coverting the md5 data to sha1 by taking the md5st data as string and then coverting it to sha1
sha1st = hashlib.sha1(str(md5st.hexdigest()).encode())

#now coverting the md5 data to sha1 by taking the sha1st data as string and then coverting it to sha256
sha256st = hashlib.sha256(str(sha1st.hexdigest()).encode())
print sha256st.hexdigest()
