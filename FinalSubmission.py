from tkinter import *
from tkinter import ttk
import tkinter as tk
from sqlalchemy import create_engine
import pandas as pd
from turtle import bgcolor
from PIL import ImageTk, Image  
import tkinter.font as tkFont

database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library')
LARGEFONT = ("Verdana",15)

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side= "top",fill="both",expand = True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.attributes("-fullscreen", True) # only tk() can fullscreen. 

        self.frames = {}

        self.shared_data = {
                "memberid" : tk.StringVar()
            }

        for F in (ALSMainPage, Membership, MemberCreation, MemberDeletion, MemberUpdate,
                  Fines, FinesPayment,
                  CancelReservation, Reservations, BookReserve, Books, BookAcquisition,
                  BookWithdrawal, Loans ,BookBorrow, BookReturn, Reports, booksOnLoan,
                  BookSearch, booksOnReservation, outstandingFines,
                  BooksOnLoanToMember):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(ALSMainPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class ALSMainPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=100)
        label =ttk.Label(self, text = "ALS", font = fontstyle)
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)
        frame2 = tk.Frame(self)
        frame2.pack(expand=True)

        button1 = tk.Button(frame,text = "Membership", bg="#FFFFE7", command = lambda : controller.show_frame(Membership))
        button1.grid(row=0, column=1, ipady=100, ipadx=100)
        button2 = tk.Button(frame,text= "Books", bg="#B3F7FF", command = lambda : controller.show_frame(Books))
        button2.grid(row=0, column=2, ipady=100, ipadx=100)
        button3 = tk.Button(frame,text = "Loans", bg="#FF8706", command = lambda : controller.show_frame(Loans))
        button3.grid(row=0, column=3, ipady=100, ipadx=100)

        button4 = tk.Button(frame2,text= "Reservations", bg="#CD9FDA", command = lambda : controller.show_frame(Reservations))
        button4.grid(row=0, column=1, ipady=100, ipadx=100)
        button5 = tk.Button(frame2,text = "Fines", bg="#FFC7E7", command = lambda : controller.show_frame(Fines))
        button5.grid(row=0, column=2, ipady=100, ipadx=100)
        button6 = tk.Button(frame2,text= "Reports", bg="#FFFF85", command = lambda : controller.show_frame(Reports))
        button6.grid(row=0, column=3, ipady=100, ipadx=100)

class Membership(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        fontstyle = tkFont.Font(family="Lucida Grande", size=70)
        label = tk.Label(self, text = "Select one of the Options below:", font = fontstyle)
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        """
        image1 = Image.open("/Users/choonleng/Downloads/dannyboy.jpeg") # dannyboy not fking working
        test = ImageTk.PhotoImage(image1)
        label1 = ttk.Label(frame, image = test)
        label1.pack(side = LEFT)
        """

        angelstyle = tkFont.Font(family="Lucida Grande", size=50)

        button1 = tk.Button(frame,text = "1. Creation", bg="#CD9FDA", command = lambda : controller.show_frame(MemberCreation), font = angelstyle)
        button1.grid(row=0,column=0,ipady=40, ipadx=197)
        button2 = tk.Button(frame,text = "2. Deletion", bg="#CD9FDA", command = lambda : controller.show_frame(MemberDeletion), font = angelstyle)
        button2.grid(row=1,column=0,ipady=40, ipadx=200)
        button3 = tk.Button(frame,text = "3. Update", bg="#CD9FDA", command = lambda : controller.show_frame(MemberUpdate), font = angelstyle)
        button3.grid(row=2,column=0,ipady=40, ipadx=215)

        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)

        button4 = tk.Button(ButtonFrame,text = "Back To Main Menu", command = lambda : controller.show_frame(ALSMainPage)) # height=100, width=500,
        button4.grid(row=0,column=0,ipady=30, ipadx=70) # grid(ipady=100, ipadx=100)


