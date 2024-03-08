from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x850+0+0")
        
        
        
        
        #************VARIABLE DECLEARATION**************************
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()

        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="blue",fg="green",bd=20,
                       relief=RIDGE,font=("time new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1550,height=410)
        
        # ***************DATA FRAME LEFT************************
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("time new roman",15,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=860,height=370)
        
        lblMemebr=Label(DataFrameLeft,bg="powder blue",textvariable=self.member_var,text="Member Type:",font=("time new roman",13,"bold"),padx=2,pady=6)
        lblMemebr.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",13,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)
        
        lblPRN_NO=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN NO:",padx=4,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        lblPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        lblPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile No:",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        lblMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        lblBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        lblBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        lblBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        lblBookTitle.grid(row=1,column=3)
        
        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        lblAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
        lblAuther.grid(row=2,column=3)
        
        # lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,pady=6,bg="powder blue")
        # lblAuther.grid(row=2,column=2,sticky=W)
        # lblAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        # lblAuther.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        lblDateBorrowed.grid(row=3,column=3,sticky=W)
        
        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        lblDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        lblDateDue.grid(row=4,column=3,sticky=W)
        
        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        lblDaysOnBook.grid(row=5,column=3,sticky=W)
        
        lbllateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lbllateReturnFine.grid(row=6,column=2,sticky=W)
        lbllateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        lbllateReturnFine.grid(row=6,column=3,sticky=W)
        
        lblOvedate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="powder blue")
        lblOvedate.grid(row=7,column=2,sticky=W)
        lblOvedate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        lblOvedate.grid(row=7,column=3,sticky=W)
        
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        lblActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice,width=29)
        lblActualPrice.grid(row=8,column=3,sticky=W)
        
        
        
        #****************DATAFRAME RIGHT************************************
        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,bg="powder blue",
                                    font=("arial",12,"bold"),text="Book Details")
        DataFrameRight.place(x=870,y=5,width=580,height=368)
        
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScroolbar=Scrollbar(DataFrameRight)
        listScroolbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=['Hindi','English','Maths','Physics','Chemistry','Biology','Geography','History','Civise','Economics','Home Science','Physpholy','Dental','Neuro Surjen'
                   ,'C Programming','C++ Programming','Networking','Pyhton','Degital Electronics','Graphics and Multimedia,',
                   'My Sql','PHP','Java Script','Perl','Linux','Operating System','Software Engerring','SAD']
        
        
        def select_Book(event=""):
            selected_index = listBox.curselection()
            if selected_index:  # Check if an item is selected
                values = str(listBox.get(selected_index))
                print(values)  # Print the selected value for debugging purposes

                if values == "Hindi":
                    self.bookid_var.set("BKID1456")
                    self.booktitle_var.set("Literature")  # Corrected spelling
                    self.auther_var.set("KC Sinha")  # Corrected author name format

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹258")
                else:
                    print("no")

                
        
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",select_Book)
        listBox.grid(row=0,column=0,padx=4)
        listScroolbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
            
        
        #***************BUTTON FRAME********************
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1550,height=70)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="ADD DATA",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,command=self.showData,text="SHOW DATA",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,text="UPDATE",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.delete,text="DELETE",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,command=self.reset,text="RESET",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=5) 
        
        #***************INFORMATION FRAME********************
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="cyan")
        FrameDetails.place(x=0,y=600,width=1530,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1470,height=170)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname",
                                                            "address1","address2","postid","mobile","bookid",
                                                            "booktitle","auther","dateborrowed","datedue","days",
                                                            "latereturnfine","dateoverdue","finalprice"),
                                                             xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PNR No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID:")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID:")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="lms")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO library VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                 self.member_var.get(),
                                                                                                                 self.prn_var.get(),
                                                                                                                 self.id_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.address1_var.get(),
                                                                                                                 self.address2_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.mobile_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.auther_var.get(),
                                                                                                                 self.dateborrowed_var.get(),
                                                                                                                 self.datedue_var.get(),
                                                                                                                 self.daysonbook.get(),
                                                                                                                 self.lateratefine_var.get(),
                                                                                                                 self.dateoverdue.get(),
                                                                                                                 self.finalprice.get()
                                                                                                            ))
        
        conn.commit()
        self.fetch_data
        conn.close()
        messagebox.showinfo("Success","Member Has Been inserted sucessfully")
        
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="lms")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Membertype=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,Bookborrowed=%s,Auther=%s,datedue=%s,daysofbook=%s,latereturnfine=%s,dateovedue=%s,finalprice=%s where PNR_NO=%s",(
            
                                                                                                                 self.member_var.get(),
                                                                                                                 
                                                                                                                 self.id_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.address1_var.get(),
                                                                                                                 self.address2_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.mobile_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.auther_var.get(),
                                                                                                                 self.dateborrowed_var.get(),
                                                                                                                 self.datedue_var.get(),
                                                                                                                 self.daysonbook.get(),
                                                                                                                 self.lateratefine_var.get(),
                                                                                                                 self.dateoverdue.get(),
                                                                                                                 self.finalprice.get(),
                                                                                                                 self.prn_var.get()
                                                                                                                 
                                                                                        ))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Sucess","Member Has been Updated")
        
        
        
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="lms")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+ "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+self.prn_var.get()+ "\n")
        self.txtBox.insert(END,"ID No:\t\t"+self.id_var.get()+ "\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstname_var.get()+ "\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+ "\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+ "\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+ "\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+ "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+ "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+ "\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+ "\n")
        self.txtBox.insert(END,"Auther\t\t"+self.auther_var.get()+ "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+ "\n")
        self.txtBox.insert(END,"DateDue\t\t"+self.datedue_var.get()+ "\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.daysonbook.get()+ "\n")
        self.txtBox.insert(END,"LateRateFine\t\t"+self.lateratefine_var.get()+ "\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue.get()+ "\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+self.finalprice.get()+ "\n")
        
    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set(""),
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.lateratefine_var.set("")
        self.dateoverdue.set("")
        self.finalprice.set("")
        self.txtBox.delete("1.0",END)
        
    def iExit(self):
        iExit=messagebox.askyesno("Library management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the member")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="",database="lms")
             my_cursor=conn.cursor()
             query="DELETE FROM library WHERE PRN_NO=%s"
             value=(self.prn_var.get(),)
             my_cursor.execute(query,value)

             
             conn.commit()
             self.fetch_data()
             self.reset()
             conn.close()
             
             messagebox.showinfo("Sucess","Member has been deleted")
        
if __name__== "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)        
    root.mainloop()
        
