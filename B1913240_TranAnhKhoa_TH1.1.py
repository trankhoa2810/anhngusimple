# Ho va ten sinh vien: Tran Anh Khoa
# Ma so sinh vien: B1913240
# STT: 32

from tempfile import tempdir
from tkinter import *


def Char2Num(c):
    return ord(c)


def Num2Char(n):
    return chr(n)


def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r


def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 127
    entxt = encryptAF(plaintxt.get(), a, b, m)
    ciphertxt3.delete(0, END)
    ciphertxt3.insert(INSERT, entxt)


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

def runDescriptAF():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 127
    temptxt = decryptAF(ciphertxt3.get(), a, b, m)
    encryptAFtxt.delete(0, END)
    encryptAFtxt.insert(INSERT, temptxt)


# -*- coding: utf8 -*-
# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")
# Them cac control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ AFFINE", font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLAIN TEXT", font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window, width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR", font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window, width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window, width=5)
KEYB1.grid(column=4, row=3)

# Hoc vien bo sung code tai day
# de co duoc giao dien nhu yeu cau cua bai toan
plainlb4 = Label(window, text="CIPHER TEXT", font=("Arial", 14))
plainlb4.grid(column=0, row=4)
ciphertxt3 = Entry(window, width=20)
ciphertxt3.grid(column=1, row=4)
encryptAFtxt = Entry(window, width=20)
encryptAFtxt.grid(column=3, row=4)

# Tao nut co ten AFbtn
AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)

# Hoc vien bo sung code de tao nut co ten la DEAFbtn
DEAFbtn = Button(window, text="Giải Mã", command=runDescriptAF)
DEAFbtn.grid(column=2, row=4)


# Hien thi cua so
window.geometry('1000x600')
window.mainloop()