class MemberCreation(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        fontstyle = tkFont.Font(family="Lucida Grande", size=40)
        label = ttk.Label(self, text = "To create Member, Please Enter Requested Information Below:", font = fontstyle)
        label.pack(expand=True)

        mainFrame = tk.Frame(self) # encapsulates the label entry pair. 
        mainFrame.pack(expand=True)

        bottomF = tk.Frame(self) # encapsulates the buttons
        bottomF.pack(expand=True)

        f1 = tk.Frame(mainFrame) # stacked inside the mainframe. 
        f1.pack(expand=True)

        f2 = tk.Frame(mainFrame)
        f2.pack(expand=True)

        f3 = tk.Frame(mainFrame)
        f3.pack(expand=True)

        f4 = tk.Frame(mainFrame)
        f4.pack(expand=True)

        f5 = tk.Frame(mainFrame)
        f5.pack(expand=True)

        memberlabel = Label(f1,text="Membership ID")
        memberlabel.grid(row=0,column=0,ipady=40, ipadx=70)
        member_id_entry = Entry(f1)
        member_id_entry.grid(row=0,column=1,ipady=40, ipadx=130)
        
        namelabel = Label(f2,text="Name")
        name_entry = Entry(f2)
        namelabel.grid(row=0,column=0,ipady=40, ipadx=95)
        name_entry.grid(row=0,column=1,ipady=40, ipadx=130)

        facultylabel = Label(f3,text="Faculty")
        faculty_entry = Entry(f3)
        facultylabel.grid(row=0,column=0,ipady=40, ipadx=90)
        faculty_entry.grid(row=0,column=1,ipady=40, ipadx=130)
        
        phonelabel = Label(f4,text="Phone Number")
        phone_entry = Entry(f4)
        phonelabel.grid(row=0,column=0,ipady=40, ipadx=70)
        phone_entry.grid(row=0,column=1,ipady=40, ipadx=130)
        

        emaillabel = Label(f5,text="Email Address")
        email_entry = Entry(f5)
        emaillabel.grid(row=0,column=0,ipady=40, ipadx=75)
        email_entry.grid(row=0,column=1,ipady=40, ipadx=130)

        def memberCreate():

    
            memberid = member_id_entry.get()
            name = name_entry.get()
            faculty = faculty_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()

            allmembers = pd.read_sql_query("SELECT * FROM Member",database).values


            if len(memberid) != 0 and len(name) != 0 and len(faculty) != 0 and (len(phone) == 8) and ("@als.edu" in email) and memberid not in allmembers  :
                
                query = f"INSERT INTO Member VALUES ('{memberid}','{name}','{faculty}','{phone}','{email}');"
                database.execute(query)
                                        
                member_id_entry.delete(0, END)
                name_entry.delete(0, END)
                faculty_entry.delete(0, END)
                phone_entry.delete(0, END)
                email_entry.delete(0, END)
                
                win = tk.Toplevel()
                frame = tk.Frame(win) #width = 400, height = 1000
                frame.pack(expand=True)
                # win.geometry('400x1000')
                style1 = tkFont.Font(family="Lucida Grande", size=50)
                l = tk.Label(frame, text = "Success!", font = style1)
                l.pack(expand=True)
                style2 = tkFont.Font(family="Lucida Grande", size=30)
                l2 = tk.Label(frame, text = "ALS Membership created.", font = style2)
                l2.pack(expand=True)
                b = tk.Button(frame, height = 50, width = 100, text = "Back to Create Function.", command = lambda : [win.destroy(),controller.show_frame(MemberCreation)])
                b.pack(expand=True)
                
            else :

                member_id_entry.delete(0, END)
                name_entry.delete(0, END)
                faculty_entry.delete(0, END)
                phone_entry.delete(0, END)
                email_entry.delete(0, END)
                
                win = tk.Toplevel()
                frame = tk.Frame(win, width = 400, height = 700)
                frame.pack(expand=True)
                fontstyle = tkFont.Font(family="Lucida Grande", size=100)
                l = tk.Label(frame, text = "Error!", font = fontstyle) 
                l.pack(expand=True)

                style2 = tkFont.Font(family="Lucida Grande", size=30)
                l2 = ttk.Label(frame, text = "Member already exists; Missing or incomplete fields.", font = style2)
                l2.pack(expand=True)

                b = tk.Button(frame, text = "Back to Create Function.", command = lambda : [win.destroy(),controller.show_frame(MemberCreation)])
                b.pack(expand=True)
        
        button1 = tk.Button(bottomF,text="Create Member", command = memberCreate)
        button1.grid(row=0,column=0,ipady=50, ipadx=100)
        button2 = tk.Button(bottomF,text="Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button2.grid(row=0,column=1,ipady=50, ipadx=100)

# above all done!

class MemberDeletion(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        fontstyle = tkFont.Font(family="Lucida Grande", size=50)
        label = tk.Label(self,text = "To Delete Member, Please Enter Membership ID:", font = fontstyle, bg="red")
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        fsv = tkFont.Font(family="Lucida Grande", size=30)
        memberlabel = tk.Label(frame,text="Membership ID", font = fsv) # possible
        memberlabel.grid(row=0, column=0, ipady=100, ipadx=80)
        memberid_entry = Entry(frame)
        memberid_entry.grid(row=0, column=1, ipady=100, ipadx=150)

        def memberDelete():
            

            memberid = memberid_entry.get()

            query1 = f"SELECT COUNT(*) FROM Borrows WHERE memberID = '{memberid}' GROUP BY memberID"
            query2 = f"SELECT COUNT(*) FROM Reserves WHERE memberID = '{memberid}' GROUP BY memberID"
            query3 = f"SELECT COUNT(*) FROM Fine WHERE memberID = '{memberid}' GROUP BY memberID"
            loanscount = (pd.read_sql_query(query1,database)).count()
            reservecount = (pd.read_sql_query(query2,database)).count()
            fines = (pd.read_sql_query(query3,database)).count()

            if (loanscount != 0).all() | (fines != 0).all() :  #(reservecount != 0).all() |

                
                win = tk.Toplevel()
                
                memberid_entry.delete(0, END)
                
                l = tk.Label(win,text = "Error! Member has loans, reservations or outstanding fines")
                l.grid(row=5,column=0)
                b = ttk.Button(win, text = "Back to delete function.", command = win.destroy)
                b.grid(row=8,column=0)

            
            else :

                query4 = f"SELECT * FROM Member WHERE memberID = '{memberid}'"
                infolist = pd.read_sql_query(query4,database).values.tolist()
                showmemberid = infolist[0][0]
                showname = infolist[0][1]
                showfaculty = infolist[0][2]
                showphone = infolist[0][3]
                showemail = infolist[0][4]

                def confirmDelete():


                    query5 = f"DELETE FROM Member WHERE memberID = '{memberid}'"
                    database.execute(query5)
                    


                win = tk.Toplevel()
                # fgknot = tkFont.Font(family="Lucida Grande", size=40)
                #label = tk.Label(win, text = "Please Confirm Details to Be Correct") #, font = fgknot)
                #label.pack(expand=True)

                framery = tk.Frame(win)
                framery.pack(expand=True)
                
                l = tk.Label(framery, text = str(showmemberid))
                l.grid(row=0,column=0,ipady=30, ipadx=70)
                p = tk.Label(framery, text = str(showname))
                p.grid(row=1,column=0,ipady=30, ipadx=70)
                t = tk.Label(framery, text = str(showfaculty))
                t.grid(row=2,column=0,ipady=30, ipadx=70)
                q = tk.Label(framery, text = str(showphone))
                q.grid(row=3,column=0,ipady=30, ipadx=70)
                w = tk.Label(framery, text = str(showemail))
                w.grid(row=4,column=0,ipady=30, ipadx=70)

                memberid_entry.delete(0, END)

                framerybutton = tk.Frame(win)
                framerybutton.pack(expand=True)
                
                b1 = ttk.Button(framerybutton, text = "confirm deletion", command = lambda : [win.destroy(),confirmDelete()])
                b1.grid(row=0, column=0, ipady=50, ipadx=100)
                b2 = ttk.Button(framerybutton, text = "Back to delete function", command = lambda : [win.destroy(),controller.show_frame(MemberDeletion)])
                b2.grid(row=0, column=1, ipady=50, ipadx=100)
                
        frame2 = tk.Frame(self)
        frame2.pack(expand=True)
        
        button1 = ttk.Button(frame2,text="Delete Member",command = memberDelete)
        button1.grid(row=0, column=0, ipady=50, ipadx=100)
        button2 = ttk.Button(frame2,text="Back to Membership Menu", command = lambda : controller.show_frame(Membership))
        button2.grid(row=0, column=1, ipady=50, ipadx=100)


    

class MemberUpdate(tk.Frame):
    
    def __init__(self,parent,controller):
        
        tk.Frame.__init__(self,parent)
        self.controller = controller

        fontstyle = tkFont.Font(family="Lucida Grande", size=40)
        label = tk.Label(self,text = "To Update a Member, Please Enter Membership ID:", font = fontstyle, bg="green")
        label.pack(expand=True)

        global memberid_entry

        frame = tk.Frame(self)
        frame.pack(expand=True)

        sizer = tkFont.Font(family="Lucida Grande", size=25)
        memberlabel = tk.Label(frame,text="Membership ID", font = sizer)
        memberlabel.grid(row=0, column=0, ipady=50, ipadx=80)
        memberid_entry = Entry(frame)
        memberid_entry.grid(row=0, column=1, ipady=50, ipadx=140)

        def MemberUpdatePageTwo():
            
            win = tk.Toplevel()
            style2= tkFont.Font(family="Lucida Grande", size=25)
            label = ttk.Label(win,text = "Please Enter Requested Information Below:",font = style2)
            label.pack(expand=True)

            middleFrame = tk.Frame(win)
            middleFrame.pack(expand=True)

            leftFrame = tk.Frame(middleFrame)
            leftFrame.pack(side = LEFT, expand=True)

            rightFrame = tk.Frame(middleFrame)
            rightFrame.pack(side = LEFT, expand=True)
            
            memberlabel = Label(leftFrame, text = "Membership ID")
            memberlabel.grid(row=0, column=0, ipady=30, ipadx=70)
            memberidlabel = Label(rightFrame,text = memberid_entry.get())
            memberidlabel.grid(row=0, column=0, ipady=30, ipadx=140)
            
            global memberidtravel
            memberidtravel = memberid_entry.get()
            
            global name,faculty,phone,email
            
            namelabel = Label(leftFrame,text="Name")
            name = Entry(rightFrame)
            namelabel.grid(row=1, column=0, ipady=30, ipadx=70)
            name.grid(row=1, column=0, ipady=30, ipadx=140)
            
         
            
            facultylabel = Label(leftFrame,text="Faculty")
            faculty = Entry(rightFrame)
            facultylabel.grid(row=2, column=0, ipady=30, ipadx=70)
            faculty.grid(row=2, column=0, ipady=30, ipadx=140)

      

            phonelabel = Label(leftFrame, text = "Phone Number")
            phone = Entry(rightFrame)
            phonelabel.grid(row=3, column=0, ipady=30, ipadx=70)
            phone.grid(row=3, column=0, ipady=30, ipadx=140)

     

            emaillabel = Label(leftFrame,text="Email Address")
            email= Entry(rightFrame)
            emaillabel.grid(row=4, column=0, ipady=30, ipadx=70)
            email.grid(row=4, column=0, ipady=30, ipadx=140)

            memberid_entry.delete(0, END)
              
            def memberUpdate():

                global newname, newfaculty, newphone, newemail
                newname = name.get()
                newfaculty = faculty.get()
                newphone = phone.get()
                newemail = email.get()
                
                global memberidtravel2
                memberidtravel2 = memberidtravel

                if len(newname) == 0 or len(newfaculty) == 0 or len(newphone) != 8 or "@als.edu" not in newemail:

                    win2 = tk.Toplevel()
                    l = tk.Label(win2,text = "Error! Missing or incomplete fields")
                    l.grid(row=5,column=0)
                    b = ttk.Button(win2,text = "Back to Update function.", command = lambda : [win2.destroy(), controller.show_frame(MemberUpdate)])
                    b.grid(row=8,column=3)

                else :

                    def confirmUpdate() :

                        query1 = f"UPDATE Member SET name = '{newname}' WHERE memberID = '{memberidtravel2}'"
                        query2 = f"UPDATE Member SET faculty = '{newfaculty}' WHERE memberID = '{memberidtravel2}'"
                        query3 = f"UPDATE Member SET phone = '{newphone}' WHERE memberID = '{memberidtravel2}'"
                        query4 = f"UPDATE Member SET email = '{newemail}' WHERE memberID = '{memberidtravel2}'"
                        database.execute(query1)
                        database.execute(query2)
                        database.execute(query3)
                        database.execute(query4)

                        win4 = tk.Toplevel()
                        success = tk.Label(win4, text = "Success! ALS Membership Updated")
                        success.grid(row=1,column=0)

                        b3 = ttk.Button(win4, text = "Update Another member", command = lambda : [win4.destroy(), controller.show_frame(MemberUpdate)])
                        b3.grid(row=7,column=2)
                        b4 = ttk.Button(win4, text = "Back to Update Function", command = lambda : [win4.destroy(), controller.show_frame(MemberUpdate)])
                        b4.grid(row=7,column=4)

                    win3 = tk.Toplevel()
                    l = tk.Label(win3, text = memberid_entry.get())
                    l.grid(row=1,column =0)
                    z = tk.Label(win3, text = str(newname))
                    z.grid(row=2,column=0)
                    q = tk.Label(win3, text = str(newfaculty))
                    q.grid(row=3,column=0)
                    p = tk.Label(win3, text = str(newphone))
                    p.grid(row=4,column=0)
                    t = tk.Label(win3, text = str(newemail))
                    t.grid(row=5,column=0)
                
                    b1 = ttk.Button(win3, text = "confirm Update", command = lambda : [win3.destroy(),confirmUpdate()])
                    b1.grid(row=7,column=2)
                    b2 = ttk.Button(win3, text = "Back to Update function", command = lambda : [win3.destroy(),controller.show_frame(MemberUpdate)])
                    b2.grid(row=8,column=2)

                    memberid_entry.delete(0,END)
                    name.delete(0,END)
                    faculty.delete(0,END)
                    phone.delete(0,END)
                    email.delete(0,END)

            buttFrame = tk.Frame(win)
            buttFrame.pack(expand = True)
                    
            button5 = ttk.Button(buttFrame, text = "Update Member", command = lambda : [memberUpdate(),win.destroy()])
            button5.grid(row=0,column=0,ipady=30, ipadx=60)
            button6 = ttk.Button(buttFrame, text = "Back to Membership Menu", command = lambda : [win.destroy(), controller.show_frame(Membership)])
            button6.grid(row=0,column=1,ipady=30, ipadx=60)


        frame2 = tk.Frame(self)
        frame2.pack(expand=True) 

        button1 = ttk.Button(frame2,text="Update Member",command = MemberUpdatePageTwo)
        button1.grid(row=0, column=0, ipady=30, ipadx=60)
        button2 = ttk.Button(frame2,text="Back to Membership Menu", command = lambda : controller.show_frame(Membership))
        button2.grid(row=0, column=1, ipady=30, ipadx=60)

 
                    
            
            


##class MemberUpdatePageTwo(tk.Frame):
##    def __init__(self,parent,controller):
##        tk.Frame.__init__(self,parent)
##        self.controller = controller 
##        label = ttk.Label(self,text = "Please Enter Requested Information Below:", font = LARGEFONT)
##        label.grid(row=0,column = 4,padx=5,pady=5)
##        
##
##
##
##        def memberUpdate():
##
##            newname = name.get()
##            newfaculty = faculty.get()
##            newphone = faculty.get()
##            newemail = email.get()
##
##            if len(newname) == 0 or len(newfaculty) == 0 or len(newphone) != 8 or "@als.edu" not in newemail:
##
##                win = tk.Toplevel()
##                l = tk.Label(win,text = "Error! Missing or incomplete fields")
##                l.grid(row=5,column=0)
##                b = ttk.Button(win, text = "Back to Update function.", command = lambda : [win.destroy(),controller.show_frame(MemberUpdate)])
##                b.grid(row=10,column=0)
##
##
##            else :
##
##
##                def confirmUpdate():
##
##
##                    query1 = f"UPDATE Member SET name = '{newname}' WHERE memberID = '{memberid}'"
##                    query2 = f"UPDATE Member SET faculty = '{newfaculty}' WHERE memberID = '{memberid}'"
##                    query3 = f"UPDATE Member SET phone = '{newphone}' WHERE memberID = '{memberid}'"
##                    query4 = f"UPDATE Member SET email = '{newemail}' WHERE memberID = '{memberid}'"
##                    database.execute(query1)
##                    database.execute(query2)
##                    database.execute(query3)
##                    database.execute(query4)
##                    
## 
##                    win2 = tk.Toplevel()
##                    successl = tk.Label(win2,text = "Success! ALS Membership Updated")
##                    successl.grid(row=1,column=0)
##
##                    b3 = ttk.Button(win2,text = "Update Another member", command = lambda : [win2.destroy(),controller.show_frame(MemberUpdate)])
##                    b3.grid(row=7,column=2)
##                    b4 = ttk.Button(win2,text = "Back to Update Function", command = lambda : [win2.destroy(),controller.show_frame(MemberUpdate)])
##                    b4.grid(row=7,column=4)
##
##
##                win = tk.Toplevel()
##                l = tk.Label(win, text = usethis) #
##                l.grid(row=1,column=0)
##                z = tk.Label(win, text = str(newname))
##                z.grid(row=2,column=0)
##                q = tk.Label(win, text = str(newfaculty))
##                q.grid(row=3,column=0)
##                p = tk.Label(win, text = str(newphone))
##                p.grid(row=4,column=0)
##                t = tk.Label(win, text = str(newemail))
##                t.grid(row=5,column=0)
##                
##                b1 = ttk.Button(win, text = "confirm Update", command = confirmUpdate)
##                b1.grid(row=7,column=2)
##                b2 = ttk.Button(win, text = "Back to Update function", command = lambda : [win.destroy(),controller.show_frame(MemberUpdate)])
##                b2.grid(row=8,column=2)
##                
##        button1 = ttk.Button(self,text="Update Member",command = memberUpdate)
##        button1.grid(row=6,column=4,padx=5,pady=5)
##        button2 = ttk.Button(self,text="Back to Membership Menu", command = lambda : controller.show_frame(Membership))
##        button2.grid(row=7,column=4,padx=5,pady=5)

        
class Books(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=60)
        label = tk.Label(self, text = "Select one of the Options below:", font = fontstyle, bg="gray")
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        button1 = ttk.Button(frame,text = "4. Acquisition", command = lambda : controller.show_frame(BookAcquisition))
        button1.grid(row=0,column=0,ipady=100, ipadx=200)
        button2 = ttk.Button(frame,text = "5. Withdrawal", command = lambda : controller.show_frame(BookWithdrawal))
        button2.grid(row=0,column=1,ipady=100, ipadx=200)
        button3 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button3.pack(expand=True)

class BookAcquisition(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=40)
        label = tk.Label(self, text = "For New Book Acquisition, Please Enter Required Information Below:", font = fontstyle, bg="yellow")
        label.pack(expand=True)

        middleFrame = tk.Frame(self)
        middleFrame.pack(expand=True)

        leftFrame = tk.Frame(middleFrame)
        leftFrame.pack(side = LEFT, expand=True)

        rightFrame = tk.Frame(middleFrame)
        rightFrame.pack(side = LEFT, expand=True)
        

        accessionNolabel = tk.Label(leftFrame,text="Accession Number")
        accessionNolabel.grid(row=0,column=0,ipady=30, ipadx=70)
        accessionNo_entry = Entry(rightFrame)
        accessionNo_entry.grid(row=0,column=0,ipady=30, ipadx=180)
        
        titlelabel = Label(leftFrame,text="Title")
        title_entry = Entry(rightFrame)
        titlelabel.grid(row=1,column=0,ipady=30, ipadx=70)
        title_entry.grid(row=1,column=0,ipady=30, ipadx=180)

        authorlabel = Label(leftFrame,text="Authors")
        author_entry = Entry(rightFrame)
        authorlabel.grid(row=2,column=0,ipady=30, ipadx=70)
        author_entry.grid(row=2,column=0,ipady=30, ipadx=180)

        isbnlabel = Label(leftFrame,text="ISBN")
        isbn_entry = Entry(rightFrame)
        isbnlabel.grid(row=3,column=0,ipady=30, ipadx=70)
        isbn_entry.grid(row=3,column=0,ipady=30, ipadx=180)
        

        publisherlabel = Label(leftFrame,text="Publisher")
        publisher_entry = Entry(rightFrame)
        publisherlabel.grid(row=4,column=0,ipady=30, ipadx=70)
        publisher_entry.grid(row=4,column=0,ipady=30, ipadx=180)

        pubyearlabel = Label(leftFrame,text="Publication Year")
        pubyear_entry = Entry(rightFrame)
        pubyearlabel.grid(row=5,column=0,ipady=30, ipadx=70)
        pubyear_entry.grid(row=5,column=0,ipady=30, ipadx=180)

        buttonFrame = tk.Frame(self)
        buttonFrame.pack(expand=True)


        def bookAcquire():
            accno = accessionNo_entry.get()
            title = title_entry.get()
            authors = author_entry.get() #this will take multiple authors as one string
            isbn = isbn_entry.get()
            publisher = publisher_entry.get()
            pubyear = pubyear_entry.get()
            valid = True
            authorlist = authors.split(",")
        
            allbooks = pd.read_sql_query("SELECT * FROM Book",database)
            
            if accno in allbooks['accessionNo'].values or len(title) == 0 or len(isbn) == 0 or len(publisher) == 0 or len(pubyear) != 4 or len(accno) == 0 or len(authors) == 0:
                valid = False

            if valid:
                query = f"INSERT INTO Book VALUES (\"{accno}\",\"{title}\",{isbn},\"{publisher}\",{pubyear});"
                database.execute(query)
                for i in authorlist:
                    query2 = f"INSERT INTO Author VALUES ('{accno}','{i}');"
                    database.execute(query2)
                win = tk.Toplevel()
                

                
                l = tk.Label(win, text = "Success! New Book added in Library.")
                l.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Acquisition Function.",command = lambda:[win.destroy(),controller.show_frame(BookAcquisition)])
                b.grid(row=5,column=0)
            else:
                win = tk.Toplevel()
                l = tk.Label(win,text = "Error! Book already added; Duplicate, Missing or Incomplete fields.")
                l.grid(row=0,column=0)
                b = ttk.Button(win, text = "Back to Acquisition Function.", command =lambda:[ win.destroy(), controller.show_frame(BookAcquisition)])
                b.grid(row=5,column=0)

            accessionNo_entry.delete(0,END)
            title_entry.delete(0,END)
            author_entry.delete(0,END)
            isbn_entry.delete(0,END)
            publisher_entry.delete(0,END)
            pubyear_entry.delete(0,END)

        button1 = ttk.Button(buttonFrame,text = "Add New Book", command = bookAcquire)
        button1.grid(row=0,column=0,ipady=50, ipadx=120)
        button2 = ttk.Button(buttonFrame,text="Back to Books Menu", command = lambda : controller.show_frame(Books))
        button2.grid(row=0,column=1,ipady=50, ipadx=120)
        
class BookWithdrawal(tk.Frame): #problem is after successfully withdrawn, cannot auto exit both windows
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=30)
        label = tk.Label(self, text = "To Remove Outdated Books From System, Please Enter Required Information Below:", font = fontstyle, bg="pink")
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        acclabel = Label(frame, text = "Accession Number", font = fontstyle, bg="pink")
        acclabel.grid(row=0,column=0,ipady=70, ipadx=80)
        accno_entry = Entry(frame)
        accno_entry.grid(row=0,column=1,ipady=70, ipadx=180)


        
        def bookWithdraw():
            accno = accno_entry.get()

            allbooks = pd.read_sql_query("SELECT * FROM Book", database)
            borrowed = pd.read_sql_query("SELECT * FROM Borrows", database)
            reserved = pd.read_sql_query("SELECT * FROM Reserves", database)
            win = tk.Toplevel()
            valid = False

            if accno in borrowed['accessionNo'].values:
                f1 = tk.Label(win, text="Error! Book is currently on Loan")
                f1.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Withdrawal Function.",command = lambda:[win.destroy(),controller.show_frame(BookWithdrawal)])
                b.grid(row=5,column=0)
                
            
            elif accno in reserved['accessionNo'].values:
                f2 = tk.Label(win, text="Error! Book is currently Reserved")
                f2.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Withdrawal Function.",command = lambda:[win.destroy(),controller.show_frame(BookWithdrawal)])
                b.grid(row=5,column=0)
                
                
            else:
                query1 = f"SELECT * FROM Book WHERE accessionNo = '{accno}'"
                query2 = f"SELECT * FROM Author WHERE accessionNo = '{accno}'"
                booklist=pd.read_sql_query(query1,database).values.tolist()
                authorlist=pd.read_sql_query(query2,database).values.tolist()
                title = booklist[0][1]
                isbn = booklist[0][2]
                publisher = booklist[0][3]
                year = booklist[0][4]
                author = authorlist[0][1]
                valid = True
            

            def confirmWithdraw():
                query3 = f"DELETE FROM Book WHERE accessionNo = '{accno}'"
                database.execute(query3)
                query4 = f"DELETE FROM Author WHERE accessionNo = '{accno}'"
                database.execute(query4)

                
                
                win = tk.Toplevel()
                d1 = tk.Label(win,text="Success!Book successfully withdrawn.")
                d1.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Withdrawal Function.",command = lambda:[win.destroy(),controller.show_frame(BookWithdrawal)])
                b.grid(row=5,column=0)
                
                
            accno_entry.delete(0,END)    

            if valid:
                l1 = tk.Label(win,text = f"Accession Number      {accno}")
                l1.grid(row=1,column=0)
                l2 = tk.Label(win,text = f"Title                 {title}")
                l2.grid(row=2,column=0)
                l3 = tk.Label(win,text = f"Authors               {author}")
                l3.grid(row=3,column=0)
                l4 = tk.Label(win,text = f"ISBN                  {isbn}")
                l4.grid(row=4,column=0)
                l5 = tk.Label(win,text = f"Publisher             {publisher}")
                l5.grid(row=5,column=0)
                l6 = tk.Label(win,text = f"Year                  {year}")
                l6.grid(row=6,column=0)

                b1 = ttk.Button(win, text = "Confirm Withdrawal", command = lambda: [win.destroy(),confirmWithdraw()])
                b1.grid(row =7,column = 2)
                b2 = ttk.Button(win, text="Back to Withdrawal Function", command = win.destroy)
                b2.grid(row = 8,column=2)


        buttonFrame = tk.Frame(self)
        buttonFrame.pack(expand=True)
        
        button1 = ttk.Button(buttonFrame,text = "Withdraw Book",command = bookWithdraw)
        button1.grid(row=0,column=0,ipady=30, ipadx=100)
        button2 = ttk.Button(buttonFrame,text="Back to Books Menu", command = lambda : controller.show_frame(Books))
        button2.grid(row=0,column=1,ipady=30, ipadx=100)

class Loans(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=70)
        label = ttk.Label(self, text = "Select one of the Options below:", font = fontstyle)
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        button1 = tk.Button(frame,text = "6. Borrow", bg = "blue",command = lambda : controller.show_frame(BookBorrow))
        button1.grid(row=0, column=0, ipady=100, ipadx=220)
        button2 = tk.Button(frame,text = "7. Return", bg = "yellow", command = lambda : controller.show_frame(BookReturn))
        button2.grid(row=1, column=0, ipady=100, ipadx=220)
        button3 = tk.Button(self,text = "Back to Main Menu", bg = "orange", height = 10, width = 80, command = lambda : controller.show_frame(ALSMainPage))
        button3.pack(side = BOTTOM)

class BookBorrow(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=50)
        label = ttk.Label(self,text = "To Borrow a Book, Please Enter Information Below:", font = fontstyle)
        label.pack(expand=True)

        middleFrame = tk.Frame(self)
        middleFrame.pack(expand=True)

        leftFrame = tk.Frame(middleFrame)
        leftFrame.pack(side = LEFT, expand=True)

        rightFrame = tk.Frame(middleFrame)
        rightFrame.pack(side = LEFT, expand=True)

        angelstyle = tkFont.Font(family="Lucida Grande", size=30)

        acclabel = Label(leftFrame,text = "Accession Number", font = angelstyle) #, bg="magenta"
        acclabel.grid(row=0, column=0, ipady=40, ipadx=80)
        memberidlabel = Label(leftFrame,text = "Membership ID", font = angelstyle) # bg="cyan"
        memberidlabel.grid(row=1, column=0, ipady=40, ipadx=80)
        
        accno_entry = Entry(rightFrame)
        accno_entry.grid(row=0, column=0, ipady=40, ipadx=200)
        memberid_entry= Entry(rightFrame)
        memberid_entry.grid(row=1, column=0,ipady=40, ipadx=200)
        
        def bookBorrow():
            def confirmBorrow():
                query = f"INSERT INTO Borrows VALUES ('{accno}','{memberid}',DATE '{borrowdate}', DATE '{duedate}')"
                database.execute(query)
                if memberreserving == memberid:
                    query2 = f"DELETE FROM Reserves WHERE accessionNo = '{accno}'"
                    database.execute(query2)

                
            
                win =tk.Toplevel()
                d1 = tk.Label(win, text = "Success! Book successfully borrowed.")
                d1.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Borrow Function.",command = lambda:[win.destroy(),controller.show_frame(BookBorrow)])
                b.grid(row=5,column=0)
                
            memberid = memberid_entry.get()
            accno = accno_entry.get()
 
            borrowdate = pd.read_sql_query("SELECT curdate()",database).iat[0,0] #gets the current date
            duedate = pd.read_sql_query("SELECT DATE_ADD(curdate(), INTERVAL +14 DAY)",database).iat[0,0] #gets the due date(T-14)
            borrowed = pd.read_sql_query("SELECT * FROM Borrows", database)
            fined = pd.read_sql_query("SELECT * FROM Fine", database)
            reserves = pd.read_sql_query("SELECT * FROM Reserves", database)
            counts = pd.read_sql_query(f"SELECT COUNT(*) FROM Borrows WHERE memberid = '{memberid}'", database).iat[0,0]
            q1 = f"SELECT * FROM Book WHERE accessionNo = '{accno}'"
            q2 = f"SELECT * FROM Member WHERE memberID = '{memberid}'"
            booklist = pd.read_sql_query(q1,database).values.tolist()
            memberlist = pd.read_sql_query(q2,database).values.tolist()
            title = booklist[0][1]
            name = memberlist[0][1]
            try:
                fineamt = pd.read_sql_query(f"SELECT * FROM Fine WHERE memberID = '{memberid}'",database).values.tolist()[0][1]
            except:
                fineamt = 0

            try:
                memberreserving = pd.read_sql_query(f"SELECT memberID FROM Reserves where accessionNo = \"{accno}\"",database).iat[0,0]
            except:
                memberreserving = False

            if counts == 2:
                win = tk.Toplevel()
                f1 = tk.Label(win, text = "Error! Member loan quota exceeded.")
                f1.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Borrow Function.",command = lambda:[win.destroy(),controller.show_frame(BookBorrow)])
                b.grid(row=5,column=0)
                
            elif accno in borrowed['accessionNo'].values:
                query = f"SELECT * FROM Borrows WHERE accessionNo = '{accno}'"
                borrowlist = pd.read_sql_query(query,database).values.tolist()
                loantill = borrowlist[0][-1]
                win = tk.Toplevel()
                f2 = tk.Label(win, text = f"Error! Book currently on Loan until: {loantill}")
                f2.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Borrow Function.",command = lambda:[win.destroy(),controller.show_frame(BookBorrow)])
                b.grid(row=5,column=0)
                
            elif fineamt != 0:
                win = tk.Toplevel()
                f3 = tk.Label(win,text= "Error! Member has outstanding fines.")
                f3.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Borrow Function.",command = lambda:[win.destroy(),controller.show_frame(BookBorrow)])
                b.grid(row=5,column=0)
                
            elif (accno in reserves['accessionNo'].values and memberreserving != memberid) or (memberreserving != False and memberreserving != memberid):
                win = tk.Toplevel()
                f4 = tk.Label(win, text = "Error! Book is currently reserved.")
                f4.grid(row=0,column=0)
                b = ttk.Button(win,text="Back to Borrow Function.",command = lambda:[win.destroy(),controller.show_frame(BookBorrow)])
                b.grid(row=5,column=0)
                
            else:
                win = tk.Toplevel()
                l1 = tk.Label(win,text = f"Accession Number      {accno}")
                l1.grid(row=1,column=0)
                l2 = tk.Label(win,text = f"Book Title            {title}")
                l2.grid(row=2,column=0)
                l3 = tk.Label(win,text = f"Borrow Date           {borrowdate}")
                l3.grid(row=3,column=0)
                l4 = tk.Label(win,text = f"Membership ID         {memberid}")
                l4.grid(row=4,column=0)
                l5 = tk.Label(win,text = f"Member name           {name}")
                l5.grid(row=5,column=0)
                l6 = tk.Label(win,text = f"Due Date              {duedate}")
                l6.grid(row=6,column=0)

                b1 = ttk.Button(win, text = "Confirm Loan", command = lambda: [win.destroy(),confirmBorrow()])
                b1.grid(row =7,column = 2)
                b2 = ttk.Button(win, text="Back to Borrow Function", command = win.destroy)
                b2.grid(row = 8,column=2)

            memberid_entry.delete(0,END)
            accno_entry.delete(0,END)
        
        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)

        button1 = ttk.Button(ButtonFrame,text = "Borrow Book", command = bookBorrow)
        button1.grid(row=0,column=0,ipady=50, ipadx=100)
        button2 = ttk.Button(ButtonFrame,text="Back to Loans Menu", command = lambda : controller.show_frame(Loans))
        button2.grid(row=0,column=1,ipady=50, ipadx=100)

class BookReturn(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=50)
        label = tk.Label(self,text = "To Return a Book, Please Enter Information Below:", font = fontstyle, bg="cyan")
        label.pack(expand=True)

        middleFrame = tk.Frame(self)
        middleFrame.pack(expand=True)

        leftFrame = tk.Frame(middleFrame)
        leftFrame.pack(side = LEFT, expand=True)

        rightFrame = tk.Frame(middleFrame)
        rightFrame.pack(side = LEFT, expand=True)

        angelstyle = tkFont.Font(family="Lucida Grande", size=30)

        acclabel = Label(leftFrame,text="Accession Number", font = angelstyle)
        acclabel.grid(row=0, column=0, ipady=40, ipadx=80)
        
        returndatelabel = Label(leftFrame,text="Return date", font = angelstyle)
        returndatelabel.grid(row=1, column=0, ipady=40, ipadx=80)
        
        returndate_entry = Entry(rightFrame)
        returndate_entry.grid(row=1, column=0,ipady=40, ipadx=200)

        accno_entry = Entry(rightFrame)
        accno_entry.grid(row=0, column=0,ipady=40, ipadx=200)
        
        def bookReturn():
            accno = accno_entry.get()
            actualreturndate = returndate_entry.get()
            query1 = f"SELECT * FROM Book WHERE accessionNo = '{accno}'"
            booklist = pd.read_sql_query(query1,database).values.tolist()
            title = booklist[0][1]
            borrowlist = pd.read_sql_query(f"SELECT * FROM Borrows WHERE accessionNo = '{accno}'",database).values.tolist()
            memberid = borrowlist[0][1]
            duedate = borrowlist[0][-1]
            name = pd.read_sql_query(f"SELECT name FROM Member WHERE memberID = '{memberid}'",database).iat[0,0]
            fine = pd.read_sql_query(f"SELECT DATEDIFF(DATE'{actualreturndate}',DATE'{duedate}')",database).iat[0,0]
            outstanding = 0
            if fine > 0:
                try:
                    outstanding = pd.read_sql_query(f"SELECT fineAmt FROM Fine WHERE memberID = '{memberid}'",database).iat[0,0]
                except:
                    outstanding = 0
            else :
                fine = 0
                
            fine += outstanding
            
            def confirmReturn():
                database.execute(f"DELETE FROM Borrows WHERE memberID = '{memberid}' AND accessionNo = '{accno}'")
                if fine > 0:
                    try:
                        exists = pd.read_sql_query(f"SELECT * FROM FINE WHERE memberID = '{memberid}'",database).values.tolist()
                    except:
                        exists = False 
                    if exists:
                        database.execute(f"UPDATE Fine SET fineAmt = {fine} WHERE memberID = '{memberid}'")
                    else:
                        database.execute(f"INSERT INTO Fine VALUES('{memberid}',{fine},NULL)")
                    win = tk.Toplevel()
                    d1 = tk.Label(win,text="Error! Book returned successfully but has fines.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Return Function.",command = lambda:[win.destroy(),controller.show_frame(BookReturn)])
                    b.grid(row=5,column=0)
                else:
                    win = tk.Toplevel()
                    d1 = tk.Label(win,text="Success!Book successfully returned.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Return Function.",command = lambda:[win.destroy(),controller.show_frame(BookReturn)])
                    b.grid(row=5,column=0)
                    
                
            win = tk.Toplevel()
            l1 = tk.Label(win,text = f"Accession Number      {accno}")
            l1.grid(row=1,column=0)
            l2 = tk.Label(win,text = f"Book Title            {title}")
            l2.grid(row=2,column=0)
            l3 = tk.Label(win,text = f"Membership ID         {memberid}")
            l3.grid(row=3,column=0)
            l4 = tk.Label(win,text = f"Member Name           {name}")
            l4.grid(row=4,column=0)
            l5 = tk.Label(win,text = f"Return Date           {actualreturndate}")
            l5.grid(row=5,column=0)
            l6 = tk.Label(win,text = f"Fine                  ${fine}")
            l6.grid(row=6,column=0)

            accno_entry.delete(0,END)
            returndate_entry.delete(0,END)
            
            b1 = ttk.Button(win, text = "Confirm Return", command = lambda: [win.destroy(),confirmReturn()])
            b1.grid(row =7,column = 2)
            b2 = ttk.Button(win, text="Back to Return Function", command = win.destroy)
            b2.grid(row = 8,column=2)        

        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)
        
        button1 = ttk.Button(ButtonFrame,text = "Return Book", command = bookReturn)
        button1.grid(row=0,column=0,ipady=50, ipadx=100)
        button2 = ttk.Button(ButtonFrame,text="Back to Loans Menu", command = lambda : controller.show_frame(Loans))
        button2.grid(row=0,column=1,ipady=50, ipadx=100)
        
