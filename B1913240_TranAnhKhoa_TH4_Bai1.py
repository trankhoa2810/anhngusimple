# Ho va ten sinh vien: Tran Anh Khoa
# Ma so sinh vien: B1913240

from tkinter import *
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64

def hashing():
    content = plaintxt.get().encode()
    func = hashmode.get()
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
    hashvalue.delete(0,END)
    hashvalue.insert(INSERT,rs)

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")
app_name = Label(window, text="CHƯƠNG TRÌNH BĂM", font=("Arial Bold", 20))
app_name.grid(column=1, row=1)
plainlb0 = Label(window, text="Văn bản", font=("Arial", 14))
plainlb0.grid(column=0, row=3)
plaintxt = Entry(window, width=95)
plaintxt.grid(column=1, row=3)

# radio
radioGroup = LabelFrame(window, text = "Hàm băm")
radioGroup.grid(row=4, column=1)
hashmode = IntVar()
hashmode.set(-1)

# md5
md5_func = Radiobutton(radioGroup,
    text="Hash MD5",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=0,
    command=hashing)
md5_func.grid(row=4, column=0)

# sha1
sha1_func = Radiobutton(radioGroup,
    text="Hash SHA1",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=1,
    command=hashing)
sha1_func.grid(row=5, column=0)

# sha256
sha1_func = Radiobutton(radioGroup,
    text="Hash SHA256",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=2,
    command=hashing)
sha1_func.grid(row=6, column=0)

# sha512
sha1_func = Radiobutton(radioGroup,
    text="Hash SHA512",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=3,
    command=hashing)
sha1_func.grid(row=7, column=0)

# hash out put
hash_out_put = Label(window, text="Giá trị băm", font=("Arial", 14))
hash_out_put.grid(column=0, row=5)
hashvalue = Entry(window, width=95)
hashvalue.grid(column=1, row=5)

# Tương tự đối với sha256 và sha512
window.geometry('800x500')
window.mainloop()
