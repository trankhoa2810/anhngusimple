# Ho va ten sinh vien: Tran Anh Khoa
# Ma so sinh vien: B1913240
# STT: 32

def Char2Num(c):
    return ord(c) - 65

def Num2Char(n):
    return chr(n+65)

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0:
        x0 = temp+x0
    return x0


def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1*(Char2Num(c)-b)) % m
        r = r+Num2Char(e)
    return r

string = 'LOLYLTQOLTHDZTDC'
la = [1, 3, 5, 7, 11, 15, 17, 19, 21, 23, 25]

for b in range(0, 26):
    for a in la:
        if 'LAMUOI' in decryptAF(string,a,b,26):
            print("GUESS: " + decryptAF(string,a,b,26))