class Reservations(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=70)
        label = tk.Label(self, text = "Select one of the Options below:", font = fontstyle, bg="yellow")
        label.pack(expand=True)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        button1 = tk.Button(frame,text = "8. Reserve a Book", bg="cyan", command = lambda : controller.show_frame(BookReserve))
        button1.grid(row=0,column=0,ipady=80, ipadx=110)
        button2 = tk.Button(frame,text = "9. Cancel Reservation", bg="pink", command = lambda : controller.show_frame(CancelReservation))
        button2.grid(row=1,column=0,ipady=80, ipadx=100)
        button3 = ttk.Button(self,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
        button3.pack(expand=True)


class BookReserve(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=40)
        label = tk.Label(self, text = "To Reserve a Book, Please Enter Information Below:", font = fontstyle, bg="pink")
        label.pack(expand=True)

        middleFrame = tk.Frame(self)
        middleFrame.pack(expand=True)

        leftFrame = tk.Frame(middleFrame)
        leftFrame.pack(side = LEFT, expand=True)

        rightFrame = tk.Frame(middleFrame)
        rightFrame.pack(side = LEFT, expand=True)

        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)
        
        angelstyle = tkFont.Font(family="Lucida Grande", size=30)
        
        acclabel = Label(leftFrame, text = "Accession Number", font = angelstyle)
        acclabel.grid(row=0,column=0,ipady=30, ipadx=80)
        memberidlabel = Label(leftFrame, text = "Membership ID", font = angelstyle)
        memberidlabel.grid(row=1,column=0,ipady=30, ipadx=80)
        reservedatelabel = Label(leftFrame, text = "Reserve date", font = angelstyle)
        reservedatelabel.grid(row=2,column=0,ipady=30, ipadx=80)

        accno_entry = Entry(rightFrame)
        accno_entry.grid(row=0,column=0,ipady=30, ipadx=180)
        memberid_entry = Entry(rightFrame)
        memberid_entry.grid(row=1,column=0,ipady=30, ipadx=180)
        reservedate_entry = Entry(rightFrame)
        reservedate_entry.grid(row=2,column=0,ipady=30, ipadx=180)


        def bookReserve():
            accno = accno_entry.get()
            memberid = memberid_entry.get()
            reservedate = reservedate_entry.get()
            memberlist = pd.read_sql_query(f"SELECT * FROM Member WHERE memberID = '{memberid}'",database).values.tolist()
            name = memberlist[0][1]
            booklist = pd.read_sql_query(f"SELECT * FROM Book WHERE accessionNo = '{accno}'",database).values.tolist()
            title = booklist[0][1]
            counts = pd.read_sql_query(f"SELECT COUNT(*) FROM Reserves WHERE memberID = '{memberid}'",database).iat[0,0]
            try:
                fineamt = pd.read_sql_query(f"SELECT fineAmt FROM Fine WHERE memberid = '{memberid}'",database).iat[0,0]
            except:
                fineamt = 0
            
            
            def confirmReserve():
                if counts >= 2:
                    win = tk.Toplevel()
                    d1 = tk.Label(win,text="Error!Member currently has 2 Books on Reservation.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Reserve Function.",command = lambda:[win.destroy(),controller.show_frame(BookReserve)])
                    b.grid(row=5,column=0)
                elif fineamt > 0:
                    win=tk.Toplevel()
                    d1 = tk.Label(win,text=f"Error! Member has Outstanding Fine of: ${fineamt}.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Reserve Function.",command = lambda:[win.destroy(),controller.show_frame(BookReserve)])
                    b.grid(row=5,column=0) 
                else:
                    win = tk.Toplevel()
                    query = f"INSERT INTO Reserves VALUES('{accno}','{memberid}',DATE '{reservedate}')"
                    database.execute(query)
                    d1 = tk.Label(win,text="Success!Book successfully reserved.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Reserve Function.",command = lambda:[win.destroy(),controller.show_frame(Reservations)])
                    b.grid(row=5,column=0)
                
            win = tk.Toplevel()
            l1 = tk.Label(win,text = f"Accession Number      {accno}")
            l1.grid(row=1,column=0)
            l2 = tk.Label(win,text = f"Book Title            {title}")
            l2.grid(row=2,column=0)
            l3 = tk.Label(win,text = f"Membership ID         {memberid}")
            l3.grid(row=3,column=0)
            l4 = tk.Label(win,text = f"Member Name           {name}")
            l4.grid(row=4,column=0)
            l5 = tk.Label(win,text = f"Reserve Date          {reservedate}")
            l5.grid(row=5,column=0)

            accno_entry.delete(0,END)
            memberid_entry.delete(0, END)
            reservedate_entry.delete(0, END)

            b1 = ttk.Button(win, text = "Confirm Reservation", command = lambda: [win.destroy(),confirmReserve()])
            b1.grid(row =6,column = 2)
            b2 = ttk.Button(win, text="Back to Reserve Function", command = win.destroy)
            b2.grid(row = 7,column=2)
       
        button1 = ttk.Button(ButtonFrame,text = "Reserve Book",command = bookReserve)
        button1.grid(row=0,column=0,ipady=50, ipadx=80)
        button2 = ttk.Button(ButtonFrame,text="Back to Reservations Menu", command = lambda : controller.show_frame(Reservations))
        button2.grid(row=0,column=1,ipady=50, ipadx=80)

