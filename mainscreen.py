from tkinter import *
from database import *

root=Tk()
#Var
id=StringVar
name=StringVar
year=StringVar
root.title('Quản lý học sinh')
root.minsize (height=500, width=500)
Label(root, text="ỨNG DỤNG QUẢN LÝ SINH VIÊN", fg="lime", font=("Lora",15),width=50).grid(row=0)
listbox=Listbox(root, width=80, height=20)
listbox.grid(row=1, columnspan=2)

Label(root,text="Mã SV:").grid(row=2, column=0)
Entry(root,width=30,textvariable=id).grid(row=2, column=1)

Label(root,text="Tên SV:").grid(row=3, column=0)
Entry(root,width=30,textvariable=name).grid(row=3, column=1)

Label(root,text="Năm sinh:").grid(row=4, column=0)
Entry(root,width=30,textvariable=year).grid(row=4, column=1)
def show():
    sv=read()
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)

def add():
    line=id.get()+'-'+name.get()+'-'+year.get()
    save(line)
    show()

button=Frame(root)
Button(button, text='Thêm',command=add).pack(side=LEFT)
Button(button, text='Xem').pack(side=LEFT)
Button(button, text='Sắp xếp').pack(side=LEFT)
Button(button, text='Thoát',command=root.quit).pack(side=LEFT)
button.grid(row=5, column=1)

show()
root.mainloop()