import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
import csv
import random,string
from datetime import datetime
import time
import ast
from PIL import ImageTk,Image
import tkinter.font
#AUTO GENERATING CODE
def autocode():
       code=random.randint(1000,9999)
       f=open("customerdetails.csv","r")
       csvobj=csv.reader(f)
       for rec in csvobj:
                     if code==int(rec[0]):
                            autocode()
       return code
#AUTO GENERATING KEY
def autokey():
       global key
       size=4
       char=string.digits + string.ascii_letters
       s=""
       key=s.join(random.choice(char) for x in range(size))
       f=open("customerdetails.csv","r")
       csvobj=csv.reader(f)
       for rec in csvobj:
                     if key==rec[1]:
                            autokey()
       return key
#NAME VALIDATION
def callbackname(input):
    if input.isalpha():
        return True
    elif input=="":
        return True
    else:
        return False
#GENDER VALIDATION
def OnButtonClickGender(value):
    global gender
    if value ==1:
        gender="M"
    elif value==2:
        gender="F"
    elif value==3:
        gender="other"
#MOBILE NUMBER VALIDATION
def callbackmobile(input):
    if input.isdigit():
        return True
    elif input=="":
        return True
    else:
        return False
#AUTO GENERATING USERNAME
def autousername(fname,lname):
              char=string.digits
              s=""
              fname_random=s.join(random.choice(fname) for x in range(2))
              num=s.join(random.choice(char) for x in range(3))
              lname_random=s.join(random.choice(lname) for x in range(2))
              username=fname_random+num+lname_random
              f=open("customerdetails.csv","r")
              csvobj=csv.reader(f)
              for rec in csvobj:
                            if username==rec[7]:
                                   autousername()
              return username
#AUTO GENERATING PASSWORD
def autopassword():
       size=10
       char=string.digits + string.ascii_letters
       s=""
       password=s.join(random.choice(char) for x in range(size))
       f=open("customerdetails.csv","r")
       csvobj=csv.reader(f)
       for rec in csvobj:
                     if password==rec[8]:
                            autopassword()
       return password
#ACCOUNT TYPE
def OnButtonClickAccType(value):
    global acctype
    if value ==1:
        acctype="SAVING"
    elif value==2:
        acctype="CHECKING"
#AUTO GENERATING ACCOUNT NUMBER
def autoaccountnum(acctype):
       char=string.digits
       s=""
       accnum=s.join(random.choice(char) for x in range(6))
       if acctype=="CHECKING":
              accnum="3475"+accnum
       elif acctype=="SAVING":
              accnum="9532"+accnum
       f=open("customerdetails.csv","r")
       csvobj=csv.reader(f)
       for rec in csvobj:
                     if accnum==rec[10]:
                            autoaccountnum()
       return accnum
#TRANSACTION HISTORY
def yearlytrans():
    global ytrans
    ytrans=tk.Tk()
    ytrans.title("Yearly Transaction History")
    ytrans.configure(background="#3300AA")
    ytrans.geometry("1069x742")
    scrollbar =tk.Scrollbar(ytrans)
    scrollbar.pack(side=tk.RIGHT, fill =tk.Y )
    f=open("customerdetails.csv","r")
    csvobj=csv.reader(f)
    mylist =tk.Listbox(ytrans, yscrollcommand = scrollbar.set,height = 10,width=500,justify=tk.CENTER,font=("Times", 25))
    code=log3.get()
    current_year= datetime.now().strftime('%Y')
    for rec in csvobj:
            if rec[0]==code:
                   balance=rec[11]
                   list1=rec[13]
                   list2=ast.literal_eval(list1)
                   for k in list2:
                      date=k[0]
                      year=date[7]+date[8]+date[9]+date[10]
                      if k[1]=="-":
                             depwith="Amount withdrawn:"
                      else:
                             depwith="Amount deposited:"
                      amount=str(k[2])
                      if year==current_year:
                             mylist.insert(tk.END,"Date:"+date+''+depwith+amount)
                   break
    mylist.insert(tk.END,"Your current balance is:"+ str(balance))
    mylist.pack(side=tk.LEFT,fill=tk.BOTH)
    scrollbar.config(command=mylist.yview)
    ytrans.mainloop()



def monthlytrans():
    global mtrans
    mtrans=tk.Tk()
    mtrans.title("Monthly Transaction History")
    mtrans.configure(background="#3300AA")
    mtrans.geometry("1069x742")
    scrollbar =tk.Scrollbar(mtrans)
    scrollbar.pack(side=tk.RIGHT, fill =tk.Y )
    f=open("customerdetails.csv","r")
    csvobj=csv.reader(f)
    mylist =tk.Listbox(mtrans, yscrollcommand = scrollbar.set,height = 10,width=500,justify=tk.CENTER,font=("Times", 25))
    code=log3.get()
    current_month = datetime.now().strftime('%h')
    current_year= datetime.now().strftime('%Y')
    for rec in csvobj:
            if rec[0]==code:
                   balance=rec[11]
                   list1=rec[13]
                   list2=ast.literal_eval(list1)
                   for k in list2:
                      date=k[0]  
                      month=date[3]+date[4]+date[5]
                      year=date[7]+date[8]+date[9]+date[10]
                      if k[1]=="-":
                             depwith="Amount withdrawn:"
                      else:
                             depwith="Amount deposited:"
                      amount=str(k[2])
                      if month==current_month and year==current_year:
                             mylist.insert(tk.END,"Date:"+date+''+depwith+amount)
                   break
    mylist.insert(tk.END,"Your current balance is:"+ str(balance))
    mylist.pack(side=tk.LEFT,fill=tk.BOTH)
    scrollbar.config(command=mylist.yview)
    mtrans.mainloop()

def alltimetrans():
    global alltrans
    alltrans=tk.Tk()
    alltrans.title("All Time Transaction History")
    alltrans.configure(background="#3300AA")
    alltrans.geometry("1069x742")
    scrollbar =tk.Scrollbar(alltrans)
    scrollbar.pack(side=tk.RIGHT, fill =tk.Y )
    f=open("customerdetails.csv","r")
    csvobj=csv.reader(f)
    mylist =tk.Listbox(alltrans, yscrollcommand = scrollbar.set,height = 10,width=500,justify=tk.CENTER,font=("Times", 25))
    code=log3.get()
    for rec in csvobj:
        if rec[0]==code:
               balance=rec[11]
               list1=rec[13]
               list2=ast.literal_eval(list1)
               for k in list2:
                      date=k[0]
                      if k[1]=="-":
                             depwith="Amount withdrawn:"
                      else:
                             depwith="Amount deposited:"
                      amount=str(k[2])
                      mylist.insert(tk.END,"Date:"+date+''+depwith+amount)
               break
    mylist.insert(tk.END,"Your current balance is:"+ str(balance))
    mylist.pack(side=tk.LEFT,fill=tk.BOTH)
    scrollbar.config(command=mylist.yview)
    alltrans.mainloop()