class CancelReservation(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=40)
        label = tk.Label(self, text = "To Cancel a Reservation, Please Enter Information Below:", font = fontstyle, bg="pink")
        label.pack(expand=True)

        middleFrame = tk.Frame(self)
        middleFrame.pack(expand=True)

        leftFrame = tk.Frame(middleFrame)
        leftFrame.pack(side = LEFT, expand=True)

        rightFrame = tk.Frame(middleFrame)
        rightFrame.pack(side = LEFT, expand=True)

        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)

        angelstyle = tkFont.Font(family="Lucida Grande", size=30)
        
        acclabel = Label(leftFrame, text = "Accession Number", font = angelstyle)
        acclabel.grid(row=0,column=0,ipady=40, ipadx=70)
        
        memberidlabel = Label(leftFrame, text = "Membership ID", font = angelstyle)
        memberidlabel.grid(row=1,column=0,ipady=40, ipadx=70)

        canceldatelabel = Label(leftFrame, text = "Cancel date", font = angelstyle)
        canceldatelabel.grid(row=2,column=0,ipady=40, ipadx=70)
        
        accno_entry = Entry(rightFrame)
        accno_entry.grid(row=0,column=0,ipady=40, ipadx=200)
        
        memberid_entry = Entry(rightFrame)
        memberid_entry.grid(row=1,column=0,ipady=40, ipadx=200)
        
        canceldate_entry = Entry(rightFrame)
        canceldate_entry.grid(row=2,column=0,ipady=40, ipadx=200)
        
        def cancelReserve():
            accno = accno_entry.get()
            memberid = memberid_entry.get()
            canceldate = canceldate_entry.get()
            memberlist = pd.read_sql_query(f"SELECT * FROM Member WHERE memberID = '{memberid}'",database).values.tolist()
            name = memberlist[0][1]
            booklist = pd.read_sql_query(f"SELECT * FROM Book WHERE accessionNo = '{accno}'",database).values.tolist()
            title = booklist[0][1]
            try:
                reservation = pd.read_sql_query(f"SELECT * FROM Reserves WHERE accessionNo = '{accno}' AND memberID = '{memberid}'",database).values.tolist()[0]
            except:
                reservation = False     
            
            def confirmCancel():
                if not reservation:
                    win = tk.Toplevel()
                    d1 = tk.Label(win,text="Error!Member has no such reservation.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Cancellation Function.",command = lambda:[win.destroy(),controller.show_frame(CancelReservation)])
                    b.grid(row=5,column=0)
                else:
                    win = tk.Toplevel()
                    query = f"DELETE FROM Reserves WHERE accessionNo = '{accno}' AND memberID = '{memberid}'"
                    database.execute(query)
                    d1 = tk.Label(win,text="Success!Reservation successfully cancelled.")
                    d1.grid(row=0,column=0)
                    b = ttk.Button(win,text="Back to Cancellation Function.",command = lambda:[win.destroy(),controller.show_frame(CancelReservation)])
                    b.grid(row=5,column=0)
                    
                
            win = tk.Toplevel()
            l1 = tk.Label(win,text = f"Accession Number      {accno}")
            l1.grid(row=1,column=0)
            l2 = tk.Label(win,text = f"Book Title            {title}")
            l2.grid(row=2,column=0)
            l3 = tk.Label(win,text = f"Membership ID         {memberid}")
            l3.grid(row=3,column=0)
            l4 = tk.Label(win,text = f"Member Name           {name}")
            l4.grid(row=4,column=0)
            l5 = tk.Label(win,text = f"Cancellation Date     {canceldate}")
            l5.grid(row=5,column=0)

            accno_entry.delete(0,END)
            memberid_entry.delete(0,END)
            canceldate_entry.delete(0,END)

            b1 = ttk.Button(win, text = "Confirm Cancellation", command = lambda: [win.destroy(),confirmCancel()])
            b1.grid(row =6,column = 2)
            b2 = ttk.Button(win, text="Back to Cancellation Function", command = win.destroy)
            b2.grid(row = 7,column=2)

        button1 = ttk.Button(ButtonFrame,text = "Cancel Reservation", command = cancelReserve)
        button1.grid(row=0,column=0,ipady=50, ipadx=80)
        button2 = ttk.Button(ButtonFrame,text="Back to Reservations Menu", command = lambda : controller.show_frame(Reservations))
        button2.grid(row=0,column=1,ipady=50, ipadx=80)

