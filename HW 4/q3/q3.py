import shelve
from tkinter import messagebox
from tkinter import *

data = shelve.open("database")
root = Tk()
root.geometry("500x300")
root.title("CSE 337 Phonebook")

def openWindow():
    def addRecord():
        if (nametxt.get() == "" or phonenum.get() == "" or addrtxt.get() == "" or pbvar.get() == ""):
            cr.withdraw()
            messagebox.showerror("Error",  "Missing/invalid fields")
        else:
            data[nametxt.get()] = [phonenum.get(), addrtxt.get(), pbvar.get()]
            nametxt.delete(0, END)
            phonenum.delete(0, END)
            addrtxt.delete(0, END)
            pbvar.set("")
            cr.withdraw()
            messagebox.showinfo("Saved", "Record saved.")
        
    cr = Toplevel(root)
    pbvar = StringVar()
    pbvar.set("Personal")
    namelabel = Label(cr, text="Name")
    nametxt = Entry(cr, width=50)
    phonelabel = Label(cr, text="Phone")
    phonenum = Entry(cr, width=50)
    addrlabel = Label(cr, text="Address")
    addrtxt = Entry(cr, width=50)
    radiop = Radiobutton(cr, text="Personal", variable=pbvar, value="Personal", tristatevalue="tst")
    radiob = Radiobutton(cr, text="Business", variable=pbvar, value="Business", tristatevalue="tst")
    savebtn = Button(cr, text="Save record", width=30, command=addRecord)

    namelabel.grid(row=0, column=0)
    nametxt.grid(row=0, column=1)
    phonelabel.grid(row=1, column=0)
    phonenum.grid(row=1, column=1)
    addrlabel.grid(row=2, column=0)
    addrtxt.grid(row=2, column=1)
    radiop.grid(row=3, column=0)
    radiob.grid(row=3, column=1)
    savebtn.grid(row=4)

def searchRecord():
    def search():
        if searchname.get() in data:
            recfound.insert(END, "Record found:")
            namefound.insert(END, searchname.get())
            phonefound.insert(END, data[searchname.get()][0])
            addrfound.insert(END, data[searchname.get()][1])
            typefound.insert(END, data[searchname.get()][2])
        else:
            recfound.insert(END, "Record does not exist:")
    sr = Toplevel(root)
    snamelbl = Label(sr, text="Name")
    searchname = Entry(sr, width=50)
    recfound = Text(sr, width=30, height=1)
    namefound = Text(sr, width=30, height=1)
    phonefound = Text(sr, width=30, height=1)
    addrfound = Text(sr, width=30, height=1)
    typefound = Text(sr, width=30, height=1)
    searchbtn = Button(sr, text="Search", command=search)
    snamelbl.grid(row=0, column=0)
    searchname.grid(row=0, column=1)
    recfound.grid(row=1, columnspan=2)
    namefound.grid(row=2, columnspan=2)
    phonefound.grid(row=3, columnspan=2)
    addrfound.grid(row=4, columnspan=2)
    typefound.grid(row=5, columnspan=2)
    searchbtn.grid(row=6, columnspan=2)

def deleteRecord():
    def delete():
        if deletename.get() in data:
            del data[deletename.get()]
            messagebox.showinfo("Delete", "Record succesfully deleted.")
            deletename.delete(0, END)
        else:
            messagebox.showerror("Delete", "Record does not exist.\nFailed to delete.")
            deletename.delete(0, END)
    dr = Toplevel(root)
    dr.geometry("500x50")
    dnamelbl = Label(dr, text="Name")
    deletename = Entry(dr, width=50)
    deletebtn = Button(dr, text="Delete", width=30, command=delete)
    dnamelbl.pack(side=LEFT)
    deletename.pack(side=LEFT)
    deletebtn.pack(side=LEFT)

def showAll():
    sa = Toplevel(root)
    sa.geometry("800x50")
    size = 1
    counter = 0
    for record in data:
        nr = Text(sa, width=25, height=1)
        pr = Text(sa, width=15, height=1)
        ar = Text(sa, width=35, height=1)
        tr = Text(sa, width=25, height=1)
        nr.insert(END, record)
        pr.insert(END, data[record][0])
        ar.insert(END, data[record][1])
        tr.insert(END, data[record][2])
        nr.grid(row=counter, column=0)
        pr.grid(row=counter, column=1)
        ar.grid(row=counter, column=2)
        tr.grid(row=counter, column=3)
        counter += 1
        size += 1
    
    strsize = "800x" + str(size * 20)
    sa.geometry(strsize)

#make widgets
ce_record = Button(root, text="Create/Edit Record", width=30, command=openWindow)
s_record = Button(root, text="Search Record", width=30, command=searchRecord)
d_record = Button(root, text="Delete Record", width=30, command=deleteRecord)
show_records = Button(root, text="Show All Records", width=30, command=showAll)

ce_record.pack()
s_record.pack()
d_record.pack()
show_records.pack()

root.mainloop()
