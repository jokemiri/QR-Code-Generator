from tkinter import *
import qrcode
import PIL
from PIL import Image

root = Tk()
root.title('QR Code Generator')
root.geometry('1000x550')
root.config(bg='#AE2321')
root.resizable(False, False)

#window icon
image_icon = PhotoImage(file='icon.png')
root.iconphoto(False, image_icon)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save('QRCode/'+ str(name)+'.png')

    global Image
    Image = PhotoImage(file='QRCode/'+ str(name)+'.png')
    Image_view.config(image=Image)
    
Image_view = Label(root, bg='#AE2321')
Image_view.pack(pady=10, side=RIGHT)

Label(root, text='Title', fg='white', bg='#AE2321', font=15).place(x=50, y=170)
title=Entry(root, width=13, font='arial 15')
title.place(x=50, y=200)

entry=Entry(root, width=28, font='arial 15')
entry.place(x=50, y=250)

generate_button = Button(root, text='Generate', width=20, height=2, bg='black', fg='white', command=generate)
generate_button.place(x=50, y=300)

root.mainloop()