##def ConfirmCancellation(a_num, mem_id, can_date):
##    # within functions, ttk.labels is still a thing. 
##    confirmWanCancel = Toplevel()
##    # my labels below needs to access the data that was inputted, it can remain a label
##
##    header = ttk.Label(confirmWanCancel, text = "Confirm Cancellation Details To Be Correct")
##    header.grid(row=0,column=0,padx=10,pady=10)
##
##    AN = ttk.Label(confirmWanCancel, text = "Accession Number" + a_num.get())
##    AN.grid(row=1,column=0,padx=10,pady=10)
##    
##    BT = ttk.Label(confirmWanCancel, text = "Book Title") # Pull from SQL
##    BT.grid(row=2,column=0,padx=10,pady=10)
##
##    MemID = ttk.Label(confirmWanCancel, text = "Membership ID" + mem_id.get())
##    MemID.grid(row=3,column=0,padx=10,pady=10)
##
##    MemName = ttk.Label(confirmWanCancel, text = "Member Name") # pull from SQL
##    MemName.grid(row=4,column=0,padx=10,pady=10)
##
##    CanDate = ttk.Label(confirmWanCancel, text = "Cancellation Date" + can_date.get())
##    CanDate.grid(row=5,column=0,padx=10,pady=10)
##
##    DoubleConfirm = ttk.Button(confirmWanCancel, text ='Confirm Cancellation', command = lambda : ErrorNoSuchThing()) 
##    # needs a logical loop here after data has been pulled
##    DoubleConfirm.grid(row=6,column=0,padx=10,pady=10)
##
##    GoBack = ttk.Button(confirmWanCancel, text ='Back to Cancellation Function', command = lambda : confirmWanCancel.destroy())
##    GoBack.grid(row=6,column=2,padx=10,pady=10) # next to double confirm button both bottom.
##
##    # def CheckIfGotError():
##    # pulls data to see if member has made the appropriate reservation to be cancelled. 
##
##    def ErrorNoSuchThing():
##        # No such Reservation recorded, hence cannot delete 
##        confirmWanCancel.destroy()
##        
##        Error_1 = Toplevel()
##        header = ttk.Label(Error_1, text = "Error!", font = LARGEFONT)
##        header.pack()
##
##        body = ttk.Label(Error_1, text = "Member has no such reservation")
##        body.pack()
##        
##        GoBack = ttk.Button(Error_1, text ='Back to Cancellation Function', command = lambda : Error_1.destroy())
##        GoBack.pack()

