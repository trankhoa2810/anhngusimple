# Tran Anh Khoa
# B1913240

import pandas as pd
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import filedialog

def save_file(content, _mode, _title, _filetypes,_defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,
    initialdir = "D:/",
    title = _title,
    filetypes = _filetypes,
    defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def generate_key():
    key = RSA.generate(1024)
    pri = save_file(key.exportKey('PEM'),
    'wb',
    'Lưu khóa cá nhân',
    (("All files", "*.*"), ("PEM files", "*.pem")),
    ".pem")
    pub = save_file(key.publickey().exportKey('PEM'),
    'wb',
    'Lưu khóa công khai',
    (("All files", "*.*"),("PEM files", "*.pem")),
    ".pem")
    privateKeytxt.delete('1.0',END)
    privateKeytxt.insert(END,key.exportKey('PEM'))
    publicKeytxt.delete('1.0',END)
    publicKeytxt.insert(END,key.publickey().exportKey('PEM'))


def mahoa_rsa():
    txt = plaintxt.get().encode()
    publicKeytxt = get_key("Public Key")
    cipher = PKCS1_v1_5.new(publicKeytxt)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

def giaima_rsa():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    privateKeytxt = get_key("Private Key")
    cipher = PKCS1_v1_5.new(privateKeytxt)
    dsize = 128
    sentinel = Random.new().read(dsize)
    entxt = cipher.decrypt(txt, sentinel)
    denctxt.delete(0,END)
    denctxt.insert(INSERT,entxt)


def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "D:/",
    title = "Open " + key_style,
    filetypes = (("PEM files", "*.pem"),("All files", "*.*")))
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

# -*- coding: utf8 -*-
# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG RSA", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

widthEntry = 80
height = 5

plainlb3 = Label(window, text="Văn bản gốc", font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window, width=widthEntry)
plaintxt.grid(column=1, row=3)

cipherlb5 = Label(window, text="Văn bản được mã hoá", font=("Arial", 14))
cipherlb5.grid(column=0, row=4)
ciphertxt = Entry(window, width=widthEntry)
ciphertxt.grid(column=1, row=4)

denclb6 = Label(window, text="Văn bản được giải mã", font=("Arial", 14))
denclb6.grid(column=0, row=5)
denctxt = Entry(window, width=widthEntry)
denctxt.grid(column=1, row=5)

privateKeylb4 = Label(window, text="Khoá Cá Nhân", font=("Arial", 14))
privateKeylb4.grid(column=0, row=6)
privateKeytxt = Text(window, width=50, height=height)
privateKeytxt.grid(column=1, row=6)

publicKeylb4 = Label(window, text="Khoá Công Khai", font=("Arial", 14))
publicKeylb4.grid(column=0, row=7)
publicKeytxt = Text(window, width=50, height=height)
publicKeytxt.grid(column=1, row=7)

createKeybtn= Button(window, text="Tạo Khóa", command=generate_key)
createKeybtn.grid(column=1, row=8)

AFbtn = Button(window, text="Mã Hóa", command=mahoa_rsa)
AFbtn.grid(column=1, row=9)

DEAFbtn = Button(window, text="Giải Mã", command=giaima_rsa)
DEAFbtn.grid(column=1, row=10)

# Hien thi cua so
window.geometry('800x500')
window.mainloop()