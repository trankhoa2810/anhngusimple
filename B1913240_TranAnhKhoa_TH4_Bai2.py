# Ho va ten sinh vien: Tran Anh Khoa
# Ma so sinh vien: B1913240

import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
import os
import csv
import random
from pathlib import Path

def hashing(username):
    content = password.get().encode()
    func = random.randint(0, 3)
    if func == 0:
        result = MD5.new(content)
    if func == 1:
        result = SHA1.new(content)
    if func == 2:
        result = SHA256.new(content)
    if func == 3:
        result = SHA512.new(content)
    # Học viên tự cài đặt các phương thức cho SHA256 và SHA512
    rs = result.hexdigest().upper()
    # create records
    directory = os.path.abspath(os.path.join(os.path.curdir))
    file = Path(directory + "/CSDL.csv")
    file.touch(exist_ok=True)
    write_able = True
    with open(directory + "/CSDL.csv", "r") as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            try:
                if(row[0] == username):
                    tk.messagebox.showinfo("Thông báo thất bại.",  "Tài khoản đã tồn tại")
                    write_able = FALSE
            except IndexError:
                print('except block ran')
                continue
    if(write_able == True):
        tk.messagebox.showinfo("Thông báo thành công.",  "Thêm tài khoản thành công")
        with open(directory + "/CSDL.csv", "a") as file_obj:
            csvWriter = csv.writer(file_obj, delimiter=',')
            csvWriter.writerow([username, rs])
    return rs

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")
app_name = Label(window, text="Tạo tài khoản", font=("Arial Bold", 20))
app_name.grid(column=1, row=1)

usernamelb = Label(window, text="Tên đăng nhập", font=("Arial", 14))
usernamelb.grid(column=0, row=3)
username = Entry(window, width=50)
username.grid(column=1, row=3)

passwordlb = Label(window, text="Mật khẩu", font=("Arial", 14))
passwordlb.grid(column=0, row=4)
password = Entry(window, width=50)
password.grid(column=1, row=4)

create_account = Button(window, text="Tạo tài khoản", command= lambda: hashing(username.get()))
create_account.grid(column=1, row=9)

window.geometry('500x200')
window.mainloop()