class Fines(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent) # parent class constructor? not super() meh?
        fontstyle = tkFont.Font(family="Lucida Grande", size=50)
        header = tk.Label(self, text = "Select one of the Options below:", font = fontstyle, bg="yellow")
        header.pack(expand=True)

        angelstyle = tkFont.Font(family="Lucida Grande", size=50)

        frame = tk.Frame(self)
        frame.pack(expand=True)

        button1 = tk.Button(frame,text = "10. Payment", command = lambda : controller.show_frame(FinesPayment), font = angelstyle, bg="red")
        button1.grid(row=0,column=0,ipady=80, ipadx=200)

        fram2 = tk.Frame(self)
        fram2.pack(expand=True)    
        
        button3 = tk.Button(fram2,text="Back To Main Menu", height = 10, width = 40, command = lambda : controller.show_frame(ALSMainPage))
        button3.grid(row=0,column=0,ipady=10, ipadx=40)

class FinesPayment(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=50)
        header = tk.Label(self,text = "To Pay a Fine, Please Enter Information Below", font = fontstyle, bg="yellow")
        header.pack(expand=True)

        middleFrame = tk.Frame(self)
        middleFrame.pack(expand=True)

        leftFrame = tk.Frame(middleFrame)
        leftFrame.pack(side = LEFT, expand=True)

        rightFrame = tk.Frame(middleFrame)
        rightFrame.pack(side = LEFT, expand=True)

        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)

        angelstyle = tkFont.Font(family="Lucida Grande", size=30)

        global entry_1
        label_1 = tk.Label(leftFrame,text="Membership ID", font = angelstyle)
        label_1.grid(row=0,column=0,ipady=40, ipadx=90)
        
        entry_1 = ttk.Entry(rightFrame) #####
        entry_1.grid(row=0,column=0,ipady=40, ipadx=180)

        global entry_2
        label_2 = tk.Label(leftFrame,text="Payment Date", font = angelstyle)
        label_2.grid(row=1,column=0,ipady=40, ipadx=90)
        
        entry_2 = ttk.Entry(rightFrame) #####
        entry_2.grid(row=1,column=0,ipady=40, ipadx=180)
        
        global entry_3
        label_3 = tk.Label(leftFrame,text="Payment Amount", font = angelstyle)
        label_3.grid(row=2,column=0,ipady=40, ipadx=90)
        
        entry_3 = ttk.Entry(rightFrame) #####
        entry_3.grid(row=2,column=0,ipady=40, ipadx=180)

        def payFine():

            win = tk.Toplevel()
            label = ttk.Label(win, text = "Please Confirm Details to be Correct", font = LARGEFONT)
            label.grid(row=0,column=0,padx=10,pady=10)
            amtDue = ttk.Label(win, text = "Payment Due: \n" + entry_3.get())
            amtDue.grid(row=1,column=0,padx=10,pady=10)
            identifier = ttk.Label(win, text = "Member ID \n" + entry_1.get())
            identifier.grid(row=1,column=1,padx=10,pady=10)

            warning = ttk.Label(win,text = " Exact Fee Only")
            warning.grid(row=2,column=0,padx=10,pady=10)

            whenpay = ttk.Label(win, text = "Payment Date: \n" + entry_2.get())
            whenpay.grid(row=2,column=1,padx=10,pady=10)

            global globalmemberid, globalpaydate, globalpayamt
            globalmemberid = entry_1.get()
            globalpaydate = entry_2.get()
            globalpayamt = entry_3.get()

            def confirmPay():

                membershipid = globalmemberid#entry_1.get()
                paymentdate = globalpaydate#entry_2.get() 
                paymentamt = globalpayamt#entry_3.get()
               

                query = f"SELECT fineAmt FROM Fine WHERE memberID = '{membershipid}'"
                try:
                    fineamt = pd.read_sql_query(query,database).iat[0,0]
                
                    if str(fineamt) == paymentamt :
                        query2= f"DELETE FROM Fine WHERE memberID = '{membershipid}'"
                        database.execute(query2)
                        win2 = tk.Toplevel()
                        label2 = ttk.Label(win2, text = "Success! Fine paid.", font = LARGEFONT)
                        label2.grid(row=0,column=0,padx=10,pady=10)
                        button5 = ttk.Button(win2, text = "Back to Fines Menu", command = lambda : [win2.destroy(), controller.show_frame(Fines)])
                        button5.grid(row=3,column=1,padx=10,pady=10)

                    else :
                        win2 = tk.Toplevel()
                        label2 = ttk.Label(win2, text="Error! Incorrect fine payment amount.",font=LARGEFONT)
                        label2.grid(row=0,column=0,padx=10,pady=10)
                        button5 = ttk.Button(win2, text ="Back to Payment Function", command = win2.destroy)
                        button5.grid(row=3,column=1,padx=10,pady=10)

                except:

                    win2 = tk.Toplevel()
                    label2 = ttk.Label(win2, text = "Error! Member has no fine.",font = LARGEFONT)
                    label2.grid(row=0,column=0,padx=10,pady=10)
                    button5 = ttk.Button(win2, text = "Back to Payment Function", command = win2.destroy)
                    button5.grid(row=3,column=1,padx=10,pady=10)
                    
                

            
            button3 = ttk.Button(win, text = "Confirm Payment", command = lambda : [win.destroy(),confirmPay()])
            button3.grid(row=3,column=0,padx=10,pady=10)
            button4 = ttk.Button(win, text = "Back to Payment Function", command = win.destroy)
            button4.grid(row=3,column=1,padx=10,pady=10)

            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)
            
            
        
        button1 = ttk.Button(ButtonFrame, text = "Pay Fine", command = payFine)
        button1.grid(row=0,column=0,ipady=30, ipadx=80)
        button2 = ttk.Button(ButtonFrame,text = "Back to Fines Menu", command = lambda : controller.show_frame(Fines))
        button2.grid(row=0,column=1,ipady=30, ipadx=80)


##class FinesPayment(tk.Frame):
##    def __init__(self,parent,controller):
##        tk.Frame.__init__(self,parent)
##
##        header = ttk.Label(self,text = "To Pay a Fine, Please Enter Information Below", font = LARGEFONT)
##        header.grid(row=0,column=0,padx=10,pady=10)
##
##        global entry_1
##        label_1 = ttk.Label(self,text="Membership ID")
##        label_1.grid(row=1,column=0,padx=10,pady=10)
##        entry_1 = ttk.Entry(self) #####
##        entry_1.grid(row=1,column=1,padx=10,pady=10)
##
##        global entry_2
##        label_2 = ttk.Label(self,text="Payment Date")
##        label_2.grid(row=2,column=0,padx=10,pady=10)
##        entry_2 = ttk.Entry(self) #####
##        entry_2.grid(row=2,column=1,padx=10,pady=10)
##
##        global entry_3
##        label_3 = ttk.Label(self,text="Payment Amount")
##        label_3.grid(row=3,column=0,padx=10,pady=10)
##        entry_3 = ttk.Entry(self) #####
##        entry_3.grid(row=3,column=1,padx=10,pady=10)
##
##        def payFine():
##
##            win = tk.Toplevel()
##            label = ttk.Label(win, text = "Please Confirm Details to be Correct", font = LARGEFONT)
##            label.grid(row=0,column=0,padx=10,pady=10)
##            amtDue = ttk.Label(win, text = "Payment Due: \n" + entry_3.get())
##            amtDue.grid(row=1,column=0,padx=10,pady=10)
##
##            identifier = ttk.Label(win, text = "Member ID \n" + entry_1.get())
##            identifier.grid(row=1,column=1,padx=10,pady=10)
##
##            warning = ttk.Label(win,text = " Exact Fee Only")
##            warning.grid(row=2,column=0,padx=10,pady=10)
##
##            whenpay = ttk.Label(win, text = "Payment Date: \n" + entry_2.get())
##            whenpay.grid(row=2,column=1,padx=10,pady=10)
##
##            def confirmPay():
##
##                membershipid = entry_1.get()
##                paymentdate = entry_2.get() 
##                paymentamt = entry_3.get()
##
##                query = f"SELECT fineAmt FROM Fine WHERE memberID = '{membershipid}'"
##                try:
##                    fineamt = (pd.read_sql_query(query,database).values.tolist())[0][0]
##                    if str(fineamt) == paymentamt :
##                        
##                        query2= f"DELETE FROM Fine WHERE memberID = '{membershipid}'"
##                        database.execute(query2)
##                        win2 = tk.Toplevel()
##                        label2 = ttk.Label(win2, text = "Success! Fine paid.", font = LARGEFONT)
##                        label2.grid(row=0,column=0,padx=10,pady=10)
##                        button5 = ttk.Button(win2, text = "Back to Fines Menu", command = lambda : [win2.destroy(), controller.show_frame(Fines)])
##                        button5.grid(row=3,column=1,padx=10,pady=10)
##
##                    else :
##                        
##                        win2 = tk.Toplevel()
##                        label2 = ttk.Label(win2, text="Error! Incorrect fine payment amount.",font=LARGEFONT)
##                        label2.grid(row=0,column=0,padx=10,pady=10)
##                        button5 = ttk.Button(win2, text ="Back to Payment Function", command = win2.destroy)
##                        button5.grid(row=3,column=1,padx=10,pady=10)
##
##                except:
##
##                    win2 = tk.Toplevel()
##                    label2 = ttk.Label(win2, text = "Error! Member has no fine.",font = LARGEFONT)
##                    label2.grid(row=0,column=0,padx=10,pady=10)
##                    button5 = ttk.Button(win2, text = "Back to Payment Function", command = win2.destroy)
##                    button5.grid(row=3,column=1,padx=10,pady=10)
##                    
##                
##
##            
##            button3 = ttk.Button(win, text = "Confirm Payment", command = lambda : [win.destroy(),confirmPay()])
##            button3.grid(row=3,column=0,padx=10,pady=10)
##            button4 = ttk.Button(win, text = "Back to Payment Function", command = win.destroy)
##            button4.grid(row=3,column=1,padx=10,pady=10)
##            
##            
##        
##        button1 = ttk.Button(self, text = "Pay Fine", command = payFine)
##        button1.grid(row=6,column=4,padx=5,pady=5)
##        button2 = ttk.Button(self,text = "Back to Fines Menu", command = lambda : controller.show_frame(Fines))
##        button2.grid(row=7,column=4,padx=5,pady=5)
##

