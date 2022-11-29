import base64
from Crypto.Cipher import DES
import pandas as pd

df = pd.read_csv('nation.csv', delimiter=",")

print(df.value)

rawText1 = "The treasure is under the coconut tree"
Encode1 = "lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=="
Encode2 = "LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=="
Encode3 = "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)


def unpad(s):
    return s[:-ord(s[len(s)-1:])]


def mahoa_DES(Key):
    txt = pad(rawText1).encode("utf8")
    key = pad(Key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    # print(entxt)
    return str(entxt)

def giaima_DES(Key, encodetxt):
    txt = encodetxt
    txt = base64.b64decode(txt)
    key = pad(str(Key)).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    return str(detxt)


for k in df.value:
    if len(k) < 7:
        if Encode1 in mahoa_DES(k):
            key = k
            break

print(key)
print( giaima_DES(key, Encode2))
print( giaima_DES(key, Encode3))