def transactionhistory():
    global trans
    trans=tk.Tk()
    trans.title("Transaction History")
    trans.configure(background="#3300AA")
    trans.geometry("1069x742")
    l_title=tk.Message(trans,text="My Transcation History",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    var=tk.IntVar()
    M1= tk.Radiobutton(trans, text="Show all time transaction history",variable=var,value=1,indicator=0,command=lambda:alltimetrans())
    M1.place(relx=0.15, rely=0.2, relheight=0.17, relwidth=0.6)
    M1.configure(activebackground="#bfbfbf")
    M1.configure(background="#B7DDE2")
    M1.configure(font=50)
    M1.configure(foreground="#000000")
    M1.configure(justify="left")
    M2= tk.Radiobutton(trans, text="Show my transaction history this month",variable=var,value=2,indicator=0,command=lambda:monthlytrans())
    M2.place(relx=0.15, rely=0.4, relheight=0.17,relwidth=0.6)
    M2.configure(activebackground="#bfbfbf")
    M2.configure(background="#B7DDE2")
    M2.configure(font=14)
    M2.configure(foreground="#000000")
    M2.configure(justify="left")
    M3= tk.Radiobutton(trans, text="Show my transaction history this year",variable=var,value=2,indicator=0,command=lambda:yearlytrans())
    M3.place(relx=0.15, rely=0.6, relheight=0.17,relwidth=0.6)
    M3.configure(activebackground="#bfbfbf")
    M3.configure(background="#B7DDE2")
    M3.configure(font=14)
    M3.configure(foreground="#000000")
    M3.configure(justify="left")
    M4= tk.Radiobutton(trans, text="Quit",variable=var,value=3,indicator=0,justify="left",command=trans.destroy)
    M4.place(relx=0.15, rely=0.8, relheight=0.17,relwidth=0.6)
    M4.configure(activebackground="#B7DDE2")
    M4.configure(background="#bfbfbf")   
    trans.mainloop()

#FAQ
def faq():
    faq=tk.Tk()
    faq.title("Aamshel Bank")
    faq.configure(background="#3300AA")
    faq.geometry("1069x742")
    fr1=tk.Frame(faq)
    fr1.pack(side="top")
    l_title=tk.Message(faq,text="FAQ about Loans",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    q1=tk.Message(faq,text="Am I eligible for a home loan ?"+"\n"+"At Aamshel Bank,you can get a loan ranging from a minimum of Rs 5 lakh to a maximum of Rs 1 crore,based on your repayment capacity and the cost of the property.You will be eligible for a maximum of 80% of the cost of the property or the cost of construction as applicable and 65% of the cost of land in case of purchase of land",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q1.config(font=("Times New Roman","12"))
    q1.place(relx=0, rely=0.1, relheight=0.3,relwidth=0.3)
    q2=tk.Message(faq,text="Who is a co-applicant? Is a co-applicant mandatory for a loan?"+"\n"+"A co-applicant is not mandatory to avail a Home Loan. Personal Guarantor is required if there is no co-applicant. The co-applicant may be a resident Indian or an NRI.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q2.config(font=("Times New Roman","12"))
    q2.place(relx=0.3, rely=0.1, relheight=0.3,relwidth=0.3)
    q3=tk.Message(faq,text="What are the different tenures you offer on your loans?"+"\n"+"You can select a term of up to 15 years. However, you cannot opt for a term that extends beyond your attaining retirement age or 60 years of age (whichever is earlier). For GCC: Tenure between 11-15 years. Minimum qualification: post-graduate / professional qualification.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q3.config(font=("Times New Roman","12"))
    q3.place(relx=0.6, rely=0.1, relheight=0.3,relwidth=0.5)
    q4=tk.Message(faq,text="When do you disburse the loan?"+"\n"+"Your loan will be disbursed after you have selected a property; submitted all the necessary legal documents; the property is technically and legally cleared; and you have paid your own contribution toward the purchase of the home. The cheque for the loan amount is drawn in favour of the builder or seller as the case may be. In the case of an under-construction property, ICICI Bank disburses loan amounts appropriate to the state of construction.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q4.config(font=("Times New Roman","12"))
    q4.place(relx=0, rely=0.4, relheight=0.3,relwidth=0.3)
    q5=tk.Message(faq,text="How do I repay the loan?"+"\n"+"Repayment is done in equated monthly instalments (EMIs), and includes interest and principal amount calculated on monthly rests. You can pay EMIs by issuing post-dated cheques from your NRE / NRO account, or any other account approved by the Reserve Bank of India (RBI). In the case of part-disbursement of the loan, the monthly interest is payable only on the disbursed amount. This is called pre-EMI interest, and is payable monthly till the final disbursement is made, after which EMIs will commence.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q5.config(font=("Times New Roman","12"))
    q5.place(relx=0.6, rely=0.4, relheight=0.3,relwidth=0.5)
    q6=tk.Message(faq,text="What are the prepayment options?"+"\n"+"You can prepay part of the loan at no cost during the tenure of the loan",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q6.config(font=("Times New Roman","12"))
    q6.place(relx=0.3, rely=0.4, relheight=0.3,relwidth=0.3)
    q7=tk.Message(faq,text="Can I foreclose the loan?"+"\n"+"Yes, you can foreclose the loan before its original tenure expires. You will be charged 2% on the outstanding amount and whatever has been pre-paid in the last 12 months.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q7.config(font=("Times New Roman","12"))
    q7.place(relx=0, rely=0.7, relheight=0.2,relwidth=0.3)
    q8=tk.Message(faq,text="If I foreclose the loan, how will you return the original property documents to me?"+"\n"+"Your POA holder can come and collect the original documents personally from our office. They will be handed over after he / she provides proof of identity.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q8.config(font=("Times New Roman","12"))
    q8.place(relx=0.3, rely=0.7, relheight=0.2,relwidth=0.3)
    q9=tk.Message(faq,text="Can I switch between fixed and floating interest rates during the tenure of the loan?"+"\n"+"Yes you can. You can switch from a floating rate to a fixed rate any time by paying a nominal switching fee of 1.75% of the outstanding loan. You can also switch from a fixed rate to a floating rate by paying a nominal switching fee of 1.75% of the outstanding loan.",relief="raised",fg="white",bg="#3300AA", anchor="w")
    q9.config(font=("Times New Roman","12"))
    q9.place(relx=0.6, rely=0.7, relheight=0.2,relwidth=0.5)
    var=tk.IntVar()
    M5= tk.Radiobutton(faq, text="Quit",variable=var,value=5,indicator=0,justify="left",command=faq.destroy,anchor="center")
    M5.place(relx=0.3, rely=0.9, relheight=0.1,relwidth=0.3)
    M5.configure(activebackground="#B7DDE2")
    M5.configure(font=("Courier",50,"bold"))
    M5.configure(background="#bfbfbf")   
    faq.mainloop()

#creditcardnumbergeneration
from random import randint

def genccnum(type):
    
   
    cctype= ["americanexpress","visa13", "visa16","mastercard"]
    
    def fillbefore(t):
        # typical number of digits in credit card
        def_length = 16
        
        if t == cctype[0]:
            # american express starts with 3 and is 15 digits long
            return [3, randint(4,7)], 13
            
        elif t == cctype[1] or t == cctype[2]:
            # visa starts with 4
            if t.endswith("16"):
                return [4], def_length - 1
            else:
                return [4], 12
            
        elif t == cctype[3]:
            # master card start with 5 and is 16 digits long
            return [5, randint(1,5)], def_length - 2
            
            
        else:
            return [], def_length
    
    def final(numlength):
        
        check_sum = 0
        
        #is_even = True if (len(nums) + 1 % 2) == 0 else False
        
        
        check_offset = (len(numlength) + 1) % 2
        
        for i, n in enumerate(numlength):
            if (i + check_offset) % 2 == 0:
                n_ = n*2
                check_sum += n_ -9 if n_ > 9 else n_
            else:
                check_sum += n
        return numlength + [10 - (check_sum % 10) ]
    
    # main body
    t = type.lower()
    if t not in cctype:
        print ("Unknown type: '%s'" % type)
        print ("Please pick one of these supported types: %s" % cctype)
        return
    
    initial, rem = fillbefore(t)
    chk2 = initial + [randint(1,9) for x in range(rem - 1)]
    f=open("customerdetails.csv","r")
    csvobj=csv.reader(f)
    reclist=[]
    for rec in csvobj:
                     if rec[0]==log3.get():
                            rec[14]="".join(map(str,final(chk2)))
                            reclist.append(rec)
                     else:
                            reclist.append(rec)
    f.close()
    f=open("customerdetails.csv","w",newline="")
    csvobj=csv.writer(f)
    csvobj.writerows(reclist)
    
    L1= tk.Label(credit, text="Card type-  %s: "% t)
    L1.place(relx=0.15, rely=0.6, relheight=0.1, relwidth=0.6)
    L1.configure(background="#B7DDE2")
    L1.configure(font=50)
    L1.configure(foreground="#000000")
    L1.configure(justify="left")
    L2= tk.Label(credit, text="".join(map(str,final(chk2))))
    L2.place(relx=0.15, rely=0.7, relheight=0.1, relwidth=0.6)
    L2.configure(background="#B7DDE2")
    L2.configure(font=50)
    L2.configure(foreground="#000000")
    L2.configure(justify="left")
    
       
       
def generate_credit_card():
        global credit
        credit=tk.Tk()
        credit.title("Aamshel Bank")
        credit.configure(background="#3300AA")
        credit.geometry("1069x742")
        l_title=tk.Message(credit,text="Choose a credit card type ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        var=tk.IntVar()
        M1= tk.Radiobutton(credit, text="americanexpress",variable=var,value=1,indicator=0,command=lambda:genccnum("americanexpress"))
        M1.place(relx=0.15, rely=0.2, relheight=0.1, relwidth=0.6)
        M1.configure(activebackground="#bfbfbf")
        M1.configure(background="#B7DDE2")
        M1.configure(font=50)
        M1.configure(foreground="#000000")
        M1.configure(justify="left")
        M2= tk.Radiobutton(credit, text="visa13",variable=var,value=2,indicator=0,command=lambda:genccnum("visa13"))
        M2.place(relx=0.15, rely=0.3, relheight=0.1,relwidth=0.6)
        M2.configure(activebackground="#bfbfbf")
        M2.configure(background="#B7DDE2")
        M2.configure(font=14)
        M2.configure(foreground="#000000")
        M2.configure(justify="left")
        M3= tk.Radiobutton(credit, text="visa16",variable=var,value=3,indicator=0,command=lambda:genccnum("visa16"))
        M3.place(relx=0.15, rely=0.4, relheight=0.1, relwidth=0.6)
        M3.configure(activebackground="#bfbfbf")
        M3.configure(background="#B7DDE2")
        M3.configure(font=50)
        M3.configure(foreground="#000000")
        M3.configure(justify="left")
        M4= tk.Radiobutton(credit, text="mastercard",variable=var,value=4,indicator=0,command=lambda:genccnum("mastercard"))
        M4.place(relx=0.15, rely=0.5, relheight=0.1,relwidth=0.6)
        M4.configure(activebackground="#bfbfbf")
        M4.configure(background="#B7DDE2")
        M4.configure(font=14)
        M4.configure(foreground="#000000")
        M4.configure(justify="left")
        M5= tk.Radiobutton(credit, text="Quit",variable=var,value=5,indicator=0,justify="left",command=credit.destroy)
        M5.place(relx=0.15, rely=0.8, relheight=0.1,relwidth=0.6)
        M5.configure(activebackground="#B7DDE2")
        M5.configure(background="#bfbfbf")   
        credit.mainloop()



#WITHDRAW MONEY
def withdraw():
    f=open("customerdetails.csv","r")
    csvobj=csv.reader(f)
    code=log3.get()
    for rec in csvobj:
        if rec[0]==code:
            balance=rec[11]
            ccnum=rec[14]
    if ccnum==E2.get():
        global E3
        global withdraw_screen
        withdraw_screen=tk.Tk()
        withdraw_screen.title("Withdraw")
        withdraw_screen.configure(background="#3300AA")
        withdraw_screen.geometry("1069x742")
        l_title=tk.Message(withdraw_screen,text="Withdraw Money",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        #current balance
        L1= tk.Label(withdraw_screen, text="Current Balance : £"+balance)
        L1.place(relx=0.15, rely=0.2, relheight=0.17, relwidth=0.6)
        L1.configure(background="#B7DDE2")
        L1.configure(font=50)
        L1.configure(foreground="#000000")
        L1.configure(justify="left")
        #Amont Label
        L2= tk.Label(withdraw_screen, text="Amount to be withdrawn: ")
        L2.place(relx=0.15, rely=0.4, relheight=0.05,relwidth=0.25)
        L2.configure(background="#B7DDE2")
        L2.configure(font=14)
        L2.configure(foreground="#000000")
        L2.configure(justify="left")
        #Amount Entry
        E3=tk.Entry(withdraw_screen,relief="solid",bd=3)
        E3.place(relx=0.50, rely=0.4, relheight=0.05, relwidth=0.25)
        reg=withdraw_screen.register(callbackmobile)
        E3.config(validate ="key",validatecommand =(reg, '%P'))
        #OK
        var=tk.IntVar()
        b1=tk.Radiobutton(withdraw_screen,text="OK",command=finish_withdraw,variable=var,value=1,indicator=0,justify="left")
        b1.place(relx=0.3, rely=0.7, relheight=0.05, relwidth=0.25)
        b1.configure(activebackground="#B7DDE2")
        b1.configure(background="#bfbfbf")   
        #QUIT
        b2= tk.Radiobutton(withdraw_screen, text="Quit",variable=var,value=2,indicator=0,justify="left",command=withdraw_screen.destroy)
        b2.place(relx=0.3, rely=0.8, relheight=0.05,relwidth=0.25)
        b2.configure(activebackground="#B7DDE2")
        b2.configure(background="#bfbfbf")   
        withdraw_screen.mainloop()    
    else:
        tk.messagebox.showinfo("Error","Invalid credit card number entered",parent=withdep_screen)
        withdep_screen.destroy()
def finish_withdraw():
    global updated_balance
    if E3.get() == "":
        tk.messagebox.showinfo('Error', "Amount is Required",parent=withdraw_screen)
        withdraw_screen.destroy()
        withdraw_deposit()
    else:
        f = open("customerdetails.csv", "r",newline="")
        csvobj= csv.reader(f)
        reclist=[]
        code=log3.get()
        for rec in csvobj:
            if rec[0]==code:
                if float(E3.get())>float(rec[11]):
                    tk.messagebox.showinfo('Error', "You do not have the required amount in your bank account",parent=withdraw_screen)
                    withdraw_screen.destroy()
                    withdraw_deposit()
                else:
                    updated_balance=float(rec[11])-float(E3.get())
                    rec[11]=updated_balance
                    dateTimeObj = datetime.now()
                    dateStr = dateTimeObj.strftime("%d %b %Y ")
                    list1=rec[13]
                    list2=ast.literal_eval(list1)
                    list2+=[[dateStr,"-",float(E3.get())]]
                    rec[13]=list2
                    reclist.append(rec)
            else:
                   reclist.append(rec)
        f.close()
        f = open("customerdetails.csv", "w",newline="")
        csvobj= csv.writer(f)
        csvobj.writerows(reclist)
        f.close()
        tk.messagebox.showinfo('Balance', "Current Balance : £"+str(updated_balance),parent=withdraw_screen)
        withdraw_screen.destroy()
        window1.destroy()




#DEPOSIT MONEY
def deposit():
    f=open("customerdetails.csv","r")
    csvobj=csv.reader(f)
    code=log3.get()
    for rec in csvobj:
        if rec[0]==code:
            balance=rec[11]
            ccnum=rec[14]
    if ccnum==E2.get():
        global E1
        global deposit_screen
        deposit_screen=tk.Tk()
        deposit_screen.title("Deposit")
        deposit_screen.configure(background="#3300AA")
        deposit_screen.geometry("1069x742")
        l_title=tk.Message(deposit_screen,text="Deposit Money",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
        l_title.config(font=("Courier","50","bold"))
        l_title.pack(side="top")
        #current balance
        L1= tk.Label(deposit_screen, text="Current Balance : £"+balance)
        L1.place(relx=0.15, rely=0.2, relheight=0.17, relwidth=0.6)
        L1.configure(background="#B7DDE2")
        L1.configure(font=50)
        L1.configure(foreground="#000000")
        L1.configure(justify="left")
        #Amont Label
        L2= tk.Label(deposit_screen, text="Amount to be deposited: ")
        L2.place(relx=0.15, rely=0.4, relheight=0.05,relwidth=0.25)
        L2.configure(background="#B7DDE2")
        L2.configure(font=14)
        L2.configure(foreground="#000000")
        L2.configure(justify="left")
        #Amount Entry
        E1=tk.Entry(deposit_screen,relief="solid",bd=3)
        E1.place(relx=0.50, rely=0.4, relheight=0.05, relwidth=0.25)
        reg=deposit_screen.register(callbackmobile)
        E1.config(validate ="key",validatecommand =(reg, '%P'))
        #OK
        var=tk.IntVar()
        b1=tk.Radiobutton(deposit_screen,text="OK",command=finish_deposit,variable=var,value=1,indicator=0,justify="left")
        b1.place(relx=0.3, rely=0.7, relheight=0.05, relwidth=0.25)
        b1.configure(activebackground="#B7DDE2")
        b1.configure(background="#bfbfbf")   
        #QUIT
        b2= tk.Radiobutton(deposit_screen, text="Quit",variable=var,value=2,indicator=0,justify="left",command=deposit_screen.destroy)
        b2.place(relx=0.3, rely=0.8, relheight=0.05,relwidth=0.25)
        b2.configure(activebackground="#B7DDE2")
        b2.configure(background="#bfbfbf")   
        deposit_screen.mainloop()
    else:
        tk.messagebox.showinfo("Error","Invalid credit card number entered",parent=withdep_screen)
        withdep_screen.destroy()
def finish_deposit():
    if E1.get() == "":
        tk.messagebox.showinfo('Error', "Amount is Required",parent=deposit_screen)
        deposit_screen.destroy()
        withdraw_deposit()
    elif float(E1.get()) <=0:
        tk.messagebox.showinfo('Error', "Negative currency is not accepted",parent=deposit_screen)
        deposit_screen.destroy()
        withdraw_deposit()
    else:
        f = open("customerdetails.csv", "r",newline="")
        csvobj= csv.reader(f)
        reclist=[]
        code=log3.get()
        for rec in csvobj:
            if rec[0]==code:
                updated_balance=float(rec[11])+float(E1.get())
                rec[11]=updated_balance
                dateTimeObj = datetime.now()
                dateStr = dateTimeObj.strftime("%d %b %Y ")
                list1=rec[13]
                list2=ast.literal_eval(list1)
                list2+=[[dateStr,"+",float(E1.get())]]
                rec[13]=list2
                reclist.append(rec)
            else:
                reclist.append(rec)
        f.close()
        f = open("customerdetails.csv", "w",newline="")
        csvobj= csv.writer(f)
        csvobj.writerows(reclist)
        tk.messagebox.showinfo('Balance', "Current Balance : £"+str(updated_balance),parent=deposit_screen)
        deposit_screen.destroy()      
        window1.destroy()





#WITHDRAW AND DEPOSIT
def check_ccnum(type_):
    global E2
    global withdep_screen
    withdep_screen=tk.Tk()
    withdep_screen.title("Withdraw and Deposit")
    withdep_screen.configure(background="#3300AA")
    withdep_screen.geometry("1069x742")
    l_title=tk.Message( withdep_screen,text="Withdraw Money",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    #Check credit card
    L3= tk.Label( withdep_screen, text="Enter your credit card number: ")
    L3.place(relx=0.15, rely=0.2, relheight=0.05,relwidth=0.25)
    L3.configure(background="#B7DDE2")
    L3.configure(font=14)
    L3.configure(foreground="#000000")
    L3.configure(justify="left")
    E2=tk.Entry(withdep_screen,relief="solid",bd=3)
    E2.place(relx=0.5, rely=0.2, relheight=0.05, relwidth=0.25)
    reg=withdep_screen.register(callbackmobile)
    E2.config(validate ="key",validatecommand =(reg, '%P'))
    var=tk.IntVar()
    if type_=="withdraw":
        b1=tk.Radiobutton( withdep_screen,text="OK",command=withdraw,variable=var,value=1,indicator=0,justify="left")
        b1.place(relx=0.3, rely=0.5, relheight=0.05, relwidth=0.25)
        b1.configure(activebackground="#B7DDE2")
        b1.configure(background="#bfbfbf")
    else:
        b1=tk.Radiobutton( withdep_screen,text="OK",command=deposit,variable=var,value=1,indicator=0,justify="left")
        b1.place(relx=0.3, rely=0.5, relheight=0.05, relwidth=0.25)
        b1.configure(activebackground="#B7DDE2")
        b1.configure(background="#bfbfbf")
    b2= tk.Radiobutton( withdep_screen, text="Quit",variable=var,value=2,indicator=0,justify="left",command= withdep_screen.destroy)
    b2.place(relx=0.3, rely=0.7, relheight=0.05,relwidth=0.25)
    b2.configure(activebackground="#B7DDE2")
    b2.configure(background="#bfbfbf")   
    withdep_screen.mainloop()
def withdraw_deposit():
    global window1
    window1=tk.Tk()
    window1.title("Withdraw and Deposit")
    window1.configure(background="#3300AA")
    window1.geometry("1069x742")
    l_title=tk.Message(window1,text="Withdraw and Deposit Money",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    var=tk.IntVar()
    M1= tk.Radiobutton(window1, text="Withdraw Money",variable=var,value=1,indicator=0,command=lambda:check_ccnum("withdraw"))
    M1.place(relx=0.15, rely=0.3, relheight=0.17, relwidth=0.6)
    M1.configure(activebackground="#bfbfbf")
    M1.configure(background="#B7DDE2")
    M1.configure(font=50)
    M1.configure(foreground="#000000")
    M1.configure(justify="left")
    M2= tk.Radiobutton(window1, text="Deposit Money",variable=var,value=2,indicator=0,command=lambda:check_ccnum("deposit"))
    M2.place(relx=0.15, rely=0.5, relheight=0.17,relwidth=0.6)
    M2.configure(activebackground="#bfbfbf")
    M2.configure(background="#B7DDE2")
    M2.configure(font=14)
    M2.configure(foreground="#000000")
    M2.configure(justify="left")
    M3= tk.Radiobutton(window1, text="Quit",variable=var,value=3,indicator=0,justify="left",command=window1.destroy)
    M3.place(relx=0.15, rely=0.7, relheight=0.17,relwidth=0.6)
    M3.configure(activebackground="#B7DDE2")
    M3.configure(background="#bfbfbf")   
    window1.mainloop()

#CHANGE ACCOUNT DETAILS
def change_details_in_file():
            global val
            f=open("customerdetails.csv","r",newline='')
            csvobj=csv.reader(f)
            reclist=[]
            for rec in csvobj:
                if rec[0]==log3.get():
                    if val==1:
                                 rec[2]=e1.get()
                                 reclist.append(rec)
                    elif val==2:
                                 rec[3]=e1.get()
                                 reclist.append(rec)
                    elif val==3:
                                 rec[4]=gender
                                 reclist.append(rec)
                    elif val==4:
                                 rec[5]=e1.get()
                                 reclist.append(rec)
                    elif val==5:
                                 rec[6]=e1.get()
                                 reclist.append(rec)
                    elif val==6:
                                   if len(e1.get())<8:
                                          tk.messagebox.showinfo('Error', "Username not storng enough.Must be minimum 8 characters",parent=change)
                                          change.destroy()
                                          changedetails()
                                          break
                
                                   else:
                                          rec[7]=e1.get()
                                          reclist.append(rec)
                    elif val==7:
                                   if len(e1.get())<8:
                                          tk.messagebox.showinfo('Error', "Password not storng enough.Must be minimum 8 characters",parent=change)
                                          change.destroy()
                                          changedetails()
                                          break
                                   else:
                                          rec[8]=e1.get()
                                          reclist.append(rec)
                    else:
                                   reclist.append(rec)
                else:
                    reclist.append(rec)
            f.close()
            f=open("customerdetails.csv","w",newline='')
            csvobj=csv.writer(f)
            csvobj.writerows(reclist)
            f.close()
            tk.messagebox.showinfo('Details', "Details successfully changed",parent=change)
            change.destroy()

def OnButtonClickChange(value):
            global val
            global e1
            if value==1:
                      l1=tk.Label(change,text="Enter New First Name:",relief="raised",background="#B7DDE2")
                      l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                      e1=tk.Entry(change,relief="solid",bd=3)
                      e1.place(relx=0.5, rely=0.7, relheight=0.05, relwidth=0.25)
                      reg = change.register(callbackname)
                      e1.config(validate ="key",validatecommand =(reg, '%P'))
                      val=1
            if value==2:
                     l1=tk.Label(change,text="Enter New Last Name:",relief="raised",background="#B7DDE2")
                     l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                     e1=tk.Entry(change,relief="solid",bd=3)
                     e1.place(relx=0.5, rely=0.7, relheight=0.05, relwidth=0.25)
                     reg = change.register(callbackname)
                     e1.config(validate ="key",validatecommand =(reg, '%P'))
                     val=2
            if value==3:
                     l1=tk.Label(change,text="New Gender:",relief="raised",background="#B7DDE2")
                     l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                     var1 =tk.IntVar()
                     R1 = tk.Radiobutton(change, text="Male",value=1,variable=var1,indicator=0,command=lambda:OnButtonClickGender(1))
                     R1.place(relx=0.5, rely=0.7,relheight=0.05, relwidth=0.25)
                     R1.configure(activebackground="#B7DDE2")
                     R1.configure(background="#bfbfbf")
                     R2 = tk.Radiobutton(change, text="Female",value=2,variable=var1,indicator=0,command=lambda:OnButtonClickGender(2))
                     R2.place(relx=0.50, rely=0.75,relheight=0.05, relwidth=0.25)
                     R2.configure(activebackground="#B7DDE2")
                     R2.configure(background="#bfbfbf")
                     R3 = tk.Radiobutton(change, text="Other",value=3,variable=var1,indicator=0,command=lambda:OnButtonClickGender(3))
                     R3.place(relx=0.50, rely=0.8,relheight=0.05, relwidth=0.25)
                     R3.configure(activebackground="#B7DDE2")
                     R3.configure(background="#bfbfbf")
                     val=3
            if value==4:
                     l1=tk.Label(change,text="Enter New Mobile Name:",relief="raised",background="#B7DDE2")
                     l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                     e1=tk.Entry(change,relief="solid",bd=3)
                     e1.place(relx=0.5, rely=0.7, relheight=0.05, relwidth=0.25)
                     reg=change.register(callbackmobile)
                     e1.config(validate ="key",validatecommand =(reg, '%P'))
                     val=4
            if value==5:
                     l1=tk.Label(change,text="Enter New Address:",relief="raised",background="#B7DDE2")
                     l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                     e1=tk.Entry(change,relief="solid",bd=3)
                     e1.place(relx=0.5, rely=0.7, relheight=0.05, relwidth=0.25)
                     val=5
            if value==6:
                     l1=tk.Label(change,text="Enter New Username:",relief="raised",background="#B7DDE2")
                     l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                     e1=tk.Entry(change,relief="solid",bd=3)
                     e1.place(relx=0.5, rely=0.7, relheight=0.05, relwidth=0.25)
                     val=6
            if value==7:
                     l1=tk.Label(change,text="Enter New Password:",relief="raised",background="#B7DDE2")
                     l1.place(relx=0.15, rely=0.7, relheight=0.05, relwidth=0.25)
                     e1=tk.Entry(change,relief="solid",bd=3)
                     e1.place(relx=0.5, rely=0.7, relheight=0.05, relwidth=0.25)
                     val=7
            M9= tk.Radiobutton(change, text="Submit",variable=var,value=8,indicator=0,justify="left",command=change_details_in_file)
            M9.place(relx=0.3, rely=0.85, relheight=0.05,relwidth=0.25)
            M9.configure(activebackground="#B7DDE2")
            M9.configure(background="#bfbfbf")   
            change.mainloop()
def changedetails():
     global var
     global change
     change=tk.Tk()
     change.title("Amshel Bank")
     change.configure(background="#3300AA")
     change.geometry("1069x742")
     l_title=tk.Message(change,text="Which Details Would You Like To Change? ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
     l_title.config(font=("Courier","25","bold"))
     l_title.pack(side="top")
     var =tk.IntVar()
     M1= tk.Radiobutton(change, text="First Name",variable=var,value=1,indicator=0,command=lambda:OnButtonClickChange(1))
     M1.place(relx=0.15, rely=0.3, relheight=0.05, relwidth=0.6)
     M1.configure(activebackground="#bfbfbf")
     M1.configure(background="#B7DDE2")
     M1.configure(font=50)
     M1.configure(foreground="#000000")
     M1.configure(justify="left")
     M2= tk.Radiobutton(change, text="Last Name",variable=var,value=2,indicator=0,command=lambda:OnButtonClickChange(2))
     M2.place(relx=0.15, rely=0.35, relheight=0.05,relwidth=0.6)
     M2.configure(activebackground="#bfbfbf")
     M2.configure(background="#B7DDE2")
     M2.configure(font=14)
     M2.configure(foreground="#000000")
     M2.configure(justify="left")
     M3= tk.Radiobutton(change, text="Gender",variable=var,value=3,indicator=0,command=lambda:OnButtonClickChange(3))
     M3.place(relx=0.15, rely=0.4, relheight=0.05, relwidth=0.6)
     M3.configure(activebackground="#bfbfbf")
     M3.configure(background="#B7DDE2")
     M3.configure(font=50)
     M3.configure(foreground="#000000")
     M3.configure(justify="left")
     M4= tk.Radiobutton(change, text="Mobile",variable=var,value=4,indicator=0,command=lambda:OnButtonClickChange(4))
     M4.place(relx=0.15, rely=0.45, relheight=0.05,relwidth=0.6)
     M4.configure(activebackground="#bfbfbf")
     M4.configure(background="#B7DDE2")
     M4.configure(font=14)
     M4.configure(foreground="#000000")
     M4.configure(justify="left")
     M5= tk.Radiobutton(change, text="Address",variable=var,value=5,indicator=0,command=lambda:OnButtonClickChange(5))
     M5.place(relx=0.15, rely=0.5, relheight=0.05,relwidth=0.6)
     M5.configure(activebackground="#bfbfbf")
     M5.configure(background="#B7DDE2")
     M5.configure(font=14)
     M5.configure(foreground="#000000")
     M5.configure(justify="left")
     M6= tk.Radiobutton(change, text="Username",variable=var,value=6,indicator=0,command=lambda:OnButtonClickChange(6))
     M6.place(relx=0.15, rely=0.55, relheight=0.05,relwidth=0.6)
     M6.configure(activebackground="#bfbfbf")
     M6.configure(background="#B7DDE2")
     M6.configure(font=14)
     M6.configure(foreground="#000000")
     M6.configure(justify="left")
     M7= tk.Radiobutton(change, text="Password",variable=var,value=7,indicator=0,command=lambda:OnButtonClickChange(7))
     M7.place(relx=0.15, rely=0.6, relheight=0.05,relwidth=0.6)
     M7.configure(activebackground="#bfbfbf")
     M7.configure(background="#B7DDE2")
     M7.configure(font=14)
     M7.configure(foreground="#000000")
     M7.configure(justify="left")
     M8= tk.Radiobutton(change, text="Quit",variable=var,value=8,indicator=0,justify="left",command=change.destroy)
     M8.place(relx=0.3, rely=0.9, relheight=0.05,relwidth=0.25)
     M8.configure(activebackground="#B7DDE2")
     M8.configure(background="#bfbfbf")   
     change.mainloop()

#ACCESS ACCOUNT DETAILS
def accessdetails():
    details=tk.Tk()
    details.title("Amshel Bank")
    details.configure(background="#3300AA")
    details.geometry("1069x742")
    l_title=tk.Message(details,text="Your Account Details !",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    f=open("customerdetails.csv","r",newline='')
    csvobj=csv.reader(f)
    for rec in csvobj:
        code=log3.get()
        if rec[0]==code:
            tk.Label(details,text="Code:"+str(rec[0]),background="#B7DDE2").place(relx=0.3, rely=0.12, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Key:"+rec[1],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.17, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="First Name:"+rec[2],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.22, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Last Name:"+rec[3],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.27, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Gender:"+rec[4],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.32, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Mobile:"+rec[5],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.37, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Address:"+rec[6],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.42, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Username:"+rec[7],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.47, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Password:"+rec[8],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.52, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Account Type:"+rec[9],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.57, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Account Number:"+rec[10],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.62, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Balance:"+rec[11],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.67, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Opening Date:"+rec[12],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.72, relheight=0.05, relwidth=0.25)
            tk.Label(details,text="Credit Card Number:"+rec[14],relief="raised",background="#B7DDE2").place(relx=0.3, rely=0.77, relheight=0.05, relwidth=0.25)
            var=tk.IntVar()
            M1= tk.Radiobutton(details, text="Quit",variable=var,value=1,indicator=0,justify="left",command=details.destroy)
            M1.place(relx=0.3, rely=0.82, relheight=0.05,relwidth=0.25)
            M1.configure(activebackground="#B7DDE2")
            M1.configure(background="#bfbfbf") 
            details.mainloop()
#OPTIONS AFTER LOGIN
def login_options():
    global window
    window=tk.Tk()
    window.title("Amshel Bank")
    window.configure(background="#3300AA")
    window.geometry("1069x742")
    fr1=tk.Frame(window)
    l_title=tk.Message(window,text="Welcome to Aamshel bank \n Vishawas se Vikas tak !",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    var=tk.IntVar()
    M1= tk.Radiobutton(window, text="Access Account Details",variable=var,value=1,indicator=0,command=accessdetails)
    M1.place(relx=0.15, rely=0.3, relheight=0.05, relwidth=0.6)
    M1.configure(activebackground="#bfbfbf")
    M1.configure(background="#B7DDE2")
    M1.configure(font=50)
    M1.configure(foreground="#000000")
    M1.configure(justify="left")
    M2= tk.Radiobutton(window, text="Change Account Details",variable=var,value=2,indicator=0,command=changedetails)
    M2.place(relx=0.15, rely=0.35, relheight=0.05,relwidth=0.6)
    M2.configure(activebackground="#bfbfbf")
    M2.configure(background="#B7DDE2")
    M2.configure(font=14)
    M2.configure(foreground="#000000")
    M2.configure(justify="left")
    M3= tk.Radiobutton(window, text="Withdraw or Deposit Money",variable=var,value=3,indicator=0,command=withdraw_deposit)
    M3.place(relx=0.15, rely=0.4, relheight=0.05, relwidth=0.6)
    M3.configure(activebackground="#bfbfbf")
    M3.configure(background="#B7DDE2")
    M3.configure(font=50)
    M3.configure(foreground="#000000")
    M3.configure(justify="left")
    M4= tk.Radiobutton(window, text="Frequently Asked Questions about Loans",variable=var,value=4,indicator=0,command=faq)
    M4.place(relx=0.15, rely=0.45, relheight=0.05,relwidth=0.6)
    M4.configure(activebackground="#bfbfbf")
    M4.configure(background="#B7DDE2")
    M4.configure(font=14)
    M4.configure(foreground="#000000")
    M4.configure(justify="left")
    M7= tk.Radiobutton(window, text="Generate a credit card number.",command=generate_credit_card,variable=var,value=5,indicator=0)
    M7.place(relx=0.15, rely=0.5, relheight=0.05,relwidth=0.6)
    M7.configure(activebackground="#bfbfbf")
    M7.configure(background="#B7DDE2")
    M7.configure(font=14)
    M7.configure(foreground="#000000")
    M7.configure(justify="left")
    M8= tk.Radiobutton(window, text="Show transaction history.",command=transactionhistory,variable=var,value=5,indicator=0)
    M8.place(relx=0.15, rely=0.55, relheight=0.05,relwidth=0.6)
    M8.configure(activebackground="#bfbfbf")
    M8.configure(background="#B7DDE2")
    M8.configure(font=14)
    M8.configure(foreground="#000000")
    M8.configure(justify="left")
    M6= tk.Radiobutton(window, text="Quit",variable=var,value=6,indicator=0,justify="left",command=window.destroy)
    M6.place(relx=0.15, rely=0.6, relheight=0.05,relwidth=0.6)
    M6.configure(activebackground="#B7DDE2")
    M6.configure(background="#bfbfbf")   
    window.mainloop()


#LOGIN
def check_login_validity():
    f=open("customerdetails.csv","r",newline='')
    csvobj=csv.reader(f)
    username=log1.get()
    password=log2.get()
    code=log3.get()
    key=log4.get()
    found=0
    for rec in csvobj:
        if rec[7]==username:
            if rec[8]==password:
                if rec[0]==str(code):
                    if rec[1]==key:
                           found=1
                           break
    if found==0:
            tk.messagebox.showinfo('Error', "Invalid details",parent=login_screen)
            login_screen.destroy()
    else:
           
           tk.messagebox.showinfo('Login', "Login Successfull",parent=login_screen)
           login_options()
def login():
    global login_screen
    global log1,log2,log3,log4
    login_screen=tk.Tk()
    login_screen.geometry("1069x742")
    login_screen.title("LOGIN")
    login_screen.configure(background="#3300AA")
    fr1=tk.Frame(login_screen)
    l_title=tk.Message(login_screen,text="Login",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    #Username
    l1=tk.Label(login_screen,text="Username:",relief="raised",background="#B7DDE2")
    l1.place(relx=0.15, rely=0.12, relheight=0.05, relwidth=0.25)
    log1=tk.Entry(login_screen,relief="solid",bd=3)
    log1.place(relx=0.50, rely=0.12, relheight=0.05, relwidth=0.25)
    #Password
    l2=tk.Label(login_screen,text="Password:",relief="raised",background="#B7DDE2")
    l2.place(relx=0.15, rely=0.2, relheight=0.05, relwidth=0.25)
    log2=tk.Entry(login_screen,relief="solid",bd=3,show="*")
    log2.place(relx=0.50, rely=0.2, relheight=0.05, relwidth=0.25)
    #Code
    l3=tk.Label(login_screen,text="Code:",relief="raised",background="#B7DDE2")
    l3.place(relx=0.15, rely=0.28, relheight=0.05, relwidth=0.25)
    log3=tk.Entry(login_screen,relief="solid",bd=3)
    log3.place(relx=0.50, rely=0.28, relheight=0.05, relwidth=0.25)
    #Key
    l4=tk.Label(login_screen,text="Key:",relief="raised",background="#B7DDE2")
    l4.place(relx=0.15, rely=0.36, relheight=0.05, relwidth=0.25)
    log4=tk.Entry(login_screen,relief="solid",bd=3)
    log4.place(relx=0.50, rely=0.36, relheight=0.05, relwidth=0.25)
    #Submit
    var=tk.IntVar()
    M1=tk.Radiobutton(login_screen, text="Submit",command=check_login_validity,variable=var,value=1,justify="left",indicator=0)
    M1.place(relx=0.3, rely=0.46, relheight=0.05,relwidth=0.25)
    M1.configure(activebackground="#B7DDE2")
    M1.configure(background="#bfbfbf")
    #Quit
    M2= tk.Radiobutton(login_screen, text="Quit",variable=var,value=2,indicator=0,justify="left",command=login_screen.destroy)
    M2.place(relx=0.3, rely=0.56, relheight=0.05,relwidth=0.25)
    M2.configure(activebackground="#B7DDE2")
    M2.configure(background="#bfbfbf")       
    login_screen.mainloop()
    

#CREATING ACCOUNT
def createcustomerfile():
    f=open("customerdetails.csv","a",newline="")
    csvobj=csv.writer(f)
    code=autocode()
    key=autokey()
    fname=e1.get()
    lname=e2.get()
    mobile=e4.get()
    address=e5.get()
    username=autousername(fname,lname)
    password=autopassword()
    accnum=autoaccountnum(acctype)
    balance=e9.get()
    dateTimeObj =datetime.now()
    openingdate=dateTimeObj.strftime("%d %b %Y ")
    transaction_history=[[openingdate,"+",balance]]
    ccnum="-"
    rec=[code,key,fname,lname,gender,mobile,address,username,password,acctype,accnum,balance,openingdate,transaction_history,ccnum]
    csvobj.writerow(rec)
    root.option_add('*Dialog.msg.font', 'Courier 20')
    tk.messagebox.showinfo('Details',"Your Account Details are:"+
                                           "\n"+"Code: "+str(code)+
                                           "\n"+"Key: "+key+
                                           "\n"+"First Name: "+fname+
                                           "\n"+"Last Name: "+lname+
                                           "\n"+"Gender: "+gender+
                                           "\n"+"Mobile: "+str(mobile)+
                                           "\n"+"Address: "+address+
                                           "\n"+"Username: "+username+
                                           "\n"+"Password: "+password+
                                           "\n"+"Account Type: "+acctype+
                                           "\n"+"Account Number: "+str(accnum)+
                                           "\n"+"Starting Amount: "+str(balance)+
                                           "\n"+"Opening Date: "+str(openingdate),parent=root)

    root.destroy()
    f.close()
def createaccount():
    global root
    root=tk.Tk()
    root.geometry("1069x742")
    root.title("CREATE ACCOUNT")
    root.configure(background="#3300AA")
    fr1=tk.Frame(root)
    l_title=tk.Message(root,text="Register",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    global e1,e2,e4,e5,e9
    #First Name
    l1=tk.Label(root,text="Enter First Name:",relief="raised",background="#B7DDE2")
    l1.place(relx=0.15, rely=0.12, relheight=0.05, relwidth=0.25)
    e1=tk.Entry(root,relief="solid",bd=3)
    e1.place(relx=0.50, rely=0.12, relheight=0.05, relwidth=0.25)
    reg = root.register(callbackname)
    e1.config(validate ="key",validatecommand =(reg, '%P'))
    #Last Name
    l2=tk.Label(root,text="Enter Last Name:",relief="raised",background="#B7DDE2")
    l2.place(relx=0.15, rely=0.2, relheight=0.05, relwidth=0.25)
    e2=tk.Entry(root,relief="solid",bd=3)
    e2.place(relx=0.50, rely=0.2, relheight=0.05, relwidth=0.25)
    reg = root.register(callbackname)
    e2.config(validate ="key",validatecommand =(reg, '%P'))
    #Gender
    l3=tk.Label(root,text="Gender:",relief="raised",background="#B7DDE2")
    l3.place(relx=0.15, rely=0.28, relheight=0.05, relwidth=0.25)
    var1 =tk.IntVar()
    R1 = tk.Radiobutton(root, text="Male",value=1,variable=var1,indicator=0,command=lambda:OnButtonClickGender(1))
    R1.place(relx=0.5, rely=0.28,relheight=0.05, relwidth=0.25)
    R1.configure(activebackground="#B7DDE2")
    R1.configure(background="#bfbfbf")
    R2 = tk.Radiobutton(root, text="Female",value=2,variable=var1,indicator=0,command=lambda:OnButtonClickGender(2))
    R2.place(relx=0.50, rely=0.33,relheight=0.05, relwidth=0.25)
    R2.configure(activebackground="#B7DDE2")
    R2.configure(background="#bfbfbf")
    R3 = tk.Radiobutton(root, text="Other",value=3,variable=var1,indicator=0,command=lambda:OnButtonClickGender(3))
    R3.place(relx=0.50, rely=0.38,relheight=0.05, relwidth=0.25)
    R3.configure(activebackground="#B7DDE2")
    R3.configure(background="#bfbfbf")
    #Mobile Number
    l4=tk.Label(root,text="Enter Mobile Number:",relief="raised",background="#B7DDE2")
    l4.place(relx=0.15, rely=0.46,relheight=0.05, relwidth=0.25)
    e4=tk.Entry(root,relief="solid",bd=3)
    e4.place(relx=0.5, rely=0.46,relheight=0.05, relwidth=0.25)
    reg = root.register(callbackmobile)
    e4.config(validate ="key",validatecommand =(reg, '%P'))
    #Address
    l5=tk.Label(root,text="Enter Address:",relief="raised",background="#B7DDE2")
    l5.place(relx=0.15, rely=0.54,relheight=0.05, relwidth=0.25)
    e5=tk.Entry(root,relief="solid",bd=3)
    e5.place(relx=0.5, rely=0.54,relheight=0.05, relwidth=0.25)
    #Account Type
    l8=tk.Label(root,text="Account Type:",relief="raised",background="#B7DDE2")
    l8.place(relx=0.15, rely=0.62,relheight=0.05, relwidth=0.25)
    var2 =tk.IntVar()
    R4= tk.Radiobutton(root, text="Saving",value=1,variable=var2,indicator=0,command=lambda:OnButtonClickAccType(1))
    R4.place(relx=0.5, rely=0.62,relheight=0.05, relwidth=0.25)
    R4.configure(activebackground="#B7DDE2")
    R4.configure(background="#bfbfbf")
    R5 = tk.Radiobutton(root, text="Checking",value=2,variable=var2,indicator=0,command=lambda:OnButtonClickAccType(2))
    R5.place(relx=0.5, rely=0.67,relheight=0.05, relwidth=0.25)
    R5.configure(activebackground="#B7DDE2")
    R5.configure(background="#bfbfbf")
    var3=tk.IntVar()
    #Starting Amount
    l9=tk.Label(root,text="Enter Starting Amount:",relief="raised",background="#B7DDE2")
    l9.place(relx=0.15, rely=0.75,relheight=0.05, relwidth=0.25)
    e9=tk.Entry(root,relief="solid",bd=3)
    e9.place(relx=0.5, rely=0.75,relheight=0.05, relwidth=0.25)
    reg = root.register(callbackmobile)
    e9.config(validate ="key",validatecommand =(reg, '%P'))
    #Submit
    M1=tk.Radiobutton(root, text="Submit",command=createcustomerfile,variable=var3,value=1,justify="left",indicator=0)
    M1.place(relx=0.3, rely=0.85, relheight=0.05,relwidth=0.25)
    M1.configure(activebackground="#B7DDE2")
    M1.configure(background="#bfbfbf")
    #Quit
    M2= tk.Radiobutton(root, text="Quit",variable=var3,value=2,indicator=0,justify="left",command=root.destroy)
    M2.place(relx=0.3, rely=0.93, relheight=0.05,relwidth=0.25)
    M2.configure(activebackground="#B7DDE2")
    M2.configure(background="#bfbfbf")
    root.mainloop()        


#ENTER AS CUSTOMER
def entercustomer():
    entercust_window=tk.Tk()
    entercust_window.title("Amshel Bank")
    entercust_window.configure(background="#3300AA")
    entercust_window.geometry("1069x742")
    fr1=tk.Frame(entercust_window)
    fr1.pack(side="top")
    img= Image.open("aamshel.png")
    image1 = img.resize((1100, 200), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.pack(side="top")
    label1.configure(background="#FFFFFF")
    var=tk.IntVar()
    M1= tk.Radiobutton( entercust_window, text="Create An Account",variable=var,value=1,indicator=0,command=createaccount)
    M1.place(relx=0.15, rely=0.3, relheight=0.17, relwidth=0.6)
    M1.configure(activebackground="#bfbfbf")
    M1.configure(background="#B7DDE2")
    M1.configure(font=50)
    M1.configure(foreground="#000000")
    M1.configure(justify="left")
    M2= tk.Radiobutton( entercust_window, text="Login",variable=var,value=2,indicator=0,command=login)
    M2.place(relx=0.15, rely=0.5, relheight=0.17,relwidth=0.6)
    M2.configure(activebackground="#bfbfbf")
    M2.configure(background="#B7DDE2")
    M2.configure(font=14)
    M2.configure(foreground="#000000")
    M2.configure(justify="left")
    M3= tk.Radiobutton( entercust_window, text="Quit",variable=var,value=3,indicator=0,command=entercust_window.destroy)
    M3.place(relx=0.15, rely=0.7, relheight=0.17,relwidth=0.6)
    M3.configure(activebackground="#bfbfbf")
    M3.configure(background="#B7DDE2")
    M3.configure(font=14)
    M3.configure(foreground="#000000")
    M3.configure(justify="left")
    entercust_window.mainloop()
entercustomer()

	
    