##
##class FinesPayment(tk.Frame): 
##    def __init__(self,parent,controller): 
##        Mem_Id = tk.StringVar() 
##        payDate = tk.StringVar() 
##        amtPaid = tk.StringVar()  
## 
##        tk.Frame.__init__(self,parent)  
##        header = ttk.Label(self, text = "To Pay a Fine, Please Enter Information Below", font = LARGEFONT) 
##        header.grid(row=0,column=0,padx=10,pady=10) 
## 
##        label_1 = ttk.Label(self, text = "Membership ID") 
##        label_1.grid(row=1,column=0 ,padx =10,pady=10) 
##        entry_1 = ttk.Entry(self, textvariable = Mem_Id) 
##        entry_1.grid(row=1,column=1 ,padx =10,pady=10) 
## 
##        label_2 = ttk.Label(self, text = "Payment Date") 
##        label_2.grid(row=2,column=0 ,padx =10,pady=10) 
##        entry_2 = ttk.Entry(self, textvariable = payDate) 
##        entry_2.grid(row=2,column=1 ,padx =10,pady=10) 
## 
##        label_3 = ttk.Label(self, text = "Payment Amount") 
##        label_3.grid(row=3,column=0 ,padx =10,pady=10) 
##        entry_3 = ttk.Entry(self, textvariable = amtPaid) 
##        entry_3.grid(row=3,column=1 ,padx =10,pady=10) 
## 
##
## 
##        def PaymentConfirmation(): 
##            ConfirmPay = Toplevel() 
##            header = ttk.Label(ConfirmPay, text = "Please Confirm Details To Be Correct") 
##            header.grid(row=0,column=0,padx=10,pady=10) 
##            amtDue = ttk.Label(ConfirmPay, text = "Payment Due: \n" + amtPaid.get()) # either the amt you pay or the amt you owe, shld be owed 
##            amtDue.grid(row=1,column=0,padx=10,pady=10) 
## 
##            identifier = ttk.Label(ConfirmPay, text = "Member ID \n" + Mem_Id.get()) 
##            identifier.grid(row=1,column=1,padx=10,pady=10) 
## 
##            warning = ttk.Label(ConfirmPay, text = "Exact Fee Only") 
##            warning.grid(row=2,column=0,padx=10,pady=10) 
## 
##            whenPay = ttk.Label(ConfirmPay, text = "Payment Due: \n" + payDate.get()) 
##            whenPay.grid(row=2,column=1,padx=10,pady=10) 
## 
##            
##            
##                
##            # Logic to deal with the input.  
##            def confirmPay():
##                def ErrorNoFine():
##                    print("Your")
##                    ConfirmPay.destroy() 
##                    payWhat = Toplevel() 
##                    print("mum")
##                    header = ttk.Label(payWhat, text = "Error!", font = LARGEFONT) 
##                    header.grid(row=0,column=0,padx=10,pady=10) 
##                    body = ttk.Label(payWhat, text = "Member has no fine") 
##                    body.grid(row=1,column=0,padx=10,pady=10) 
##                    GoBack = ttk.Button(payWhat, text ='Back to Payment Function', command = lambda : payWhat.destroy()) 
##                    GoBack.grid(row=2,column=0,padx=10,pady=10)
##                    print("gay")
##                    
##                def ErrorPayProperly(): 
##                    ConfirmPay.destroy() 
##                    payProperly = Toplevel() 
##     
##                    header = ttk.Label(payProperly, text = "Error!", font = LARGEFONT) 
##                    header.grid(row=0,column=0,padx=10,pady=10) 
##                    body = ttk.Label(payProperly, text = "Incorrect fine payment amount") 
##                    body.grid(row=1,column=0,padx=10,pady=10) 
##                    GoBack = ttk.Button(payProperly, text ='Back to Payment Function', command = lambda : payProperly.destroy()) 
##                    GoBack.grid(row=2,column=0,padx=10,pady=10)
##                    
##                # if got fineamount, means havent pay -> but might not have payment date.  
##                query = f"SELECT memberID FROM Fine WHERE fineAmt > 0 AND memberID = '{Mem_Id.get()}' "  
##                # for members in fine, select their * from Member relation. 
##                kenafined = pd.read_sql_query(query,database).values.tolist()
##                print(kenafined)
##                print([Mem_Id.get()] not in kenafined)
##                if [Mem_Id.get()] not in kenafined:
##                    print('joemama')
##                    lambda : ErrorNoFine()  
##                else:
##                    fineamt = pd.read_sql_query(f"SELECT fineAmt FROM Fine WHERE memberid = '{Mem_Id.get()}'",database).iat[0,0] 
##                    if fineamt == int(amtPaid.get()): 
##                        action = f"UPDATE Fine SET fineAmt = 0, paymentDate = '{payDate.get()}'WHERE memberID = '{Mem_Id.get()}'" 
##                        database.execute(action) 
##                    else:  
##                        lambda : ErrorPayProperly()
##                        
##   
## 
##            
##
##            button1 = ttk.Button(ConfirmPay,text = "Confirm Payment", command = lambda : confirmPay()) 
##            button1.grid(row=3,column=0 ,padx =10,pady=10) 
##            button3 = ttk.Button(ConfirmPay,text="Back To Fines Menu", command = lambda : ConfirmPay.destroy()) 
##            button3.grid(row=3,column=1,padx=10,pady=10) 
##                
##        button1 = ttk.Button(self,text = "Pay Fine", command = PaymentConfirmation)#(Mem_Id, payDate, amtPaid)) 
##        button1.grid(row=4,column=0 ,padx =10,pady=10) 
##        button3 = ttk.Button(self,text="Back To Fines Menu", command = lambda : controller.show_frame(Fines)) 
##        button3.grid(row=4,column=1,padx=10,pady=10) 
##

class Reports(tk.Frame):
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       
       fontstyle = tkFont.Font(family="Lucida Grande", size=40)
       label = tk.Label(self,text="Select one of the Options below:",font=fontstyle)
       label.pack(expand=True)

       frame = tk.Frame(self)
       frame.pack(expand=True)

       ButtonFrame = tk.Frame(self)
       ButtonFrame.pack(expand=True)

       database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library')
       
       angelstyle = tkFont.Font(family="Lucida Grande", size=30)

       button1 = tk.Button(frame,text = "11. Book Search", command = lambda : [self.update(),controller.show_frame(BookSearch)],font=angelstyle)
       button1.grid(row=0,column=0,ipady=20, ipadx=180)
       button2 = tk.Button(frame,text = "12. Books on Loan", command = lambda : [self.update(),controller.show_frame(booksOnLoan)],font=angelstyle)#command
       button2.grid(row=1,column=0,ipady=20, ipadx=180)
       button3 = tk.Button(frame,text = "13. Books on Reservation", command = lambda : [self.update(),controller.show_frame(booksOnReservation)],font=angelstyle) #command
       button3.grid(row=3,column=0,ipady=20, ipadx=180)
       button4 = tk.Button(frame,text = "14. Outstanding Fines", command = lambda : [self.update(),controller.show_frame(outstandingFines)],font=angelstyle) #command
       button4.grid(row=2,column=0,ipady=20, ipadx=180)
       button5 = tk.Button(frame,text = "15. Books on Loan to Member", command = lambda : [self.update(),controller.show_frame(BooksOnLoanToMember)],font=angelstyle)
       button5.grid(row=4,column=0,ipady=20, ipadx=180)
       
       button6 = ttk.Button(ButtonFrame,text = "Back to Main Menu", command = lambda : controller.show_frame(ALSMainPage))
       button6.grid(row=0,column=0,ipady=50, ipadx=100)

