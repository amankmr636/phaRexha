from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

class Bill:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Management")
        self.root.geometry("1550x700+0+0")

        self.var=StringVar()
        self.var2=StringVar()

        self.row2 = StringVar()

        self.a1=StringVar()
        self.a2 = StringVar()
        self.a3 = StringVar()
        self.a4 = StringVar()
        self.a5 = StringVar()
        self.a6=StringVar()
        self.a7 = StringVar()

        self.a8 = StringVar()
        self.a9 = StringVar()
        self.a10 = StringVar()


        img = Image.open("C:\lill.png")
        img = img.resize((1300,130))
        self.photoimg = ImageTk.PhotoImage(img)
        labelimg = Label(self.root, image=self.photoimg)
        labelimg.place(x=0, y=0, width=1300, height=90)
        labelttl=Label(self.root,text="Billing Software phaREXHA",font=("times new roman",30,"bold"),bg="white",fg="red")
        labelttl.place(x=0,y=90,width=1540,height=45)

        MainFrame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        MainFrame.place(x=0,y=130,width=1530,height=620)

        #================================Label Frame 1====================================================

        lblframe=LabelFrame(MainFrame,text="Patient",font=("times new roman",13,"bold"),fg="red",bg="white")
        lblframe.place(x=0,y=2,width=300,height=140)

        self.lblbillid=Label(lblframe,text="Bill ID",font=("times new roman",13,"bold"),fg="green",bg="white")
        self.lblbillid.grid(row=0,column=0,padx=5,pady=2)

        self.entrybillid=ttk.Entry(lblframe,font=("times new roman",10,"bold"),width=18,textvariable=self.a1)
        self.entrybillid.grid(row=0,column=1,padx=5,pady=2)

        self.lblbilltype = Label(lblframe, text="Bill Type", font=("times new roman", 13, "bold"), fg="green",bg="white")
        self.lblbilltype.grid(row=1, column=0, padx=5, pady=2)

        billtypecombo = ttk.Combobox(lblframe, width=12, font=("arial", 12, "bold"), state="readonly",textvariable=self.a2)
        billtypecombo["values"] = ( "Medicine","Room","Both")
        billtypecombo.grid(row=1, column=1)
        billtypecombo.current(0)

        self.lblpatid = Label(lblframe, text="Patient ID", font=("times new roman", 13, "bold"), fg="green",bg="white")
        self.lblpatid.grid(row=2, column=0, padx=5, pady=2)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select PatientID from pattable")
        row = mycursor.fetchall()

        lblpatidcombo = ttk.Combobox(lblframe, width=12, font=("arial", 12, "bold"), state="readonly",textvariable=self.a3)
        lblpatidcombo["values"] = row
        lblpatidcombo.grid(row=2, column=1)
        lblpatidcombo.current(0)

        btnadd=Button(lblframe, text="Add", width=7, font=("arial", 12, "bold"), bg="brown", fg="white",
                           pady=2,command=self.add)
        btnadd.grid(row=3, column=0)

        # =============================================Billing Window=========================================

        self.textPresciption = Text(MainFrame, font=("times new roman", 12, "bold"), padx=4,
                                     pady=6,bg="gray",fg="white")
        self.textPresciption.place(x=0, y=160,width=1260,height=320)


        #===========================================Label Frame 2================================================================


        lblframe2=LabelFrame(MainFrame,text="Medicine",font=("times new roman",13,"bold"),fg="red",bg="white")
        lblframe2.place(x=320,y=2,width=300,height=140)

        btnmed = Button(lblframe2, text="Medicine", width=7, font=("arial", 12, "bold"), bg="red", fg="white",
                           pady=2,command=self.search)
        btnmed.grid(row=3, column=0)

        self.qty=Label(lblframe2,text="Qty",font=("times new roman",13,"bold"),fg="green",bg="white")
        self.qty.grid(row=2,column=0,padx=5,pady=2)

        qty2 = ttk.Combobox(lblframe2, width=12, font=("arial", 12, "bold"), state="readonly",textvariable=self.a6)
        qty2["values"] = ("0","1","2","3")
        qty2.grid(row=2, column=1)
        qty2.current(0)

        self.pay5=Label(lblframe2,text="Pay",font=("times new roman", 13, "bold"), fg="green",bg="white",textvariable=self.a4)
        self.pay5.grid(row=0, column=0,padx=5, pady=2)

        pay2 = ttk.Combobox(lblframe2, width=12, font=("arial", 12, "bold"), state="readonly")
        pay2["values"] = ("Cash","Card","UPI")
        pay2.grid(row=0, column=1)
        pay2.current(0)

        self.medic= Label(lblframe2, text="Medicine", font=("times new roman", 13, "bold"), fg="green",bg="white")
        self.medic.grid(row=1, column=0, padx=5, pady=2)


        btncart1 = Button(lblframe2, text="Cart", width=7, font=("arial", 12, "bold"), bg="orange", fg="white", pady=2,
                           command=self.medcart)
        btncart1.grid(row=3, column=1)
        #==========================Label Frame 3==========================================================

        lblframe4 = LabelFrame(MainFrame, text="Room", font=("times new roman", 13, "bold"), fg="red", bg="white")
        lblframe4.place(x=650, y=2, width=350, height=140)

        btnroom = Button(lblframe4, text="Clear", width=7, font=("arial", 12, "bold"), bg="purple", fg="white", pady=2,
                           command=self.search2)
        btnroom.grid(row=3, column=1)


        btncart2 = Button(lblframe4, text="Cart", width=7, font=("arial", 12, "bold"), bg="orange", fg="white", pady=2,
                           command=self.roomcart)
        btncart2.grid(row=3, column=2)

        self.dur = Label(lblframe4, text="Duration", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.dur.grid(row=0, column=0, padx=5, pady=2)

        self.dur2 = ttk.Entry(lblframe4, font=("times new roman", 10, "bold"), width=18, textvariable=self.a7)
        self.dur2.grid(row=0, column=1, padx=5, pady=2)

        self.roomtype = Label(lblframe4, text="Room Type", font=("times new roman", 13, "bold"), fg="green",
                                 bg="white")
        self.roomtype.grid(row=1, column=0, padx=5, pady=2)

        roomtype2 = ttk.Combobox(lblframe4, width=12, font=("arial", 12, "bold"), state="readonly", textvariable = self.a8)
        roomtype2["values"] = ("General", "Single","Large")
        roomtype2.grid(row=1, column=1)
        roomtype2.current(0)

        self.ac = Label(lblframe4, text="AC", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.ac.grid(row=2, column=0, padx=5, pady=2)

        ac2= ttk.Combobox(lblframe4, width=12, font=("arial", 12, "bold"), state="readonly", textvariable = self.a9)
        ac2["values"] = ("Yes", "No")
        ac2.grid(row=2, column=1)
        ac2.current(0)

        #==================Frame 4======================================================================

        lblframe5 = LabelFrame(MainFrame, text="Doctor ID", font=("times new roman", 13, "bold"), fg="red", bg="white")
        lblframe5.place(x=1030, y=2, width=230, height=140)


        self.docid = Label(lblframe5, text="Doctor ID", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.docid.grid(row=0, column=0, padx=5, pady=2)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select DoctorID from doctable")
        row3 = mycursor.fetchall()

        docid2 = ttk.Combobox(lblframe5, width=12, font=("arial", 12, "bold"), state="readonly", textvariable = self.a10)
        docid2["values"] = row3
        docid2.grid(row=0, column=1)
        docid2.current(0)

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("SELECT Medicine FROM consumes WHERE PatientID=%s",(self.a3.get(), ))
        row3 = mycursor.fetchall()


        medcombo = ttk.Combobox(self.root, width=12, font=("arial", 12, "bold"), state="readonly", textvariable = self.a5)
        medcombo["values"] = row3
        medcombo.place(x=413, y=188)

        conn.close()



    def medcart(self):

        self.textPresciption.insert(END,"Medicine:" +self.a5.get()+  "\t\t\t X" +  self.a6.get()+ "\n")

    def add(self):
        self.textPresciption.insert(END, "\t\t\t\t\t\t\t----------Bill----------- \n")
        self.textPresciption.insert(END, "Bill ID: " + self.a1.get() + "\t\tBill Type: " + self.a2.get() + "\t\tPatient ID: " + self.a3.get() + "\t\tDoc ID: " + self.a10.get()+"\n")
    def roomcart(self):
        self.textPresciption.insert(END,"Room: " +self.a8.get()+ "\t\tAC:"+self.a9.get()+ "\t\t\t X" +  self.a7.get()+ "days"+"\n")

    def search2(self):
        self.a1.set("")
        self.a7.set("")
        self.textPresciption.delete("1.0", END)


if __name__ == "__main__":
    root = Tk()
    obj = Bill(root)
    root.mainloop()
