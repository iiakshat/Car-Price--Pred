from tkinter import *
from numpy import array as con
from joblib import load
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ct

model = load("Reg.joblib")

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")


root2 = ct.CTk()
root2.geometry("400x470")
root2.resizable(False,False)
root2.title("Car Price Calculator")
root2.iconbitmap("files/logo1.ico")

root = ct.CTkFrame(root2, width=350, corner_radius=6, height=350)
root.pack(pady=20, padx=6)

# fn = ("Comic Sans MS", 14, "bold")
fn = ("Helvetica", 14, "bold")
fn2 = ("Helvetica", 11, "bold")
fn3 = ("Helvetica", 12, "bold")

img = ImageTk.PhotoImage(Image.open("files/txt.png"))
imag = Label(root,image=img, borderwidth=0)
imag.grid(row=0,column=0,columnspan=2,padx=(100,0),pady=(20,0))


nam = ct.StringVar(value="Choose Model")
fue = ct.StringVar(value="Petrol")
tra = ct.StringVar(value="Automatic")
own = ct.StringVar(value="First")


co = sorted(["Audi", "Mercedes", "Honda", "Maruti", "Tata","Hyundai", "Mahindra", "Volkswagen", "Land Rover", "Renault", "BMW",
        "Toyota", "Kia", "Ford", "Jaguar","Chevrolet", "Suzuki"])
fuel = ["CNG", "Petrol", "Diesel", "LPG", "Electric"]
trans= ["Automatic", "Manual"]
owner = ["First", "Second", "Third", "Fourth & Above"]



ct.CTkLabel(root, text="Brand : ", font=fn).grid(row=1,column=0,stick=W, pady=(20,0),padx=(30,0))
ct.CTkLabel(root, text="Year : ", font=fn).grid(row=2,column=0,stick=W,padx=(30,0))
ct.CTkLabel(root, text="KMs Travelled : ", font=fn).grid(row=3,column=0, padx=(18,5))
ct.CTkLabel(root, text="Fuel Type : ", font=fn).grid(row=4,column=0, padx=(2,20))
ct.CTkLabel(root, text="Trasmission : ", font=fn).grid(row=5,column=0)
ct.CTkLabel(root, text="Owner Type : ", font=fn).grid(row=6,column=0)
ct.CTkLabel(root, text="Power :", font=fn).grid(row=7,column=0, padx=(0,44))
ct.CTkLabel(root, text="bhp", font=fn).grid(row=7,column=2, padx=(0,100),pady=1)
ct.CTkLabel(root, text="Mileage : ", font=fn).grid(row=8,column=0, padx=(0,30),pady=1)
ct.CTkLabel(root, text="kmpl", font=fn).grid(row=8,column=2, padx=(0,100))
ct.CTkLabel(root, text="Engine : ", font=fn).grid(row=9,column=0, padx=(0,35))
ct.CTkLabel(root, text="CC", font=fn).grid(row=9,column=2, padx=(0,100))


# Entries :
y = ct.CTkEntry(root, width=150,height=24, corner_radius=6, placeholder_text="2012 or 11", placeholder_text_color="gray", font=fn3)
y.grid(row=2, column=1, padx=30, columnspan=2)

kt = ct.CTkEntry(root, width=150,height=24, corner_radius=6, font=fn3)
kt.grid(row=3, column=1, padx=30, columnspan=2)

po = ct.CTkEntry(root, width=80,height=24, corner_radius=6, font=fn3)
po.grid(row=7, column=1, padx=(64,0))

mi = ct.CTkEntry(root, width=80,height=24, corner_radius=6, font=fn3)
mi.insert(0,"20")
mi.grid(row=8, column=1, padx=(64,0))

e = ct.CTkEntry(root, width=80,height=24, corner_radius=6, font=fn3)
e.grid(row=9, column=1, padx=(64,0))

# Options :
n = ct.CTkComboBox(master=root,border_width=1,corner_radius=3 ,variable=nam, values=co,button_color="#2786c6", button_hover_color="#f7622a",dropdown_font=fn2)
n.configure(width=150)
n.grid(row=1,column=1, columnspan=2, pady=(20,0))

f = ct.CTkComboBox(master=root,border_width=1,corner_radius=3 ,variable=fue, values=fuel,button_color="#2786c6", button_hover_color="#f7622a",dropdown_font=fn2)
f.configure(width=150)
f.grid(row=4,column=1, columnspan=2, pady=1)

t = ct.CTkComboBox(master=root,border_width=1,corner_radius=3 ,variable=tra, values=trans,button_color="#2786c6", button_hover_color="#f7622a",dropdown_font=fn2)
t.configure(width=150)
t.grid(row=5,column=1, columnspan=2, pady=1)

o = ct.CTkComboBox(master=root,border_width=1,corner_radius=3 ,variable=own, values=owner,button_color="#2786c6", button_hover_color="#f7622a",dropdown_font=fn2)
o.configure(width=150)
o.grid(row=6,column=1, columnspan=2, pady=1)

def fetch():
    t = {"Automatic" : 0, "Manual" : 1}
    f = {"CNG" :0, "Petrol" : 1, "Diesel" : 2, "LPG" : 3, "Electric" : 4}
    oe ={"First" :0, "Second" : 1, "Third" : 2, "Fourth & Above" : 3}
    yv = y.get()
    if int(yv)>1500: yv = 2023-int(yv)
    l = [yv, int(kt.get()), int(f[fue.get()]),int(t[tra.get()]), int(oe[own.get()]), float(po.get()), float(mi.get()), int(e.get())]
    l = con([l])
    pred = model.predict(l)
    pred= pred[0]
    if pred>99:
        messagebox.showinfo("Price",f"This Car Will Cost Around {pred} Crore Rs.\nClick 'Ok' To Continue.")
    elif pred<1:
        messagebox.showinfo("Price",f"This Car Will Cost Around {pred*10}0000 Rs.\nClick 'Ok' To Continue.")
    else:
        messagebox.showinfo("Price",f"This Car Will Cost Around {pred} Lakh Rs.\nClick 'Ok' To Continue.")

submit = ct.CTkButton(root, text="Calculate Price",command=fetch, width=40,height=30, corner_radius=12, hover_color="#f7622a", font=fn)
submit.grid(row=10,column=0, columnspan=3, pady=20,padx=(0,50))
root2.mainloop()