class BookSearch(tk.Frame):
   def __init__(self,parent,controller):
       Book_Title = tk.StringVar()
       Author = tk.StringVar()
       ISBN_Num = tk.StringVar()
       Publisher = tk.StringVar()
       Year_Published = tk.StringVar()

       tk.Frame.__init__(self,parent)
       fontstyle = tkFont.Font(family="Lucida Grande", size=40)
       label = tk.Label(self, text = "Search based on one of the categories below:", font = fontstyle, bg="cyan")
       label.pack(expand=True)

       middleFrame = tk.Frame(self)
       middleFrame.pack(expand=True)

       leftFrame = tk.Frame(middleFrame)
       leftFrame.pack(side = LEFT, expand=True)

       rightFrame = tk.Frame(middleFrame)
       rightFrame.pack(side = LEFT, expand=True)
  
       ButtonFrame = tk.Frame(self)
       ButtonFrame.pack(expand=True)

       angelstyle = tkFont.Font(family="Lucida Grande", size=30)

       l1 = tk.Label(leftFrame, text = "Title", font = angelstyle)
       l1.grid(row=0,column=0,ipady=30, ipadx=80)
       e1 = ttk.Entry(rightFrame, textvariable = Book_Title)
       e1.grid(row=0,column=0,ipady=30, ipadx=170)

       l2 = tk.Label(leftFrame, text = "Authors", font = angelstyle)
       l2.grid(row=1,column=0,ipady=30, ipadx=80)
       e2 = ttk.Entry(rightFrame, textvariable = Author)
       e2.grid(row=1,column=0,ipady=30, ipadx=170)

       l3 = tk.Label(leftFrame, text = "ISBN", font = angelstyle)
       l3.grid(row=2,column=0,ipady=30, ipadx=80)
       e3 = ttk.Entry(rightFrame, textvariable = ISBN_Num)
       e3.grid(row=2,column=0,ipady=30, ipadx=170)

       l4 = tk.Label(leftFrame, text = "Publisher", font = angelstyle)
       l4.grid(row=3,column=0,ipady=30, ipadx=80)
       e4 = ttk.Entry(rightFrame, textvariable = Publisher)
       e4.grid(row=3,column=0,ipady=30, ipadx=170)

       l5 = tk.Label(leftFrame, text = "Publication Year", font = angelstyle)
       l5.grid(row=4,column=0,ipady=30, ipadx=80)
       e5 = ttk.Entry(rightFrame, textvariable = Year_Published)
       e5.grid(row=4,column=0,ipady=30, ipadx=170)

       def bookSearch():

            title = e1.get()
            author = e2.get()
            isbn = e3.get()
            pub = e4.get()
            pubyr = e5.get()

            touse = ["title", "author", "isbn", "publisher", "pubYear"]  
            lst = [title, author, isbn, pub, pubyr]
            use = title
            indx = 0
            
            for i in range(5) :
                if len(lst[i]) != 0:
                    use = lst[i]
                    break
                
                indx += 1
                
            database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library') ###
            colToSearch = touse[indx]

            if colToSearch == "author" :
                
                query = f"SELECT accessionNo, title, isbn, publisher, pubYear FROM Book WHERE accessionNo IN (SELECT accessionNo FROM author WHERE author LIKE '% {use} %'\
                OR author LIKE '{use}' OR author LIKE '% {use}' OR author LIKE '{use} %')"
                lst = pd.read_sql_query(query,database).values.tolist()

                mainlist = []
                accnolst = []
                for row in lst :
                    accnolst.append(row[0])
                    inner = []
                    inner.append(row[1])
                    inner.append(row[2])
                    inner.append(row[3])
                    inner.append(row[4])
                    mainlist.append(inner)

                authorlist = []

                for accno in accnolst:
                    authorstring = ""
                    query2 = f"SELECT author FROM Author WHERE accessionNo = '{accno}'"
                    authorforonebook = pd.read_sql_query(query2,database).values.tolist()
                    for author in authorforonebook:
                        if authorstring == "" :
                            authorstring += author[0]
                        else:
                            authorstring += f", {author[0]}"

                    authorlist.append(authorstring)

                for i in range(len(mainlist)) :

                    mainlist[i].insert(1, authorlist[i])
                    


                    

            else :
                
                query = f"SELECT * FROM Book WHERE {colToSearch} LIKE '% {use} %' OR {colToSearch} LIKE '{use}' OR {colToSearch} LIKE '% {use}' OR {colToSearch} LIKE '{use} %' "
                lst = pd.read_sql_query(query,database).values.tolist()

                mainlist = []
                accnolst = []

                for row in lst:
                    accnolst.append(row[0])
                    inner = []
                    inner.append(row[1])
                    inner.append(row[2])
                    inner.append(row[3])
                    inner.append(row[4])
                    mainlist.append(inner)

                authorlist = []

                for accno in accnolst:
                    authorstring = ""
                    query2 = f"SELECT author FROM Author WHERE accessionNo = '{accno}'"
                    authorforonebook = pd.read_sql_query(query2, database).values.tolist()
                    for author in authorforonebook:
                        if authorstring == "":
                            authorstring += author[0]
                        else:
                            authorstring += f", {author[0]}"

                    authorlist.append(authorstring)

                for i in range(len(mainlist)):

                    mainlist[i].insert(1,authorlist[i])
                    
                
            
            
            heynow = Toplevel()
            tree = ttk.Treeview(heynow, columns = tuple(touse), show = 'headings')
            tree.pack()

            for i in range(5):
                tree.heading(touse[i], text = touse[i])

            for row in mainlist:
                tree.insert("",tk.END, value = tuple(row))

            button1 = ttk.Button(heynow, text = "Back to Search function", command = lambda : [heynow.destroy(),controller.show_frame(BookSearch)])
            button1.pack(side = BOTTOM)

            e1.delete(0,END) #this
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END) #to this


       button1 = ttk.Button(ButtonFrame,text = "Search Book", command = bookSearch)
       button1.grid(row=0,column=0,ipady=40, ipadx=90)
       button2 = ttk.Button(ButtonFrame,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
       button2.grid(row=0,column=1,ipady=40, ipadx=90)

       



class booksOnLoan(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fontstyle = tkFont.Font(family="Lucida Grande", size=70)
        label = tk.Label(self, text = "Books on Loan Report", font = fontstyle)
        label.pack(expand=True) # side = TOP as default. 
        # we try the .pack() method of arranging things. 
        # label.grid(row=0,column=2,padx=10,pady=10) 

        frame = Frame(self)
        frame.pack(expand=True)

        ButtonFrame = tk.Frame(self)
        ButtonFrame.pack(expand=True)
        
        database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library') #
        
        query ="SELECT AccessionNo FROM Borrows"
        accnolist = pd.read_sql_query(query,database).values.tolist()
        booksonloanlist = []
        for accno in accnolist:
            acclist = []
            woauthor = []
            query2 = f"SELECT * FROM Book WHERE accessionNo = '{accno[0]}'"
            query3 = f"SELECT author FROM Author WHERE accessionNo = '{accno[0]}'"
            authorstring = ""
            authorlist = pd.read_sql_query(query3,database).values.tolist()
            
            for i in authorlist:
                if i == authorlist[0]:
                    authorstring +=i[0]
                else:
                    authorstring += f", {i[0]}"
            acclist+=(pd.read_sql_query(query2,database).values.tolist())
            acclist[0].insert(2,authorstring)
            booksonloanlist += acclist
                
                
                
           
           
           
           
        columns = ("Acc_Num", "Tit", "Auth", "isbn", "Pub", "Yr")
        nama_col = ("Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year")
        tree = ttk.Treeview(frame, columns=columns, show='headings')
        tree.pack()
        for i in range(6):
            tree.heading(columns[i], text = nama_col[i])
       

        for row in booksonloanlist :
            tree.insert("", tk.END, value= tuple(row))

        angelstyle = tkFont.Font(family="Lucida Grande", size=20)

        button1 = tk.Button(ButtonFrame,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports), font = angelstyle)
        button1.grid(row=0,column=0,ipady=40, ipadx=80)

class booksOnReservation(tk.Frame):
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)

       fontstyle = tkFont.Font(family="Lucida Grande", size=70)
       label = tk.Label(self, text = "Books on Reservation Report", font = fontstyle, bg="pink")
       label.pack(expand=True)

       frame = Frame(self)
       frame.pack(expand=True)
       
       database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library') ##
       
       query = "SELECT r.accessionNo, b.title, r.memberID, m.name FROM reserves r LEFT JOIN Book b ON r.accessionNo = b.accessionNo LEFT JOIN Member m ON r.memberID = m.memberID"
       bor = pd.read_sql_query(query,database).values.tolist()
       
       columns = ("a", "b", "c", "d")
       nama_col = ("Accession Number", "Title", "Membership ID", "Name")
       tree = ttk.Treeview(frame, columns=columns, show='headings')
       tree.pack(expand=True)
       
       for i in range(len(columns)):
           tree.heading(columns[i], text = nama_col[i])

       for row in bor :
           tree.insert("", tk.END, value = tuple(row))

       ButtonFrame = tk.Frame(self)
       ButtonFrame.pack(expand=True)
       
       button1 = ttk.Button(ButtonFrame,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
       button1.grid(row=0,column=0,ipady=30, ipadx=60)

class outstandingFines(tk.Frame):
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       
       fontstyle = tkFont.Font(family="Lucida Grande", size=70)
       label = tk.Label(self, text = "Members With Outstanding Fines", font = fontstyle, bg="pink")
       label.pack(expand=True)

       frame = Frame(self)
       frame.pack(expand=True)
       
       database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library') ###
       
       query = "SELECT * FROM Member WHERE memberID IN (SELECT memberID FROM Fine)"
       outstandingfines = pd.read_sql_query(query,database).values.tolist()
       
       columns = ("a", "b", "c", "d", "e")
       nama_col = ("Membership ID", "Name", "Faculty", "Phone Number", "Email Address")
       tree = ttk.Treeview(frame, columns=columns, show='headings')
       tree.pack(expand=True)
       
       for i in range(len(columns)):
           tree.heading(columns[i], text = nama_col[i])

       for row in outstandingfines :
           tree.insert("", tk.END, value = tuple(row))

       ButtonFrame = tk.Frame(self)
       ButtonFrame.pack(expand=True)

       button1 = ttk.Button(ButtonFrame,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
       button1.grid(row=0,column=0,ipady=30, ipadx=60)


class BooksOnLoanToMember(tk.Frame):
   def __init__(self,parent,controller):
       Member_Id = tk.StringVar() # is this object created within the scope of this class? or global?

       tk.Frame.__init__(self,parent)
       
       fontstyle = tkFont.Font(family="Lucida Grande", size=70)
       label = tk.Label(self, text = "Books on Loan to Member", font = fontstyle, bg="cyan")
       label.pack(expand=True)

       frame = tk.Frame(self)
       frame.pack(expand=True)

       angelstyle = tkFont.Font(family="Lucida Grande", size=40)
       
       database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library')#
       
       l1 = tk.Label(frame, text = "Membership_ID",font = angelstyle)
       l1.grid(row=0,column=0,ipady=50, ipadx=90)
       entry_1 = ttk.Entry(frame, textvariable = Member_Id)
       entry_1.grid(row=0,column=1,ipady=50, ipadx=150)

       def booksonloantomembersresults():

           memberid = entry_1.get() 
           win = tk.Toplevel()
           
           database = create_engine('mysql+mysqlconnector://root:wyerock@localhost/library')#
           
           label = ttk.Label(win, text = "Books on Loan to Member", font = LARGEFONT)
           label.pack()

           #frame = Frame(win)
           #frame.pack()
           columns = ("a", "b", "c", "d", "e", "f")
           colname = ("Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year")
           tree = ttk.Treeview(win, columns=columns, show = "headings")
           tree.pack()

           for i in range(len(columns)):
               tree.heading(columns[i], text = colname[i])



           mainlist = []

           authorlist = []
           
           query = f"SELECT accessionNo FROM Borrows WHERE memberID = '{memberid}'"
           accnolst = pd.read_sql_query(query,database).values.tolist()


           for accno in accnolst :
               query2 = f"SELECT author FROM Author WHERE accessionNo = '{accno[0]}'"
               authorstring = "" 
               authorlst = pd.read_sql_query(query2,database).values.tolist()

               for author in authorlst:
                   if authorstring == "" :
                       authorstring += author[0]
                   else:
                       authorstring += f", {author[0]}"

                   authorlist.append(authorstring)
           

           for accno in accnolst :
               query3 = f"SELECT title, isbn, publisher, pubYear FROM Book WHERE accessionNo = '{accno[0]}'"
               lstofitems = pd.read_sql_query(query3,database).values.tolist()
               
               for row in lstofitems :
                   inner = []
                   inner.append(row[0])
                   inner.append(row[1])
                   inner.append(row[2])
                   inner.append(row[3])
                   mainlist.append(inner)

            
           for i in range(len(mainlist)):

               mainlist[i].insert(1,authorlist[i])


           for row in mainlist:
               
               tree.insert("", tk.END, value = tuple(row))

           button2 = ttk.Button(win, text = "Back to Reports Menu",command = lambda : [win.destroy(), controller.show_frame(Reports)])
           button2.pack(side = BOTTOM)

           entry_1.delete(0, END)


       ButtonFrame = tk.Frame(self)
       ButtonFrame.pack(expand=True)
            
       button1 = ttk.Button(ButtonFrame,text = "Search Member", command = booksonloantomembersresults) 
       button1.grid(row=0,column=0,ipady=30, ipadx=70)
       button2 = ttk.Button(ButtonFrame,text="Back to Reports Menu", command = lambda : controller.show_frame(Reports))
       button2.grid(row=0,column=1,ipady=30, ipadx=70)

       



        
app = tkinterApp()
app.mainloop()
