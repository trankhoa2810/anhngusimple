# Ho va ten: Trần Anh Khoa
# MSSV: B1913240

import pandas as pd
from tkinter import *
from Crypto.Cipher import DES
import base64
from tkinter import filedialog

def hack_execute():
    countries = pd.read_csv("D:/ATBMTT/countrylist.csv", delimiter=",")
    for key in countries.value:
        try:
            temp = giaima_DES(ciphertxt.get(), key)
            try:
                temp = plaintxt.decode("utf-8")
            except:
                continue
            if len(temp) > 0:
                print(temp, key)
                denctxt.delete(0, END)
                denctxt.insert(INSERT, temp)
                keytxt.delete(0, END)
                keytxt.insert(INSERT, key)
                return
        except:
            continue

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    keytxt.insert(END, 'haha')
    plaintxt.insert(END, data)
    tf.close()

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf8")
    key = pad(keytxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)

def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(keytxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    denctxt.delete(0, END)
    denctxt.insert(INSERT, detxt)

# -*- coding: utf8 -*-
# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Them cac control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

width = 70

plainlb3 = Label(window, text="Văn bản gốc", font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window, width=width)
plaintxt.grid(column=1, row=3)

keylb4 = Label(window, text="Khoá", font=("Arial", 14))
keylb4.grid(column=0, row=4)
keytxt = Entry(window, width=width)
keytxt.grid(column=1, row=4)

cipherlb5 = Label(window, text="Văn bản được mã hoá", font=("Arial", 14))
cipherlb5.grid(column=0, row=5)
ciphertxt = Entry(window, width=width)
ciphertxt.grid(column=1, row=5)

denclb6 = Label(window, text="Văn bản được giải mã", font=("Arial", 14))
denclb6.grid(column=0, row=6)
denctxt = Entry(window, width=width)
denctxt.grid(column=1, row=6)

# Tao nut co ten AFbtn
AFbtn = Button(window, text="Mã Hóa", command=mahoa_DES)
AFbtn.grid(column=0, row=7)

# Hoc vien bo sung code de tao nut co ten la DEAFbtn
DEAFbtn = Button(window, text="Giải Mã", command=giaima_DES)
DEAFbtn.grid(column=1, row=7)

selecfileButton = Button(window, text='Chọn file để mã hoá', command=openFile)
selecfileButton.grid(column=0, row=8)

selecfileButton = Button(window, text='Hack', command=hack_execute)
selecfileButton.grid(column=1, row=8)

# Hien thi cua so
window.geometry('1000x400')
window.mainloop()