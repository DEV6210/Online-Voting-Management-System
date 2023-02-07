from cgi import test
from tabnanny import check
from tkinter import*
from msilib.schema import ComboBox
from operator import concat
from tkinter import ttk
from tkinter import messagebox
from venv import create
from sqlalchemy import null
from tkinter import filedialog
import sqlite3
import re
import random
from twilio.rest import Client
from fpdf import FPDF
import os
from PIL import Image, ImageTk
import io
from win10toast import ToastNotifier
import time
from tkinter.colorchooser import *
import webbrowser
from win10toast_click import ToastNotifier 
import threading
import socket
import time
from urllib import request
from tkvideo import tkvideo
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

try:
    db=sqlite3.connect('voting management system.db')
    cr=db.cursor()
    print('Database is connected with Home Page')
    db.commit()
except:    
    print('Database is connected with Home Page')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#--------- @new screen-333333 this portion is not mendatory -----------#

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



def lunch_first_body3():
    splash_screen=Tk()
    splash_screen.minsize(600,400)
    splash_screen.state("zoomed")
    splash_screen.resizable(False,False)
    splash_screen.attributes("-fullscreen",True)
    splash_screen.config(bg="white")
    splash_screen.overrideredirect(True)

    sp_img=Image.open("img/v5.png")
    # sp_img=ImageTk.PhotoImage(file="img/v1.jpg")
    resize_img=  ImageTk.PhotoImage(sp_img.resize((500,300)))

    place_img=Label(splash_screen,image=resize_img,bg="white")
    place_img.place(x=500,y=230)

    def main_screen3():
        #close splash screen....
        splash_screen.destroy()

        #Execute Main Body....    
        root=Tk()
        root.title('Online Voting Management System')
        root.geometry('600x600+500+0')
        root.minsize(600,400)
        root.wm_iconbitmap('icon/vote-sign.ico')
        root.resizable(False,False)#maximize option disable
        # root.attributes('-fullscreen',True)
        root.state('zoomed')#default open fullscreen
    


        #-------------------------------------- Main Body ---------------------------------------- #

        '''------------------------------ Count Total Real-Time Vote-------------------------------'''
        cr.execute("select vot_status from registration")
        vt_data=cr.fetchall()
        tmc=0
        bjp=0
        cong=0
        for v_c in vt_data:
            total_v=v_c[0]
            if total_v=='TMC':
                tmc += 1
            if total_v== 'BJP':
                bjp +=1
            if total_v== 'Congress':
                cong +=1

        # print('tmc=',tmc)
        # print('bjp=',bjp)
        # print('conj=',cong)
        '''-----------------------------------------------------------------------------------------'''

        #-----------------------------------<<< About >>>------------------------------------ #
        def about():
            messagebox.showinfo('Details','Develop by ' ' ----> ' ' Amit Mandal\nDevelop by ' ' ----> '  ' Purnendu Mandal\nDevelop by ' ' ----> '  ' Rakesh Hossain\nDevelop by ' ' ----> '  ' Sridam Mandal\n ' ' \nApplication Verson 2.0')

        def feedback():
            feedwin=Toplevel()
            feedwin.title('Feedback or Report')
            feedwin.geometry('550x680+480+25')
            feedwin.wm_iconbitmap('icon/feedback.ico')
            feedwin.resizable(False,False)
            feedwin.config(bg='#D9D9D9')
            feedwin.config(bg='#C9C5C5')
            #aboutwin.attributes('-fullscreen',True)
            try:
                db=sqlite3.connect('voting management system.db')
                cr=db.cursor()
                cr.execute('create table feedback(email text,feedback_receive text)')
                
            except:
                print('feedback table is connected')
                
            

            #send feedback to database............
            feedemail=StringVar()
            def senddata():

                #define variable
                feed_email=feedemail.get()
                feed_data=feed_e.get('1.0','end-1c')

            
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
                # Define a function for
                # for validating an Email   
                def check(feed_email):
                
                    # pass the regular expression
                    # and the string into the fullmatch() method
                    if(re.fullmatch(regex, feed_email)):
                        #print("Valid Email")
                        #insert data..........
                        cr.execute('insert into feedback(email,feedback_receive) values(?,?)',(feed_email,feed_data))
                        db.commit()
                        messagebox.showinfo('Feedback','Thank You for Submit Feedback\n we will notify you after review feedback')
                        feedwin.destroy()
                
                    else:
                        #print("Invalid Email")
                        invalid=Label(feedwin,text='Please Enter Valid E-mail',font=('Regular',10),bg='white',fg='red')
                        invalid.place(x=175,y=210)
                check(feed_email)  

            


            #bg thems..............
            feedback_img=PhotoImage(file='themes/feedback_b.png')
            feed_l=Label(feedwin,image=feedback_img,bg='#C9C5C5',width=500,height=600)
            feed_l.place(x=25,y=10)

            #emai...........    
            em_img=PhotoImage(file='button/feedem.png')
            feed_l=Label(feedwin,image=em_img,bg='white')
            feed_l.place(x=60,y=166)
            #entry.........
            feed_e=Entry(feedwin,font=('Regular',24),width=18,bd=0,bg='#D4F6CC',textvar=feedemail)
            feed_e.place(x=175,y=169)

            #report........
            report_img=PhotoImage(file='button/feedreport.png')
            report_l=Label(feedwin,image=report_img,bg='white')
            report_l.place(x=60,y=250)
            #entry........
            feed_e=Text(feedwin,font=('Regular',16),height=8,width=36,bd=0,bg='#D4F6CC')
            feed_e.place(x=62,y=280)




            #send button img import
            send_bg=PhotoImage(file='button/fedsend.png')
            send=Button(feedwin,image=send_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=senddata)
            send.place(x=125,y=530)

            #cancel button img import
            can_bg=PhotoImage(file='button/cancel.png')
            login=Button(feedwin,image=can_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:feedwin.destroy())
            login.place(x=290,y=530)

            feedwin.mainloop()




        #--------------------------------<<< Registration Form >>>-------------------------------- #
        def RegistrationForm():
            root.destroy()
            import registration_form
            

        #-----------------------------------<<< Login Form >>>------------------------------------ #
        def LoginForm():
                
            logwin=Toplevel()
            logwin.title('Login Form')
            logwin.geometry('550x680')#+510+50')
            logwin.wm_iconbitmap('icon/login.ico')
            #logwin.resizable(False,False)
            logwin.config(bg='#D9D9D9')
            logwin.attributes('-fullscreen',True)
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Database Connect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            null=0
            uid=StringVar()
            upass=StringVar()
            def login():
                userid=uid.get()
                upassword=upass.get()
                
                #userid.................
                userid_length=len(userid)
                if null == userid_length:
                    #validation.....
                            
                    validation=Label(logwin,text='Please Enter User ID',font=('Regular',10),fg='red',bg='white')
                    validation.place(x=730,y=280)
                else:
                    #password..............
                    password_length=len(upassword)
                    if null == password_length:
                        p='Please Enter Password'
                        validation=Label(logwin,text=p,font=('Regular',10),fg='red',bg='white')
                        validation.place(x=730,y=360)
                    else:
                        cr.execute("select phone,password from registration")
                        data=cr.fetchall()
                        check=0
                        for i in data:
                            a=i[0]
                            b=i[1]
                            if userid==a and upassword==b:
                                check=1
                                break
                            else:
                                check=0
                        if check == 1:
                            #successfully login
                            afterloginwin=Toplevel()     
                            afterloginwin.title('My Profile')
                            afterloginwin.geometry('550x680+498+30')
                            afterloginwin.wm_iconbitmap('icon/myprofile.ico')
                            afterloginwin.resizable(False,False)
                            afterloginwin.config(bg='#D9D9D9')                    
                            afterloginwin.overrideredirect(1) 
                                        
                            cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={a}')
                            data=cr.fetchall()
                            for i in data:
                                n=i[0]
                                d=i[1]
                                g=i[2]
                                f=i[3]
                                p=i[4]
                                aah=i[5]
                                vill=i[6]
                                po=i[7]
                                pin=i[8]
                                dist=i[9]
                                state=i[10]
                                cd=i[11]
                                vs=i[12]
                                myphoto=i[13]

                            '''--------------------------- Give Vote -------------------------'''
                            def give():
                                votewin=Toplevel()
                                votewin.title('Give Vote')
                                votewin.geometry('550x680+480+25')
                                votewin.wm_iconbitmap('icon/feedback.ico')
                                votewin.resizable(False,False)
                                votewin.config(bg='#D9D9D9')
                                #votewin.attributes('-fullscreen',True)
                                votewin.overrideredirect(1)
                                # db=sqlite3.connect('voting management system.db')
                                # cr=db.cursor()   
                                # c='9382370394'

                                # cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status from registration where phone={c}')
                                # data=cr.fetchall()
                                # for i in data:
                                #     n=i[0]
                                #     d=i[1]
                                #     g=i[2]
                                #     f=i[3]
                                #     p=i[4]
                                #     aah=i[5]
                                #     vill=i[6]
                                #     po=i[7]
                                #     pin=i[8]
                                #     dist=i[9]
                                #     state=i[10]
                                #     cd=i[11]
                                #     vs=i[12]

                                if cd=='Not Generated':
                                    nota='Sorry Your not Eligible for Vote\n Beacuse your voter number is not gengrated'
                                    #background...
                                    gv_img=PhotoImage(file='themes/voteback.png')
                                    gv_l=Label(votewin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                    gv_l.place(x=30,y=10) 
                                    not_l=Label(votewin,text=nota,font=('Regular',18),bg='white',fg='blue')
                                    not_l.place(x=35,y=200)
                                    #cancel button img import
                                    canc_bg=PhotoImage(file='button/close.png')
                                    canc=Button(votewin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:votewin.destroy())
                                    canc.place(x=225,y=350)
                                else:
                                    null=0
                                    v1=IntVar()
                                    def give():
                                        v2=v1.get()
                                        if v2==null:
                                            #choose party.......
                                            cpp_l=Label(votewin,text='Please Choose Party',font=('Regular',8),fg='red',bg='white')
                                            cpp_l.place(x=223,y=210)
                                            v3='please choose party'
                                        elif v2==1:
                                            v3='BJP'
                                        elif v2==2:
                                            v3='TMC'
                                        else:
                                            v3='Congress'

                                        if v3=='BJP' or v3=='TMC' or v3=='Congress':
                                            rsotp=StringVar()
                                            
                                            cppp_l=Label(votewin,font=('Regular',10),bg='white',width=30)
                                            cppp_l.place(x=223,y=210)
                                            #resend otp
                                            #resend_bg=PhotoImage(file='button/resend.png')
                                            resend=Button(votewin,text='Resent OTP',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',command=give,padx=10)
                                            resend.place(x=225,y=240)
                                            
                                            '''------------------------------------------------------'''
                                            #generate otp.........
                                            motp=str(random.randint(1111,9999))
                                            #print(motp)
                                            #    
                                            '''-------------------TESTING OTP-------------------------'''

                                            ottp='Only for testing purposr OTP: ' +motp
                                            test_l=Label(votewin,text=ottp,fg='red')
                                            test_l.place(x=50,y=550)

                                            '''------------------Twillo OTP Service------------------'''
                                            # account_sid = 'AC714959399352b0bebabaac962eb62449'
                                            # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                                            # client = Client(account_sid, auth_token)
                                            # too='+91'+p
                                            # msg='Online Voting System\nDo not Share OTP\nyour Give vote OTP is: '+motp
                                            # client.messages.create(body=msg,from_='+19788308309',to=too)

                                            '''-------------------------------------------------------'''            
                                            
                                            cr.execute(f'update registration set otp={motp} where card_no={cd}')
                                            db.commit()
                                            already='Already Voted'
                                            def submitotp():
                                                reseveotp=rsotp.get()
                                                cr.execute(f'select voting_status,otp from registration where card_no={cd}')                
                                                otpdata=cr.fetchall()
                                                for ot in otpdata:
                                                    vts=ot[0]
                                                    sotp=ot[1]
                                                
                                            
                                                if sotp==reseveotp:
                                                    if vts=='Not Voted':
                                                        cr.execute('update registration set voting_status=?,vot_status=? where card_no=?',(already,v3,cd))
                                                        db.commit()

                                                        #Thanks for vote...................
                                                        successwin=Toplevel()
                                                        successwin.title('success full vote')
                                                        successwin.geometry('550x680+480+25')
                                                        successwin.wm_iconbitmap('icon/feedback.ico')
                                                        successwin.resizable(False,False)
                                                        successwin.config(bg='#D9D9D9')
                                                        #successwin.attributes('-fullscreen',True)
                                                        successwin.overrideredirect(1)

                                                        note='Thank You For Give Vote...'
                                                        #background...
                                                        gv_img=PhotoImage(file='themes/voteback.png')
                                                        gv_l=Label(successwin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                                        gv_l.place(x=33,y=10) 

                                                        warning_img=PhotoImage(file='logo/check.png')
                                                        war_l=Label(successwin,image=warning_img,width=200,height=100,bg='white')
                                                        war_l.place(x=180,y=70)

                                                        not_l=Label(successwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                        not_l.place(x=150,y=200)

                                                        
                                                        # Re-fetch Voting count data.......................
                                                        cr.execute("select vot_status from registration")
                                                        vt_data=cr.fetchall()
                                                        tmc=0
                                                        bjp=0
                                                        cong=0
                                                        for v_c in vt_data:
                                                            total_v=v_c[0]
                                                            if total_v=='TMC':
                                                                tmc += 1
                                                            if total_v== 'BJP':
                                                                bjp +=1
                                                            if total_v== 'Congress':
                                                                cong +=1

                                                        #show count Bjp                                    
                                                        bjp_s1=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
                                                        bjp_s1.place(x=440,y=180)
                                                        #show count TMC
                                                        tmc_s1=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
                                                        tmc_s1.place(x=440,y=370)
                                                        #show count CONJ
                                                        conj_s1=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
                                                        conj_s1.place(x=440,y=560)




                                                        def closesuccess():                                                    
                                                            votewin.destroy()
                                                            successwin.destroy()
                                                            
                                                        #cancel button img import
                                                        tgv_bg=PhotoImage(file='button/close.png')
                                                        tgv=Button(successwin,image=tgv_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=closesuccess)
                                                        tgv.place(x=230,y=370)
                                                        successwin.mainloop()
                                                    else:
                                                        #already voted...................
                                                        alwin=Toplevel()
                                                        alwin.title('Already Voted')
                                                        alwin.geometry('550x680+480+25')
                                                        alwin.wm_iconbitmap('icon/feedback.ico')
                                                        alwin.resizable(False,False)
                                                        alwin.config(bg='#D9D9D9')
                                                        #alwin.attributes('-fullscreen',True)
                                                        alwin.overrideredirect(1)

                                                        note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                                                        #background...
                                                        gv_img=PhotoImage(file='themes/voteback.png')
                                                        gv_l=Label(alwin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                                        gv_l.place(x=30,y=10) 

                                                        warning_img=PhotoImage(file='logo/warning.png')
                                                        war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                                                        war_l.place(x=180,y=70)

                                                        not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                        not_l.place(x=85,y=200)
                                                        #cancel button img import
                                                        canc_bg=PhotoImage(file='button/close.png')
                                                        canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                                                        canc.place(x=225,y=370)
                                                        alwin.mainloop()
                                                else:
                                                    #print('wrong otp')                       
                                                    w_l=Label(votewin,text='Please Enter Valid OTP',bg='White',fg='red',width=50)
                                                    w_l.place(x=130,y=372) 

                                            #otp..........
                                            otp_l=Label(votewin,text='Enter OTP ',font=('Regular',18))
                                            otp_l.place(x=110,y=340)
                                            otp_s=Label(votewin,text='4 Digit OTP Send Your Mobile Number',font=('Regular',8),bg='white')
                                            otp_s.place(x=245,y=370)
                                            otp_e=Entry(votewin,font=('Regular',18),bg='#DFF6FF',width=16,textvar=rsotp)
                                            otp_e.place(x=245,y=340)  
                                            #login button img import
                                            #sub1_img=PhotoImage(file='button/u_login.png')
                                            sub1=Button(votewin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=submitotp)
                                            sub1.place(x=140,y=450)
                                            #cancel button img import
                                            #canc_bg=PhotoImage(file='button/cancel.png')
                                            canc=Button(votewin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:votewin.destroy())
                                            canc.place(x=310,y=450)                                    
                                        else:
                                            print()
                                            #please select party

                                    # stream = io.BytesIO(n)
                                    # img=Image.open(stream)
                                    # img =PhotoImage(img) 
                                    #bg thems..............
                                    gv_img=PhotoImage(file='themes/voteback.png')
                                    gv_l=Label(votewin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                    gv_l.place(x=30,y=10) 

                                    #choose party.......
                                    cp_l=Label(votewin,text='Choose Your Favourite Party',font=('Regular',22),bg='white',fg='blue')
                                    cp_l.place(x=96,y=70)
                                    cp1_e=Radiobutton(votewin,text='BJP',font=('times new roman',18),fg='#FF9F29',bg='white',activebackground='white',value=1,cursor='hand2',variable=v1)
                                    cp1_e.place(x=110,y=150)
                                    cp2_e=Radiobutton(votewin,text='TMC',font=('times new roman',18),fg='green',bg='white',activebackground='white',value=2,cursor='hand2',variable=v1)
                                    cp2_e.place(x=220,y=150)
                                    cp3_e=Radiobutton(votewin,text='Congress',font=('times new roman',18),fg='red',bg='white',activebackground='white',value=3,cursor='hand2',variable=v1)
                                    cp3_e.place(x=340,y=150)
                                    
                                    #give vote button img import
                                    #gvote_bg=PhotoImage(file='button/verify.png')
                                    gvote=Button(votewin,text='✓ Verify ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',command=give,padx=10)
                                    gvote.place(x=225,y=240)
                                votewin.mainloop()

                            '''---------------------- Profile Area----------------------'''

                            afterlogin_img=PhotoImage(file='themes/afterlogin.png')
                            afterlogin_l=Label(afterloginwin,image=afterlogin_img,bg='#D9D9D9',width=500,height=600)
                            afterlogin_l.place(x=25,y=10)

                            u_img=PhotoImage(file='button/uphoto.png')
                            userphoto=Label(afterloginwin,image=u_img)
                            userphoto.place(x=210,y=50)

                            #////////////////////////////////
                            fp = io.BytesIO(myphoto)
                            # load the image
                            image = Image.open(fp)
                            res=image.resize((114,134))
                            # drawing image to top window
                            userimg = ImageTk.PhotoImage(res)

                            userphoto=Label(afterloginwin,image=userimg)
                            userphoto.place(x=210,y=50)

                            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                            #------------------------------------
                            #card no
                            ucard_no=Label(afterloginwin,text='Voter ID: ',font=('Regular',10),bg='white')
                            ucard_no.place(x=200,y=200)

                            ucard_p=Label(afterloginwin,text=cd,font=('Regular',10),bg='white')
                            ucard_p.place(x=260,y=200)
                            
                            #>>>>>>>>>>>>>>>>>>>>>>>

                            #name
                            uname=Label(afterloginwin,text='Name: ',font=('Regular',10),bg='white')
                            uname.place(x=70,y=250)    
                            uname_p=Label(afterloginwin,text=n,font=('Regular',10),bg='white')
                            uname_p.place(x=180,y=250)

                            #father name
                            fname=Label(afterloginwin,text='Father Name: ',font=('Regular',10),bg='white')
                            fname.place(x=70,y=280)
                            fname_p=Label(afterloginwin,text=f,font=('Regular',10),bg='white')
                            fname_p.place(x=180,y=280)

                            #gender
                            ugender=Label(afterloginwin,text='Gender: ',font=('Regular',10),bg='white')
                            ugender.place(x=70,y=310)
                            ugender_p=Label(afterloginwin,text=g,font=('Regular',10),bg='white')
                            ugender_p.place(x=180,y=310)

                            #date of birth
                            udob=Label(afterloginwin,text='Date Of Birth: ',font=('Regular',10),bg='white')
                            udob.place(x=70,y=340)
                            udob_p=Label(afterloginwin,text=d,font=('Regular',10),bg='white')
                            udob_p.place(x=180,y=340)

                            #phone no
                            uphone=Label(afterloginwin,text='Phone Number : ',font=('Regular',10),bg='white')
                            uphone.place(x=70,y=370)
                            uphone_p=Label(afterloginwin,text=p,font=('Regular',10),bg='white')
                            uphone_p.place(x=180,y=370)

                            #aadhaar no
                            uaadhaar=Label(afterloginwin,text='Linked Aadhaar: ',font=('Regular',10),bg='white')
                            uaadhaar.place(x=70,y=400)
                            uaadhaar_p=Label(afterloginwin,text=aah,font=('Regular',10),bg='white')
                            uaadhaar_p.place(x=180,y=400)

                            uvstatus=Label(afterloginwin,text='Voting Status _: ',font=('Regular',10),bg='white')
                            uvstatus.place(x=70,y=430)
                            uvstatus_p=Label(afterloginwin,text=vs,font=('Regular',10),bg='white',fg='red')
                            uvstatus_p.place(x=180,y=430)

                            #>>>>>>>>>>>>
                            #village
                            uvill=Label(afterloginwin,text='Vill: ',font=('Regular',10),bg='white')
                            uvill.place(x=340,y=250)
                            uvill_p=Label(afterloginwin,text=vill,font=('Regular',10),bg='white')
                            uvill_p.place(x=390,y=250)

                            #post
                            upost=Label(afterloginwin,text='Post: ',font=('Regular',10),bg='white')
                            upost.place(x=340,y=280)
                            upost=Label(afterloginwin,text=po,font=('Regular',10),bg='white')
                            upost.place(x=390,y=280)

                            #Pin
                            upin=Label(afterloginwin,text='Pin : ',font=('Regular',10),bg='white')
                            upin.place(x=340,y=310)
                            upin=Label(afterloginwin,text=pin,font=('Regular',10),bg='white')
                            upin.place(x=390,y=310)

                            #district
                            udist=Label(afterloginwin,text='Dist: ',font=('Regular',10),bg='white')
                            udist.place(x=340,y=340)
                            udist=Label(afterloginwin,text=dist,font=('Regular',10),bg='white')
                            udist.place(x=390,y=340)

                            #stste
                            ustate=Label(afterloginwin,text='State: ',font=('Regular',10),bg='white')
                            ustate.place(x=340,y=370)
                            ustate=Label(afterloginwin,text=state,font=('Regular',10),bg='white')
                            ustate.place(x=390,y=370)

                            #button area  >>>>>>>>>>>>>>>>>>>>>>

                            #give vote button img import
                            gvote_bg=PhotoImage(file='button/gvote.png')
                            gvote=Button(afterloginwin,image=gvote_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=give)
                            gvote.place(x=105,y=530)

                            def upd():
                                lw=Label(afterloginwin,text='Sorry You Can Not Update Any Detaile, It\' Possiable After Upcomming Upgrade',fg='red',bg='white' )
                                lw.place(x=75,y=495)

                            #Update button
                            upd_bg=PhotoImage(file='button/upd.png')
                            upd=Button(afterloginwin,image=upd_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=upd)
                            upd.place(x=232,y=530)

                            def ulogout():
                                afterloginwin.destroy()
                                logwin.destroy()

                            #logout button img import
                            logout_bg=PhotoImage(file='button/ulogout.png')
                            logout=Button(afterloginwin,image=logout_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=ulogout)
                            logout.place(x=360,y=530)

                            afterloginwin.mainloop()
                        else:
                            #cancel button img import
                            Warning_u_p=Label(logwin,text='Wrong User ID or Password',bg='white',fg='red')
                            Warning_u_p.place(x=690,y=180)

                    

            def forgetpass():
                try:
                    db=sqlite3.connect('voting management system.db')
                    cr=db.cursor()
                except:
                    print('Forgt db is running...')
                forgetwin=Toplevel()
                forgetwin.title('Forget Password')
                forgetwin.geometry('550x680+485+25')
                forgetwin.wm_iconbitmap('icon/login.ico')
                forgetwin.resizable(False,False)
                entphone=StringVar()
                #send OTP
                def sendotpp():
                    fphone_num=entphone.get()
                    cr.execute('select phone from registration')
                    fp_data=cr.fetchall()
                    fcheck=0
                    for ff in fp_data:
                        fp=ff[0]
                        if fphone_num==fp:
                            fcheck=1
                            break
                        else:
                            fcheck=0
                    if fcheck==1:
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_phone=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_phone.place(x=250,y=94)
                        #resend button
                        sendotp=Button(forgetwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                        sendotp.place(x=198,y=130)

                        '''------------------------------------------------------'''
                        #generate otp.........
                        fotp=str(random.randint(1111,9999))
                        #print('otp is: ',fotp)
                        #       
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        # account_sid = 'AC714959399352b0bebabaac962eb62449'
                        # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        # client = Client(account_sid, auth_token)
                        # too='+91'+fp
                        # msg='Online Voting System\nForget Password OTP: '+fotp
                        # client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
                        '''--------------------- Testing Otp ----------------------'''        
                        otpnote='Only for Testing Purpose OTP: '+fotp
                        testing=Label(forgetwin,text=otpnote,font=('Regular',8),fg='red')
                        testing.place(x=5,y=650)

                        #update otp..............
                        cr.execute('update registration set otp=? where phone=?',(fotp,fp))
                        db.commit()
                        #print('changed otp')

                        rotp=StringVar()
                        def verifyfotp():
                            rsotp=rotp.get()
                            cr.execute(f'select otp from registration where phone={fp}')
                            fetchotp=cr.fetchall()
                            for fe in fetchotp:
                                dotp=fe[0]

                            #if matched otp............
                            if dotp==rsotp:
                                #hide invalid otp error
                                invalid_OTP=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)
                                #verified otp button
                                Verifyotp=Button(forgetwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                                Verifyotp.place(x=205,y=290)

                                pass1=StringVar()
                                pass2=StringVar()
                                def changepass():
                                    pass11=pass1.get()
                                    pass22=pass2.get()
                                    if pass11==pass22:
                                        cr.execute('update registration set password=?,conform_password=? where phone=?',(pass11,pass22,fp))
                                        db.commit()
                                        # print('pass changed')  
                                        
                                        #close forgetwindow............
                                        forgetwin.destroy()

                                        changedwin=Toplevel()
                                        changedwin.title('Successfully changed Password')
                                        changedwin.geometry('550x680+485+25')
                                        changedwin.wm_iconbitmap('icon/login.ico')
                                        changedwin.resizable(False,False)
                                        changedwin.overrideredirect()


                                        ch_img=PhotoImage(file='logo/check.png')
                                        ch_l=Label(changedwin,image=ch_img)
                                        ch_l.place(x=215,y=100)

                                        ph_l=Label(changedwin,text='Your Password Successfully changed',font=('times new roman',20),fg='blue')
                                        ph_l.place(x=70,y=230)

                                        changedwin.mainloop()

                                    else:
                                        # print('conform pass not match')
                                        #password not match
                                        invalid_pass=Label(forgetwin,text='Conform Password Not Matched',font=('times new roman',8),fg='red')
                                        invalid_pass.place(x=250,y=462)

                                #import password image
                                pass_f=Label(forgetwin,text='New Password',font=('times new roman',18),bg='white')
                                pass_f.place(x=80,y=380)
                                #entry password
                                pass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,textvar=pass1)
                                pass_fe.place(x=250,y=380)


                                #import conform password image
                                con_pass_e=Label(forgetwin,text='Re... Password',font=('times new roman',18),bg='white')
                                con_pass_e.place(x=80,y=430)
                                #entry conform password
                                conpass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,show='*',textvar=pass2)
                                conpass_fe.place(x=250,y=430)
                                #login button img import
                                #sub1_img=PhotoImage(file='button/u_login.png')
                                sub11=Button(forgetwin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=changepass)
                                sub11.place(x=145,y=550)
                                #cancel button img import
                                #canc_bg=PhotoImage(file='button/cancel.png')
                                canc1=Button(forgetwin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:forgetwin.destroy())
                                canc1.place(x=295,y=550)  
                            else:
                                # print('Please Enter Valid OTP')
                                invalid_OTP=Label(forgetwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)



                        #verify otp..........
                        otp_l1=Label(forgetwin,text='Enter OTP ',font=('Regular',18))
                        otp_l1.place(x=110,y=200)
                        otp_s1=Label(forgetwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_s1.place(x=245,y=230)
                        otp_e1=Entry(forgetwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=rotp)
                        otp_e1.place(x=245,y=200) 

                        Verifyotp=Button(forgetwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                        Verifyotp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_phone=Label(forgetwin,text='Please Enter Registered Phone Number',font=('times new roman',8),fg='red')
                        invalid_phone.place(x=250,y=90)

                #label of phone number
                fphone=Label(forgetwin,text='Phone Number :',font=('times new roman',18,'bold'),fg='black',bd=0)
                fphone.place(x=50,y=50)
                #enter phone number
                fphone_e=Entry(forgetwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entphone)
                fphone_e.place(x=250,y=50)


                sendotp=Button(forgetwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                sendotp.place(x=198,y=130)

                forgetwin.mainloop()

            #frame bg image import
            fbg=PhotoImage(file='themes/login form.png')
            login_background=Label(logwin,image=fbg,bg='#D9D9D9',width=518,height=654)
            login_background.place(x=510,y=10)

            #uid label img import
            uid_bg=PhotoImage(file='button/uid.png')
            uid_l=Label(logwin,image=uid_bg,bd=0,bg='white')
            uid_l.place(x=565,y=240)

            #uid input       ----*** Entry Box ***----
            uid_e=Entry(logwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',textvar=uid)
            uid_e.place(x=730,y=242)

            #password label img import
            pass_bg=PhotoImage(file='button/password.png')
            password=Label(logwin,image=pass_bg,bd=0,bg='white')
            password.place(x=565,y=320)

            #password input  ----*** Entry Box ***----
            pass_e=Entry(logwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',show='*',textvar=upass)
            pass_e.place(x=730,y=322)


            #login button img import
            log_bg=PhotoImage(file='button/u_login.png')
            login=Button(logwin,image=log_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=login)
            login.place(x=565,y=410)

            #cancel button img import
            cancel_bg=PhotoImage(file='button/cancel.png')
            login=Button(logwin,image=cancel_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:logwin.destroy())
            login.place(x=730,y=410)

            #forget button img import
            #forget_bg=PhotoImage(file='button/forget.png')
            forget=Button(logwin,text='Forget Pasword?',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=forgetpass)
            forget.place(x=570,y=512)

            #slash / button img import
            slash_bg=PhotoImage(file='button/slash.png')
            slash=Button(logwin,image=slash_bg,bd=0,bg='white',activebackground='white')
            slash.place(x=705,y=512)

            #Create new account button img import
            #create_new_ac_bg=PhotoImage(file='button/create_new_ac.png')
            create=Button(logwin,text='Apply For New Candidate',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=RegistrationForm)
            create.place(x=730,y=512)

            logwin.mainloop()


        def givevote_now():
            gv2=Toplevel()
            gv2.title('Give Vote')
            gv2.geometry('550x680+480+25')
            gv2.wm_iconbitmap('icon/vote-sign.ico')
            gv2.resizable(False,False)
            cr=db.cursor()  


            entcard=StringVar()
            def sub_vot_otp():
                inputcard_no=entcard.get()
                cr.execute(f'select card_no from registration')
                data22=cr.fetchall()
                vnc=0
                for ii in data22:
                    vn=ii[0]
                    if inputcard_no == vn:
                        vnc=1
                        break
                    else:
                        vnc=0
                if vnc==1:
                    # print('match')
                    #print('Phone number not match')
                    invalid_card=Label(gv2,text=' ',font=('times new roman',8),fg='red',width=30)
                    invalid_card.place(x=250,y=90)
                    cr.execute(f'select phone,voting_status from registration where card_no={vn}')
                    fvts=cr.fetchall()
                    for jj in fvts:
                        vtphone=jj[0]
                        votingstatus=jj[1]
                    # print(votingstatus)
                    # print(vtphone)
                    if votingstatus=='Not Voted':
                        null=0
                        v1=IntVar()
                        def give():
                            v2=v1.get()
                            if v2==null:
                                #choose party.......
                                cpp_l=Label(gv2,text='Please Choose Party',font=('Regular',8),fg='red')
                                cpp_l.place(x=213,y=310)
                                v3='please choose party'
                            elif v2==1:
                                v3='BJP'
                            elif v2==2:
                                v3='TMC'
                            else:
                                v3='Congress'

                            if v3=='BJP' or v3=='TMC' or v3=='Congress':
                                # print(v3)
                                cpp_l=Label(gv2,text=' ',font=('Regular',8),fg='red',width=30)
                                cpp_l.place(x=213,y=310)
                                #gvote_bg=PhotoImage(file='button/verify.png')
                                gvote=Button(gv2,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=give)
                                gvote.place(x=210,y=330)                    

                                '''------------------------------------------------------'''
                                #generate otp.........
                                motpp=str(random.randint(1111,9999))
                                # print(motpp)
                                #    
                                '''-------------------TESTING OTP-------------------------'''

                                ottp='Only for testing purposr OTP: ' +motpp
                                test_l=Label(gv2,text=ottp,fg='red')
                                test_l.place(x=10,y=630)

                                # '''------------------Twillo OTP Service------------------'''
                                # account_sid = 'AC714959399352b0bebabaac962eb62449'
                                # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                                # client = Client(account_sid, auth_token)
                                # too='+91'+vtphone
                                # msg='Online Voting System\nyou can give vote\nyour OTP is: '+motpp
                                # client.messages.create(body=msg,from_='+19788308309',to=too)

                                '''-------------------------------------------------------'''            

                                cr.execute(f'update registration set otp={motpp} where card_no={vn}')
                                db.commit()

                                rsotp=StringVar()
                                def urs_otp():
                                    reseveotp=rsotp.get()
                                    cr.execute(f'select voting_status,otp from registration where card_no={vn}')                
                                    otpdata=cr.fetchall()
                                    for ot in otpdata:
                                        vts=ot[0]
                                        sotp=ot[1]
                                    already='Already Voted'
                                    if sotp==reseveotp:
                                        if vts=='Not Voted':
                                            cr.execute('update registration set voting_status=?,vot_status=? where card_no=?',(already,v3,vn))
                                            db.commit()

                                            #Thanks for vote...................
                                            successwin=Toplevel()
                                            successwin.title('success full vote')
                                            successwin.geometry('550x680+487+25')
                                            successwin.wm_iconbitmap('icon/feedback.ico')
                                            successwin.resizable(False,False)
                                            #successwin.attributes('-fullscreen',True)
                                            successwin.overrideredirect(1)

                                            note='Thank You For Give Vote...'
                                            #background...
                                            gv_img=PhotoImage(file='themes/voteback.png')
                                            gv_l=Label(successwin,image=gv_img,width=500,height=600)
                                            gv_l.place(x=33,y=10) 

                                            warning_img=PhotoImage(file='logo/check.png')
                                            war_l=Label(successwin,image=warning_img,width=200,height=100,bg='white')
                                            war_l.place(x=180,y=70)

                                            not_l=Label(successwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                            not_l.place(x=150,y=200)

                                            # Re-fetch voting count data.........
                                            
                                            cr.execute("select vot_status from registration")
                                            vt_data=cr.fetchall()
                                            tmc=0
                                            bjp=0
                                            cong=0
                                            for v_c in vt_data:
                                                total_v=v_c[0]
                                                if total_v=='TMC':
                                                    tmc += 1
                                                if total_v== 'BJP':
                                                    bjp +=1
                                                if total_v== 'Congress':
                                                    cong +=1

                                            # #show count Bjp                                    
                                            # bjp_s1=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
                                            # bjp_s1.place(x=440,y=180)
                                            # #show count TMC
                                            # tmc_s1=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
                                            # tmc_s1.place(x=440,y=370)
                                            # #show count CONJ
                                            # conj_s1=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
                                            # conj_s1.place(x=440,y=560)

                                            # #percentage
                                            # tperentage=bjp+cong+tmc
                                            # cpercentage_bjp=round((bjp/tperentage)*100,2) ,"%"
                                            # bjp_p=Label(root,text=cpercentage_bjp,font=('Regular',16),bg='white',fg='blue',width=8)
                                            # bjp_p.place(x=560,y=235)
                                            # #percentage
                                            # cpercentage_tmc=round((tmc/tperentage)*100,2) ,"%"
                                            # tmc_p=Label(root,text=cpercentage_tmc,font=('Regular',16),bg='white',fg='blue',width=8)
                                            # tmc_p.place(x=560,y=425)
                                            # #percentage
                                            # cpercentage_cong=round((cong/tperentage)*100,2) ,"%"
                                            # cong_p=Label(root,text=cpercentage_cong,font=('Regular',16),bg='white',fg='blue',width=8)
                                            # cong_p.place(x=560,y=610)

                                            # #progress
                                            # for i in range(0,len(cpercentage_bjp)):
                                            #     bjp_percentage=round(cpercentage_bjp[0])
                                            #     break
                                            # # print(type(bjp_percentage))

                                            # progressbar_bjp=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                            # progressbar_bjp['value']=bjp_percentage
                                            # progressbar_bjp.place(x=300,y=240)

                                            # #progress
                                            # for i in range(0,len(cpercentage_tmc)):
                                            #     tmc_percentage=round(cpercentage_tmc[0])
                                            #     break
                                            # # print(type(tmc_percentage))

                                            # progressbar_tmc=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                            # progressbar_tmc['value']=tmc_percentage
                                            # progressbar_tmc.place(x=300,y=430)

                                            # #progress
                                            # for i in range(0,len(cpercentage_cong)):
                                            #     cong_percentage=round(cpercentage_cong[0])
                                            #     break
                                            # # print(type(cong_percentage))

                                            # progressbar_cong=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                            # progressbar_cong['value']=cong_percentage
                                            # progressbar_cong.place(x=300,y=615)
                                            #vote count....
                                            bjp_s=Label(root,text=bjp,font=('Regular',20),bg='#BCEAD5',fg='blue')
                                            bjp_s.place(x=190,y=232)
                                            tmc_s=Label(root,text=tmc,font=('Regular',20),bg='#BCEAD5',fg='blue')
                                            tmc_s.place(x=410,y=232)
                                            conj_s=Label(root,text=cong,font=('Regular',20),bg='#BCEAD5',fg='blue')
                                            conj_s.place(x=630,y=232)

                                            
                                            #pie chart.....
                                            figure2=Figure(figsize=(4,4),dpi=100)
                                            subplot2=figure2.add_subplot(111)

                                            vot_per=[bjp,tmc,cong]
                                            party_name=['BJP','TMC','CONGRESS']
                                            exp=[0,0,0]
                                            color_pi=['#FF9700','green','yellow']

                                            subplot2.pie(vot_per, labels=party_name, explode=exp, autopct='%2.2f%%', colors=color_pi)
                                            pie2=FigureCanvasTkAgg(figure2,root)
                                            pie2.get_tk_widget().place(x=150,y=380)
                                            pr=Label(text='Pie Chart Report',font=('Regular',20),bg='white')
                                            pr.place(x=50,y=370) 
                                            
                                           
                                            def closesuccess():              
                                                successwin.destroy()
                                                gv2.destroy()    

                                            #cancel button img import
                                            tgv_bg=PhotoImage(file='button/close.png')
                                            tgv=Button(successwin,image=tgv_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=closesuccess)
                                            tgv.place(x=230,y=370)
                                            
                                            successwin.mainloop()
                                        else:
                                            #already voted...................
                                            alwin=Toplevel()
                                            alwin.title('Already Voted')
                                            alwin.geometry('550x680+487+25')
                                            alwin.wm_iconbitmap('icon/feedback.ico')
                                            alwin.resizable(False,False)
                                            #alwin.attributes('-fullscreen',True)
                                            alwin.overrideredirect(1)

                                            note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                                            #background...
                                            gv_img=PhotoImage(file='themes/voteback.png')
                                            gv_l=Label(alwin,image=gv_img,width=500,height=600)
                                            gv_l.place(x=30,y=10) 

                                            warning_img=PhotoImage(file='logo/warning.png')
                                            war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                                            war_l.place(x=180,y=70)

                                            not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                            not_l.place(x=85,y=200)
                                            #cancel button img import
                                            canc_bg=PhotoImage(file='button/close.png')
                                            canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                                            canc.place(x=225,y=370)
                                            alwin.mainloop()
                                    else:
                                        #print('wrong otp')                                
                                        w_l=Label(gv2,text='Please Enter Valid OTP',fg='red',width=50)
                                        w_l.place(x=130,y=430)
                                #otp..........
                                otp_l=Label(gv2,text='Enter OTP ',font=('Regular',18))
                                otp_l.place(x=110,y=400)
                                otp_s=Label(gv2,text='4 Digit OTP Send Your Mobile Number',font=('Regular',8))
                                otp_s.place(x=245,y=430)
                                otp_e=Entry(gv2,font=('Regular',18),bg='#DFF6FF',width=16,textvar=rsotp)
                                otp_e.place(x=245,y=400)  
                                #login button img import
                                #sub1_img=PhotoImage(file='button/u_login.png')
                                sub1=Button(gv2,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=urs_otp)
                                sub1.place(x=140,y=490)
                                #cancel button img import
                                #canc_bg=PhotoImage(file='button/cancel.png')
                                canc=Button(gv2,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:gv2.destroy())
                                canc.place(x=310,y=490)                    
                        #choose party.......
                        cp_l=Label(gv2,text='Choose Your Favourite Party',font=('Regular',22),fg='blue')
                        cp_l.place(x=96,y=200)

                        cp1_e=Radiobutton(gv2,text='BJP',font=('times new roman',18),fg='#FF9F29',activebackground='white',value=1,cursor='hand2',variable=v1)
                        cp1_e.place(x=110,y=265)
                        cp2_e=Radiobutton(gv2,text='TMC',font=('times new roman',18),fg='green',activebackground='white',value=2,cursor='hand2',variable=v1)
                        cp2_e.place(x=220,y=265)
                        cp3_e=Radiobutton(gv2,text='Congress',font=('times new roman',18),fg='red',activebackground='white',value=3,cursor='hand2',variable=v1)
                        cp3_e.place(x=340,y=265)

                        #gvote_bg=PhotoImage(file='button/verify.png')
                        gvote=Button(gv2,text='✓ Verify ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=give)
                        gvote.place(x=210,y=330)

                                
                    else:
                        # print('cant not take vote')
                        #already voted...................
                        alwin=Toplevel()
                        alwin.title('Already Voted')
                        alwin.geometry('550x680+487+25')
                        alwin.wm_iconbitmap('icon/feedback.ico')
                        alwin.resizable(False,False)
                        
                        #alwin.attributes('-fullscreen',True)
                        alwin.overrideredirect(1)

                        note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                        #background...
                        gv_img=PhotoImage(file='themes/voteback.png')
                        gv_l=Label(alwin,image=gv_img,width=500,height=600)
                        gv_l.place(x=30,y=10) 

                        warning_img=PhotoImage(file='logo/warning.png')
                        war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                        war_l.place(x=180,y=70)

                        not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                        not_l.place(x=85,y=200)
                        #cancel button img import
                        canc_bg=PhotoImage(file='button/close.png')
                        canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                        canc.place(x=225,y=370)
                        alwin.mainloop()

                else:
                    #print('Phone number not match')
                    invalid_card=Label(gv2,text='Please Enter Valid Voter ID',font=('times new roman',8),fg='red')
                    invalid_card.place(x=250,y=90)
                
            #label of phone number
            card_num=Label(gv2,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
            card_num.place(x=50,y=55)
            #enter phone number
            card_num_e=Entry(gv2,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
            card_num_e.place(x=250,y=50)

            send_card_otp=Button(gv2,text=' Submit ', fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sub_vot_otp)
            send_card_otp.place(x=210,y=130)

            gv2.mainloop()





        #required to login......
        def required_to_login():        
            def update_verify():
                update_verify_win=Toplevel()
                update_verify_win.title('Update Details')
                update_verify_win.geometry('550x580+485+95')
                update_verify_win.wm_iconbitmap('icon/notap.ico')
                update_verify_win.resizable(False,False)

                entcard=StringVar()
                #send OTP
                def sendcardotp():
                    cardn=entcard.get()
                    cr.execute('select card_no from registration')
                    sc_data=cr.fetchall()
                    cfetch=0
                    for sc in sc_data:
                        sc1=sc[0]
                        if cardn==sc1:
                            cfetch=1
                            break
                        else:
                            cfetch=0
                    if cfetch==1:
                        # print('valid card number')
                        # print(sc1)
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_card=Label(update_verify_win,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_card.place(x=250,y=94)
                        #resend button
                        send_card_otp=Button(update_verify_win,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                        send_card_otp.place(x=198,y=130)

                        cr.execute(f'select phone from registration where card_no={sc1}')
                        fetchcard_phone=cr.fetchall()
                        for fpp in fetchcard_phone:
                            cpn=fpp[0]
                        # print(cpn)
                        #generate otp.........
                        viewotp=str(random.randint(1111,9999))
                        # print('otp is: ',viewotp)
                        #       
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        # account_sid = 'AC714959399352b0bebabaac962eb62449'
                        # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        # client = Client(account_sid, auth_token)
                        # too='+91'+cpn
                        # msg='Online Voting System\nFor card verification\nyour OTP is: '+viewotp
                        # client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                        '''--------------------- Testing Otp ----------------------'''  

                        otpnote_view='Only for Testing Purpose OTP: '+viewotp
                        testing=Label(update_verify_win,text=otpnote_view,font=('Regular',8),fg='red')
                        testing.place(x=5,y=0)

                        #update otp..............
                        cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                        db.commit()
                        # print('changed/update otp')
                        view_l=Button(update_verify_win,text='  ',fg='white',font=('Regular',15),bd=0,cursor='hand2',padx=10,width=70)
                        view_l.place(x=100,y=400)

                        ue_otp=StringVar()
                        def verify_ue_otp():
                            rs_otp=ue_otp.get()
                            cr.execute(f'select otp from registration where phone={cpn}')
                            f_otpdata=cr.fetchall()
                            for dotpp in f_otpdata:
                                ot=dotpp[0]

                            if ot==rs_otp:
                                # print('otp match')
                                Verifyotpp=Button(update_verify_win,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                                Verifyotpp.place(x=205,y=290)


                                def edit():
                                    update_verify_win.destroy()
                                    log_result=messagebox.askyesno('Login Required','You Can\'t Change/Update any Details Now\n It\'s Possiable After UpComming Update\n Our Team Workin On This System for better Upgrad...\n         \nAre You Want To Login Now ?')
                                    if log_result == True:
                                        LoginForm()

                                updatenow=Button(update_verify_win,text="Click here to Edit Your Details",font=("times new roman",14),bg="blue",fg="white",cursor="hand2", command=edit)
                                updatenow.place(x=155,y=390)

                                
                                







                                

                                

                        #verify otp..........
                        otp_t1=Label(update_verify_win,text='Enter OTP ',font=('Regular',18))
                        otp_t1.place(x=110,y=200)
                        otp_w1=Label(update_verify_win,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_w1.place(x=245,y=230)
                        otp_ee=Entry(update_verify_win,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                        otp_ee.place(x=245,y=200) 

                        Verifyotpp=Button(update_verify_win,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                        Verifyotpp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_card=Label(update_verify_win,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                        invalid_card.place(x=250,y=90)
                #label of phone number
                card_num=Label(update_verify_win,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
                card_num.place(x=50,y=55)
                #enter phone number
                card_num_e=Entry(update_verify_win,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                card_num_e.place(x=250,y=50)

                send_card_otp=Button(update_verify_win,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                send_card_otp.place(x=198,y=130)

                update_verify_win.mainloop()



            update_verify()

            
        #Track Application..................................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        def trackapplication():

            trackwin=Toplevel()
            trackwin.geometry('550x680+490+50')
            trackwin.wm_iconbitmap('icon/track.ico')
            trackwin.title('Track Application Status')
            trackwin.resizable(False,False)
            trackwin.config(background='#EAF6F6')
            db=sqlite3.connect('voting management system.db')
            cr=db.cursor()

            tid=StringVar()
            def aptrack():
                apno=tid.get()
                #print(apno)
                cr.execute('select application_no from registration')
                data=cr.fetchall()
                db.commit()
                for i in data:
                    a=i[0]
                    check=0
                    if apno==a:
                        check=1
                        break
                    else:
                        check=0        
                if check==1:
                    cr.execute(f'select card_no from registration where application_no={a}')
                    card_no=cr.fetchall()
                    for k in card_no:
                        card=k[0]
                    
                    w='You are Voter Id is ' +card            
                    track = Label(trackwin, text=w, font=('Regular', 16), fg='blue',width=45,bg='#EAF6F6')
                    track.place(x=0, y=270)
                else:
                    track1 = Label(trackwin, text='Please Enter Valid Application No', font=('Regular', 8), fg='red',bg='#EAF6F6')
                    track1.place(x=240, y=135)            


            L2=Label(trackwin,text='Application No :',font=('times new roman',20,'bold'),bg='#EAF6F6',fg='black',bd=0)
            L2.place(x=25,y=100)

            E1=Entry(trackwin,font=('times new roman',20,'bold'),textvar=tid)
            E1.place(x=240,y=100)

            B1_img=PhotoImage(file='button/appsearch.png')    
            B1=Button(trackwin,image=B1_img,bd=0,bg='#EAF6F6',fg='black',command=aptrack,cursor='hand2')
            B1.place(x=200,y=185)


            trackwin.mainloop()

        def adminlogin_from():    
            adlogwin=Toplevel()
            adlogwin.title('Administrator Login')
            adlogwin.geometry('550x670+485+25')
            adlogwin.wm_iconbitmap('icon/admin.ico')
            adlogwin.resizable(False,False)
            #frame bg image import
            fbg=PhotoImage(file='themes/adlog.png')
            login_background=Label(adlogwin,image=fbg,width=518,height=654)
            login_background.place(x=15,y=8)
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Database Connect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            null=0
            uid=StringVar()
            upass=StringVar()
            def adlogin():
                userid=uid.get()
                upassword=upass.get()
                    
                #userid.................
                userid_length=0
                userid_length=len(userid)
                if null == userid_length:
                    #validation.....                 
                    validation=Label(adlogwin,text='Please Enter User ID',font=('Regular',10),fg='red',bg='white')
                    validation.place(x=240,y=270)
                else:
                    #password..............
                    password_length=len(upassword)
                if null == password_length:
                    p='Please Enter Password'
                    validation=Label(adlogwin,text=p,font=('Regular',10),fg='red',bg='white')
                    validation.place(x=240,y=360)
                else:
                    cr.execute("select uid,password from admin")
                    data=cr.fetchall()
                    check=0
                    for i in data:
                        a=i[0]
                        b=i[1]

                        if userid==a and upassword==b:
                            check=1
                            break
                        else:
                            check=0
                    if check == 1:

                        #//////////////////////////////////////<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        # admin login successfull

                        adlogwin.destroy()   

                        adminwin=Toplevel()
                        adminwin.title('Admin Panel')
                        adminwin.geometry('600x600')
                        adminwin.minsize(600,400)
                        adminwin.wm_iconbitmap('icon/admin.ico')
                        adminwin.resizable(False,False)#maximize option disable
                        adminwin.attributes('-fullscreen',True)
                        adminwin.state('zoomed')#default open fullscreen
                        #-------------------------------------- Main Body ---------------------------------------- #
                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        #approved candidate
                        s=ttk.Style()
                        s.theme_use('clam')
                        s.configure('Treeview', rowheight=20)

                        tv1=ttk.Treeview(adminwin)
                        tv1['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16')
                        tv1.column('#0',width='0')
                        tv1.column('1',width='40')
                        tv1.column('2',width='150')
                        tv1.column('3',width='60')
                        tv1.column('4',width='50')
                        tv1.column('5',width='150')
                        tv1.column('6',width='70')
                        tv1.column('7',width='80')
                        tv1.column('8',width='100')
                        tv1.column('9',width='100')
                        tv1.column('10',width='50')
                        tv1.column('11',width='80')
                        tv1.column('12',width='80')
                        tv1.column('13',width='60')
                        tv1.column('14',width='88')
                        tv1.column('15',width='85')
                        tv1.column('16',width='80')

                        # name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,Voted by
                        tv1.heading('#0',text='+')
                        tv1.heading('1',text='Sl No')
                        tv1.heading('2',text='Name')
                        tv1.heading('3',text='DOB')
                        tv1.heading('4',text='Gender')
                        tv1.heading('5',text='Father Name')
                        tv1.heading('6',text='Phone No')
                        tv1.heading('7',text='Aadhaar No')
                        tv1.heading('8',text='Village')
                        tv1.heading('9',text='Post')
                        tv1.heading('10',text='Pin')
                        tv1.heading('11',text='District')
                        tv1.heading('12',text='State')
                        tv1.heading('13',text='Application No')
                        tv1.heading('14',text='Card No')
                        tv1.heading('15',text='Voting Status')
                        tv1.heading('16',text='Voted By')

                        def displayAll_1():
                            cr.execute('select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,account_status from registration')
                            adata=cr.fetchall()
                            fdata=0
                            a=0
                            tv1.delete(*tv1.get_children())
                            for i in adata:
                                f=i[12]
                                if f!='Not Generated':
                                    fdata += 1
                                    a += 1    
                                    tv1.insert(parent="", index="end", iid=i, text="", values=((a,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14])))
                        displayAll_1()



                        tv1.place(x=90,y=130)

                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        # not approve candidate..........

                        tv=ttk.Treeview(adminwin)
                        tv['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16')
                        tv.column('#0',width='0')
                        tv.column('1',width='40')
                        tv.column('2',width='150')
                        tv.column('3',width='60')
                        tv.column('4',width='50')
                        tv.column('5',width='150')
                        tv.column('6',width='70')
                        tv.column('7',width='80')
                        tv.column('8',width='100')
                        tv.column('9',width='100')
                        tv.column('10',width='50')
                        tv.column('11',width='80')
                        tv.column('12',width='80')
                        tv.column('13',width='60')
                        tv.column('14',width='88')
                        tv.column('15',width='85')
                        tv.column('16',width='80')

                        # name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,Voted by
                        tv.heading('#0',text='+')
                        tv.heading('1',text='Sl No')
                        tv.heading('2',text='Name')
                        tv.heading('3',text='DOB')
                        tv.heading('4',text='Gender')
                        tv.heading('5',text='Father Name')
                        tv.heading('6',text='Phone No')
                        tv.heading('7',text='Aadhaar No')
                        tv.heading('8',text='Village')
                        tv.heading('9',text='Post')
                        tv.heading('10',text='Pin')
                        tv.heading('11',text='District')
                        tv.heading('12',text='State')
                        tv.heading('13',text='Application No')
                        tv.heading('14',text='Card No')
                        tv.heading('15',text='Voting Status')
                        tv.heading('16',text='Voted By')

                        def displayAll_2():
                            cr.execute('select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,account_status from registration')
                            adata=cr.fetchall()
                            fdata=0
                            a=0
                            tv.delete(*tv.get_children())
                            for i in adata:
                                f=i[12]
                                if f=='Not Generated':
                                    fdata += 1
                                    a += 1    
                                    tv.insert(parent="", index="end", iid=i, text="", values=((a,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14])))
                        displayAll_2()
                        

                        tv.place(x=90,y=420)

                        #>......>>>>>>>>>>>>>>............>>>>>>>>>>>>>>>...................>>>>>>>>>>>>>>>>..............>>>>>>>>>>>>>>>>.
                        topnav=Label(adminwin,text='Welcome to Administrator Panel',font=('times new roman',28),fg='white',bg='blue')
                        topnav.pack(fill=X)

                        candidate=Label(adminwin,text='Approved Candidate Details',font=('times new roman',20),fg='blue')
                        candidate.place(x=90,y=90)

                        exit=Button(adminwin,text='Exit / Logout', font=('times new roman',14),fg='white',bg='#FF8B8B',command=lambda:adminwin.destroy(),cursor='hand2')
                        exit.place(x=1270,y=90)

                        notapcandidate=Label(adminwin,text='Not Approved Candidate Details',font=('times new roman',20),fg='blue')
                        notapcandidate.place(x=90,y=380)

                        def approved():
                            approvewin=Toplevel()
                            approvewin.title('Generate Card Number')
                            approvewin.geometry('550x680+485+25')
                            approvewin.wm_iconbitmap('icon/aprove.ico')
                            approvewin.resizable(False,False)

                            entcard=StringVar()
                            #send OTP
                            def sendcardotp():
                                ll=0
                                cardn=entcard.get()
                                cr.execute('select application_no,card_no from registration')
                                sc_data=cr.fetchall()
                                cfetch=0
                                for sc in sc_data:
                                    sc1=sc[0]
                                    crd=sc[1]
                                    if cardn==sc1:
                                        cfetch=1
                                        break
                                    else:
                                        cfetch=0

                                if ll != len(cardn):
                                    if cfetch==1:
                                        invalid_phone=Label(approvewin,text='',font=('times new roman',8),width=50)
                                        invalid_phone.place(x=265,y=90)
                                        
                                        if crd=='Not Generated': 
                                    
                                            invalid=Label(approvewin,text='',font=('times new roman',18),fg='red',width=30)
                                            invalid.place(x=135,y=300)

                                            c1=random.randint(1111111111,9999999999)
                                            cr.execute('update registration set card_no=? where application_no=?',(c1,sc1))
                                            db.commit()
                                            approvewin.destroy()
                                            apsuccesswin=Toplevel()    
                                            apsuccesswin.title('Generate Card Number')
                                            apsuccesswin.geometry('550x680+485+25')
                                            apsuccesswin.wm_iconbitmap('icon/aprove.ico')
                                            apsuccesswin.resizable(False,False)            

                                            warning_img=PhotoImage(file='logo/check.png')
                                            war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                            war_l.place(x=165,y=70)

                                            ge=Label(apsuccesswin,text="Successfully Generated Candidate Card Number...",font=('times new roman',14),fg='blue')
                                            ge.place(x=80,y=200) 
                                            displayAll_1()
                                            displayAll_2()                                        
                                            apsuccesswin.mainloop()
                                            entcard.set("")
                                        else:
                                            apsuccesswin=Toplevel()    
                                            apsuccesswin.title('Already Generate Card Number')
                                            apsuccesswin.geometry('550x680+485+25')
                                            apsuccesswin.wm_iconbitmap('icon/notap.ico')
                                            apsuccesswin.resizable(False,False)            
                                            
                                            warning_img=PhotoImage(file='logo/warning.png')
                                            war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                            war_l.place(x=165,y=70)

                                            ge=Label(apsuccesswin,text="Already Generated Card Number...",font=('times new roman',14),fg='blue')
                                            ge.place(x=135,y=200)                                
                                            apsuccesswin.mainloop()

                                    else:
                                        invalid=Label(approvewin,text='Invalid Application Number',font=('times new roman',18),fg='red')
                                        invalid.place(x=135,y=300)
                                else:
                                    invalid_phone=Label(approvewin,text='Please Enter Valid Application Number',font=('times new roman',8),fg='red')
                                    invalid_phone.place(x=265,y=90)

                            #label of phone number
                            card_num=Label(approvewin,text='Enter Application No: ',font=('times new roman',18,'bold'),fg='black',bd=0)
                            card_num.place(x=30,y=55)
                            #enter phone number
                            card_num_e=Entry(approvewin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                            card_num_e.place(x=265,y=50)

                            send_card_otp=Button(approvewin,text=' Generated ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                            send_card_otp.place(x=205,y=130)
                            approvewin.mainloop()

                        def suspend():
                            approvewin=Toplevel()
                            approvewin.title('Suspend / Delete User')
                            approvewin.geometry('550x680+485+25')
                            approvewin.wm_iconbitmap('icon/suspend.ico')
                            approvewin.resizable(False,False)

                            entcard=StringVar()
                            #send OTP
                            def sendcardotp():
                                cardn=entcard.get()
                                l=0                    
                                if l != len(cardn):
                                    cr.execute('select application_no,card_no,phone from registration')
                                    sc_data=cr.fetchall()
                                    cfetch=0
                                    for sc in sc_data:
                                        sc1=sc[0]
                                        crd=sc[1]
                                        ph=sc[2]
                                        if cardn==sc1 or cardn==crd:
                                            cfetch=1
                                            break
                                        else:
                                            cfetch=0
                    
                                    if cfetch==1:
                                        invalid_phone=Label(approvewin,text=' ',font=('times new roman',8),width=50)
                                        invalid_phone.place(x=265,y=90)

                                        invalid2=Label(approvewin,text=' ',font=('times new roman',18),fg='red',width=50,height=30)
                                        invalid2.place(x=25,y=300)


                                        cr.execute('delete from registration where phone=?',(ph,))
                                        db.commit()

                                        approvewin.destroy()
                                        apsuccesswin=Toplevel()         
                                        apsuccesswin.title('Generate Card Number')
                                        apsuccesswin.geometry('550x680+485+25')
                                        apsuccesswin.wm_iconbitmap('icon/suspend.ico')
                                        apsuccesswin.resizable(False,False)         

                                        warning_img=PhotoImage(file='logo/check.png')
                                        war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                        war_l.place(x=165,y=70)

                                        ge=Label(apsuccesswin,text="Candidate Card Number Permanently Deleted...",font=('times new roman',14),fg='red')
                                        ge.place(x=80,y=200)  
                                        displayAll_1()
                                        displayAll_2()          
                                        apsuccesswin.mainloop()
                                    else:                                
                                        invalid2=Label(approvewin,text='Enter Application / Card Number Already Suspend \nor\n Not Registered Our System',font=('times new roman',18),fg='red')
                                        invalid2.place(x=25,y=300)

                                else:
                                    invalid_phone=Label(approvewin,text='Enter Valid Application / Card Number',font=('times new roman',8),fg='red')
                                    invalid_phone.place(x=272,y=90)
                                    
                            
                            #label of phone number
                            card_num=Label(approvewin,text='Application / Card No: ',font=('times new roman',18,'bold'),fg='black',bd=0)
                            card_num.place(x=20,y=55)
                            #enter phone number
                            card_num_e=Entry(approvewin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                            card_num_e.place(x=275,y=50)

                            send_card_otp=Button(approvewin,text=' Suspend ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                            send_card_otp.place(x=198,y=130)

                            approvewin.mainloop()



                        approve=Button(adminwin,text=' Generate Card Number', font=('times new roman',14),bg='#00FFDD',cursor='hand2',command=approved)
                        approve.place(x=520,y=700)

                        suspend=Button(adminwin,text='Suspend Candidate', font=('times new roman',14),bg='#FC4F4F',cursor='hand2',command=suspend)
                        suspend.place(x=780,y=700)

                        adminwin.mainloop()

                        #//////////////////////////////////////<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    else:
                        #cancel button img import
                        wp=Label(adlogwin,text='Wrong User ID or Password',bg='white',fg='red')
                        wp.place(x=195,y=180)                


            def forgetadminpass():
                forgetwin=Toplevel()
                forgetwin.title('Forget User ID or Password')
                forgetwin.geometry('550x680+485+25')
                forgetwin.wm_iconbitmap('icon/admin.ico')
                forgetwin.resizable(False,False)
                entphone=StringVar()
                #send OTP
                def sendotpp():
                    fphone_num=entphone.get()
                    cr.execute('select phone from admin')
                    fp_data=cr.fetchall()
                    fcheck=0
                    for ff in fp_data:
                        fp=ff[0]
                        if fphone_num==fp:
                            fcheck=1
                            break
                        else:
                            fcheck=0
                    if fcheck==1:
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_phone=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_phone.place(x=250,y=94)
                        #resend button
                        sendotp=Button(forgetwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                        sendotp.place(x=198,y=130)

                        '''------------------------------------------------------'''
                        #generate otp.........
                        fotp=str(random.randint(1111,9999))
                        #print('otp is: ',fotp)
                        #              
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        account_sid = 'AC714959399352b0bebabaac962eb62449'
                        auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        client = Client(account_sid, auth_token)
                        too='+91'+fp
                        msg='Online Voting System\nForget Admin Password OTP: '+fotp
                        client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
                        '''--------------------- Testing Otp ----------------------'''          
                        otpnote='Only for Testing Purpose OTP: '+fotp
                        testing=Label(forgetwin,text=otpnote,font=('Regular',8),fg='red')
                        testing.place(x=5,y=650)

                        #update otp..............
                        cr.execute('update admin set otp=? where phone=?',(fotp,fp))
                        db.commit()
                        #print('changed otp')

                        rotp=StringVar()
                        def verifyfotp():
                            rsotp=rotp.get()
                            cr.execute(f'select uid,otp from admin where phone={fp}')
                            fetchotp=cr.fetchall()
                            for fe in fetchotp:
                                ud=fe[0]
                                dotp=fe[1]

                            #if matched otp............
                            if dotp==rsotp:
                                #hide invalid otp error
                                invalid_OTP=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)
                                #verified otp button
                                Verifyotp=Button(forgetwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                                Verifyotp.place(x=205,y=290)

                                pass1=StringVar()
                                pass2=StringVar()
                                def changepass():
                                    pass11=pass1.get()
                                    pass22=pass2.get()
                                    if pass11==pass22:
                                        cr.execute('update admin set password=? where phone=?',(pass11,fp))
                                        db.commit()
                                        # print('pass changed')  

                                        #close forgetwindow............
                                        forgetwin.destroy()

                                        changedwin=Toplevel()
                                        changedwin.title('Successfully changed Password')
                                        changedwin.geometry('550x680+485+25')
                                        changedwin.wm_iconbitmap('icon/login.ico')
                                        changedwin.resizable(False,False)
                                        changedwin.overrideredirect()


                                        ch_img=PhotoImage(file='logo/check.png')
                                        ch_l=Label(changedwin,image=ch_img)
                                        ch_l.place(x=215,y=100)

                                        ph_l=Label(changedwin,text='Your Password Successfully changed',font=('times new roman',20),fg='blue')
                                        ph_l.place(x=70,y=230)

                                        changedwin.mainloop()

                                    else:
                                        # print('conform pass not match')
                                        #password not match
                                        invalid_pass=Label(forgetwin,text='Conform Password Not Matched',font=('times new roman',8),fg='red')
                                        invalid_pass.place(x=250,y=462)

                                #import password image
                                pass_f=Label(forgetwin,text='New Password',font=('times new roman',18),bg='white')
                                pass_f.place(x=80,y=400)
                                #entry password
                                pass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,textvar=pass1)
                                pass_fe.place(x=250,y=400)
                                #import conform password image
                                con_pass_e=Label(forgetwin,text='Re... Password',font=('times new roman',18),bg='white')
                                con_pass_e.place(x=80,y=450)
                                #entry conform password
                                conpass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,show='*',textvar=pass2)
                                conpass_fe.place(x=250,y=450)

                                #import uid
                                uuid='Your User ID: '+ud
                                puid_f=Label(forgetwin,text=uuid,font=('times new roman',14),fg='red')
                                puid_f.place(x=180,y=345)


                                #login button img import
                                #sub1_img=PhotoImage(file='button/u_login.png')
                                sub11=Button(forgetwin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=changepass)
                                sub11.place(x=145,y=550)
                                #cancel button img import
                                #canc_bg=PhotoImage(file='button/cancel.png')
                                canc1=Button(forgetwin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:forgetwin.destroy())
                                canc1.place(x=295,y=550)  
                            else:
                                # print('Please Enter Valid OTP')
                                invalid_OTP=Label(forgetwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)



                        #verify otp..........
                        otp_l1=Label(forgetwin,text='Enter OTP ',font=('Regular',18))
                        otp_l1.place(x=110,y=200)
                        otp_s1=Label(forgetwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_s1.place(x=245,y=230)
                        otp_e1=Entry(forgetwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=rotp)
                        otp_e1.place(x=245,y=200) 

                        Verifyotp=Button(forgetwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                        Verifyotp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_phone=Label(forgetwin,text='Please Enter Registered Phone Number',font=('times new roman',8),fg='red')
                        invalid_phone.place(x=250,y=90)

                #label of phone number
                fphone=Label(forgetwin,text='Phone Number :',font=('times new roman',18,'bold'),fg='black',bd=0)
                fphone.place(x=50,y=50)
                #enter phone number
                fphone_e=Entry(forgetwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entphone)
                fphone_e.place(x=250,y=50)


                sendotp=Button(forgetwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                sendotp.place(x=198,y=130)

                forgetwin.mainloop()



            #uid label img import
            uid_bg=PhotoImage(file='button/uid.png')
            uid_l=Label(adlogwin,image=uid_bg,bd=0,bg='white')
            uid_l.place(x=70,y=230)

            #uid input   ----*** Entry Box ***----
            uid_e=Entry(adlogwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',textvar=uid)
            uid_e.place(x=240,y=232)

            #password label img import
            pass_bg=PhotoImage(file='button/password.png')
            password=Label(adlogwin,image=pass_bg,bd=0,bg='white')
            password.place(x=70,y=310)

            #password input  ----*** Entry Box ***----
            pass_e=Entry(adlogwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',show='*',textvar=upass)
            pass_e.place(x=240,y=312)


            #login button img import
            log_bg=PhotoImage(file='button/login.png')
            login=Button(adlogwin,image=log_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=adlogin)
            login.place(x=70,y=410)

            #cancel button img import
            cancel_bg=PhotoImage(file='button/cancel.png')
            cancel=Button(adlogwin,image=cancel_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:adlogwin.destroy())
            cancel.place(x=240,y=410)

            #forget button img import
            #forget_bg=PhotoImage(file='button/forget.png')
            forget=Button(adlogwin,text='Forget User ID or Pasword?',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=forgetadminpass)
            forget.place(x=75,y=480)

            adlogwin.mainloop()


        #screen-3
        def setting():
            setting_root=Toplevel()
            setting_root.geometry('100x200+1405+610')
            setting_root.overrideredirect(True)
            setting_root.config(bg='#C9C5C5')

            def set_s():
                exit_res=messagebox.askyesno('Exit','Are you sure you want to Close This Application?')
                if exit_res==True:
                    root.destroy()


                    # function 
                    page_url = 'https://github.com/Developer-Amit-Mandal/Online-Voting-Management-System#online-voting-management-system-dashboard'

                    def open_url():
                        try: 
                            webbrowser.open_new(page_url)
                            print('Opening URL...')  
                        except: 
                            print('Failed to open URL. Unsupported variable type.')

                    # initialize 
                    toaster = ToastNotifier()

                    # showcase
                    toaster.show_toast(
                        "Online Voting Management System 1.0",
                        "Thank you for Using, Visit  For More Info..",
                        icon_path= 'icon/votingicon.ico', threaded=True, callback_on_click=open_url, duration=10
                        )
                

            themeimg=PhotoImage(file='button/set.png')
            theme_appm=Label(setting_root,bd=0,image=themeimg,background='#C9C5C5')
            theme_appm.pack()

            close_app_img=PhotoImage(file='button/exitset.png')
            close_app=Button(setting_root,bd=0,image=close_app_img,cursor='hand2',background='white',activebackground='white',command=set_s)
            close_app.place(x=25,y=25)

            def theme_old():
                root.destroy()
                old_dashboard()
                

          
            theme_app_img=PhotoImage(file='button/change.png')
            theme_app=Button(setting_root,bd=0,image=theme_app_img,cursor='hand2',background='white',activebackground='white',command=theme_old)
            theme_app.place(x=25,y=85)

            themephoto=PhotoImage(file='button/cross.png')
            theme_color=Button(setting_root,bd=0,image=themephoto,cursor='hand2',background='white',activebackground='white',command=lambda:setting_root.destroy())
            theme_color.place(x=30,y=150)

            setting_root.mainloop()     

            
        


        #------------------------------------ Top Nav Area --------------------------------------- #
        #Background Themes
        theme_img=PhotoImage(file='themes/background_theme.png')
        theme=Label(root,image=theme_img)
        theme.pack()

        #Top Nav button------------->

        #About Button
        about_logo=PhotoImage(file='button/about.png')
        about_button=Button(theme,image=about_logo,bd=0,bg='#1A1A1A',activebackground='#1A1A1A',cursor='hand2',command=about)
        about_button.place(x=1350,y=14)

        #feedback.........
        feedback_logo=PhotoImage(file='button/feedback.png')
        feedback_button=Button(theme,image=feedback_logo,bd=0,bg='#1A1A1A',activebackground='#1A1A1A',cursor='hand2',command=feedback)
        feedback_button.place(x=1180,y=14)

        #Admin Button
        admin_logo=PhotoImage(file='button/adminlogin.png')
        admin_button=Button(theme,image=admin_logo,bd=0,bg='#1A1A1A',cursor='hand2',activebackground='#1A1A1A',command=adminlogin_from)
        admin_button.place(x=1005,y=14)
        
        #title img......
        vote_title=Label(theme,text='Online Voting Management System',bd=0,bg='#1A1A1A',fg='white',font=('Regular',24))
        vote_title.place(x=40,y=14)
        
        #------------------------------------ Top Nav End --------------------------------------- #






        #------------------------------------- Main Body End -------------------------------------- #

        #################################### Voting Count Area ######################################
        # l1=Label(theme,height=8,width=20,bg='red')
        # l1.place(x=50,y=120)

        # l2=Label(theme,height=8,width=20,bg='blue')
        # l2.place(x=230,y=120)

        # l3=Label(theme,height=8,width=20,bg='blue')
        # l3.place(x=410,y=120)

        # l3=Label(theme,height=8,width=20,bg='blue')
        # l3.place(x=590,y=120)





        def viewvoter_card():
            viewcardwin=Toplevel()
            viewcardwin.title('View Voter Card')
            viewcardwin.geometry('550x680+485+25')
            viewcardwin.wm_iconbitmap('icon/ind.ico')
            viewcardwin.resizable(False,False)

            entcard=StringVar()
            #send OTP
            def sendcardotp():
                cardn=entcard.get()
                cr.execute('select card_no from registration')
                sc_data=cr.fetchall()
                cfetch=0
                for sc in sc_data:
                    sc1=sc[0]
                    if cardn==sc1:
                        cfetch=1
                        break
                    else:
                        cfetch=0
                if cfetch==1:
                    # print('valid card number')
                    # print(sc1)
                    # print('phone nummber matched')
                    #hide invalid phone number error
                    invalid_card=Label(viewcardwin,text=' ',font=('times new roman',8),fg='red',width=50)
                    invalid_card.place(x=250,y=94)
                    #resend button
                    send_card_otp=Button(viewcardwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                    send_card_otp.place(x=198,y=130)

                    cr.execute(f'select phone from registration where card_no={sc1}')
                    fetchcard_phone=cr.fetchall()
                    for fpp in fetchcard_phone:
                        cpn=fpp[0]
                    # print(cpn)
                    #generate otp.........
                    viewotp=str(random.randint(1111,9999))
                    # print('otp is: ',viewotp)
                    #       
                    '''-------------------TESTING OTP-------------------------'''

                    '''------------------Twillo OTP Service------------------'''
                    # account_sid = 'AC714959399352b0bebabaac962eb62449'
                    # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                    # client = Client(account_sid, auth_token)
                    # too='+91'+cpn
                    # msg='Online Voting System\nYour card verification OTP is: '+viewotp
                    # client.messages.create(body=msg,from_='+19788308309',to=too)

                    '''-------------------------------------------------------'''

                    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                    '''--------------------- Testing Otp ----------------------'''  

                    otpnote_view='Only for Testing Purpose OTP: '+viewotp
                    testing=Label(viewcardwin,text=otpnote_view,font=('Regular',8),fg='red')
                    testing.place(x=5,y=0)
                    #update otp..............
                    cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                    db.commit()
                    # print('changed/update otp')

                    ue_otp=StringVar()
                    def verify_ue_otp():
                        rs_otp=ue_otp.get()
                        cr.execute(f'select otp from registration where phone={cpn}')
                        f_otpdata=cr.fetchall()
                        for dotpp in f_otpdata:
                            ot=dotpp[0]

                        if ot==rs_otp:
                            # print('otp match')
                            Verifyotpp=Button(viewcardwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                            Verifyotpp.place(x=205,y=290)

                            def view():
                                #successfully login  
                                cv=Toplevel()
                                cv.title('View Voter Card')
                                cv.geometry('550x680+485+25')
                                cv.wm_iconbitmap('icon/ind.ico')
                                cv.resizable(False,False)
                                #successfully login  
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''---------------------- Profile Area----------------------'''
                                #bg thems..............
                                vc_p=PhotoImage(file='themes/cardimg.png')
                                vc_l=Label(cv,image=vc_p)
                                vc_l.place(x=70,y=120)

                                fp = io.BytesIO(myphoto)
                                # load the image
                                image = Image.open(fp)
                                res=image.resize((85,100))
                                # drawing image to top window
                                userimg = ImageTk.PhotoImage(res)                      

                                userphoto=Label(cv,image=userimg)
                                userphoto.place(x=125,y=185)
                                #------------------------------------
                                #card no
                                ucard_no=Label(cv,text='Voter ID: ',font=('Regular',8),bg='#44FFDD')
                                ucard_no.place(x=111,y=295)

                                ucard_p=Label(cv,text=cd,font=('Regular',8),bg='#44FFDD')
                                ucard_p.place(x=160,y=295)

                                #>>>>>>>>>>>>>>>>>>>>>>>

                                #name
                                uname=Label(cv,text='Name: ',font=('Regular',8),bg='#44FFDD')
                                uname.place(x=90,y=325)
                                uname_p=Label(cv,text=n,font=('Regular',8),bg='#44FFDD')
                                uname_p.place(x=170,y=325)

                                #father name
                                fname=Label(cv,text='Father Name: ',font=('Regular',8),bg='#44FFDD')
                                fname.place(x=90,y=349)
                                fname_p=Label(cv,text=f,font=('Regular',8),bg='#44FFDD')
                                fname_p.place(x=170,y=349)

                                #gender
                                ugender=Label(cv,text='Gender: ',font=('Regular',8),bg='#44FFDD')
                                ugender.place(x=90,y=373)
                                ugender_p=Label(cv,text=g,font=('Regular',8),bg='#44FFDD')
                                ugender_p.place(x=170,y=373)

                                # #date of birth
                                udob=Label(cv,text='Date Of Birth: ',font=('Regular',8),bg='#44FFDD')
                                udob.place(x=90,y=398)
                                udob_p=Label(cv,text=d,font=('Regular',8),bg='#44FFDD')
                                udob_p.place(x=170,y=398)

                                # #phone no
                                # uphone=Label(cv,text='Phone Number : ',font=('Regular',8),bg='#44FFDD')
                                # uphone.place(x=70,y=370)
                                # uphone_p=Label(cv,text=p,font=('Regular',8),bg='#44FFDD')
                                # uphone_p.place(x=170,y=370)

                                # #aadhaar no
                                # uaadhaar=Label(cv,text='Linked Aadhaar: ',font=('Regular',8),bg='#44FFDD')
                                # uaadhaar.place(x=70,y=400)
                                # uaadhaar_p=Label(cv,text=aah,font=('Regular',8),bg='#44FFDD')
                                # uaadhaar_p.place(x=170,y=400)

                                # uvstatus=Label(cv,text='Voting Status _: ',font=('Regular',8),bg='#44FFDD')
                                # uvstatus.place(x=70,y=430)
                                # uvstatus_p=Label(cv,text=vs,font=('Regular',8),bg='#44FFDD',fg='red')
                                # uvstatus_p.place(x=170,y=430)

                                # #>>>>>>>>>>>>
                                #village
                                uvill=Label(cv,text='Vill: ',font=('Regular',8),bg='#44FFDD')
                                uvill.place(x=300,y=145)
                                uvill_p=Label(cv,text=vill,font=('Regular',8),bg='#44FFDD')
                                uvill_p.place(x=340,y=145)

                                #post
                                upost=Label(cv,text='Post: ',font=('Regular',8),bg='#44FFDD')
                                upost.place(x=300,y=165)
                                upost=Label(cv,text=po,font=('Regular',8),bg='#44FFDD')
                                upost.place(x=340,y=165)

                                #Pin
                                upin=Label(cv,text='Pin : ',font=('Regular',8),bg='#44FFDD')
                                upin.place(x=300,y=187)
                                upin=Label(cv,text=pin,font=('Regular',8),bg='#44FFDD')
                                upin.place(x=340,y=187)

                                #district
                                udist=Label(cv,text='Dist: ',font=('Regular',8),bg='#44FFDD')
                                udist.place(x=300,y=207)
                                udist=Label(cv,text=dist,font=('Regular',8),bg='#44FFDD')
                                udist.place(x=340,y=207)

                                #signature........
                                sign_img=PhotoImage(file='img/sig.png')
                                sig_l=Label(cv,image=sign_img,bg='#44FFDD')
                                sig_l.place(x=355,y=235)
                                cv.mainloop()
                            view()
                            # view_l=Button(viewcardwin,text=' View Card ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=view)
                            # view_l.place(x=205,y=380)
                        else:
                            # print('Please Enter Valid OTP')
                            invalid_OTP=Label(viewcardwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                            invalid_OTP.place(x=134,y=231)

                    #verify otp..........
                    otp_t1=Label(viewcardwin,text='Enter OTP ',font=('Regular',18))
                    otp_t1.place(x=110,y=200)
                    otp_w1=Label(viewcardwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                    otp_w1.place(x=245,y=230)
                    otp_ee=Entry(viewcardwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                    otp_ee.place(x=245,y=200) 

                    Verifyotpp=Button(viewcardwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                    Verifyotpp.place(x=205,y=290)
                else:
                    #print('Phone number not match')
                    invalid_card=Label(viewcardwin,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                    invalid_card.place(x=250,y=90)
            #label of phone number
            card_num=Label(viewcardwin,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
            card_num.place(x=50,y=55)
            #enter phone number
            card_num_e=Entry(viewcardwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
            card_num_e.place(x=250,y=50)

            send_card_otp=Button(viewcardwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
            send_card_otp.place(x=198,y=130)
            viewcardwin.mainloop()



        def download():
            viewcardwin=Toplevel()
            viewcardwin.title('Download Voter Card')
            viewcardwin.geometry('550x680+485+25')
            viewcardwin.wm_iconbitmap('icon/download.ico')
            viewcardwin.resizable(False,False)    

            entcard=StringVar()
            #send OTP
            def sendcardotp():
                cardn=entcard.get()
                cr.execute('select card_no from registration')
                sc_data=cr.fetchall()
                cfetch=0
                for sc in sc_data:
                    sc1=sc[0]
                    if cardn==sc1:
                        cfetch=1
                        break
                    else:
                        cfetch=0
                if cfetch==1:
                    # print('valid card number')
                    # print(sc1)
                    # print('phone nummber matched')
                    #hide invalid phone number error
                    invalid_card=Label(viewcardwin,text=' ',font=('times new roman',8),fg='red',width=50)
                    invalid_card.place(x=250,y=94)
                    #resend button
                    send_card_otp=Button(viewcardwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                    send_card_otp.place(x=198,y=130)

                    cr.execute(f'select phone from registration where card_no={sc1}')
                    fetchcard_phone=cr.fetchall()
                    for fpp in fetchcard_phone:
                        cpn=fpp[0]
                    # print(cpn)
                    #generate otp.........
                    viewotp=str(random.randint(1111,9999))
                    # print('otp is: ',viewotp)
                    #       
                    '''-------------------TESTING OTP-------------------------'''

                    '''------------------Twillo OTP Service------------------'''
                    # account_sid = 'AC714959399352b0bebabaac962eb62449'
                    # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                    # client = Client(account_sid, auth_token)
                    # too='+91'+cpn
                    # msg='Online Voting System\nFor card verification\nyour OTP is: '+viewotp
                    # client.messages.create(body=msg,from_='+19788308309',to=too)

                    '''-------------------------------------------------------'''

                    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                    '''--------------------- Testing Otp ----------------------'''  

                    otpnote_view='Only for Testing Purpose OTP: '+viewotp
                    testing=Label(viewcardwin,text=otpnote_view,font=('Regular',8),fg='red')
                    testing.place(x=5,y=0)

                    #update otp..............
                    cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                    db.commit()
                    # print('changed/update otp')
                    view_l=Button(viewcardwin,text='  ',fg='white',font=('Regular',15),bd=0,cursor='hand2',padx=10,width=70)
                    view_l.place(x=100,y=400)

                    df_d1=Label(viewcardwin,text='  ',fg='white',font=('Regular',11),padx=20,width=100)
                    df_d1.place(x=102,y=520) 

                    df_d=Label(viewcardwin,text='  ',fg='white',font=('Regular',15),padx=20,width=100)
                    df_d.place(x=123,y=480) 

                    ue_otp=StringVar()
                    def verify_ue_otp():
                        rs_otp=ue_otp.get()
                        cr.execute(f'select otp from registration where phone={cpn}')
                        f_otpdata=cr.fetchall()
                        for dotpp in f_otpdata:
                            ot=dotpp[0]

                        if ot==rs_otp:
                            # print('otp match')
                            Verifyotpp=Button(viewcardwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                            Verifyotpp.place(x=205,y=290)

                            def view():
                                #successfully login  
                                cv=Toplevel()
                                cv.title('View Voter Card')
                                cv.geometry('550x680+485+25')
                                cv.wm_iconbitmap('icon/ind.ico')
                                cv.resizable(False,False)
                                #successfully login  
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''---------------------- Profile Area----------------------'''
                                
                                #bg thems..............
                                vc_p=PhotoImage(file='themes/cardimg.png')
                                vc_l=Label(cv,image=vc_p)
                                vc_l.place(x=70,y=120)

                                #////////////////////////////////                        
                                fp = io.BytesIO(myphoto)
                                # load the image
                                image = Image.open(fp)
                                res=image.resize((85,100))
                                # drawing image to top window
                                userimg = ImageTk.PhotoImage(res)                      

                                userphoto=Label(cv,image=userimg)
                                userphoto.place(x=125,y=185)
                                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                #------------------------------------
                                #card no
                                ucard_no=Label(cv,text='Voter ID: ',font=('Regular',8),bg='#44FFDD')
                                ucard_no.place(x=111,y=295)

                                ucard_p=Label(cv,text=cd,font=('Regular',8),bg='#44FFDD')
                                ucard_p.place(x=160,y=295)

                                #>>>>>>>>>>>>>>>>>>>>>>>

                                #name
                                uname=Label(cv,text='Name: ',font=('Regular',8),bg='#44FFDD')
                                uname.place(x=90,y=325)
                                uname_p=Label(cv,text=n,font=('Regular',8),bg='#44FFDD')
                                uname_p.place(x=170,y=325)

                                #father name
                                fname=Label(cv,text='Father Name: ',font=('Regular',8),bg='#44FFDD')
                                fname.place(x=90,y=349)
                                fname_p=Label(cv,text=f,font=('Regular',8),bg='#44FFDD')
                                fname_p.place(x=170,y=349)

                                #gender
                                ugender=Label(cv,text='Gender: ',font=('Regular',8),bg='#44FFDD')
                                ugender.place(x=90,y=373)
                                ugender_p=Label(cv,text=g,font=('Regular',8),bg='#44FFDD')
                                ugender_p.place(x=170,y=373)

                                # #date of birth
                                udob=Label(cv,text='Date Of Birth: ',font=('Regular',8),bg='#44FFDD')
                                udob.place(x=90,y=398)
                                udob_p=Label(cv,text=d,font=('Regular',8),bg='#44FFDD')
                                udob_p.place(x=170,y=398)

                                # #phone no
                                # uphone=Label(cv,text='Phone Number : ',font=('Regular',8),bg='#44FFDD')
                                # uphone.place(x=70,y=370)
                                # uphone_p=Label(cv,text=p,font=('Regular',8),bg='#44FFDD')
                                # uphone_p.place(x=170,y=370)

                                # #aadhaar no
                                # uaadhaar=Label(cv,text='Linked Aadhaar: ',font=('Regular',8),bg='#44FFDD')
                                # uaadhaar.place(x=70,y=400)
                                # uaadhaar_p=Label(cv,text=aah,font=('Regular',8),bg='#44FFDD')
                                # uaadhaar_p.place(x=170,y=400)

                                # uvstatus=Label(cv,text='Voting Status _: ',font=('Regular',8),bg='#44FFDD')
                                # uvstatus.place(x=70,y=430)
                                # uvstatus_p=Label(cv,text=vs,font=('Regular',8),bg='#44FFDD',fg='red')
                                # uvstatus_p.place(x=170,y=430)

                                # #>>>>>>>>>>>>
                                #village
                                uvill=Label(cv,text='Vill: ',font=('Regular',8),bg='#44FFDD')
                                uvill.place(x=300,y=145)
                                uvill_p=Label(cv,text=vill,font=('Regular',8),bg='#44FFDD')
                                uvill_p.place(x=340,y=145)

                                #post
                                upost=Label(cv,text='Post: ',font=('Regular',8),bg='#44FFDD')
                                upost.place(x=300,y=165)
                                upost=Label(cv,text=po,font=('Regular',8),bg='#44FFDD')
                                upost.place(x=340,y=165)

                                #Pin
                                upin=Label(cv,text='Pin : ',font=('Regular',8),bg='#44FFDD')
                                upin.place(x=300,y=187)
                                upin=Label(cv,text=pin,font=('Regular',8),bg='#44FFDD')
                                upin.place(x=340,y=187)

                                #district
                                udist=Label(cv,text='Dist: ',font=('Regular',8),bg='#44FFDD')
                                udist.place(x=300,y=207)
                                udist=Label(cv,text=dist,font=('Regular',8),bg='#44FFDD')
                                udist.place(x=340,y=207)

                                #signature........
                                sign_img=PhotoImage(file='img/sig.png')
                                sig_l=Label(cv,image=sign_img,bg='#44FFDD')
                                sig_l.place(x=355,y=235)
                                cv.mainloop()

                            def createpdf():  
                                df_d1=Label(viewcardwin,text='  ',fg='white',font=('Regular',11),padx=20,width=100)
                                df_d1.place(x=102,y=520) 

                                df_d=Label(viewcardwin,text='  ',fg='white',font=('Regular',15),padx=20,width=100)
                                df_d.place(x=123,y=480) 
                                # Progress bar widget                            
                                progress = ttk.Progressbar(viewcardwin, orient = HORIZONTAL,length = 300, mode = 'determinate')
                                # of the progress bar value
                                def bar():
                                    import time
                                    progress['value'] = 20
                                    root.update_idletasks()
                                    time.sleep(1)
                                    progress['value'] = 60
                                    root.update_idletasks()
                                    time.sleep(1)
                                    progress['value'] = 100  
                                progress.place(x=125,y=480)                            
                                bar()


                                #select data from data base....                        
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''---------------------- Profile Area----------------------'''    
                                #------------------------------------
                                #card no
                                cardnum='Voter ID: '
                                cd #card number
                                carduser_name='Name: '
                                n #holder name
                                father='Father Name: '
                                f #father name
                                gender='Gender: '
                                g #gender
                                dob='Date Of Birth: '
                                d #dob..
                                phone='Phone Number : '
                                p #phone    

                                village='Vill: '
                                vill
                                post='Post'
                                po
                                pn='Pin : '
                                pin
                                dst='Dist: '
                                dist
                                st='State: '
                                state  
                                
                                #step 1
                                def convert_data(data, file_name):     
                                    # Convert binary format to
                                    # images or files data
                                    with open(file_name, 'wb') as file:
                                        file.write(data)
                                    img = Image.open(file_name)
                                    #declear image type global
                                    global image_type
                                    image_type=img.format  
                                    # print(image_type) 
                                img_path=os.getcwd()+'\\temp\\'+cd+'.png'
                                convert_data(myphoto,img_path)
                                tc=image_type.lower()
                                
                                #step 2    
                                if(image_type != 'PNG'):    
                                    os.remove(img_path)
                                    # print('not png')
                                    def convert_data(data, file_name):     
                                        # Convert binary format to
                                        # images or files data
                                        with open(file_name, 'wb') as file:
                                            file.write(data)
                                        img = Image.open(file_name)
                                        #declear image type global
                                        global image_type
                                        image_type=img.format  
                                        # print(image_type) 
                                    img_path=os.getcwd()+'\\temp\\'+cd+'.'+tc
                                    convert_data(myphoto,img_path)


                                pdf=FPDF()
                                pdf.add_page()
                                pdf.image('themes/cardimg.png',x=33,y=20)
                                pdf.image('temp/'+cd+'.'+tc,56,42,25,30)
                                pdf.image('img/sig.png',x=135,y=70)
                                pdf.set_font("Arial",size=10) #set font size 10
                                pdf.set_text_color(0,0,0)
                                #>>>>>>>>>>>>>>>>>> font  <<<<<<<<<<<<<<<<<<<<<<<
                                pdf.text(52,80,txt=cardnum)
                                pdf.text(67,80,txt=cd)

                                pdf.set_font("Arial",size=10) #set font size 8

                                pdf.text(38,90,txt=carduser_name)
                                pdf.text(64,90,txt=n)

                                pdf.text(38,98,txt=father)
                                pdf.text(64,98,txt=f)
                                
                                pdf.text(38,106,txt=gender)
                                pdf.text(64,106,txt=g)

                                pdf.text(38,114,txt=dob)
                                pdf.text(64,114,txt=d)

                                pdf.text(38,122,txt=phone)
                                pdf.text(64,122,txt=p)

                                #>>>>>>>>>>>>>>>>>> Back  <<<<<<<<<<<<<<<<<<<<<<<
                                pdf.text(114,32,txt=village)
                                pdf.text(125,32,txt=vill)

                                pdf.text(114,40,txt=post)
                                pdf.text(125,40,txt=po)

                                pdf.text(114,48,txt=pn)
                                pdf.text(125,48,txt=pin)

                                pdf.text(114,56,txt=dst)
                                pdf.text(125,56,txt=dist)

                                pdf.text(114,64,txt=st)
                                pdf.text(125,64,txt=state)                                         
            
                                path=os.environ['USERPROFILE']
                                savefile=path+'\\'+'OneDrive\Desktop\\'+cd+'.pdf'
                                pdf.output(savefile)

                                #delete temp img
                                os.remove(img_path)
                                
                                showpath='Path: '+savefile
                                df_d1=Label(viewcardwin,text=showpath,fg='red',font=('Regular',11),padx=20)
                                df_d1.place(x=102,y=520) 

                                df_d=Label(viewcardwin,text='File Downloaded On Desktop',fg='white',font=('Regular',15),bg='red',padx=20)
                                df_d.place(x=123,y=480) 

                            down_l=Button(viewcardwin,text='  Download  ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=createpdf)
                            down_l.place(x=120,y=400)

                            view_l=Button(viewcardwin,text=' View Card ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=view)
                            view_l.place(x=300,y=400)    
                        
                            #>>>>>>>>>>>>
                        else:
                            # print('Please Enter Valid OTP')
                            invalid_OTP=Label(viewcardwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                            invalid_OTP.place(x=134,y=231)

                    #verify otp..........
                    otp_t1=Label(viewcardwin,text='Enter OTP ',font=('Regular',18))
                    otp_t1.place(x=110,y=200)
                    otp_w1=Label(viewcardwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                    otp_w1.place(x=245,y=230)
                    otp_ee=Entry(viewcardwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                    otp_ee.place(x=245,y=200) 

                    Verifyotpp=Button(viewcardwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                    Verifyotpp.place(x=205,y=290)
                else:
                    #print('Phone number not match')
                    invalid_card=Label(viewcardwin,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                    invalid_card.place(x=250,y=90)
            #label of phone number
            card_num=Label(viewcardwin,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
            card_num.place(x=50,y=55)
            #enter phone number
            card_num_e=Entry(viewcardwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
            card_num_e.place(x=250,y=50)

            send_card_otp=Button(viewcardwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
            send_card_otp.place(x=198,y=130)


            viewcardwin.mainloop()

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        #################################### User Panel / Area  #######################################

        #button theme...
        button_area_theme=PhotoImage(file='themes/back_theme_vt.png')
        button_area_img=Label(root,image=button_area_theme,bg='#C9C5C5')
        button_area_img.place(x=753,y=75)
        
        #row --------------->  1 
        button_back_color='#C9C5C5'
        button_active_bg_color='#C9C5C5'
        #give vote
        give_img=PhotoImage(file='button/givevote.png')
        give_vote_b=Button(root,image=give_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=givevote_now)
        give_vote_b.place(x=780,y=100)

        #view card
        view_img=PhotoImage(file='button/viewcard.png')
        view_card_b=Button(root,image=view_img,bg=button_back_color,bd=0,activebackground=button_active_bg_color,cursor='hand2',command=viewvoter_card)
        view_card_b.place(x=1032,y=100)

        #track application
        search_img=PhotoImage(file='button/searchstatus.png')
        search_app_status_b=Button(root,image=search_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=trackapplication)
        search_app_status_b.place(x=1280,y=100)


        #row --------------->  2
        #registration
        new_img=PhotoImage(file='button/regc.png')
        new_b=Button(root,image=new_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=RegistrationForm)
        new_b.place(x=780,y=295)
        #download
        download_img=PhotoImage(file='button/download.png')
        download_b=Button(root,image=download_img,bg=button_back_color,bd=0,activebackground=button_active_bg_color,cursor='hand2',command=download)
        download_b.place(x=1032,y=295)
        #update
        update_img=PhotoImage(file='button/update.png')
        update_card_b=Button(root,image=update_img,bg=button_back_color,bd=0,activebackground=button_active_bg_color,cursor='hand2',command=required_to_login)
        update_card_b.place(x=1280,y=295)


        #row --------------->  3
        log_img=PhotoImage(file='button/loginc.png')
        log_b=Button(root,image=log_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=LoginForm)
        log_b.place(x=780,y=488)

        #settingTheme.........
        themephoto_setting=PhotoImage(file='button/setting.png')
        theme_color_setting=Button(root,bd=0,image=themephoto_setting,activebackground=button_active_bg_color,cursor='hand2',background=button_back_color,command=setting)
        theme_color_setting.place(x=1440,y=750)




        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  left side old <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        # #rbjp --------------->  
        # bjp_img=PhotoImage(file='logo/bjp logo.png')
        # bjp_b=Label(root,image=bjp_img ,bg='#C9C5C5')
        # bjp_b.place(x=20,y=121)
        # #count......
        # bjp1_b=Label(root,bg='white',width=60,height=10)
        # bjp1_b.place(x=250,y=123)

        # bjp_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
        # bjp_l1.place(x=300,y=180)
        # #show count
        # bjp_s=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
        # bjp_s.place(x=440,y=180)

        # #percentage
        # tperentage=bjp+cong+tmc
        # cpercentage_bjp=round((bjp/tperentage)*100,2) ,"%"
        # bjp_p=Label(root,text=cpercentage_bjp,font=('Regular',16),bg='white',fg='blue')
        # bjp_p.place(x=560,y=235)


        # #progress
        # for i in range(0,len(cpercentage_bjp)):
        #     bjp_percentage=round(cpercentage_bjp[0])
        #     break
        # # print(type(bjp_percentage))

        # progressbar_bjp=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
        # progressbar_bjp['value']=bjp_percentage
        # progressbar_bjp.place(x=300,y=240)

        # ####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................................................................

        # #tmc..........
        # tmc_img=PhotoImage(file='logo/tmc logo.png')
        # tmc_b=Label(root,image=tmc_img ,bg='#C9C5C5')
        # tmc_b.place(x=16,y=310)
        # #count........
        # tmc1_b=Label(root,bg='white',width=60,height=10)
        # tmc1_b.place(x=250,y=312)

        # tmc_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
        # tmc_l1.place(x=300,y=370)
        # #show count
        # tmc_s=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
        # tmc_s.place(x=440,y=370)
        

        # #percentage
        # cpercentage_tmc=round((tmc/tperentage)*100,2) ,"%"
        # tmc_p=Label(root,text=cpercentage_tmc,font=('Regular',16),bg='white',fg='blue')
        # tmc_p.place(x=560,y=425)

        # #progress
        # for i in range(0,len(cpercentage_tmc)):
        #     tmc_percentage=round(cpercentage_tmc[0])
        #     break
        # # print(type(tmc_percentage))

        # progressbar_tmc=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
        # progressbar_tmc['value']=tmc_percentage
        # progressbar_tmc.place(x=300,y=430)


        # ####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....................................................................



        # #conj......
        # conj_img=PhotoImage(file='logo/cong logo.png')
        # conj_b=Label(root,image=conj_img ,bg='#C9C5C5')
        # conj_b.place(x=20,y=499)
        # #count.....
        # conj_b=Label(root,bg='white',width=60,height=10)
        # conj_b.place(x=250,y=501)

        # conj_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
        # conj_l1.place(x=300,y=560)
        # #show count
        # conj_s=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
        # conj_s.place(x=440,y=560)

        # #percentage
        # cpercentage_cong=round((cong/tperentage)*100,2) ,"%"
        # cong_p=Label(root,text=cpercentage_cong,font=('Regular',16),bg='white',fg='blue')
        # cong_p.place(x=560,y=610)

        # #progress
        # for i in range(0,len(cpercentage_cong)):
        #     cong_percentage=round(cpercentage_cong[0])
        #     break
        # # print(type(cong_percentage))

        # progressbar_cong=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
        # progressbar_cong['value']=cong_percentage
        # progressbar_cong.place(x=300,y=615)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  left side new <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        total_report_bg=PhotoImage(file='logo/total.png')
        total_report=Label(root,image=total_report_bg,bg='#C9C5C5')
        total_report.place(x=28,y=75)

        #vote count....
        bjp_s=Label(root,text=bjp,font=('Regular',20),bg='#BCEAD5',fg='blue')
        bjp_s.place(x=190,y=232)
        tmc_s=Label(root,text=tmc,font=('Regular',20),bg='#BCEAD5',fg='blue')
        tmc_s.place(x=410,y=232)
        conj_s=Label(root,text=cong,font=('Regular',20),bg='#BCEAD5',fg='blue')
        conj_s.place(x=630,y=232)


        #pie chart.....
        figure2=Figure(figsize=(4,4),dpi=100)
        subplot2=figure2.add_subplot(111)

        vot_per=[bjp,tmc,cong]
        party_name=['BJP','TMC','CONGRESS']
        exp=[0,0,0]
        color_pi=['#FF9700','#00FF17','#FBFF00']

        subplot2.pie(vot_per, labels=party_name, explode=exp, autopct='%2.2f%%', colors=color_pi)
        pie2=FigureCanvasTkAgg(figure2,root)
        pie2.get_tk_widget().place(x=150,y=380)

        pr=Label(root,text='Pie Chart Report',font=('Regular',20),bg='white')
        pr.place(x=50,y=370)


        root.mainloop()


    splash_screen.after(0,main_screen3)
    splash_screen.mainloop()




def check_connection3():
    try:
        request.urlopen("https://www.google.com/",timeout=5)
        print('online')
        lunch_first_body3()

    except OSError:
        print('offline')
        def second_body3():
            second_body3=Tk()
            second_body3.geometry('1080x920')
            second_body3.attributes('-fullscreen',True)
            second_body3.config(bg='white')
            my_label = Label(second_body3,bg='white')
            my_label.place(x=160,y=150)
            player = tkvideo("video/107013-loader-for-wi-fi-connection.mp4", my_label, loop = 1, size = (500,500))
            player.play()
            def notconnect3():
                second_body3.destroy()
                ifnot3()
            

            nosig_img=PhotoImage(file='button/nosignal.png')
            nosig_label=Label(second_body3,image=nosig_img,bd=0,bg='white')
            nosig_label.place(x=870,y=235)

            re_img=PhotoImage(file='button/retry.png')
            re_button=Button(second_body3,image=re_img,command=notconnect3,bg='white',activebackground='white',bd=0,cursor='hand2')
            re_button.place(x=1035,y=515)
        
            second_body3.mainloop()
        second_body3()
def ifnot3():
    check_connection3()


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^







#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#----------------------------- @OLD  -------------------------------#

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def old_dashboard():
    def lunch_old_body():
        splash_screen=Tk()
        splash_screen.minsize(600,400)
        splash_screen.state("zoomed")
        splash_screen.resizable(False,False)
        splash_screen.attributes("-fullscreen",True)
        splash_screen.config(bg="white")
        splash_screen.overrideredirect(True)

        sp_img=Image.open("img/v5.png")
        # sp_img=ImageTk.PhotoImage(file="img/v1.jpg")
        resize_img=  ImageTk.PhotoImage(sp_img.resize((500,300)))

        place_img=Label(splash_screen,image=resize_img,bg="white")
        place_img.place(x=500,y=230)

        def main_screen2():
            #close splash screen....
            splash_screen.destroy()

            #Execute Main Body....    
            root=Tk()
            root.title('Online Voting Management System')
            root.geometry('600x600+500+0')
            root.minsize(600,400)
            root.wm_iconbitmap('icon/vote-sign.ico')
            root.resizable(False,False)#maximize option disable
            # root.attributes('-fullscreen',True)
            root.state('zoomed')#default open fullscreen
        


            #-------------------------------------- Main Body ---------------------------------------- #

            '''------------------------------ Count Total Real-Time Vote-------------------------------'''
            cr.execute("select vot_status from registration")
            vt_data=cr.fetchall()
            tmc=0
            bjp=0
            cong=0
            for v_c in vt_data:
                total_v=v_c[0]
                if total_v=='TMC':
                    tmc += 1
                if total_v== 'BJP':
                    bjp +=1
                if total_v== 'Congress':
                    cong +=1

            # print('tmc=',tmc)
            # print('bjp=',bjp)
            # print('conj=',cong)
            '''-----------------------------------------------------------------------------------------'''

            #-----------------------------------<<< About >>>------------------------------------ #
            def about():
                messagebox.showinfo('Details','Develop by ' ' ----> ' ' Amit Mandal\nDevelop by ' ' ----> '  ' Purnendu Mandal\nDevelop by ' ' ----> '  ' Rakesh Hossain\nDevelop by ' ' ----> '  ' Sridam Mandal\n ' ' \nApplication Verson 1.0')

            def feedback():
                feedwin=Toplevel()
                feedwin.title('Feedback or Report')
                feedwin.geometry('550x680+480+25')
                feedwin.wm_iconbitmap('icon/feedback.ico')
                feedwin.resizable(False,False)
                feedwin.config(bg='#D9D9D9')
                feedwin.config(bg='#C9C5C5')
                #aboutwin.attributes('-fullscreen',True)
                try:
                    db=sqlite3.connect('voting management system.db')
                    cr=db.cursor()
                    cr.execute('create table feedback(email text,feedback_receive text)')
                    
                except:
                    print('feedback table is connected')
                    
                

                #send feedback to database............
                feedemail=StringVar()
                def senddata():

                    #define variable
                    feed_email=feedemail.get()
                    feed_data=feed_e.get('1.0','end-1c')

                
                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
                    # Define a function for
                    # for validating an Email   
                    def check(feed_email):
                    
                        # pass the regular expression
                        # and the string into the fullmatch() method
                        if(re.fullmatch(regex, feed_email)):
                            #print("Valid Email")
                            #insert data..........
                            cr.execute('insert into feedback(email,feedback_receive) values(?,?)',(feed_email,feed_data))
                            db.commit()
                            messagebox.showinfo('Feedback','Thank You for Submit Feedback\n we will notify you after review feedback')
                            feedwin.destroy()
                    
                        else:
                            #print("Invalid Email")
                            invalid=Label(feedwin,text='Please Enter Valid E-mail',font=('Regular',10),bg='white',fg='red')
                            invalid.place(x=175,y=210)
                    check(feed_email)  

                


                #bg thems..............
                feedback_img=PhotoImage(file='themes/feedback_b.png')
                feed_l=Label(feedwin,image=feedback_img,bg='#C9C5C5',width=500,height=600)
                feed_l.place(x=25,y=10)

                #emai...........    
                em_img=PhotoImage(file='button/feedem.png')
                feed_l=Label(feedwin,image=em_img,bg='white')
                feed_l.place(x=60,y=166)
                #entry.........
                feed_e=Entry(feedwin,font=('Regular',24),width=18,bd=0,bg='#D4F6CC',textvar=feedemail)
                feed_e.place(x=175,y=169)

                #report........
                report_img=PhotoImage(file='button/feedreport.png')
                report_l=Label(feedwin,image=report_img,bg='white')
                report_l.place(x=60,y=250)
                #entry........
                feed_e=Text(feedwin,font=('Regular',16),height=8,width=36,bd=0,bg='#D4F6CC')
                feed_e.place(x=62,y=280)




                #send button img import
                send_bg=PhotoImage(file='button/fedsend.png')
                send=Button(feedwin,image=send_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=senddata)
                send.place(x=125,y=530)

                #cancel button img import
                can_bg=PhotoImage(file='button/cancel.png')
                login=Button(feedwin,image=can_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:feedwin.destroy())
                login.place(x=290,y=530)

                feedwin.mainloop()




            #--------------------------------<<< Registration Form >>>-------------------------------- #
            def RegistrationForm():
                root.destroy()
                import registration_form
                

            #-----------------------------------<<< Login Form >>>------------------------------------ #
            def LoginForm():
                    
                logwin=Toplevel()
                logwin.title('Login Form')
                logwin.geometry('550x680')#+510+50')
                logwin.wm_iconbitmap('icon/login.ico')
                #logwin.resizable(False,False)
                logwin.config(bg='#D9D9D9')
                logwin.attributes('-fullscreen',True)
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Database Connect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                null=0
                uid=StringVar()
                upass=StringVar()
                def login():
                    userid=uid.get()
                    upassword=upass.get()
                    
                    #userid.................
                    userid_length=len(userid)
                    if null == userid_length:
                        #validation.....
                                
                        validation=Label(logwin,text='Please Enter User ID',font=('Regular',10),fg='red',bg='white')
                        validation.place(x=730,y=280)
                    else:
                        #password..............
                        password_length=len(upassword)
                        if null == password_length:
                            p='Please Enter Password'
                            validation=Label(logwin,text=p,font=('Regular',10),fg='red',bg='white')
                            validation.place(x=730,y=360)
                        else:
                            cr.execute("select phone,password from registration")
                            data=cr.fetchall()
                            check=0
                            for i in data:
                                a=i[0]
                                b=i[1]
                                if userid==a and upassword==b:
                                    check=1
                                    break
                                else:
                                    check=0
                            if check == 1:
                                #successfully login
                                afterloginwin=Toplevel()     
                                afterloginwin.title('My Profile')
                                afterloginwin.geometry('550x680+498+30')
                                afterloginwin.wm_iconbitmap('icon/myprofile.ico')
                                afterloginwin.resizable(False,False)
                                afterloginwin.config(bg='#D9D9D9')                    
                                afterloginwin.overrideredirect(1) 
                                            
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={a}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''--------------------------- Give Vote -------------------------'''
                                def give():
                                    votewin=Toplevel()
                                    votewin.title('Give Vote')
                                    votewin.geometry('550x680+480+25')
                                    votewin.wm_iconbitmap('icon/feedback.ico')
                                    votewin.resizable(False,False)
                                    votewin.config(bg='#D9D9D9')
                                    #votewin.attributes('-fullscreen',True)
                                    votewin.overrideredirect(1)
                                    # db=sqlite3.connect('voting management system.db')
                                    # cr=db.cursor()   
                                    # c='9382370394'

                                    # cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status from registration where phone={c}')
                                    # data=cr.fetchall()
                                    # for i in data:
                                    #     n=i[0]
                                    #     d=i[1]
                                    #     g=i[2]
                                    #     f=i[3]
                                    #     p=i[4]
                                    #     aah=i[5]
                                    #     vill=i[6]
                                    #     po=i[7]
                                    #     pin=i[8]
                                    #     dist=i[9]
                                    #     state=i[10]
                                    #     cd=i[11]
                                    #     vs=i[12]

                                    if cd=='Not Generated':
                                        nota='Sorry Your not Eligible for Vote\n Beacuse your voter number is not gengrated'
                                        #background...
                                        gv_img=PhotoImage(file='themes/voteback.png')
                                        gv_l=Label(votewin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                        gv_l.place(x=30,y=10) 
                                        not_l=Label(votewin,text=nota,font=('Regular',18),bg='white',fg='blue')
                                        not_l.place(x=35,y=200)
                                        #cancel button img import
                                        canc_bg=PhotoImage(file='button/close.png')
                                        canc=Button(votewin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:votewin.destroy())
                                        canc.place(x=225,y=350)
                                    else:
                                        null=0
                                        v1=IntVar()
                                        def give():
                                            v2=v1.get()
                                            if v2==null:
                                                #choose party.......
                                                cpp_l=Label(votewin,text='Please Choose Party',font=('Regular',8),fg='red',bg='white')
                                                cpp_l.place(x=223,y=210)
                                                v3='please choose party'
                                            elif v2==1:
                                                v3='BJP'
                                            elif v2==2:
                                                v3='TMC'
                                            else:
                                                v3='Congress'

                                            if v3=='BJP' or v3=='TMC' or v3=='Congress':
                                                rsotp=StringVar()
                                                
                                                cppp_l=Label(votewin,font=('Regular',10),bg='white',width=30)
                                                cppp_l.place(x=223,y=210)
                                                #resend otp
                                                #resend_bg=PhotoImage(file='button/resend.png')
                                                resend=Button(votewin,text='Resent OTP',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',command=give,padx=10)
                                                resend.place(x=225,y=240)
                                                
                                                '''------------------------------------------------------'''
                                                #generate otp.........
                                                motp=str(random.randint(1111,9999))
                                                #print(motp)
                                                #    
                                                '''-------------------TESTING OTP-------------------------'''

                                                ottp='Only for testing purposr OTP: ' +motp
                                                test_l=Label(votewin,text=ottp,fg='red')
                                                test_l.place(x=50,y=550)

                                                '''------------------Twillo OTP Service------------------'''
                                                # account_sid = 'AC714959399352b0bebabaac962eb62449'
                                                # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                                                # client = Client(account_sid, auth_token)
                                                # too='+91'+p
                                                # msg='Online Voting System\nDo not Share OTP\nyour Give vote OTP is: '+motp
                                                # client.messages.create(body=msg,from_='+19788308309',to=too)

                                                '''-------------------------------------------------------'''            
                                                
                                                cr.execute(f'update registration set otp={motp} where card_no={cd}')
                                                db.commit()
                                                already='Already Voted'
                                                def submitotp():
                                                    reseveotp=rsotp.get()
                                                    cr.execute(f'select voting_status,otp from registration where card_no={cd}')                
                                                    otpdata=cr.fetchall()
                                                    for ot in otpdata:
                                                        vts=ot[0]
                                                        sotp=ot[1]
                                                    
                                                
                                                    if sotp==reseveotp:
                                                        if vts=='Not Voted':
                                                            cr.execute('update registration set voting_status=?,vot_status=? where card_no=?',(already,v3,cd))
                                                            db.commit()

                                                            #Thanks for vote...................
                                                            successwin=Toplevel()
                                                            successwin.title('success full vote')
                                                            successwin.geometry('550x680+480+25')
                                                            successwin.wm_iconbitmap('icon/feedback.ico')
                                                            successwin.resizable(False,False)
                                                            successwin.config(bg='#D9D9D9')
                                                            #successwin.attributes('-fullscreen',True)
                                                            successwin.overrideredirect(1)

                                                            note='Thank You For Give Vote...'
                                                            #background...
                                                            gv_img=PhotoImage(file='themes/voteback.png')
                                                            gv_l=Label(successwin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                                            gv_l.place(x=33,y=10) 

                                                            warning_img=PhotoImage(file='logo/check.png')
                                                            war_l=Label(successwin,image=warning_img,width=200,height=100,bg='white')
                                                            war_l.place(x=180,y=70)

                                                            not_l=Label(successwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                            not_l.place(x=150,y=200)

                                                            
                                                            # Re-fetch Voting count data.......................
                                                            cr.execute("select vot_status from registration")
                                                            vt_data=cr.fetchall()
                                                            tmc=0
                                                            bjp=0
                                                            cong=0
                                                            for v_c in vt_data:
                                                                total_v=v_c[0]
                                                                if total_v=='TMC':
                                                                    tmc += 1
                                                                if total_v== 'BJP':
                                                                    bjp +=1
                                                                if total_v== 'Congress':
                                                                    cong +=1

                                                            #show count Bjp                                    
                                                            bjp_s1=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
                                                            bjp_s1.place(x=440,y=180)
                                                            #show count TMC
                                                            tmc_s1=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
                                                            tmc_s1.place(x=440,y=370)
                                                            #show count CONJ
                                                            conj_s1=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
                                                            conj_s1.place(x=440,y=560)




                                                            def closesuccess():                                                    
                                                                votewin.destroy()
                                                                successwin.destroy()
                                                                
                                                            #cancel button img import
                                                            tgv_bg=PhotoImage(file='button/close.png')
                                                            tgv=Button(successwin,image=tgv_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=closesuccess)
                                                            tgv.place(x=230,y=370)
                                                            successwin.mainloop()
                                                        else:
                                                            #already voted...................
                                                            alwin=Toplevel()
                                                            alwin.title('Already Voted')
                                                            alwin.geometry('550x680+480+25')
                                                            alwin.wm_iconbitmap('icon/feedback.ico')
                                                            alwin.resizable(False,False)
                                                            alwin.config(bg='#D9D9D9')
                                                            #alwin.attributes('-fullscreen',True)
                                                            alwin.overrideredirect(1)

                                                            note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                                                            #background...
                                                            gv_img=PhotoImage(file='themes/voteback.png')
                                                            gv_l=Label(alwin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                                            gv_l.place(x=30,y=10) 

                                                            warning_img=PhotoImage(file='logo/warning.png')
                                                            war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                                                            war_l.place(x=180,y=70)

                                                            not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                            not_l.place(x=85,y=200)
                                                            #cancel button img import
                                                            canc_bg=PhotoImage(file='button/close.png')
                                                            canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                                                            canc.place(x=225,y=370)
                                                            alwin.mainloop()
                                                    else:
                                                        #print('wrong otp')                       
                                                        w_l=Label(votewin,text='Please Enter Valid OTP',bg='White',fg='red',width=50)
                                                        w_l.place(x=130,y=372) 

                                                #otp..........
                                                otp_l=Label(votewin,text='Enter OTP ',font=('Regular',18))
                                                otp_l.place(x=110,y=340)
                                                otp_s=Label(votewin,text='4 Digit OTP Send Your Mobile Number',font=('Regular',8),bg='white')
                                                otp_s.place(x=245,y=370)
                                                otp_e=Entry(votewin,font=('Regular',18),bg='#DFF6FF',width=16,textvar=rsotp)
                                                otp_e.place(x=245,y=340)  
                                                #login button img import
                                                #sub1_img=PhotoImage(file='button/u_login.png')
                                                sub1=Button(votewin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=submitotp)
                                                sub1.place(x=140,y=450)
                                                #cancel button img import
                                                #canc_bg=PhotoImage(file='button/cancel.png')
                                                canc=Button(votewin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:votewin.destroy())
                                                canc.place(x=310,y=450)                                    
                                            else:
                                                print()
                                                #please select party

                                        # stream = io.BytesIO(n)
                                        # img=Image.open(stream)
                                        # img =PhotoImage(img) 
                                        #bg thems..............
                                        gv_img=PhotoImage(file='themes/voteback.png')
                                        gv_l=Label(votewin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                        gv_l.place(x=30,y=10) 

                                        #choose party.......
                                        cp_l=Label(votewin,text='Choose Your Favourite Party',font=('Regular',22),bg='white',fg='blue')
                                        cp_l.place(x=96,y=70)
                                        cp1_e=Radiobutton(votewin,text='BJP',font=('times new roman',18),fg='#FF9F29',bg='white',activebackground='white',value=1,cursor='hand2',variable=v1)
                                        cp1_e.place(x=110,y=150)
                                        cp2_e=Radiobutton(votewin,text='TMC',font=('times new roman',18),fg='green',bg='white',activebackground='white',value=2,cursor='hand2',variable=v1)
                                        cp2_e.place(x=220,y=150)
                                        cp3_e=Radiobutton(votewin,text='Congress',font=('times new roman',18),fg='red',bg='white',activebackground='white',value=3,cursor='hand2',variable=v1)
                                        cp3_e.place(x=340,y=150)
                                        
                                        #give vote button img import
                                        #gvote_bg=PhotoImage(file='button/verify.png')
                                        gvote=Button(votewin,text='✓ Verify ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',command=give,padx=10)
                                        gvote.place(x=225,y=240)
                                    votewin.mainloop()

                                '''---------------------- Profile Area----------------------'''

                                afterlogin_img=PhotoImage(file='themes/afterlogin.png')
                                afterlogin_l=Label(afterloginwin,image=afterlogin_img,bg='#D9D9D9',width=500,height=600)
                                afterlogin_l.place(x=25,y=10)

                                u_img=PhotoImage(file='button/uphoto.png')
                                userphoto=Label(afterloginwin,image=u_img)
                                userphoto.place(x=210,y=50)

                                #////////////////////////////////
                                fp = io.BytesIO(myphoto)
                                # load the image
                                image = Image.open(fp)
                                res=image.resize((114,134))
                                # drawing image to top window
                                userimg = ImageTk.PhotoImage(res)

                                userphoto=Label(afterloginwin,image=userimg)
                                userphoto.place(x=210,y=50)

                                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                #------------------------------------
                                #card no
                                ucard_no=Label(afterloginwin,text='Voter ID: ',font=('Regular',10),bg='white')
                                ucard_no.place(x=200,y=200)

                                ucard_p=Label(afterloginwin,text=cd,font=('Regular',10),bg='white')
                                ucard_p.place(x=260,y=200)
                                
                                #>>>>>>>>>>>>>>>>>>>>>>>

                                #name
                                uname=Label(afterloginwin,text='Name: ',font=('Regular',10),bg='white')
                                uname.place(x=70,y=250)    
                                uname_p=Label(afterloginwin,text=n,font=('Regular',10),bg='white')
                                uname_p.place(x=180,y=250)

                                #father name
                                fname=Label(afterloginwin,text='Father Name: ',font=('Regular',10),bg='white')
                                fname.place(x=70,y=280)
                                fname_p=Label(afterloginwin,text=f,font=('Regular',10),bg='white')
                                fname_p.place(x=180,y=280)

                                #gender
                                ugender=Label(afterloginwin,text='Gender: ',font=('Regular',10),bg='white')
                                ugender.place(x=70,y=310)
                                ugender_p=Label(afterloginwin,text=g,font=('Regular',10),bg='white')
                                ugender_p.place(x=180,y=310)

                                #date of birth
                                udob=Label(afterloginwin,text='Date Of Birth: ',font=('Regular',10),bg='white')
                                udob.place(x=70,y=340)
                                udob_p=Label(afterloginwin,text=d,font=('Regular',10),bg='white')
                                udob_p.place(x=180,y=340)

                                #phone no
                                uphone=Label(afterloginwin,text='Phone Number : ',font=('Regular',10),bg='white')
                                uphone.place(x=70,y=370)
                                uphone_p=Label(afterloginwin,text=p,font=('Regular',10),bg='white')
                                uphone_p.place(x=180,y=370)

                                #aadhaar no
                                uaadhaar=Label(afterloginwin,text='Linked Aadhaar: ',font=('Regular',10),bg='white')
                                uaadhaar.place(x=70,y=400)
                                uaadhaar_p=Label(afterloginwin,text=aah,font=('Regular',10),bg='white')
                                uaadhaar_p.place(x=180,y=400)

                                uvstatus=Label(afterloginwin,text='Voting Status _: ',font=('Regular',10),bg='white')
                                uvstatus.place(x=70,y=430)
                                uvstatus_p=Label(afterloginwin,text=vs,font=('Regular',10),bg='white',fg='red')
                                uvstatus_p.place(x=180,y=430)

                                #>>>>>>>>>>>>
                                #village
                                uvill=Label(afterloginwin,text='Vill: ',font=('Regular',10),bg='white')
                                uvill.place(x=340,y=250)
                                uvill_p=Label(afterloginwin,text=vill,font=('Regular',10),bg='white')
                                uvill_p.place(x=390,y=250)

                                #post
                                upost=Label(afterloginwin,text='Post: ',font=('Regular',10),bg='white')
                                upost.place(x=340,y=280)
                                upost=Label(afterloginwin,text=po,font=('Regular',10),bg='white')
                                upost.place(x=390,y=280)

                                #Pin
                                upin=Label(afterloginwin,text='Pin : ',font=('Regular',10),bg='white')
                                upin.place(x=340,y=310)
                                upin=Label(afterloginwin,text=pin,font=('Regular',10),bg='white')
                                upin.place(x=390,y=310)

                                #district
                                udist=Label(afterloginwin,text='Dist: ',font=('Regular',10),bg='white')
                                udist.place(x=340,y=340)
                                udist=Label(afterloginwin,text=dist,font=('Regular',10),bg='white')
                                udist.place(x=390,y=340)

                                #stste
                                ustate=Label(afterloginwin,text='State: ',font=('Regular',10),bg='white')
                                ustate.place(x=340,y=370)
                                ustate=Label(afterloginwin,text=state,font=('Regular',10),bg='white')
                                ustate.place(x=390,y=370)

                                #button area  >>>>>>>>>>>>>>>>>>>>>>

                                #give vote button img import
                                gvote_bg=PhotoImage(file='button/gvote.png')
                                gvote=Button(afterloginwin,image=gvote_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=give)
                                gvote.place(x=105,y=530)

                                def upd():
                                    lw=Label(afterloginwin,text='Sorry You Can Not Update Any Detaile, It\' Possiable After Upcomming Upgrade',fg='red',bg='white' )
                                    lw.place(x=75,y=495)

                                #Update button
                                upd_bg=PhotoImage(file='button/upd.png')
                                upd=Button(afterloginwin,image=upd_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=upd)
                                upd.place(x=232,y=530)

                                def ulogout():
                                    afterloginwin.destroy()
                                    logwin.destroy()

                                #logout button img import
                                logout_bg=PhotoImage(file='button/ulogout.png')
                                logout=Button(afterloginwin,image=logout_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=ulogout)
                                logout.place(x=360,y=530)

                                afterloginwin.mainloop()
                            else:
                                #cancel button img import
                                Warning_u_p=Label(logwin,text='Wrong User ID or Password',bg='white',fg='red')
                                Warning_u_p.place(x=690,y=180)

                        

                def forgetpass():
                    try:
                        db=sqlite3.connect('voting management system.db')
                        cr=db.cursor()
                    except:
                        print('Forgt db is running...')
                    forgetwin=Toplevel()
                    forgetwin.title('Forget Password')
                    forgetwin.geometry('550x680+485+25')
                    forgetwin.wm_iconbitmap('icon/login.ico')
                    forgetwin.resizable(False,False)
                    entphone=StringVar()
                    #send OTP
                    def sendotpp():
                        fphone_num=entphone.get()
                        cr.execute('select phone from registration')
                        fp_data=cr.fetchall()
                        fcheck=0
                        for ff in fp_data:
                            fp=ff[0]
                            if fphone_num==fp:
                                fcheck=1
                                break
                            else:
                                fcheck=0
                        if fcheck==1:
                            # print('phone nummber matched')
                            #hide invalid phone number error
                            invalid_phone=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                            invalid_phone.place(x=250,y=94)
                            #resend button
                            sendotp=Button(forgetwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                            sendotp.place(x=198,y=130)

                            '''------------------------------------------------------'''
                            #generate otp.........
                            fotp=str(random.randint(1111,9999))
                            #print('otp is: ',fotp)
                            #       
                            '''-------------------TESTING OTP-------------------------'''

                            '''------------------Twillo OTP Service------------------'''
                            # account_sid = 'AC714959399352b0bebabaac962eb62449'
                            # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                            # client = Client(account_sid, auth_token)
                            # too='+91'+fp
                            # msg='Online Voting System\nForget Password OTP: '+fotp
                            # client.messages.create(body=msg,from_='+19788308309',to=too)

                            '''-------------------------------------------------------'''

                            #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
                            '''--------------------- Testing Otp ----------------------'''        
                            otpnote='Only for Testing Purpose OTP: '+fotp
                            testing=Label(forgetwin,text=otpnote,font=('Regular',8),fg='red')
                            testing.place(x=5,y=650)

                            #update otp..............
                            cr.execute('update registration set otp=? where phone=?',(fotp,fp))
                            db.commit()
                            #print('changed otp')

                            rotp=StringVar()
                            def verifyfotp():
                                rsotp=rotp.get()
                                cr.execute(f'select otp from registration where phone={fp}')
                                fetchotp=cr.fetchall()
                                for fe in fetchotp:
                                    dotp=fe[0]

                                #if matched otp............
                                if dotp==rsotp:
                                    #hide invalid otp error
                                    invalid_OTP=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                                    invalid_OTP.place(x=134,y=231)
                                    #verified otp button
                                    Verifyotp=Button(forgetwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                                    Verifyotp.place(x=205,y=290)

                                    pass1=StringVar()
                                    pass2=StringVar()
                                    def changepass():
                                        pass11=pass1.get()
                                        pass22=pass2.get()
                                        if pass11==pass22:
                                            cr.execute('update registration set password=?,conform_password=? where phone=?',(pass11,pass22,fp))
                                            db.commit()
                                            # print('pass changed')  
                                            
                                            #close forgetwindow............
                                            forgetwin.destroy()

                                            changedwin=Toplevel()
                                            changedwin.title('Successfully changed Password')
                                            changedwin.geometry('550x680+485+25')
                                            changedwin.wm_iconbitmap('icon/login.ico')
                                            changedwin.resizable(False,False)
                                            changedwin.overrideredirect()


                                            ch_img=PhotoImage(file='logo/check.png')
                                            ch_l=Label(changedwin,image=ch_img)
                                            ch_l.place(x=215,y=100)

                                            ph_l=Label(changedwin,text='Your Password Successfully changed',font=('times new roman',20),fg='blue')
                                            ph_l.place(x=70,y=230)

                                            changedwin.mainloop()

                                        else:
                                            # print('conform pass not match')
                                            #password not match
                                            invalid_pass=Label(forgetwin,text='Conform Password Not Matched',font=('times new roman',8),fg='red')
                                            invalid_pass.place(x=250,y=462)

                                    #import password image
                                    pass_f=Label(forgetwin,text='New Password',font=('times new roman',18),bg='white')
                                    pass_f.place(x=80,y=380)
                                    #entry password
                                    pass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,textvar=pass1)
                                    pass_fe.place(x=250,y=380)


                                    #import conform password image
                                    con_pass_e=Label(forgetwin,text='Re... Password',font=('times new roman',18),bg='white')
                                    con_pass_e.place(x=80,y=430)
                                    #entry conform password
                                    conpass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,show='*',textvar=pass2)
                                    conpass_fe.place(x=250,y=430)
                                    #login button img import
                                    #sub1_img=PhotoImage(file='button/u_login.png')
                                    sub11=Button(forgetwin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=changepass)
                                    sub11.place(x=145,y=550)
                                    #cancel button img import
                                    #canc_bg=PhotoImage(file='button/cancel.png')
                                    canc1=Button(forgetwin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:forgetwin.destroy())
                                    canc1.place(x=295,y=550)  
                                else:
                                    # print('Please Enter Valid OTP')
                                    invalid_OTP=Label(forgetwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                    invalid_OTP.place(x=134,y=231)



                            #verify otp..........
                            otp_l1=Label(forgetwin,text='Enter OTP ',font=('Regular',18))
                            otp_l1.place(x=110,y=200)
                            otp_s1=Label(forgetwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                            otp_s1.place(x=245,y=230)
                            otp_e1=Entry(forgetwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=rotp)
                            otp_e1.place(x=245,y=200) 

                            Verifyotp=Button(forgetwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                            Verifyotp.place(x=205,y=290)
                        else:
                            #print('Phone number not match')
                            invalid_phone=Label(forgetwin,text='Please Enter Registered Phone Number',font=('times new roman',8),fg='red')
                            invalid_phone.place(x=250,y=90)

                    #label of phone number
                    fphone=Label(forgetwin,text='Phone Number :',font=('times new roman',18,'bold'),fg='black',bd=0)
                    fphone.place(x=50,y=50)
                    #enter phone number
                    fphone_e=Entry(forgetwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entphone)
                    fphone_e.place(x=250,y=50)


                    sendotp=Button(forgetwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                    sendotp.place(x=198,y=130)

                    forgetwin.mainloop()

                #frame bg image import
                fbg=PhotoImage(file='themes/login form.png')
                login_background=Label(logwin,image=fbg,bg='#D9D9D9',width=518,height=654)
                login_background.place(x=510,y=10)

                #uid label img import
                uid_bg=PhotoImage(file='button/uid.png')
                uid_l=Label(logwin,image=uid_bg,bd=0,bg='white')
                uid_l.place(x=565,y=240)

                #uid input       ----*** Entry Box ***----
                uid_e=Entry(logwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',textvar=uid)
                uid_e.place(x=730,y=242)

                #password label img import
                pass_bg=PhotoImage(file='button/password.png')
                password=Label(logwin,image=pass_bg,bd=0,bg='white')
                password.place(x=565,y=320)

                #password input  ----*** Entry Box ***----
                pass_e=Entry(logwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',show='*',textvar=upass)
                pass_e.place(x=730,y=322)


                #login button img import
                log_bg=PhotoImage(file='button/u_login.png')
                login=Button(logwin,image=log_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=login)
                login.place(x=565,y=410)

                #cancel button img import
                cancel_bg=PhotoImage(file='button/cancel.png')
                login=Button(logwin,image=cancel_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:logwin.destroy())
                login.place(x=730,y=410)

                #forget button img import
                #forget_bg=PhotoImage(file='button/forget.png')
                forget=Button(logwin,text='Forget Pasword?',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=forgetpass)
                forget.place(x=570,y=512)

                #slash / button img import
                slash_bg=PhotoImage(file='button/slash.png')
                slash=Button(logwin,image=slash_bg,bd=0,bg='white',activebackground='white')
                slash.place(x=705,y=512)

                #Create new account button img import
                #create_new_ac_bg=PhotoImage(file='button/create_new_ac.png')
                create=Button(logwin,text='Apply For New Candidate',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=RegistrationForm)
                create.place(x=730,y=512)

                logwin.mainloop()


            def givevote_now():
                gv2=Toplevel()
                gv2.title('Give Vote')
                gv2.geometry('550x680+480+25')
                gv2.wm_iconbitmap('icon/vote-sign.ico')
                gv2.resizable(False,False)
                cr=db.cursor()  


                entcard=StringVar()
                def sub_vot_otp():
                    inputcard_no=entcard.get()
                    cr.execute(f'select card_no from registration')
                    data22=cr.fetchall()
                    vnc=0
                    for ii in data22:
                        vn=ii[0]
                        if inputcard_no == vn:
                            vnc=1
                            break
                        else:
                            vnc=0
                    if vnc==1:
                        # print('match')
                        #print('Phone number not match')
                        invalid_card=Label(gv2,text=' ',font=('times new roman',8),fg='red',width=30)
                        invalid_card.place(x=250,y=90)
                        cr.execute(f'select phone,voting_status from registration where card_no={vn}')
                        fvts=cr.fetchall()
                        for jj in fvts:
                            vtphone=jj[0]
                            votingstatus=jj[1]
                        # print(votingstatus)
                        # print(vtphone)
                        if votingstatus=='Not Voted':
                            null=0
                            v1=IntVar()
                            def give():
                                v2=v1.get()
                                if v2==null:
                                    #choose party.......
                                    cpp_l=Label(gv2,text='Please Choose Party',font=('Regular',8),fg='red')
                                    cpp_l.place(x=213,y=310)
                                    v3='please choose party'
                                elif v2==1:
                                    v3='BJP'
                                elif v2==2:
                                    v3='TMC'
                                else:
                                    v3='Congress'

                                if v3=='BJP' or v3=='TMC' or v3=='Congress':
                                    # print(v3)
                                    cpp_l=Label(gv2,text=' ',font=('Regular',8),fg='red',width=30)
                                    cpp_l.place(x=213,y=310)
                                    #gvote_bg=PhotoImage(file='button/verify.png')
                                    gvote=Button(gv2,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=give)
                                    gvote.place(x=210,y=330)                    

                                    '''------------------------------------------------------'''
                                    #generate otp.........
                                    motpp=str(random.randint(1111,9999))
                                    # print(motpp)
                                    #    
                                    '''-------------------TESTING OTP-------------------------'''

                                    ottp='Only for testing purposr OTP: ' +motpp
                                    test_l=Label(gv2,text=ottp,fg='red')
                                    test_l.place(x=10,y=630)

                                    # '''------------------Twillo OTP Service------------------'''
                                    # account_sid = 'AC714959399352b0bebabaac962eb62449'
                                    # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                                    # client = Client(account_sid, auth_token)
                                    # too='+91'+vtphone
                                    # msg='Online Voting System\nyou can give vote\nyour OTP is: '+motpp
                                    # client.messages.create(body=msg,from_='+19788308309',to=too)

                                    '''-------------------------------------------------------'''            

                                    cr.execute(f'update registration set otp={motpp} where card_no={vn}')
                                    db.commit()

                                    rsotp=StringVar()
                                    def urs_otp():
                                        reseveotp=rsotp.get()
                                        cr.execute(f'select voting_status,otp from registration where card_no={vn}')                
                                        otpdata=cr.fetchall()
                                        for ot in otpdata:
                                            vts=ot[0]
                                            sotp=ot[1]
                                        already='Already Voted'
                                        if sotp==reseveotp:
                                            if vts=='Not Voted':
                                                cr.execute('update registration set voting_status=?,vot_status=? where card_no=?',(already,v3,vn))
                                                db.commit()

                                                #Thanks for vote...................
                                                successwin=Toplevel()
                                                successwin.title('success full vote')
                                                successwin.geometry('550x680+487+25')
                                                successwin.wm_iconbitmap('icon/feedback.ico')
                                                successwin.resizable(False,False)
                                                #successwin.attributes('-fullscreen',True)
                                                successwin.overrideredirect(1)

                                                note='Thank You For Give Vote...'
                                                #background...
                                                gv_img=PhotoImage(file='themes/voteback.png')
                                                gv_l=Label(successwin,image=gv_img,width=500,height=600)
                                                gv_l.place(x=33,y=10) 

                                                warning_img=PhotoImage(file='logo/check.png')
                                                war_l=Label(successwin,image=warning_img,width=200,height=100,bg='white')
                                                war_l.place(x=180,y=70)

                                                not_l=Label(successwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                not_l.place(x=150,y=200)

                                                # Re-fetch voting count data.........
                                                
                                                cr.execute("select vot_status from registration")
                                                vt_data=cr.fetchall()
                                                tmc=0
                                                bjp=0
                                                cong=0
                                                for v_c in vt_data:
                                                    total_v=v_c[0]
                                                    if total_v=='TMC':
                                                        tmc += 1
                                                    if total_v== 'BJP':
                                                        bjp +=1
                                                    if total_v== 'Congress':
                                                        cong +=1

                                                #show count Bjp                                    
                                                bjp_s1=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
                                                bjp_s1.place(x=440,y=180)
                                                #show count TMC
                                                tmc_s1=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
                                                tmc_s1.place(x=440,y=370)
                                                #show count CONJ
                                                conj_s1=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
                                                conj_s1.place(x=440,y=560)

                                                #percentage
                                                tperentage=bjp+cong+tmc
                                                cpercentage_bjp=round((bjp/tperentage)*100,2) ,"%"
                                                bjp_p=Label(root,text=cpercentage_bjp,font=('Regular',16),bg='white',fg='blue',width=8)
                                                bjp_p.place(x=560,y=235)
                                                #percentage
                                                cpercentage_tmc=round((tmc/tperentage)*100,2) ,"%"
                                                tmc_p=Label(root,text=cpercentage_tmc,font=('Regular',16),bg='white',fg='blue',width=8)
                                                tmc_p.place(x=560,y=425)
                                                #percentage
                                                cpercentage_cong=round((cong/tperentage)*100,2) ,"%"
                                                cong_p=Label(root,text=cpercentage_cong,font=('Regular',16),bg='white',fg='blue',width=8)
                                                cong_p.place(x=560,y=610)

                                                #progress
                                                for i in range(0,len(cpercentage_bjp)):
                                                    bjp_percentage=round(cpercentage_bjp[0])
                                                    break
                                                # print(type(bjp_percentage))

                                                progressbar_bjp=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                                progressbar_bjp['value']=bjp_percentage
                                                progressbar_bjp.place(x=300,y=240)

                                                #progress
                                                for i in range(0,len(cpercentage_tmc)):
                                                    tmc_percentage=round(cpercentage_tmc[0])
                                                    break
                                                # print(type(tmc_percentage))

                                                progressbar_tmc=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                                progressbar_tmc['value']=tmc_percentage
                                                progressbar_tmc.place(x=300,y=430)

                                                #progress
                                                for i in range(0,len(cpercentage_cong)):
                                                    cong_percentage=round(cpercentage_cong[0])
                                                    break
                                                # print(type(cong_percentage))

                                                progressbar_cong=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                                progressbar_cong['value']=cong_percentage
                                                progressbar_cong.place(x=300,y=615)




                                                def closesuccess():              
                                                    successwin.destroy()
                                                    gv2.destroy()    

                                                #cancel button img import
                                                tgv_bg=PhotoImage(file='button/close.png')
                                                tgv=Button(successwin,image=tgv_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=closesuccess)
                                                tgv.place(x=230,y=370)
                                                successwin.mainloop()
                                            else:
                                                #already voted...................
                                                alwin=Toplevel()
                                                alwin.title('Already Voted')
                                                alwin.geometry('550x680+487+25')
                                                alwin.wm_iconbitmap('icon/feedback.ico')
                                                alwin.resizable(False,False)
                                                #alwin.attributes('-fullscreen',True)
                                                alwin.overrideredirect(1)

                                                note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                                                #background...
                                                gv_img=PhotoImage(file='themes/voteback.png')
                                                gv_l=Label(alwin,image=gv_img,width=500,height=600)
                                                gv_l.place(x=30,y=10) 

                                                warning_img=PhotoImage(file='logo/warning.png')
                                                war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                                                war_l.place(x=180,y=70)

                                                not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                not_l.place(x=85,y=200)
                                                #cancel button img import
                                                canc_bg=PhotoImage(file='button/close.png')
                                                canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                                                canc.place(x=225,y=370)
                                                alwin.mainloop()
                                        else:
                                            #print('wrong otp')                                
                                            w_l=Label(gv2,text='Please Enter Valid OTP',fg='red',width=50)
                                            w_l.place(x=130,y=430)
                                    #otp..........
                                    otp_l=Label(gv2,text='Enter OTP ',font=('Regular',18))
                                    otp_l.place(x=110,y=400)
                                    otp_s=Label(gv2,text='4 Digit OTP Send Your Mobile Number',font=('Regular',8))
                                    otp_s.place(x=245,y=430)
                                    otp_e=Entry(gv2,font=('Regular',18),bg='#DFF6FF',width=16,textvar=rsotp)
                                    otp_e.place(x=245,y=400)  
                                    #login button img import
                                    #sub1_img=PhotoImage(file='button/u_login.png')
                                    sub1=Button(gv2,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=urs_otp)
                                    sub1.place(x=140,y=490)
                                    #cancel button img import
                                    #canc_bg=PhotoImage(file='button/cancel.png')
                                    canc=Button(gv2,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:gv2.destroy())
                                    canc.place(x=310,y=490)                    
                            #choose party.......
                            cp_l=Label(gv2,text='Choose Your Favourite Party',font=('Regular',22),fg='blue')
                            cp_l.place(x=96,y=200)

                            cp1_e=Radiobutton(gv2,text='BJP',font=('times new roman',18),fg='#FF9F29',activebackground='white',value=1,cursor='hand2',variable=v1)
                            cp1_e.place(x=110,y=265)
                            cp2_e=Radiobutton(gv2,text='TMC',font=('times new roman',18),fg='green',activebackground='white',value=2,cursor='hand2',variable=v1)
                            cp2_e.place(x=220,y=265)
                            cp3_e=Radiobutton(gv2,text='Congress',font=('times new roman',18),fg='red',activebackground='white',value=3,cursor='hand2',variable=v1)
                            cp3_e.place(x=340,y=265)

                            #gvote_bg=PhotoImage(file='button/verify.png')
                            gvote=Button(gv2,text='✓ Verify ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=give)
                            gvote.place(x=210,y=330)

                                    
                        else:
                            # print('cant not take vote')
                            #already voted...................
                            alwin=Toplevel()
                            alwin.title('Already Voted')
                            alwin.geometry('550x680+487+25')
                            alwin.wm_iconbitmap('icon/feedback.ico')
                            alwin.resizable(False,False)
                            
                            #alwin.attributes('-fullscreen',True)
                            alwin.overrideredirect(1)

                            note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                            #background...
                            gv_img=PhotoImage(file='themes/voteback.png')
                            gv_l=Label(alwin,image=gv_img,width=500,height=600)
                            gv_l.place(x=30,y=10) 

                            warning_img=PhotoImage(file='logo/warning.png')
                            war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                            war_l.place(x=180,y=70)

                            not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                            not_l.place(x=85,y=200)
                            #cancel button img import
                            canc_bg=PhotoImage(file='button/close.png')
                            canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                            canc.place(x=225,y=370)
                            alwin.mainloop()

                    else:
                        #print('Phone number not match')
                        invalid_card=Label(gv2,text='Please Enter Valid Voter ID',font=('times new roman',8),fg='red')
                        invalid_card.place(x=250,y=90)
                    
                #label of phone number
                card_num=Label(gv2,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
                card_num.place(x=50,y=55)
                #enter phone number
                card_num_e=Entry(gv2,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                card_num_e.place(x=250,y=50)

                send_card_otp=Button(gv2,text=' Submit ', fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sub_vot_otp)
                send_card_otp.place(x=210,y=130)

                gv2.mainloop()





            #required to login......
            def required_to_login():        
                def update_verify():
                    update_verify_win=Toplevel()
                    update_verify_win.title('Update Details')
                    update_verify_win.geometry('550x580+485+95')
                    update_verify_win.wm_iconbitmap('icon/notap.ico')
                    update_verify_win.resizable(False,False)

                    entcard=StringVar()
                    #send OTP
                    def sendcardotp():
                        cardn=entcard.get()
                        cr.execute('select card_no from registration')
                        sc_data=cr.fetchall()
                        cfetch=0
                        for sc in sc_data:
                            sc1=sc[0]
                            if cardn==sc1:
                                cfetch=1
                                break
                            else:
                                cfetch=0
                        if cfetch==1:
                            # print('valid card number')
                            # print(sc1)
                            # print('phone nummber matched')
                            #hide invalid phone number error
                            invalid_card=Label(update_verify_win,text=' ',font=('times new roman',8),fg='red',width=50)
                            invalid_card.place(x=250,y=94)
                            #resend button
                            send_card_otp=Button(update_verify_win,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                            send_card_otp.place(x=198,y=130)

                            cr.execute(f'select phone from registration where card_no={sc1}')
                            fetchcard_phone=cr.fetchall()
                            for fpp in fetchcard_phone:
                                cpn=fpp[0]
                            # print(cpn)
                            #generate otp.........
                            viewotp=str(random.randint(1111,9999))
                            # print('otp is: ',viewotp)
                            #       
                            '''-------------------TESTING OTP-------------------------'''

                            '''------------------Twillo OTP Service------------------'''
                            # account_sid = 'AC714959399352b0bebabaac962eb62449'
                            # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                            # client = Client(account_sid, auth_token)
                            # too='+91'+cpn
                            # msg='Online Voting System\nFor card verification\nyour OTP is: '+viewotp
                            # client.messages.create(body=msg,from_='+19788308309',to=too)

                            '''-------------------------------------------------------'''

                            #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                            '''--------------------- Testing Otp ----------------------'''  

                            otpnote_view='Only for Testing Purpose OTP: '+viewotp
                            testing=Label(update_verify_win,text=otpnote_view,font=('Regular',8),fg='red')
                            testing.place(x=5,y=0)

                            #update otp..............
                            cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                            db.commit()
                            # print('changed/update otp')
                            view_l=Button(update_verify_win,text='  ',fg='white',font=('Regular',15),bd=0,cursor='hand2',padx=10,width=70)
                            view_l.place(x=100,y=400)

                            ue_otp=StringVar()
                            def verify_ue_otp():
                                rs_otp=ue_otp.get()
                                cr.execute(f'select otp from registration where phone={cpn}')
                                f_otpdata=cr.fetchall()
                                for dotpp in f_otpdata:
                                    ot=dotpp[0]

                                if ot==rs_otp:
                                    # print('otp match')
                                    Verifyotpp=Button(update_verify_win,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                                    Verifyotpp.place(x=205,y=290)


                                    def edit():
                                        update_verify_win.destroy()
                                        log_result=messagebox.askyesno('Login Required','You Can\'t Change/Update any Details Now\n It\'s Possiable After UpComming Update\n Our Team Workin On This System for better Upgrad...\n         \nAre You Want To Login Now ?')
                                        if log_result == True:
                                            LoginForm()

                                    updatenow=Button(update_verify_win,text="Click here to Edit Your Details",font=("times new roman",14),bg="blue",fg="white",cursor="hand2", command=edit)
                                    updatenow.place(x=155,y=390)

                                    
                                    







                                    

                                    

                            #verify otp..........
                            otp_t1=Label(update_verify_win,text='Enter OTP ',font=('Regular',18))
                            otp_t1.place(x=110,y=200)
                            otp_w1=Label(update_verify_win,text='OTP Send Your Mobile Number',font=('Regular',8))
                            otp_w1.place(x=245,y=230)
                            otp_ee=Entry(update_verify_win,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                            otp_ee.place(x=245,y=200) 

                            Verifyotpp=Button(update_verify_win,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                            Verifyotpp.place(x=205,y=290)
                        else:
                            #print('Phone number not match')
                            invalid_card=Label(update_verify_win,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                            invalid_card.place(x=250,y=90)
                    #label of phone number
                    card_num=Label(update_verify_win,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
                    card_num.place(x=50,y=55)
                    #enter phone number
                    card_num_e=Entry(update_verify_win,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                    card_num_e.place(x=250,y=50)

                    send_card_otp=Button(update_verify_win,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                    send_card_otp.place(x=198,y=130)

                    update_verify_win.mainloop()



                update_verify()

                
            #Track Application..................................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            def trackapplication():

                trackwin=Toplevel()
                trackwin.geometry('550x680+490+50')
                trackwin.wm_iconbitmap('icon/track.ico')
                trackwin.title('Track Application Status')
                trackwin.resizable(False,False)
                trackwin.config(background='#EAF6F6')
                db=sqlite3.connect('voting management system.db')
                cr=db.cursor()

                tid=StringVar()
                def aptrack():
                    apno=tid.get()
                    #print(apno)
                    cr.execute('select application_no from registration')
                    data=cr.fetchall()
                    db.commit()
                    for i in data:
                        a=i[0]
                        check=0
                        if apno==a:
                            check=1
                            break
                        else:
                            check=0        
                    if check==1:
                        cr.execute(f'select card_no from registration where application_no={a}')
                        card_no=cr.fetchall()
                        for k in card_no:
                            card=k[0]
                        
                        w='You are Voter Id is ' +card            
                        track = Label(trackwin, text=w, font=('Regular', 16), fg='blue',width=45,bg='#EAF6F6')
                        track.place(x=0, y=270)
                    else:
                        track1 = Label(trackwin, text='Please Enter Valid Application No', font=('Regular', 8), fg='red',bg='#EAF6F6')
                        track1.place(x=240, y=135)            


                L2=Label(trackwin,text='Application No :',font=('times new roman',20,'bold'),bg='#EAF6F6',fg='black',bd=0)
                L2.place(x=25,y=100)

                E1=Entry(trackwin,font=('times new roman',20,'bold'),textvar=tid)
                E1.place(x=240,y=100)

                B1_img=PhotoImage(file='button/appsearch.png')    
                B1=Button(trackwin,image=B1_img,bd=0,bg='#EAF6F6',fg='black',command=aptrack,cursor='hand2')
                B1.place(x=200,y=185)


                trackwin.mainloop()

            def adminlogin_from():    
                adlogwin=Toplevel()
                adlogwin.title('Administrator Login')
                adlogwin.geometry('550x670+485+25')
                adlogwin.wm_iconbitmap('icon/admin.ico')
                adlogwin.resizable(False,False)
                #frame bg image import
                fbg=PhotoImage(file='themes/adlog.png')
                login_background=Label(adlogwin,image=fbg,width=518,height=654)
                login_background.place(x=15,y=8)
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Database Connect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                null=0
                uid=StringVar()
                upass=StringVar()
                def adlogin():
                    userid=uid.get()
                    upassword=upass.get()
                        
                    #userid.................
                    userid_length=0
                    userid_length=len(userid)
                    if null == userid_length:
                        #validation.....                 
                        validation=Label(adlogwin,text='Please Enter User ID',font=('Regular',10),fg='red',bg='white')
                        validation.place(x=240,y=270)
                    else:
                        #password..............
                        password_length=len(upassword)
                    if null == password_length:
                        p='Please Enter Password'
                        validation=Label(adlogwin,text=p,font=('Regular',10),fg='red',bg='white')
                        validation.place(x=240,y=360)
                    else:
                        cr.execute("select uid,password from admin")
                        data=cr.fetchall()
                        check=0
                        for i in data:
                            a=i[0]
                            b=i[1]

                            if userid==a and upassword==b:
                                check=1
                                break
                            else:
                                check=0
                        if check == 1:

                            #//////////////////////////////////////<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            # admin login successfull

                            adlogwin.destroy()   

                            adminwin=Toplevel()
                            adminwin.title('Admin Panel')
                            adminwin.geometry('600x600')
                            adminwin.minsize(600,400)
                            adminwin.wm_iconbitmap('icon/admin.ico')
                            adminwin.resizable(False,False)#maximize option disable
                            adminwin.attributes('-fullscreen',True)
                            adminwin.state('zoomed')#default open fullscreen
                            #-------------------------------------- Main Body ---------------------------------------- #
                            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                            #approved candidate
                            s=ttk.Style()
                            s.theme_use('clam')
                            s.configure('Treeview', rowheight=20)

                            tv1=ttk.Treeview(adminwin)
                            tv1['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16')
                            tv1.column('#0',width='0')
                            tv1.column('1',width='40')
                            tv1.column('2',width='150')
                            tv1.column('3',width='60')
                            tv1.column('4',width='50')
                            tv1.column('5',width='150')
                            tv1.column('6',width='70')
                            tv1.column('7',width='80')
                            tv1.column('8',width='100')
                            tv1.column('9',width='100')
                            tv1.column('10',width='50')
                            tv1.column('11',width='80')
                            tv1.column('12',width='80')
                            tv1.column('13',width='60')
                            tv1.column('14',width='88')
                            tv1.column('15',width='85')
                            tv1.column('16',width='80')

                            # name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,Voted by
                            tv1.heading('#0',text='+')
                            tv1.heading('1',text='Sl No')
                            tv1.heading('2',text='Name')
                            tv1.heading('3',text='DOB')
                            tv1.heading('4',text='Gender')
                            tv1.heading('5',text='Father Name')
                            tv1.heading('6',text='Phone No')
                            tv1.heading('7',text='Aadhaar No')
                            tv1.heading('8',text='Village')
                            tv1.heading('9',text='Post')
                            tv1.heading('10',text='Pin')
                            tv1.heading('11',text='District')
                            tv1.heading('12',text='State')
                            tv1.heading('13',text='Application No')
                            tv1.heading('14',text='Card No')
                            tv1.heading('15',text='Voting Status')
                            tv1.heading('16',text='Voted By')

                            def displayAll_1():
                                cr.execute('select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,account_status from registration')
                                adata=cr.fetchall()
                                fdata=0
                                a=0
                                tv1.delete(*tv1.get_children())
                                for i in adata:
                                    f=i[12]
                                    if f!='Not Generated':
                                        fdata += 1
                                        a += 1    
                                        tv1.insert(parent="", index="end", iid=i, text="", values=((a,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14])))
                            displayAll_1()



                            tv1.place(x=90,y=130)

                            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                            # not approve candidate..........

                            tv=ttk.Treeview(adminwin)
                            tv['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16')
                            tv.column('#0',width='0')
                            tv.column('1',width='40')
                            tv.column('2',width='150')
                            tv.column('3',width='60')
                            tv.column('4',width='50')
                            tv.column('5',width='150')
                            tv.column('6',width='70')
                            tv.column('7',width='80')
                            tv.column('8',width='100')
                            tv.column('9',width='100')
                            tv.column('10',width='50')
                            tv.column('11',width='80')
                            tv.column('12',width='80')
                            tv.column('13',width='60')
                            tv.column('14',width='88')
                            tv.column('15',width='85')
                            tv.column('16',width='80')

                            # name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,Voted by
                            tv.heading('#0',text='+')
                            tv.heading('1',text='Sl No')
                            tv.heading('2',text='Name')
                            tv.heading('3',text='DOB')
                            tv.heading('4',text='Gender')
                            tv.heading('5',text='Father Name')
                            tv.heading('6',text='Phone No')
                            tv.heading('7',text='Aadhaar No')
                            tv.heading('8',text='Village')
                            tv.heading('9',text='Post')
                            tv.heading('10',text='Pin')
                            tv.heading('11',text='District')
                            tv.heading('12',text='State')
                            tv.heading('13',text='Application No')
                            tv.heading('14',text='Card No')
                            tv.heading('15',text='Voting Status')
                            tv.heading('16',text='Voted By')

                            def displayAll_2():
                                cr.execute('select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,account_status from registration')
                                adata=cr.fetchall()
                                fdata=0
                                a=0
                                tv.delete(*tv.get_children())
                                for i in adata:
                                    f=i[12]
                                    if f=='Not Generated':
                                        fdata += 1
                                        a += 1    
                                        tv.insert(parent="", index="end", iid=i, text="", values=((a,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14])))
                            displayAll_2()
                            

                            tv.place(x=90,y=420)

                            #>......>>>>>>>>>>>>>>............>>>>>>>>>>>>>>>...................>>>>>>>>>>>>>>>>..............>>>>>>>>>>>>>>>>.
                            topnav=Label(adminwin,text='Welcome to Administrator Panel',font=('times new roman',28),fg='white',bg='blue')
                            topnav.pack(fill=X)

                            candidate=Label(adminwin,text='Approved Candidate Details',font=('times new roman',20),fg='blue')
                            candidate.place(x=90,y=90)

                            exit=Button(adminwin,text='Exit / Logout', font=('times new roman',14),fg='white',bg='#FF8B8B',command=lambda:adminwin.destroy(),cursor='hand2')
                            exit.place(x=1270,y=90)

                            notapcandidate=Label(adminwin,text='Not Approved Candidate Details',font=('times new roman',20),fg='blue')
                            notapcandidate.place(x=90,y=380)

                            def approved():
                                approvewin=Toplevel()
                                approvewin.title('Generate Card Number')
                                approvewin.geometry('550x680+485+25')
                                approvewin.wm_iconbitmap('icon/aprove.ico')
                                approvewin.resizable(False,False)

                                entcard=StringVar()
                                #send OTP
                                def sendcardotp():
                                    ll=0
                                    cardn=entcard.get()
                                    cr.execute('select application_no,card_no from registration')
                                    sc_data=cr.fetchall()
                                    cfetch=0
                                    for sc in sc_data:
                                        sc1=sc[0]
                                        crd=sc[1]
                                        if cardn==sc1:
                                            cfetch=1
                                            break
                                        else:
                                            cfetch=0

                                    if ll != len(cardn):
                                        if cfetch==1:
                                            invalid_phone=Label(approvewin,text='',font=('times new roman',8),width=50)
                                            invalid_phone.place(x=265,y=90)
                                            
                                            if crd=='Not Generated': 
                                        
                                                invalid=Label(approvewin,text='',font=('times new roman',18),fg='red',width=30)
                                                invalid.place(x=135,y=300)

                                                c1=random.randint(1111111111,9999999999)
                                                cr.execute('update registration set card_no=? where application_no=?',(c1,sc1))
                                                db.commit()
                                                approvewin.destroy()
                                                apsuccesswin=Toplevel()    
                                                apsuccesswin.title('Generate Card Number')
                                                apsuccesswin.geometry('550x680+485+25')
                                                apsuccesswin.wm_iconbitmap('icon/aprove.ico')
                                                apsuccesswin.resizable(False,False)            

                                                warning_img=PhotoImage(file='logo/check.png')
                                                war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                                war_l.place(x=165,y=70)

                                                ge=Label(apsuccesswin,text="Successfully Generated Candidate Card Number...",font=('times new roman',14),fg='blue')
                                                ge.place(x=80,y=200) 
                                                displayAll_1()
                                                displayAll_2()                                        
                                                apsuccesswin.mainloop()
                                                entcard.set("")
                                            else:
                                                apsuccesswin=Toplevel()    
                                                apsuccesswin.title('Already Generate Card Number')
                                                apsuccesswin.geometry('550x680+485+25')
                                                apsuccesswin.wm_iconbitmap('icon/notap.ico')
                                                apsuccesswin.resizable(False,False)            
                                                
                                                warning_img=PhotoImage(file='logo/warning.png')
                                                war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                                war_l.place(x=165,y=70)

                                                ge=Label(apsuccesswin,text="Already Generated Card Number...",font=('times new roman',14),fg='blue')
                                                ge.place(x=135,y=200)                                
                                                apsuccesswin.mainloop()

                                        else:
                                            invalid=Label(approvewin,text='Invalid Application Number',font=('times new roman',18),fg='red')
                                            invalid.place(x=135,y=300)
                                    else:
                                        invalid_phone=Label(approvewin,text='Please Enter Valid Application Number',font=('times new roman',8),fg='red')
                                        invalid_phone.place(x=265,y=90)

                                #label of phone number
                                card_num=Label(approvewin,text='Enter Application No: ',font=('times new roman',18,'bold'),fg='black',bd=0)
                                card_num.place(x=30,y=55)
                                #enter phone number
                                card_num_e=Entry(approvewin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                                card_num_e.place(x=265,y=50)

                                send_card_otp=Button(approvewin,text=' Generated ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                                send_card_otp.place(x=205,y=130)
                                approvewin.mainloop()

                            def suspend():
                                approvewin=Toplevel()
                                approvewin.title('Suspend / Delete User')
                                approvewin.geometry('550x680+485+25')
                                approvewin.wm_iconbitmap('icon/suspend.ico')
                                approvewin.resizable(False,False)

                                entcard=StringVar()
                                #send OTP
                                def sendcardotp():
                                    cardn=entcard.get()
                                    l=0                    
                                    if l != len(cardn):
                                        cr.execute('select application_no,card_no,phone from registration')
                                        sc_data=cr.fetchall()
                                        cfetch=0
                                        for sc in sc_data:
                                            sc1=sc[0]
                                            crd=sc[1]
                                            ph=sc[2]
                                            if cardn==sc1 or cardn==crd:
                                                cfetch=1
                                                break
                                            else:
                                                cfetch=0
                        
                                        if cfetch==1:
                                            invalid_phone=Label(approvewin,text=' ',font=('times new roman',8),width=50)
                                            invalid_phone.place(x=265,y=90)

                                            invalid2=Label(approvewin,text=' ',font=('times new roman',18),fg='red',width=50,height=30)
                                            invalid2.place(x=25,y=300)


                                            cr.execute('delete from registration where phone=?',(ph,))
                                            db.commit()

                                            approvewin.destroy()
                                            apsuccesswin=Toplevel()         
                                            apsuccesswin.title('Generate Card Number')
                                            apsuccesswin.geometry('550x680+485+25')
                                            apsuccesswin.wm_iconbitmap('icon/suspend.ico')
                                            apsuccesswin.resizable(False,False)         

                                            warning_img=PhotoImage(file='logo/check.png')
                                            war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                            war_l.place(x=165,y=70)

                                            ge=Label(apsuccesswin,text="Candidate Card Number Permanently Deleted...",font=('times new roman',14),fg='red')
                                            ge.place(x=80,y=200)  
                                            displayAll_1()
                                            displayAll_2()          
                                            apsuccesswin.mainloop()
                                        else:                                
                                            invalid2=Label(approvewin,text='Enter Application / Card Number Already Suspend \nor\n Not Registered Our System',font=('times new roman',18),fg='red')
                                            invalid2.place(x=25,y=300)

                                    else:
                                        invalid_phone=Label(approvewin,text='Enter Valid Application / Card Number',font=('times new roman',8),fg='red')
                                        invalid_phone.place(x=272,y=90)
                                        
                                
                                #label of phone number
                                card_num=Label(approvewin,text='Application / Card No: ',font=('times new roman',18,'bold'),fg='black',bd=0)
                                card_num.place(x=20,y=55)
                                #enter phone number
                                card_num_e=Entry(approvewin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                                card_num_e.place(x=275,y=50)

                                send_card_otp=Button(approvewin,text=' Suspend ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                                send_card_otp.place(x=198,y=130)

                                approvewin.mainloop()



                            approve=Button(adminwin,text=' Generate Card Number', font=('times new roman',14),bg='#00FFDD',cursor='hand2',command=approved)
                            approve.place(x=520,y=700)

                            suspend=Button(adminwin,text='Suspend Candidate', font=('times new roman',14),bg='#FC4F4F',cursor='hand2',command=suspend)
                            suspend.place(x=780,y=700)

                            adminwin.mainloop()

                            #//////////////////////////////////////<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        else:
                            #cancel button img import
                            wp=Label(adlogwin,text='Wrong User ID or Password',bg='white',fg='red')
                            wp.place(x=195,y=180)                


                def forgetadminpass():
                    forgetwin=Toplevel()
                    forgetwin.title('Forget User ID or Password')
                    forgetwin.geometry('550x680+485+25')
                    forgetwin.wm_iconbitmap('icon/admin.ico')
                    forgetwin.resizable(False,False)
                    entphone=StringVar()
                    #send OTP
                    def sendotpp():
                        fphone_num=entphone.get()
                        cr.execute('select phone from admin')
                        fp_data=cr.fetchall()
                        fcheck=0
                        for ff in fp_data:
                            fp=ff[0]
                            if fphone_num==fp:
                                fcheck=1
                                break
                            else:
                                fcheck=0
                        if fcheck==1:
                            # print('phone nummber matched')
                            #hide invalid phone number error
                            invalid_phone=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                            invalid_phone.place(x=250,y=94)
                            #resend button
                            sendotp=Button(forgetwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                            sendotp.place(x=198,y=130)

                            '''------------------------------------------------------'''
                            #generate otp.........
                            fotp=str(random.randint(1111,9999))
                            #print('otp is: ',fotp)
                            #              
                            '''-------------------TESTING OTP-------------------------'''

                            '''------------------Twillo OTP Service------------------'''
                            account_sid = 'AC714959399352b0bebabaac962eb62449'
                            auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                            client = Client(account_sid, auth_token)
                            too='+91'+fp
                            msg='Online Voting System\nForget Admin Password OTP: '+fotp
                            client.messages.create(body=msg,from_='+19788308309',to=too)

                            '''-------------------------------------------------------'''

                            #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
                            '''--------------------- Testing Otp ----------------------'''          
                            otpnote='Only for Testing Purpose OTP: '+fotp
                            testing=Label(forgetwin,text=otpnote,font=('Regular',8),fg='red')
                            testing.place(x=5,y=650)

                            #update otp..............
                            cr.execute('update admin set otp=? where phone=?',(fotp,fp))
                            db.commit()
                            #print('changed otp')

                            rotp=StringVar()
                            def verifyfotp():
                                rsotp=rotp.get()
                                cr.execute(f'select uid,otp from admin where phone={fp}')
                                fetchotp=cr.fetchall()
                                for fe in fetchotp:
                                    ud=fe[0]
                                    dotp=fe[1]

                                #if matched otp............
                                if dotp==rsotp:
                                    #hide invalid otp error
                                    invalid_OTP=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                                    invalid_OTP.place(x=134,y=231)
                                    #verified otp button
                                    Verifyotp=Button(forgetwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                                    Verifyotp.place(x=205,y=290)

                                    pass1=StringVar()
                                    pass2=StringVar()
                                    def changepass():
                                        pass11=pass1.get()
                                        pass22=pass2.get()
                                        if pass11==pass22:
                                            cr.execute('update admin set password=? where phone=?',(pass11,fp))
                                            db.commit()
                                            # print('pass changed')  

                                            #close forgetwindow............
                                            forgetwin.destroy()

                                            changedwin=Toplevel()
                                            changedwin.title('Successfully changed Password')
                                            changedwin.geometry('550x680+485+25')
                                            changedwin.wm_iconbitmap('icon/login.ico')
                                            changedwin.resizable(False,False)
                                            changedwin.overrideredirect()


                                            ch_img=PhotoImage(file='logo/check.png')
                                            ch_l=Label(changedwin,image=ch_img)
                                            ch_l.place(x=215,y=100)

                                            ph_l=Label(changedwin,text='Your Password Successfully changed',font=('times new roman',20),fg='blue')
                                            ph_l.place(x=70,y=230)

                                            changedwin.mainloop()

                                        else:
                                            # print('conform pass not match')
                                            #password not match
                                            invalid_pass=Label(forgetwin,text='Conform Password Not Matched',font=('times new roman',8),fg='red')
                                            invalid_pass.place(x=250,y=462)

                                    #import password image
                                    pass_f=Label(forgetwin,text='New Password',font=('times new roman',18),bg='white')
                                    pass_f.place(x=80,y=400)
                                    #entry password
                                    pass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,textvar=pass1)
                                    pass_fe.place(x=250,y=400)
                                    #import conform password image
                                    con_pass_e=Label(forgetwin,text='Re... Password',font=('times new roman',18),bg='white')
                                    con_pass_e.place(x=80,y=450)
                                    #entry conform password
                                    conpass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,show='*',textvar=pass2)
                                    conpass_fe.place(x=250,y=450)

                                    #import uid
                                    uuid='Your User ID: '+ud
                                    puid_f=Label(forgetwin,text=uuid,font=('times new roman',14),fg='red')
                                    puid_f.place(x=180,y=345)


                                    #login button img import
                                    #sub1_img=PhotoImage(file='button/u_login.png')
                                    sub11=Button(forgetwin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=changepass)
                                    sub11.place(x=145,y=550)
                                    #cancel button img import
                                    #canc_bg=PhotoImage(file='button/cancel.png')
                                    canc1=Button(forgetwin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:forgetwin.destroy())
                                    canc1.place(x=295,y=550)  
                                else:
                                    # print('Please Enter Valid OTP')
                                    invalid_OTP=Label(forgetwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                    invalid_OTP.place(x=134,y=231)



                            #verify otp..........
                            otp_l1=Label(forgetwin,text='Enter OTP ',font=('Regular',18))
                            otp_l1.place(x=110,y=200)
                            otp_s1=Label(forgetwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                            otp_s1.place(x=245,y=230)
                            otp_e1=Entry(forgetwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=rotp)
                            otp_e1.place(x=245,y=200) 

                            Verifyotp=Button(forgetwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                            Verifyotp.place(x=205,y=290)
                        else:
                            #print('Phone number not match')
                            invalid_phone=Label(forgetwin,text='Please Enter Registered Phone Number',font=('times new roman',8),fg='red')
                            invalid_phone.place(x=250,y=90)

                    #label of phone number
                    fphone=Label(forgetwin,text='Phone Number :',font=('times new roman',18,'bold'),fg='black',bd=0)
                    fphone.place(x=50,y=50)
                    #enter phone number
                    fphone_e=Entry(forgetwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entphone)
                    fphone_e.place(x=250,y=50)


                    sendotp=Button(forgetwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                    sendotp.place(x=198,y=130)

                    forgetwin.mainloop()



                #uid label img import
                uid_bg=PhotoImage(file='button/uid.png')
                uid_l=Label(adlogwin,image=uid_bg,bd=0,bg='white')
                uid_l.place(x=70,y=230)

                #uid input   ----*** Entry Box ***----
                uid_e=Entry(adlogwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',textvar=uid)
                uid_e.place(x=240,y=232)

                #password label img import
                pass_bg=PhotoImage(file='button/password.png')
                password=Label(adlogwin,image=pass_bg,bd=0,bg='white')
                password.place(x=70,y=310)

                #password input  ----*** Entry Box ***----
                pass_e=Entry(adlogwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',show='*',textvar=upass)
                pass_e.place(x=240,y=312)


                #login button img import
                log_bg=PhotoImage(file='button/login.png')
                login=Button(adlogwin,image=log_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=adlogin)
                login.place(x=70,y=410)

                #cancel button img import
                cancel_bg=PhotoImage(file='button/cancel.png')
                cancel=Button(adlogwin,image=cancel_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:adlogwin.destroy())
                cancel.place(x=240,y=410)

                #forget button img import
                #forget_bg=PhotoImage(file='button/forget.png')
                forget=Button(adlogwin,text='Forget User ID or Pasword?',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=forgetadminpass)
                forget.place(x=75,y=480)

                adlogwin.mainloop()

            #screen-2
            def setting():
                root.destroy()
                #check_connection()
                check_connection3()
            


            #------------------------------------ Top Nav Area --------------------------------------- #
            #Background Themes
            theme_img=PhotoImage(file='themes/background_theme.png')
            theme=Label(root,image=theme_img)
            theme.pack()

            #Top Nav button------------->

            #About Button
            about_logo=PhotoImage(file='button/about.png')
            about_button=Button(theme,image=about_logo,bd=0,bg='#1A1A1A',activebackground='#1A1A1A',cursor='hand2',command=about)
            about_button.place(x=1350,y=14)

            #feedback.........
            feedback_logo=PhotoImage(file='button/feedback.png')
            feedback_button=Button(theme,image=feedback_logo,bd=0,bg='#1A1A1A',activebackground='#1A1A1A',cursor='hand2',command=feedback)
            feedback_button.place(x=1180,y=14)

            #Admin Button
            admin_logo=PhotoImage(file='button/adminlogin.png')
            admin_button=Button(theme,image=admin_logo,bd=0,bg='#1A1A1A',cursor='hand2',activebackground='#1A1A1A',command=adminlogin_from)
            admin_button.place(x=1005,y=14)

            def system_update():
                progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 1533, mode = 'determinate')
                # of the progress bar value
                def bar():
                    import time
                    progress['value'] = 20
                    root.update_idletasks()
                    time.sleep(1)
                    progress['value'] = 40
                    root.update_idletasks()
                    time.sleep(1)
                    progress['value'] = 50 
                    root.update_idletasks()
                    time.sleep(1)
                    progress['value'] = 60
                    root.update_idletasks()
                    time.sleep(1)
                    progress['value'] = 80
                    root.update_idletasks()
                    time.sleep(1)
                    progress['value'] = 100 
                    root.update_idletasks()
                    time.sleep(1)
                    messagebox.showinfo('Update','New Update Not Available..\nSystem is Already Upgrade v2.0 \nSwitch now v2.0 if you interest..')
                progress.place(x=0,y=818)                            
                bar()
                progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 1533, mode = 'determinate')
                progress.place(x=0,y=818)            
            app_upimg=PhotoImage(file='button/systemupdate.png')
            app_up_img=Button(theme,bd=0,image=app_upimg,cursor='hand2',background='#C9C5C5',activebackground='#C9C5C5',command=system_update)
            app_up_img.place(x=1440,y=750)
            app_up=Label(theme,text='Update',background='#C9C5C5')
            app_up.place(x=1440,y=790)

            #Theme.........
            themephoto12=PhotoImage(file='button/change.png')
            theme_color112=Button(theme,bd=0,image=themephoto12,cursor='hand2',background='#C9C5C5',activebackground='#C9C5C5',command=setting)
            theme_color112.place(x=1360,y=750)
           

            theme_color1122=Label(theme,text='Switch V2.0',background='#C9C5C5')
            theme_color1122.place(x=1350,y=790)

            #------------------------------------ Top Nav End --------------------------------------- #






            #------------------------------------- Main Body End -------------------------------------- #

            #################################### Voting Count Area ######################################
            # l1=Label(theme,height=8,width=20,bg='red')
            # l1.place(x=50,y=120)

            # l2=Label(theme,height=8,width=20,bg='blue')
            # l2.place(x=230,y=120)

            # l3=Label(theme,height=8,width=20,bg='blue')
            # l3.place(x=410,y=120)

            # l3=Label(theme,height=8,width=20,bg='blue')
            # l3.place(x=590,y=120)





            def viewvoter_card():
                viewcardwin=Toplevel()
                viewcardwin.title('View Voter Card')
                viewcardwin.geometry('550x680+485+25')
                viewcardwin.wm_iconbitmap('icon/ind.ico')
                viewcardwin.resizable(False,False)

                entcard=StringVar()
                #send OTP
                def sendcardotp():
                    cardn=entcard.get()
                    cr.execute('select card_no from registration')
                    sc_data=cr.fetchall()
                    cfetch=0
                    for sc in sc_data:
                        sc1=sc[0]
                        if cardn==sc1:
                            cfetch=1
                            break
                        else:
                            cfetch=0
                    if cfetch==1:
                        # print('valid card number')
                        # print(sc1)
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_card=Label(viewcardwin,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_card.place(x=250,y=94)
                        #resend button
                        send_card_otp=Button(viewcardwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                        send_card_otp.place(x=198,y=130)

                        cr.execute(f'select phone from registration where card_no={sc1}')
                        fetchcard_phone=cr.fetchall()
                        for fpp in fetchcard_phone:
                            cpn=fpp[0]
                        # print(cpn)
                        #generate otp.........
                        viewotp=str(random.randint(1111,9999))
                        # print('otp is: ',viewotp)
                        #       
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        # account_sid = 'AC714959399352b0bebabaac962eb62449'
                        # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        # client = Client(account_sid, auth_token)
                        # too='+91'+cpn
                        # msg='Online Voting System\nYour card verification OTP is: '+viewotp
                        # client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                        '''--------------------- Testing Otp ----------------------'''  

                        otpnote_view='Only for Testing Purpose OTP: '+viewotp
                        testing=Label(viewcardwin,text=otpnote_view,font=('Regular',8),fg='red')
                        testing.place(x=5,y=0)
                        #update otp..............
                        cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                        db.commit()
                        # print('changed/update otp')

                        ue_otp=StringVar()
                        def verify_ue_otp():
                            rs_otp=ue_otp.get()
                            cr.execute(f'select otp from registration where phone={cpn}')
                            f_otpdata=cr.fetchall()
                            for dotpp in f_otpdata:
                                ot=dotpp[0]

                            if ot==rs_otp:
                                # print('otp match')
                                Verifyotpp=Button(viewcardwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                                Verifyotpp.place(x=205,y=290)

                                def view():
                                    #successfully login  
                                    cv=Toplevel()
                                    cv.title('View Voter Card')
                                    cv.geometry('550x680+485+25')
                                    cv.wm_iconbitmap('icon/ind.ico')
                                    cv.resizable(False,False)
                                    #successfully login  
                                    cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                    data=cr.fetchall()
                                    for i in data:
                                        n=i[0]
                                        d=i[1]
                                        g=i[2]
                                        f=i[3]
                                        p=i[4]
                                        aah=i[5]
                                        vill=i[6]
                                        po=i[7]
                                        pin=i[8]
                                        dist=i[9]
                                        state=i[10]
                                        cd=i[11]
                                        vs=i[12]
                                        myphoto=i[13]

                                    '''---------------------- Profile Area----------------------'''
                                    #bg thems..............
                                    vc_p=PhotoImage(file='themes/cardimg.png')
                                    vc_l=Label(cv,image=vc_p)
                                    vc_l.place(x=70,y=120)

                                    fp = io.BytesIO(myphoto)
                                    # load the image
                                    image = Image.open(fp)
                                    res=image.resize((85,100))
                                    # drawing image to top window
                                    userimg = ImageTk.PhotoImage(res)                      

                                    userphoto=Label(cv,image=userimg)
                                    userphoto.place(x=125,y=185)
                                    #------------------------------------
                                    #card no
                                    ucard_no=Label(cv,text='Voter ID: ',font=('Regular',8),bg='#44FFDD')
                                    ucard_no.place(x=111,y=295)

                                    ucard_p=Label(cv,text=cd,font=('Regular',8),bg='#44FFDD')
                                    ucard_p.place(x=160,y=295)

                                    #>>>>>>>>>>>>>>>>>>>>>>>

                                    #name
                                    uname=Label(cv,text='Name: ',font=('Regular',8),bg='#44FFDD')
                                    uname.place(x=90,y=325)
                                    uname_p=Label(cv,text=n,font=('Regular',8),bg='#44FFDD')
                                    uname_p.place(x=170,y=325)

                                    #father name
                                    fname=Label(cv,text='Father Name: ',font=('Regular',8),bg='#44FFDD')
                                    fname.place(x=90,y=349)
                                    fname_p=Label(cv,text=f,font=('Regular',8),bg='#44FFDD')
                                    fname_p.place(x=170,y=349)

                                    #gender
                                    ugender=Label(cv,text='Gender: ',font=('Regular',8),bg='#44FFDD')
                                    ugender.place(x=90,y=373)
                                    ugender_p=Label(cv,text=g,font=('Regular',8),bg='#44FFDD')
                                    ugender_p.place(x=170,y=373)

                                    # #date of birth
                                    udob=Label(cv,text='Date Of Birth: ',font=('Regular',8),bg='#44FFDD')
                                    udob.place(x=90,y=398)
                                    udob_p=Label(cv,text=d,font=('Regular',8),bg='#44FFDD')
                                    udob_p.place(x=170,y=398)

                                    # #phone no
                                    # uphone=Label(cv,text='Phone Number : ',font=('Regular',8),bg='#44FFDD')
                                    # uphone.place(x=70,y=370)
                                    # uphone_p=Label(cv,text=p,font=('Regular',8),bg='#44FFDD')
                                    # uphone_p.place(x=170,y=370)

                                    # #aadhaar no
                                    # uaadhaar=Label(cv,text='Linked Aadhaar: ',font=('Regular',8),bg='#44FFDD')
                                    # uaadhaar.place(x=70,y=400)
                                    # uaadhaar_p=Label(cv,text=aah,font=('Regular',8),bg='#44FFDD')
                                    # uaadhaar_p.place(x=170,y=400)

                                    # uvstatus=Label(cv,text='Voting Status _: ',font=('Regular',8),bg='#44FFDD')
                                    # uvstatus.place(x=70,y=430)
                                    # uvstatus_p=Label(cv,text=vs,font=('Regular',8),bg='#44FFDD',fg='red')
                                    # uvstatus_p.place(x=170,y=430)

                                    # #>>>>>>>>>>>>
                                    #village
                                    uvill=Label(cv,text='Vill: ',font=('Regular',8),bg='#44FFDD')
                                    uvill.place(x=300,y=145)
                                    uvill_p=Label(cv,text=vill,font=('Regular',8),bg='#44FFDD')
                                    uvill_p.place(x=340,y=145)

                                    #post
                                    upost=Label(cv,text='Post: ',font=('Regular',8),bg='#44FFDD')
                                    upost.place(x=300,y=165)
                                    upost=Label(cv,text=po,font=('Regular',8),bg='#44FFDD')
                                    upost.place(x=340,y=165)

                                    #Pin
                                    upin=Label(cv,text='Pin : ',font=('Regular',8),bg='#44FFDD')
                                    upin.place(x=300,y=187)
                                    upin=Label(cv,text=pin,font=('Regular',8),bg='#44FFDD')
                                    upin.place(x=340,y=187)

                                    #district
                                    udist=Label(cv,text='Dist: ',font=('Regular',8),bg='#44FFDD')
                                    udist.place(x=300,y=207)
                                    udist=Label(cv,text=dist,font=('Regular',8),bg='#44FFDD')
                                    udist.place(x=340,y=207)

                                    #signature........
                                    sign_img=PhotoImage(file='img/sig.png')
                                    sig_l=Label(cv,image=sign_img,bg='#44FFDD')
                                    sig_l.place(x=355,y=235)
                                    cv.mainloop()
                                view()
                                # view_l=Button(viewcardwin,text=' View Card ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=view)
                                # view_l.place(x=205,y=380)
                            else:
                                # print('Please Enter Valid OTP')
                                invalid_OTP=Label(viewcardwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)

                        #verify otp..........
                        otp_t1=Label(viewcardwin,text='Enter OTP ',font=('Regular',18))
                        otp_t1.place(x=110,y=200)
                        otp_w1=Label(viewcardwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_w1.place(x=245,y=230)
                        otp_ee=Entry(viewcardwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                        otp_ee.place(x=245,y=200) 

                        Verifyotpp=Button(viewcardwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                        Verifyotpp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_card=Label(viewcardwin,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                        invalid_card.place(x=250,y=90)
                #label of phone number
                card_num=Label(viewcardwin,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
                card_num.place(x=50,y=55)
                #enter phone number
                card_num_e=Entry(viewcardwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                card_num_e.place(x=250,y=50)

                send_card_otp=Button(viewcardwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                send_card_otp.place(x=198,y=130)
                viewcardwin.mainloop()



            def download():
                viewcardwin=Toplevel()
                viewcardwin.title('Download Voter Card')
                viewcardwin.geometry('550x680+485+25')
                viewcardwin.wm_iconbitmap('icon/download.ico')
                viewcardwin.resizable(False,False)    

                entcard=StringVar()
                #send OTP
                def sendcardotp():
                    cardn=entcard.get()
                    cr.execute('select card_no from registration')
                    sc_data=cr.fetchall()
                    cfetch=0
                    for sc in sc_data:
                        sc1=sc[0]
                        if cardn==sc1:
                            cfetch=1
                            break
                        else:
                            cfetch=0
                    if cfetch==1:
                        # print('valid card number')
                        # print(sc1)
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_card=Label(viewcardwin,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_card.place(x=250,y=94)
                        #resend button
                        send_card_otp=Button(viewcardwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                        send_card_otp.place(x=198,y=130)

                        cr.execute(f'select phone from registration where card_no={sc1}')
                        fetchcard_phone=cr.fetchall()
                        for fpp in fetchcard_phone:
                            cpn=fpp[0]
                        # print(cpn)
                        #generate otp.........
                        viewotp=str(random.randint(1111,9999))
                        # print('otp is: ',viewotp)
                        #       
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        # account_sid = 'AC714959399352b0bebabaac962eb62449'
                        # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        # client = Client(account_sid, auth_token)
                        # too='+91'+cpn
                        # msg='Online Voting System\nFor card verification\nyour OTP is: '+viewotp
                        # client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                        '''--------------------- Testing Otp ----------------------'''  

                        otpnote_view='Only for Testing Purpose OTP: '+viewotp
                        testing=Label(viewcardwin,text=otpnote_view,font=('Regular',8),fg='red')
                        testing.place(x=5,y=0)

                        #update otp..............
                        cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                        db.commit()
                        # print('changed/update otp')
                        view_l=Button(viewcardwin,text='  ',fg='white',font=('Regular',15),bd=0,cursor='hand2',padx=10,width=70)
                        view_l.place(x=100,y=400)

                        df_d1=Label(viewcardwin,text='  ',fg='white',font=('Regular',11),padx=20,width=100)
                        df_d1.place(x=102,y=520) 

                        df_d=Label(viewcardwin,text='  ',fg='white',font=('Regular',15),padx=20,width=100)
                        df_d.place(x=123,y=480) 

                        ue_otp=StringVar()
                        def verify_ue_otp():
                            rs_otp=ue_otp.get()
                            cr.execute(f'select otp from registration where phone={cpn}')
                            f_otpdata=cr.fetchall()
                            for dotpp in f_otpdata:
                                ot=dotpp[0]

                            if ot==rs_otp:
                                # print('otp match')
                                Verifyotpp=Button(viewcardwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                                Verifyotpp.place(x=205,y=290)

                                def view():
                                    #successfully login  
                                    cv=Toplevel()
                                    cv.title('View Voter Card')
                                    cv.geometry('550x680+485+25')
                                    cv.wm_iconbitmap('icon/ind.ico')
                                    cv.resizable(False,False)
                                    #successfully login  
                                    cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                    data=cr.fetchall()
                                    for i in data:
                                        n=i[0]
                                        d=i[1]
                                        g=i[2]
                                        f=i[3]
                                        p=i[4]
                                        aah=i[5]
                                        vill=i[6]
                                        po=i[7]
                                        pin=i[8]
                                        dist=i[9]
                                        state=i[10]
                                        cd=i[11]
                                        vs=i[12]
                                        myphoto=i[13]

                                    '''---------------------- Profile Area----------------------'''
                                    
                                    #bg thems..............
                                    vc_p=PhotoImage(file='themes/cardimg.png')
                                    vc_l=Label(cv,image=vc_p)
                                    vc_l.place(x=70,y=120)

                                    #////////////////////////////////                        
                                    fp = io.BytesIO(myphoto)
                                    # load the image
                                    image = Image.open(fp)
                                    res=image.resize((85,100))
                                    # drawing image to top window
                                    userimg = ImageTk.PhotoImage(res)                      

                                    userphoto=Label(cv,image=userimg)
                                    userphoto.place(x=125,y=185)
                                    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                    #------------------------------------
                                    #card no
                                    ucard_no=Label(cv,text='Voter ID: ',font=('Regular',8),bg='#44FFDD')
                                    ucard_no.place(x=111,y=295)

                                    ucard_p=Label(cv,text=cd,font=('Regular',8),bg='#44FFDD')
                                    ucard_p.place(x=160,y=295)

                                    #>>>>>>>>>>>>>>>>>>>>>>>

                                    #name
                                    uname=Label(cv,text='Name: ',font=('Regular',8),bg='#44FFDD')
                                    uname.place(x=90,y=325)
                                    uname_p=Label(cv,text=n,font=('Regular',8),bg='#44FFDD')
                                    uname_p.place(x=170,y=325)

                                    #father name
                                    fname=Label(cv,text='Father Name: ',font=('Regular',8),bg='#44FFDD')
                                    fname.place(x=90,y=349)
                                    fname_p=Label(cv,text=f,font=('Regular',8),bg='#44FFDD')
                                    fname_p.place(x=170,y=349)

                                    #gender
                                    ugender=Label(cv,text='Gender: ',font=('Regular',8),bg='#44FFDD')
                                    ugender.place(x=90,y=373)
                                    ugender_p=Label(cv,text=g,font=('Regular',8),bg='#44FFDD')
                                    ugender_p.place(x=170,y=373)

                                    # #date of birth
                                    udob=Label(cv,text='Date Of Birth: ',font=('Regular',8),bg='#44FFDD')
                                    udob.place(x=90,y=398)
                                    udob_p=Label(cv,text=d,font=('Regular',8),bg='#44FFDD')
                                    udob_p.place(x=170,y=398)

                                    # #phone no
                                    # uphone=Label(cv,text='Phone Number : ',font=('Regular',8),bg='#44FFDD')
                                    # uphone.place(x=70,y=370)
                                    # uphone_p=Label(cv,text=p,font=('Regular',8),bg='#44FFDD')
                                    # uphone_p.place(x=170,y=370)

                                    # #aadhaar no
                                    # uaadhaar=Label(cv,text='Linked Aadhaar: ',font=('Regular',8),bg='#44FFDD')
                                    # uaadhaar.place(x=70,y=400)
                                    # uaadhaar_p=Label(cv,text=aah,font=('Regular',8),bg='#44FFDD')
                                    # uaadhaar_p.place(x=170,y=400)

                                    # uvstatus=Label(cv,text='Voting Status _: ',font=('Regular',8),bg='#44FFDD')
                                    # uvstatus.place(x=70,y=430)
                                    # uvstatus_p=Label(cv,text=vs,font=('Regular',8),bg='#44FFDD',fg='red')
                                    # uvstatus_p.place(x=170,y=430)

                                    # #>>>>>>>>>>>>
                                    #village
                                    uvill=Label(cv,text='Vill: ',font=('Regular',8),bg='#44FFDD')
                                    uvill.place(x=300,y=145)
                                    uvill_p=Label(cv,text=vill,font=('Regular',8),bg='#44FFDD')
                                    uvill_p.place(x=340,y=145)

                                    #post
                                    upost=Label(cv,text='Post: ',font=('Regular',8),bg='#44FFDD')
                                    upost.place(x=300,y=165)
                                    upost=Label(cv,text=po,font=('Regular',8),bg='#44FFDD')
                                    upost.place(x=340,y=165)

                                    #Pin
                                    upin=Label(cv,text='Pin : ',font=('Regular',8),bg='#44FFDD')
                                    upin.place(x=300,y=187)
                                    upin=Label(cv,text=pin,font=('Regular',8),bg='#44FFDD')
                                    upin.place(x=340,y=187)

                                    #district
                                    udist=Label(cv,text='Dist: ',font=('Regular',8),bg='#44FFDD')
                                    udist.place(x=300,y=207)
                                    udist=Label(cv,text=dist,font=('Regular',8),bg='#44FFDD')
                                    udist.place(x=340,y=207)

                                    #signature........
                                    sign_img=PhotoImage(file='img/sig.png')
                                    sig_l=Label(cv,image=sign_img,bg='#44FFDD')
                                    sig_l.place(x=355,y=235)
                                    cv.mainloop()

                                def createpdf():  
                                    df_d1=Label(viewcardwin,text='  ',fg='white',font=('Regular',11),padx=20,width=100)
                                    df_d1.place(x=102,y=520) 

                                    df_d=Label(viewcardwin,text='  ',fg='white',font=('Regular',15),padx=20,width=100)
                                    df_d.place(x=123,y=480) 
                                    # Progress bar widget                            
                                    progress = ttk.Progressbar(viewcardwin, orient = HORIZONTAL,length = 300, mode = 'determinate')
                                    # of the progress bar value
                                    def bar():
                                        import time
                                        progress['value'] = 20
                                        root.update_idletasks()
                                        time.sleep(1)
                                        progress['value'] = 60
                                        root.update_idletasks()
                                        time.sleep(1)
                                        progress['value'] = 100  
                                    progress.place(x=125,y=480)                            
                                    bar()


                                    #select data from data base....                        
                                    cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                    data=cr.fetchall()
                                    for i in data:
                                        n=i[0]
                                        d=i[1]
                                        g=i[2]
                                        f=i[3]
                                        p=i[4]
                                        aah=i[5]
                                        vill=i[6]
                                        po=i[7]
                                        pin=i[8]
                                        dist=i[9]
                                        state=i[10]
                                        cd=i[11]
                                        vs=i[12]
                                        myphoto=i[13]

                                    '''---------------------- Profile Area----------------------'''    
                                    #------------------------------------
                                    #card no
                                    cardnum='Voter ID: '
                                    cd #card number
                                    carduser_name='Name: '
                                    n #holder name
                                    father='Father Name: '
                                    f #father name
                                    gender='Gender: '
                                    g #gender
                                    dob='Date Of Birth: '
                                    d #dob..
                                    phone='Phone Number : '
                                    p #phone    

                                    village='Vill: '
                                    vill
                                    post='Post'
                                    po
                                    pn='Pin : '
                                    pin
                                    dst='Dist: '
                                    dist
                                    st='State: '
                                    state  
                                    
                                    #step 1
                                    def convert_data(data, file_name):     
                                        # Convert binary format to
                                        # images or files data
                                        with open(file_name, 'wb') as file:
                                            file.write(data)
                                        img = Image.open(file_name)
                                        #declear image type global
                                        global image_type
                                        image_type=img.format  
                                        # print(image_type) 
                                    img_path=os.getcwd()+'\\temp\\'+cd+'.png'
                                    convert_data(myphoto,img_path)
                                    tc=image_type.lower()
                                    
                                    #step 2    
                                    if(image_type != 'PNG'):    
                                        os.remove(img_path)
                                        # print('not png')
                                        def convert_data(data, file_name):     
                                            # Convert binary format to
                                            # images or files data
                                            with open(file_name, 'wb') as file:
                                                file.write(data)
                                            img = Image.open(file_name)
                                            #declear image type global
                                            global image_type
                                            image_type=img.format  
                                            # print(image_type) 
                                        img_path=os.getcwd()+'\\temp\\'+cd+'.'+tc
                                        convert_data(myphoto,img_path)


                                    pdf=FPDF()
                                    pdf.add_page()
                                    pdf.image('themes/cardimg.png',x=33,y=20)
                                    pdf.image('temp/'+cd+'.'+tc,56,42,25,30)
                                    pdf.image('img/sig.png',x=135,y=70)
                                    pdf.set_font("Arial",size=10) #set font size 10
                                    pdf.set_text_color(0,0,0)
                                    #>>>>>>>>>>>>>>>>>> font  <<<<<<<<<<<<<<<<<<<<<<<
                                    pdf.text(52,80,txt=cardnum)
                                    pdf.text(67,80,txt=cd)

                                    pdf.set_font("Arial",size=10) #set font size 8

                                    pdf.text(38,90,txt=carduser_name)
                                    pdf.text(64,90,txt=n)

                                    pdf.text(38,98,txt=father)
                                    pdf.text(64,98,txt=f)
                                    
                                    pdf.text(38,106,txt=gender)
                                    pdf.text(64,106,txt=g)

                                    pdf.text(38,114,txt=dob)
                                    pdf.text(64,114,txt=d)

                                    pdf.text(38,122,txt=phone)
                                    pdf.text(64,122,txt=p)

                                    #>>>>>>>>>>>>>>>>>> Back  <<<<<<<<<<<<<<<<<<<<<<<
                                    pdf.text(114,32,txt=village)
                                    pdf.text(125,32,txt=vill)

                                    pdf.text(114,40,txt=post)
                                    pdf.text(125,40,txt=po)

                                    pdf.text(114,48,txt=pn)
                                    pdf.text(125,48,txt=pin)

                                    pdf.text(114,56,txt=dst)
                                    pdf.text(125,56,txt=dist)

                                    pdf.text(114,64,txt=st)
                                    pdf.text(125,64,txt=state)                                         
                
                                    path=os.environ['USERPROFILE']
                                    savefile=path+'\\'+'OneDrive\Desktop\\'+cd+'.pdf'
                                    pdf.output(savefile)

                                    #delete temp img
                                    os.remove(img_path)
                                    
                                    showpath='Path: '+savefile
                                    df_d1=Label(viewcardwin,text=showpath,fg='red',font=('Regular',11),padx=20)
                                    df_d1.place(x=102,y=520) 

                                    df_d=Label(viewcardwin,text='File Downloaded On Desktop',fg='white',font=('Regular',15),bg='red',padx=20)
                                    df_d.place(x=123,y=480) 

                                down_l=Button(viewcardwin,text='  Download  ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=createpdf)
                                down_l.place(x=120,y=400)

                                view_l=Button(viewcardwin,text=' View Card ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=view)
                                view_l.place(x=300,y=400)    
                            
                                #>>>>>>>>>>>>
                            else:
                                # print('Please Enter Valid OTP')
                                invalid_OTP=Label(viewcardwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)

                        #verify otp..........
                        otp_t1=Label(viewcardwin,text='Enter OTP ',font=('Regular',18))
                        otp_t1.place(x=110,y=200)
                        otp_w1=Label(viewcardwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_w1.place(x=245,y=230)
                        otp_ee=Entry(viewcardwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                        otp_ee.place(x=245,y=200) 

                        Verifyotpp=Button(viewcardwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                        Verifyotpp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_card=Label(viewcardwin,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                        invalid_card.place(x=250,y=90)
                #label of phone number
                card_num=Label(viewcardwin,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
                card_num.place(x=50,y=55)
                #enter phone number
                card_num_e=Entry(viewcardwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                card_num_e.place(x=250,y=50)

                send_card_otp=Button(viewcardwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                send_card_otp.place(x=198,y=130)


                viewcardwin.mainloop()

                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            #################################### User Panel / Area  #######################################


            #row --------------->  1 
            #give vote
            give_img=PhotoImage(file='button/givevote.png')
            give_vote_b=Button(root,image=give_img,bd=0,bg='#C9C5C5',activebackground='#C9C5C5',cursor='hand2',command=givevote_now)
            give_vote_b.place(x=780,y=121)

            #view card
            view_img=PhotoImage(file='button/viewcard.png')
            view_card_b=Button(root,image=view_img,bg='#C9C5C5',bd=0,activebackground='#C9C5C5',cursor='hand2',command=viewvoter_card)
            view_card_b.place(x=1032,y=121)

            #track application
            search_img=PhotoImage(file='button/searchstatus.png')
            search_app_status_b=Button(root,image=search_img,bd=0,bg='#C9C5C5',activebackground='#C9C5C5',cursor='hand2',command=trackapplication)
            search_app_status_b.place(x=1280,y=121)


            #row --------------->  2
            #registration
            new_img=PhotoImage(file='button/regc.png')
            new_b=Button(root,image=new_img,bd=0,bg='#C9C5C5',activebackground='#C9C5C5',cursor='hand2',command=RegistrationForm)
            new_b.place(x=780,y=310)
            #download
            download_img=PhotoImage(file='button/download.png')
            download_b=Button(root,image=download_img,bg='#C9C5C5',bd=0,activebackground='#C9C5C5',cursor='hand2',command=download)
            download_b.place(x=1032,y=310)
            #update
            update_img=PhotoImage(file='button/update.png')
            update_card_b=Button(root,image=update_img,bg='#C9C5C5',bd=0,activebackground='#C9C5C5',cursor='hand2',command=required_to_login)
            update_card_b.place(x=1280,y=310)


            #row --------------->  3
            log_img=PhotoImage(file='button/loginc.png')
            log_b=Button(root,image=log_img,bd=0,bg='#C9C5C5',activebackground='#C9C5C5',cursor='hand2',command=LoginForm)
            log_b.place(x=780,y=499)


            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  left side old <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            
            #rbjp --------------->  
            bjp_img=PhotoImage(file='logo/bjp logo.png')
            bjp_b=Label(root,image=bjp_img ,bg='#C9C5C5')
            bjp_b.place(x=20,y=121)
            #count......
            bjp1_b=Label(root,bg='white',width=60,height=10)
            bjp1_b.place(x=250,y=123)

            bjp_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
            bjp_l1.place(x=300,y=180)
            #show count
            bjp_s=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
            bjp_s.place(x=440,y=180)

            #percentage
            tperentage=bjp+cong+tmc
            cpercentage_bjp=round((bjp/tperentage)*100,2) ,"%"
            bjp_p=Label(root,text=cpercentage_bjp,font=('Regular',16),bg='white',fg='blue')
            bjp_p.place(x=560,y=235)


            #progress
            for i in range(0,len(cpercentage_bjp)):
                bjp_percentage=round(cpercentage_bjp[0])
                break
            # print(type(bjp_percentage))

            progressbar_bjp=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
            progressbar_bjp['value']=bjp_percentage
            progressbar_bjp.place(x=300,y=240)

            ####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................................................................

            #tmc..........
            tmc_img=PhotoImage(file='logo/tmc logo.png')
            tmc_b=Label(root,image=tmc_img ,bg='#C9C5C5')
            tmc_b.place(x=16,y=310)
            #count........
            tmc1_b=Label(root,bg='white',width=60,height=10)
            tmc1_b.place(x=250,y=312)

            tmc_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
            tmc_l1.place(x=300,y=370)
            #show count
            tmc_s=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
            tmc_s.place(x=440,y=370)
            

            #percentage
            cpercentage_tmc=round((tmc/tperentage)*100,2) ,"%"
            tmc_p=Label(root,text=cpercentage_tmc,font=('Regular',16),bg='white',fg='blue')
            tmc_p.place(x=560,y=425)

            #progress
            for i in range(0,len(cpercentage_tmc)):
                tmc_percentage=round(cpercentage_tmc[0])
                break
            # print(type(tmc_percentage))

            progressbar_tmc=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
            progressbar_tmc['value']=tmc_percentage
            progressbar_tmc.place(x=300,y=430)


            ####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....................................................................



            #conj......
            conj_img=PhotoImage(file='logo/cong logo.png')
            conj_b=Label(root,image=conj_img ,bg='#C9C5C5')
            conj_b.place(x=20,y=499)
            #count.....
            conj_b=Label(root,bg='white',width=60,height=10)
            conj_b.place(x=250,y=501)

            conj_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
            conj_l1.place(x=300,y=560)
            #show count
            conj_s=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
            conj_s.place(x=440,y=560)

            #percentage
            cpercentage_cong=round((cong/tperentage)*100,2) ,"%"
            cong_p=Label(root,text=cpercentage_cong,font=('Regular',16),bg='white',fg='blue')
            cong_p.place(x=560,y=610)

            #progress
            for i in range(0,len(cpercentage_cong)):
                cong_percentage=round(cpercentage_cong[0])
                break
            # print(type(cong_percentage))

            progressbar_cong=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
            progressbar_cong['value']=cong_percentage
            progressbar_cong.place(x=300,y=615)

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  left side new <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            # total_report_bg=PhotoImage(file='logo/total.png')
            # total_report=Label(root,image=total_report_bg,bg='#C9C5C5')
            # total_report.place(x=28,y=75)

            # #vote count....
            # bjp_s=Label(root,text=bjp,font=('Regular',20),bg='#BCEAD5',fg='blue')
            # bjp_s.place(x=190,y=232)
            # tmc_s=Label(root,text=tmc,font=('Regular',20),bg='#BCEAD5',fg='blue')
            # tmc_s.place(x=410,y=232)
            # conj_s=Label(root,text=cong,font=('Regular',20),bg='#BCEAD5',fg='blue')
            # conj_s.place(x=630,y=232)


            # #pie chart.....
            # figure2=Figure(figsize=(4,4),dpi=100)
            # subplot2=figure2.add_subplot(111)

            # vot_per=[bjp,tmc,cong]
            # party_name=['BJP','TMC','CONGRESS']
            # exp=[0,0,0]
            # color_pi=['#FF9700','#00FF17','#FBFF00']

            # subplot2.pie(vot_per, labels=party_name, explode=exp, autopct='%2.1f%%', colors=color_pi)
            # pie2=FigureCanvasTkAgg(figure2,root)
            # pie2.get_tk_widget().place(x=150,y=380)

            # pr=Label(root,text='Pie Chart Report',font=('Regular',20),bg='white')
            # pr.place(x=50,y=350)
            




            root.mainloop()


        splash_screen.after(0,main_screen2)
        splash_screen.mainloop()




    def check_connection1():
        try:
            request.urlopen("https://www.google.com/",timeout=5)
            print('online')
            lunch_old_body()

        except OSError:
            print('offline')
            def second_body():
                second_body=Tk()
                second_body.geometry('1080x920')
                second_body.attributes('-fullscreen',True)
                second_body.config(bg='white')
                my_label = Label(second_body,bg='white')
                my_label.place(x=160,y=150)
                player = tkvideo("video/107013-loader-for-wi-fi-connection.mp4", my_label, loop = 1, size = (500,500))
                player.play()
                def notconnect1():
                    second_body.destroy()
                    ifnot1()
                

                nosig_img=PhotoImage(file='button/nosignal.png')
                nosig_label=Label(second_body,image=nosig_img,bd=0,bg='white')
                nosig_label.place(x=870,y=235)

                re_img=PhotoImage(file='button/retry.png')
                re_button=Button(second_body,image=re_img,command=notconnect1,bg='white',activebackground='white',bd=0,cursor='hand2')
                re_button.place(x=1035,y=515)
            
                second_body.mainloop()
            second_body()
    def ifnot1():
        check_connection1()
    check_connection1()





#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#----------------------------- @NEW  -------------------------------#

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def lunch_first_body():
    splash_screen=Tk()
    splash_screen.minsize(600,400)
    splash_screen.state("zoomed")
    splash_screen.resizable(False,False)
    splash_screen.attributes("-fullscreen",True)
    splash_screen.config(bg="white")
    splash_screen.overrideredirect(True)

    sp_img=Image.open("img/v5.png")
    # sp_img=ImageTk.PhotoImage(file="img/v1.jpg")
    resize_img=  ImageTk.PhotoImage(sp_img.resize((500,300)))

    place_img=Label(splash_screen,image=resize_img,bg="white")
    place_img.place(x=500,y=230)

    def main_screen():
        #close splash screen....
        splash_screen.destroy()

        #Execute Main Body....    
        root=Tk()
        root.title('Online Voting Management System')
        root.geometry('600x600+500+0')
        root.minsize(600,400)
        root.wm_iconbitmap('icon/vote-sign.ico')
        root.resizable(False,False)#maximize option disable
        # root.attributes('-fullscreen',True)
        root.state('zoomed')#default open fullscreen
    


        #-------------------------------------- Main Body ---------------------------------------- #

        '''------------------------------ Count Total Real-Time Vote-------------------------------'''
        cr.execute("select vot_status from registration")
        vt_data=cr.fetchall()
        tmc=0
        bjp=0
        cong=0
        for v_c in vt_data:
            total_v=v_c[0]
            if total_v=='TMC':
                tmc += 1
            if total_v== 'BJP':
                bjp +=1
            if total_v== 'Congress':
                cong +=1

        # print('tmc=',tmc)
        # print('bjp=',bjp)
        # print('conj=',cong)
        '''-----------------------------------------------------------------------------------------'''

        #-----------------------------------<<< About >>>------------------------------------ #
        def about():
            messagebox.showinfo('Details','Develop by ' ' ----> ' ' Amit Mandal\nDevelop by ' ' ----> '  ' Purnendu Mandal\nDevelop by ' ' ----> '  ' Rakesh Hossain\nDevelop by ' ' ----> '  ' Sridam Mandal\n ' ' \nApplication Verson 2.0')

        def feedback():
            feedwin=Toplevel()
            feedwin.title('Feedback or Report')
            feedwin.geometry('550x680+480+25')
            feedwin.wm_iconbitmap('icon/feedback.ico')
            feedwin.resizable(False,False)
            feedwin.config(bg='#D9D9D9')
            feedwin.config(bg='#C9C5C5')
            #aboutwin.attributes('-fullscreen',True)
            try:
                db=sqlite3.connect('voting management system.db')
                cr=db.cursor()
                cr.execute('create table feedback(email text,feedback_receive text)')
                
            except:
                print('feedback table is connected')
                
            

            #send feedback to database............
            feedemail=StringVar()
            def senddata():

                #define variable
                feed_email=feedemail.get()
                feed_data=feed_e.get('1.0','end-1c')

            
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
                # Define a function for
                # for validating an Email   
                def check(feed_email):
                
                    # pass the regular expression
                    # and the string into the fullmatch() method
                    if(re.fullmatch(regex, feed_email)):
                        #print("Valid Email")
                        #insert data..........
                        cr.execute('insert into feedback(email,feedback_receive) values(?,?)',(feed_email,feed_data))
                        db.commit()
                        messagebox.showinfo('Feedback','Thank You for Submit Feedback\n we will notify you after review feedback')
                        feedwin.destroy()
                
                    else:
                        #print("Invalid Email")
                        invalid=Label(feedwin,text='Please Enter Valid E-mail',font=('Regular',10),bg='white',fg='red')
                        invalid.place(x=175,y=210)
                check(feed_email)  

            


            #bg thems..............
            feedback_img=PhotoImage(file='themes/feedback_b.png')
            feed_l=Label(feedwin,image=feedback_img,bg='#C9C5C5',width=500,height=600)
            feed_l.place(x=25,y=10)

            #emai...........    
            em_img=PhotoImage(file='button/feedem.png')
            feed_l=Label(feedwin,image=em_img,bg='white')
            feed_l.place(x=60,y=166)
            #entry.........
            feed_e=Entry(feedwin,font=('Regular',24),width=18,bd=0,bg='#D4F6CC',textvar=feedemail)
            feed_e.place(x=175,y=169)

            #report........
            report_img=PhotoImage(file='button/feedreport.png')
            report_l=Label(feedwin,image=report_img,bg='white')
            report_l.place(x=60,y=250)
            #entry........
            feed_e=Text(feedwin,font=('Regular',16),height=8,width=36,bd=0,bg='#D4F6CC')
            feed_e.place(x=62,y=280)




            #send button img import
            send_bg=PhotoImage(file='button/fedsend.png')
            send=Button(feedwin,image=send_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=senddata)
            send.place(x=125,y=530)

            #cancel button img import
            can_bg=PhotoImage(file='button/cancel.png')
            login=Button(feedwin,image=can_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:feedwin.destroy())
            login.place(x=290,y=530)

            feedwin.mainloop()




        #--------------------------------<<< Registration Form >>>-------------------------------- #
        def RegistrationForm():
            root.destroy()
            import registration_form
            

        #-----------------------------------<<< Login Form >>>------------------------------------ #
        def LoginForm():
                
            logwin=Toplevel()
            logwin.title('Login Form')
            logwin.geometry('550x680')#+510+50')
            logwin.wm_iconbitmap('icon/login.ico')
            #logwin.resizable(False,False)
            logwin.config(bg='#D9D9D9')
            logwin.attributes('-fullscreen',True)
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Database Connect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            null=0
            uid=StringVar()
            upass=StringVar()
            def login():
                userid=uid.get()
                upassword=upass.get()
                
                #userid.................
                userid_length=len(userid)
                if null == userid_length:
                    #validation.....
                            
                    validation=Label(logwin,text='Please Enter User ID',font=('Regular',10),fg='red',bg='white')
                    validation.place(x=730,y=280)
                else:
                    #password..............
                    password_length=len(upassword)
                    if null == password_length:
                        p='Please Enter Password'
                        validation=Label(logwin,text=p,font=('Regular',10),fg='red',bg='white')
                        validation.place(x=730,y=360)
                    else:
                        cr.execute("select phone,password from registration")
                        data=cr.fetchall()
                        check=0
                        for i in data:
                            a=i[0]
                            b=i[1]
                            if userid==a and upassword==b:
                                check=1
                                break
                            else:
                                check=0
                        if check == 1:
                            #successfully login
                            afterloginwin=Toplevel()     
                            afterloginwin.title('My Profile')
                            afterloginwin.geometry('550x680+498+30')
                            afterloginwin.wm_iconbitmap('icon/myprofile.ico')
                            afterloginwin.resizable(False,False)
                            afterloginwin.config(bg='#D9D9D9')                    
                            afterloginwin.overrideredirect(1) 
                                        
                            cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={a}')
                            data=cr.fetchall()
                            for i in data:
                                n=i[0]
                                d=i[1]
                                g=i[2]
                                f=i[3]
                                p=i[4]
                                aah=i[5]
                                vill=i[6]
                                po=i[7]
                                pin=i[8]
                                dist=i[9]
                                state=i[10]
                                cd=i[11]
                                vs=i[12]
                                myphoto=i[13]

                            '''--------------------------- Give Vote -------------------------'''
                            def give():
                                votewin=Toplevel()
                                votewin.title('Give Vote')
                                votewin.geometry('550x680+480+25')
                                votewin.wm_iconbitmap('icon/feedback.ico')
                                votewin.resizable(False,False)
                                votewin.config(bg='#D9D9D9')
                                #votewin.attributes('-fullscreen',True)
                                votewin.overrideredirect(1)
                                # db=sqlite3.connect('voting management system.db')
                                # cr=db.cursor()   
                                # c='9382370394'

                                # cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status from registration where phone={c}')
                                # data=cr.fetchall()
                                # for i in data:
                                #     n=i[0]
                                #     d=i[1]
                                #     g=i[2]
                                #     f=i[3]
                                #     p=i[4]
                                #     aah=i[5]
                                #     vill=i[6]
                                #     po=i[7]
                                #     pin=i[8]
                                #     dist=i[9]
                                #     state=i[10]
                                #     cd=i[11]
                                #     vs=i[12]

                                if cd=='Not Generated':
                                    nota='Sorry Your not Eligible for Vote\n Beacuse your voter number is not gengrated'
                                    #background...
                                    gv_img=PhotoImage(file='themes/voteback.png')
                                    gv_l=Label(votewin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                    gv_l.place(x=30,y=10) 
                                    not_l=Label(votewin,text=nota,font=('Regular',18),bg='white',fg='blue')
                                    not_l.place(x=35,y=200)
                                    #cancel button img import
                                    canc_bg=PhotoImage(file='button/close.png')
                                    canc=Button(votewin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:votewin.destroy())
                                    canc.place(x=225,y=350)
                                else:
                                    null=0
                                    v1=IntVar()
                                    def give():
                                        v2=v1.get()
                                        if v2==null:
                                            #choose party.......
                                            cpp_l=Label(votewin,text='Please Choose Party',font=('Regular',8),fg='red',bg='white')
                                            cpp_l.place(x=223,y=210)
                                            v3='please choose party'
                                        elif v2==1:
                                            v3='BJP'
                                        elif v2==2:
                                            v3='TMC'
                                        else:
                                            v3='Congress'

                                        if v3=='BJP' or v3=='TMC' or v3=='Congress':
                                            rsotp=StringVar()
                                            
                                            cppp_l=Label(votewin,font=('Regular',10),bg='white',width=30)
                                            cppp_l.place(x=223,y=210)
                                            #resend otp
                                            #resend_bg=PhotoImage(file='button/resend.png')
                                            resend=Button(votewin,text='Resent OTP',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',command=give,padx=10)
                                            resend.place(x=225,y=240)
                                            
                                            '''------------------------------------------------------'''
                                            #generate otp.........
                                            motp=str(random.randint(1111,9999))
                                            #print(motp)
                                            #    
                                            '''-------------------TESTING OTP-------------------------'''

                                            ottp='Only for testing purposr OTP: ' +motp
                                            test_l=Label(votewin,text=ottp,fg='red')
                                            test_l.place(x=50,y=550)

                                            '''------------------Twillo OTP Service------------------'''
                                            # account_sid = 'AC714959399352b0bebabaac962eb62449'
                                            # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                                            # client = Client(account_sid, auth_token)
                                            # too='+91'+p
                                            # msg='Online Voting System\nDo not Share OTP\nyour Give vote OTP is: '+motp
                                            # client.messages.create(body=msg,from_='+19788308309',to=too)

                                            '''-------------------------------------------------------'''            
                                            
                                            cr.execute(f'update registration set otp={motp} where card_no={cd}')
                                            db.commit()
                                            already='Already Voted'
                                            def submitotp():
                                                reseveotp=rsotp.get()
                                                cr.execute(f'select voting_status,otp from registration where card_no={cd}')                
                                                otpdata=cr.fetchall()
                                                for ot in otpdata:
                                                    vts=ot[0]
                                                    sotp=ot[1]
                                                
                                            
                                                if sotp==reseveotp:
                                                    if vts=='Not Voted':
                                                        cr.execute('update registration set voting_status=?,vot_status=? where card_no=?',(already,v3,cd))
                                                        db.commit()

                                                        #Thanks for vote...................
                                                        successwin=Toplevel()
                                                        successwin.title('success full vote')
                                                        successwin.geometry('550x680+480+25')
                                                        successwin.wm_iconbitmap('icon/feedback.ico')
                                                        successwin.resizable(False,False)
                                                        successwin.config(bg='#D9D9D9')
                                                        #successwin.attributes('-fullscreen',True)
                                                        successwin.overrideredirect(1)

                                                        note='Thank You For Give Vote...'
                                                        #background...
                                                        gv_img=PhotoImage(file='themes/voteback.png')
                                                        gv_l=Label(successwin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                                        gv_l.place(x=33,y=10) 

                                                        warning_img=PhotoImage(file='logo/check.png')
                                                        war_l=Label(successwin,image=warning_img,width=200,height=100,bg='white')
                                                        war_l.place(x=180,y=70)

                                                        not_l=Label(successwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                        not_l.place(x=150,y=200)

                                                        
                                                        # Re-fetch Voting count data.......................
                                                        cr.execute("select vot_status from registration")
                                                        vt_data=cr.fetchall()
                                                        tmc=0
                                                        bjp=0
                                                        cong=0
                                                        for v_c in vt_data:
                                                            total_v=v_c[0]
                                                            if total_v=='TMC':
                                                                tmc += 1
                                                            if total_v== 'BJP':
                                                                bjp +=1
                                                            if total_v== 'Congress':
                                                                cong +=1

                                                        #show count Bjp                                    
                                                        bjp_s1=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
                                                        bjp_s1.place(x=440,y=180)
                                                        #show count TMC
                                                        tmc_s1=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
                                                        tmc_s1.place(x=440,y=370)
                                                        #show count CONJ
                                                        conj_s1=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
                                                        conj_s1.place(x=440,y=560)




                                                        def closesuccess():                                                    
                                                            votewin.destroy()
                                                            successwin.destroy()
                                                            
                                                        #cancel button img import
                                                        tgv_bg=PhotoImage(file='button/close.png')
                                                        tgv=Button(successwin,image=tgv_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=closesuccess)
                                                        tgv.place(x=230,y=370)
                                                        successwin.mainloop()
                                                    else:
                                                        #already voted...................
                                                        alwin=Toplevel()
                                                        alwin.title('Already Voted')
                                                        alwin.geometry('550x680+480+25')
                                                        alwin.wm_iconbitmap('icon/feedback.ico')
                                                        alwin.resizable(False,False)
                                                        alwin.config(bg='#D9D9D9')
                                                        #alwin.attributes('-fullscreen',True)
                                                        alwin.overrideredirect(1)

                                                        note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                                                        #background...
                                                        gv_img=PhotoImage(file='themes/voteback.png')
                                                        gv_l=Label(alwin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                                        gv_l.place(x=30,y=10) 

                                                        warning_img=PhotoImage(file='logo/warning.png')
                                                        war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                                                        war_l.place(x=180,y=70)

                                                        not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                                        not_l.place(x=85,y=200)
                                                        #cancel button img import
                                                        canc_bg=PhotoImage(file='button/close.png')
                                                        canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                                                        canc.place(x=225,y=370)
                                                        alwin.mainloop()
                                                else:
                                                    #print('wrong otp')                       
                                                    w_l=Label(votewin,text='Please Enter Valid OTP',bg='White',fg='red',width=50)
                                                    w_l.place(x=130,y=372) 

                                            #otp..........
                                            otp_l=Label(votewin,text='Enter OTP ',font=('Regular',18))
                                            otp_l.place(x=110,y=340)
                                            otp_s=Label(votewin,text='4 Digit OTP Send Your Mobile Number',font=('Regular',8),bg='white')
                                            otp_s.place(x=245,y=370)
                                            otp_e=Entry(votewin,font=('Regular',18),bg='#DFF6FF',width=16,textvar=rsotp)
                                            otp_e.place(x=245,y=340)  
                                            #login button img import
                                            #sub1_img=PhotoImage(file='button/u_login.png')
                                            sub1=Button(votewin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=submitotp)
                                            sub1.place(x=140,y=450)
                                            #cancel button img import
                                            #canc_bg=PhotoImage(file='button/cancel.png')
                                            canc=Button(votewin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:votewin.destroy())
                                            canc.place(x=310,y=450)                                    
                                        else:
                                            print()
                                            #please select party

                                    # stream = io.BytesIO(n)
                                    # img=Image.open(stream)
                                    # img =PhotoImage(img) 
                                    #bg thems..............
                                    gv_img=PhotoImage(file='themes/voteback.png')
                                    gv_l=Label(votewin,image=gv_img,bg='#D9D9D9',width=500,height=600)
                                    gv_l.place(x=30,y=10) 

                                    #choose party.......
                                    cp_l=Label(votewin,text='Choose Your Favourite Party',font=('Regular',22),bg='white',fg='blue')
                                    cp_l.place(x=96,y=70)
                                    cp1_e=Radiobutton(votewin,text='BJP',font=('times new roman',18),fg='#FF9F29',bg='white',activebackground='white',value=1,cursor='hand2',variable=v1)
                                    cp1_e.place(x=110,y=150)
                                    cp2_e=Radiobutton(votewin,text='TMC',font=('times new roman',18),fg='green',bg='white',activebackground='white',value=2,cursor='hand2',variable=v1)
                                    cp2_e.place(x=220,y=150)
                                    cp3_e=Radiobutton(votewin,text='Congress',font=('times new roman',18),fg='red',bg='white',activebackground='white',value=3,cursor='hand2',variable=v1)
                                    cp3_e.place(x=340,y=150)
                                    
                                    #give vote button img import
                                    #gvote_bg=PhotoImage(file='button/verify.png')
                                    gvote=Button(votewin,text='✓ Verify ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',command=give,padx=10)
                                    gvote.place(x=225,y=240)
                                votewin.mainloop()

                            '''---------------------- Profile Area----------------------'''

                            afterlogin_img=PhotoImage(file='themes/afterlogin.png')
                            afterlogin_l=Label(afterloginwin,image=afterlogin_img,bg='#D9D9D9',width=500,height=600)
                            afterlogin_l.place(x=25,y=10)

                            u_img=PhotoImage(file='button/uphoto.png')
                            userphoto=Label(afterloginwin,image=u_img)
                            userphoto.place(x=210,y=50)

                            #////////////////////////////////
                            fp = io.BytesIO(myphoto)
                            # load the image
                            image = Image.open(fp)
                            res=image.resize((114,134))
                            # drawing image to top window
                            userimg = ImageTk.PhotoImage(res)

                            userphoto=Label(afterloginwin,image=userimg)
                            userphoto.place(x=210,y=50)

                            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                            #------------------------------------
                            #card no
                            ucard_no=Label(afterloginwin,text='Voter ID: ',font=('Regular',10),bg='white')
                            ucard_no.place(x=200,y=200)

                            ucard_p=Label(afterloginwin,text=cd,font=('Regular',10),bg='white')
                            ucard_p.place(x=260,y=200)
                            
                            #>>>>>>>>>>>>>>>>>>>>>>>

                            #name
                            uname=Label(afterloginwin,text='Name: ',font=('Regular',10),bg='white')
                            uname.place(x=70,y=250)    
                            uname_p=Label(afterloginwin,text=n,font=('Regular',10),bg='white')
                            uname_p.place(x=180,y=250)

                            #father name
                            fname=Label(afterloginwin,text='Father Name: ',font=('Regular',10),bg='white')
                            fname.place(x=70,y=280)
                            fname_p=Label(afterloginwin,text=f,font=('Regular',10),bg='white')
                            fname_p.place(x=180,y=280)

                            #gender
                            ugender=Label(afterloginwin,text='Gender: ',font=('Regular',10),bg='white')
                            ugender.place(x=70,y=310)
                            ugender_p=Label(afterloginwin,text=g,font=('Regular',10),bg='white')
                            ugender_p.place(x=180,y=310)

                            #date of birth
                            udob=Label(afterloginwin,text='Date Of Birth: ',font=('Regular',10),bg='white')
                            udob.place(x=70,y=340)
                            udob_p=Label(afterloginwin,text=d,font=('Regular',10),bg='white')
                            udob_p.place(x=180,y=340)

                            #phone no
                            uphone=Label(afterloginwin,text='Phone Number : ',font=('Regular',10),bg='white')
                            uphone.place(x=70,y=370)
                            uphone_p=Label(afterloginwin,text=p,font=('Regular',10),bg='white')
                            uphone_p.place(x=180,y=370)

                            #aadhaar no
                            uaadhaar=Label(afterloginwin,text='Linked Aadhaar: ',font=('Regular',10),bg='white')
                            uaadhaar.place(x=70,y=400)
                            uaadhaar_p=Label(afterloginwin,text=aah,font=('Regular',10),bg='white')
                            uaadhaar_p.place(x=180,y=400)

                            uvstatus=Label(afterloginwin,text='Voting Status _: ',font=('Regular',10),bg='white')
                            uvstatus.place(x=70,y=430)
                            uvstatus_p=Label(afterloginwin,text=vs,font=('Regular',10),bg='white',fg='red')
                            uvstatus_p.place(x=180,y=430)

                            #>>>>>>>>>>>>
                            #village
                            uvill=Label(afterloginwin,text='Vill: ',font=('Regular',10),bg='white')
                            uvill.place(x=340,y=250)
                            uvill_p=Label(afterloginwin,text=vill,font=('Regular',10),bg='white')
                            uvill_p.place(x=390,y=250)

                            #post
                            upost=Label(afterloginwin,text='Post: ',font=('Regular',10),bg='white')
                            upost.place(x=340,y=280)
                            upost=Label(afterloginwin,text=po,font=('Regular',10),bg='white')
                            upost.place(x=390,y=280)

                            #Pin
                            upin=Label(afterloginwin,text='Pin : ',font=('Regular',10),bg='white')
                            upin.place(x=340,y=310)
                            upin=Label(afterloginwin,text=pin,font=('Regular',10),bg='white')
                            upin.place(x=390,y=310)

                            #district
                            udist=Label(afterloginwin,text='Dist: ',font=('Regular',10),bg='white')
                            udist.place(x=340,y=340)
                            udist=Label(afterloginwin,text=dist,font=('Regular',10),bg='white')
                            udist.place(x=390,y=340)

                            #stste
                            ustate=Label(afterloginwin,text='State: ',font=('Regular',10),bg='white')
                            ustate.place(x=340,y=370)
                            ustate=Label(afterloginwin,text=state,font=('Regular',10),bg='white')
                            ustate.place(x=390,y=370)

                            #button area  >>>>>>>>>>>>>>>>>>>>>>

                            #give vote button img import
                            gvote_bg=PhotoImage(file='button/gvote.png')
                            gvote=Button(afterloginwin,image=gvote_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=give)
                            gvote.place(x=105,y=530)

                            def upd():
                                lw=Label(afterloginwin,text='Sorry You Can Not Update Any Detaile, It\' Possiable After Upcomming Upgrade',fg='red',bg='white' )
                                lw.place(x=75,y=495)

                            #Update button
                            upd_bg=PhotoImage(file='button/upd.png')
                            upd=Button(afterloginwin,image=upd_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=upd)
                            upd.place(x=232,y=530)

                            def ulogout():
                                afterloginwin.destroy()
                                logwin.destroy()

                            #logout button img import
                            logout_bg=PhotoImage(file='button/ulogout.png')
                            logout=Button(afterloginwin,image=logout_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=ulogout)
                            logout.place(x=360,y=530)

                            afterloginwin.mainloop()
                        else:
                            #cancel button img import
                            Warning_u_p=Label(logwin,text='Wrong User ID or Password',bg='white',fg='red')
                            Warning_u_p.place(x=690,y=180)

                    

            def forgetpass():
                try:
                    db=sqlite3.connect('voting management system.db')
                    cr=db.cursor()
                except:
                    print('Forgt db is running...')
                forgetwin=Toplevel()
                forgetwin.title('Forget Password')
                forgetwin.geometry('550x680+485+25')
                forgetwin.wm_iconbitmap('icon/login.ico')
                forgetwin.resizable(False,False)
                entphone=StringVar()
                #send OTP
                def sendotpp():
                    fphone_num=entphone.get()
                    cr.execute('select phone from registration')
                    fp_data=cr.fetchall()
                    fcheck=0
                    for ff in fp_data:
                        fp=ff[0]
                        if fphone_num==fp:
                            fcheck=1
                            break
                        else:
                            fcheck=0
                    if fcheck==1:
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_phone=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_phone.place(x=250,y=94)
                        #resend button
                        sendotp=Button(forgetwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                        sendotp.place(x=198,y=130)

                        '''------------------------------------------------------'''
                        #generate otp.........
                        fotp=str(random.randint(1111,9999))
                        #print('otp is: ',fotp)
                        #       
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        # account_sid = 'AC714959399352b0bebabaac962eb62449'
                        # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        # client = Client(account_sid, auth_token)
                        # too='+91'+fp
                        # msg='Online Voting System\nForget Password OTP: '+fotp
                        # client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
                        '''--------------------- Testing Otp ----------------------'''        
                        otpnote='Only for Testing Purpose OTP: '+fotp
                        testing=Label(forgetwin,text=otpnote,font=('Regular',8),fg='red')
                        testing.place(x=5,y=650)

                        #update otp..............
                        cr.execute('update registration set otp=? where phone=?',(fotp,fp))
                        db.commit()
                        #print('changed otp')

                        rotp=StringVar()
                        def verifyfotp():
                            rsotp=rotp.get()
                            cr.execute(f'select otp from registration where phone={fp}')
                            fetchotp=cr.fetchall()
                            for fe in fetchotp:
                                dotp=fe[0]

                            #if matched otp............
                            if dotp==rsotp:
                                #hide invalid otp error
                                invalid_OTP=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)
                                #verified otp button
                                Verifyotp=Button(forgetwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                                Verifyotp.place(x=205,y=290)

                                pass1=StringVar()
                                pass2=StringVar()
                                def changepass():
                                    pass11=pass1.get()
                                    pass22=pass2.get()
                                    if pass11==pass22:
                                        cr.execute('update registration set password=?,conform_password=? where phone=?',(pass11,pass22,fp))
                                        db.commit()
                                        # print('pass changed')  
                                        
                                        #close forgetwindow............
                                        forgetwin.destroy()

                                        changedwin=Toplevel()
                                        changedwin.title('Successfully changed Password')
                                        changedwin.geometry('550x680+485+25')
                                        changedwin.wm_iconbitmap('icon/login.ico')
                                        changedwin.resizable(False,False)
                                        changedwin.overrideredirect()


                                        ch_img=PhotoImage(file='logo/check.png')
                                        ch_l=Label(changedwin,image=ch_img)
                                        ch_l.place(x=215,y=100)

                                        ph_l=Label(changedwin,text='Your Password Successfully changed',font=('times new roman',20),fg='blue')
                                        ph_l.place(x=70,y=230)

                                        changedwin.mainloop()

                                    else:
                                        # print('conform pass not match')
                                        #password not match
                                        invalid_pass=Label(forgetwin,text='Conform Password Not Matched',font=('times new roman',8),fg='red')
                                        invalid_pass.place(x=250,y=462)

                                #import password image
                                pass_f=Label(forgetwin,text='New Password',font=('times new roman',18),bg='white')
                                pass_f.place(x=80,y=380)
                                #entry password
                                pass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,textvar=pass1)
                                pass_fe.place(x=250,y=380)


                                #import conform password image
                                con_pass_e=Label(forgetwin,text='Re... Password',font=('times new roman',18),bg='white')
                                con_pass_e.place(x=80,y=430)
                                #entry conform password
                                conpass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,show='*',textvar=pass2)
                                conpass_fe.place(x=250,y=430)
                                #login button img import
                                #sub1_img=PhotoImage(file='button/u_login.png')
                                sub11=Button(forgetwin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=changepass)
                                sub11.place(x=145,y=550)
                                #cancel button img import
                                #canc_bg=PhotoImage(file='button/cancel.png')
                                canc1=Button(forgetwin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:forgetwin.destroy())
                                canc1.place(x=295,y=550)  
                            else:
                                # print('Please Enter Valid OTP')
                                invalid_OTP=Label(forgetwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)



                        #verify otp..........
                        otp_l1=Label(forgetwin,text='Enter OTP ',font=('Regular',18))
                        otp_l1.place(x=110,y=200)
                        otp_s1=Label(forgetwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_s1.place(x=245,y=230)
                        otp_e1=Entry(forgetwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=rotp)
                        otp_e1.place(x=245,y=200) 

                        Verifyotp=Button(forgetwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                        Verifyotp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_phone=Label(forgetwin,text='Please Enter Registered Phone Number',font=('times new roman',8),fg='red')
                        invalid_phone.place(x=250,y=90)

                #label of phone number
                fphone=Label(forgetwin,text='Phone Number :',font=('times new roman',18,'bold'),fg='black',bd=0)
                fphone.place(x=50,y=50)
                #enter phone number
                fphone_e=Entry(forgetwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entphone)
                fphone_e.place(x=250,y=50)


                sendotp=Button(forgetwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                sendotp.place(x=198,y=130)

                forgetwin.mainloop()

            #frame bg image import
            fbg=PhotoImage(file='themes/login form.png')
            login_background=Label(logwin,image=fbg,bg='#D9D9D9',width=518,height=654)
            login_background.place(x=510,y=10)

            #uid label img import
            uid_bg=PhotoImage(file='button/uid.png')
            uid_l=Label(logwin,image=uid_bg,bd=0,bg='white')
            uid_l.place(x=565,y=240)

            #uid input       ----*** Entry Box ***----
            uid_e=Entry(logwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',textvar=uid)
            uid_e.place(x=730,y=242)

            #password label img import
            pass_bg=PhotoImage(file='button/password.png')
            password=Label(logwin,image=pass_bg,bd=0,bg='white')
            password.place(x=565,y=320)

            #password input  ----*** Entry Box ***----
            pass_e=Entry(logwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',show='*',textvar=upass)
            pass_e.place(x=730,y=322)


            #login button img import
            log_bg=PhotoImage(file='button/u_login.png')
            login=Button(logwin,image=log_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=login)
            login.place(x=565,y=410)

            #cancel button img import
            cancel_bg=PhotoImage(file='button/cancel.png')
            login=Button(logwin,image=cancel_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:logwin.destroy())
            login.place(x=730,y=410)

            #forget button img import
            #forget_bg=PhotoImage(file='button/forget.png')
            forget=Button(logwin,text='Forget Pasword?',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=forgetpass)
            forget.place(x=570,y=512)

            #slash / button img import
            slash_bg=PhotoImage(file='button/slash.png')
            slash=Button(logwin,image=slash_bg,bd=0,bg='white',activebackground='white')
            slash.place(x=705,y=512)

            #Create new account button img import
            #create_new_ac_bg=PhotoImage(file='button/create_new_ac.png')
            create=Button(logwin,text='Apply For New Candidate',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=RegistrationForm)
            create.place(x=730,y=512)

            logwin.mainloop()


        def givevote_now():
            gv2=Toplevel()
            gv2.title('Give Vote')
            gv2.geometry('550x680+480+25')
            gv2.wm_iconbitmap('icon/vote-sign.ico')
            gv2.resizable(False,False)
            cr=db.cursor()  


            entcard=StringVar()
            def sub_vot_otp():
                inputcard_no=entcard.get()
                cr.execute(f'select card_no from registration')
                data22=cr.fetchall()
                vnc=0
                for ii in data22:
                    vn=ii[0]
                    if inputcard_no == vn:
                        vnc=1
                        break
                    else:
                        vnc=0
                if vnc==1:
                    # print('match')
                    #print('Phone number not match')
                    invalid_card=Label(gv2,text=' ',font=('times new roman',8),fg='red',width=30)
                    invalid_card.place(x=250,y=90)
                    cr.execute(f'select phone,voting_status from registration where card_no={vn}')
                    fvts=cr.fetchall()
                    for jj in fvts:
                        vtphone=jj[0]
                        votingstatus=jj[1]
                    # print(votingstatus)
                    # print(vtphone)
                    if votingstatus=='Not Voted':
                        null=0
                        v1=IntVar()
                        def give():
                            v2=v1.get()
                            if v2==null:
                                #choose party.......
                                cpp_l=Label(gv2,text='Please Choose Party',font=('Regular',8),fg='red')
                                cpp_l.place(x=213,y=310)
                                v3='please choose party'
                            elif v2==1:
                                v3='BJP'
                            elif v2==2:
                                v3='TMC'
                            else:
                                v3='Congress'

                            if v3=='BJP' or v3=='TMC' or v3=='Congress':
                                # print(v3)
                                cpp_l=Label(gv2,text=' ',font=('Regular',8),fg='red',width=30)
                                cpp_l.place(x=213,y=310)
                                #gvote_bg=PhotoImage(file='button/verify.png')
                                gvote=Button(gv2,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=give)
                                gvote.place(x=210,y=330)                    

                                '''------------------------------------------------------'''
                                #generate otp.........
                                motpp=str(random.randint(1111,9999))
                                # print(motpp)
                                #    
                                '''-------------------TESTING OTP-------------------------'''

                                ottp='Only for testing purposr OTP: ' +motpp
                                test_l=Label(gv2,text=ottp,fg='red')
                                test_l.place(x=10,y=630)

                                # '''------------------Twillo OTP Service------------------'''
                                # account_sid = 'AC714959399352b0bebabaac962eb62449'
                                # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                                # client = Client(account_sid, auth_token)
                                # too='+91'+vtphone
                                # msg='Online Voting System\nyou can give vote\nyour OTP is: '+motpp
                                # client.messages.create(body=msg,from_='+19788308309',to=too)

                                '''-------------------------------------------------------'''            

                                cr.execute(f'update registration set otp={motpp} where card_no={vn}')
                                db.commit()

                                rsotp=StringVar()
                                def urs_otp():
                                    reseveotp=rsotp.get()
                                    cr.execute(f'select voting_status,otp from registration where card_no={vn}')                
                                    otpdata=cr.fetchall()
                                    for ot in otpdata:
                                        vts=ot[0]
                                        sotp=ot[1]
                                    already='Already Voted'
                                    if sotp==reseveotp:
                                        if vts=='Not Voted':
                                            cr.execute('update registration set voting_status=?,vot_status=? where card_no=?',(already,v3,vn))
                                            db.commit()

                                            #Thanks for vote...................
                                            successwin=Toplevel()
                                            successwin.title('success full vote')
                                            successwin.geometry('550x680+487+25')
                                            successwin.wm_iconbitmap('icon/feedback.ico')
                                            successwin.resizable(False,False)
                                            #successwin.attributes('-fullscreen',True)
                                            successwin.overrideredirect(1)

                                            note='Thank You For Give Vote...'
                                            #background...
                                            gv_img=PhotoImage(file='themes/voteback.png')
                                            gv_l=Label(successwin,image=gv_img,width=500,height=600)
                                            gv_l.place(x=33,y=10) 

                                            warning_img=PhotoImage(file='logo/check.png')
                                            war_l=Label(successwin,image=warning_img,width=200,height=100,bg='white')
                                            war_l.place(x=180,y=70)

                                            not_l=Label(successwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                            not_l.place(x=150,y=200)

                                            # Re-fetch voting count data.........
                                            
                                            cr.execute("select vot_status from registration")
                                            vt_data=cr.fetchall()
                                            tmc=0
                                            bjp=0
                                            cong=0
                                            for v_c in vt_data:
                                                total_v=v_c[0]
                                                if total_v=='TMC':
                                                    tmc += 1
                                                if total_v== 'BJP':
                                                    bjp +=1
                                                if total_v== 'Congress':
                                                    cong +=1

                                            # #show count Bjp                                    
                                            # bjp_s1=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
                                            # bjp_s1.place(x=440,y=180)
                                            # #show count TMC
                                            # tmc_s1=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
                                            # tmc_s1.place(x=440,y=370)
                                            # #show count CONJ
                                            # conj_s1=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
                                            # conj_s1.place(x=440,y=560)

                                            # #percentage
                                            # tperentage=bjp+cong+tmc
                                            # cpercentage_bjp=round((bjp/tperentage)*100,2) ,"%"
                                            # bjp_p=Label(root,text=cpercentage_bjp,font=('Regular',16),bg='white',fg='blue',width=8)
                                            # bjp_p.place(x=560,y=235)
                                            # #percentage
                                            # cpercentage_tmc=round((tmc/tperentage)*100,2) ,"%"
                                            # tmc_p=Label(root,text=cpercentage_tmc,font=('Regular',16),bg='white',fg='blue',width=8)
                                            # tmc_p.place(x=560,y=425)
                                            # #percentage
                                            # cpercentage_cong=round((cong/tperentage)*100,2) ,"%"
                                            # cong_p=Label(root,text=cpercentage_cong,font=('Regular',16),bg='white',fg='blue',width=8)
                                            # cong_p.place(x=560,y=610)

                                            # #progress
                                            # for i in range(0,len(cpercentage_bjp)):
                                            #     bjp_percentage=round(cpercentage_bjp[0])
                                            #     break
                                            # # print(type(bjp_percentage))

                                            # progressbar_bjp=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                            # progressbar_bjp['value']=bjp_percentage
                                            # progressbar_bjp.place(x=300,y=240)

                                            # #progress
                                            # for i in range(0,len(cpercentage_tmc)):
                                            #     tmc_percentage=round(cpercentage_tmc[0])
                                            #     break
                                            # # print(type(tmc_percentage))

                                            # progressbar_tmc=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                            # progressbar_tmc['value']=tmc_percentage
                                            # progressbar_tmc.place(x=300,y=430)

                                            # #progress
                                            # for i in range(0,len(cpercentage_cong)):
                                            #     cong_percentage=round(cpercentage_cong[0])
                                            #     break
                                            # # print(type(cong_percentage))

                                            # progressbar_cong=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
                                            # progressbar_cong['value']=cong_percentage
                                            # progressbar_cong.place(x=300,y=615)


                                            #vote count....
                                            bjp_s=Label(root,text=bjp,font=('Regular',20),bg='#BCEAD5',fg='blue')
                                            bjp_s.place(x=190,y=232)
                                            tmc_s=Label(root,text=tmc,font=('Regular',20),bg='#BCEAD5',fg='blue')
                                            tmc_s.place(x=410,y=232)
                                            conj_s=Label(root,text=cong,font=('Regular',20),bg='#BCEAD5',fg='blue')
                                            conj_s.place(x=630,y=232)

                                            
                                            #pie chart.....
                                            figure2=Figure(figsize=(4,4),dpi=100)
                                            subplot2=figure2.add_subplot(111)

                                            vot_per=[bjp,tmc,cong]
                                            party_name=['BJP','TMC','CONGRESS']
                                            exp=[0,0,0]
                                            color_pi=['#FF9700','green','yellow']

                                            subplot2.pie(vot_per, labels=party_name, explode=exp, autopct='%2.2f%%', colors=color_pi)
                                            pie2=FigureCanvasTkAgg(figure2,root)
                                            pie2.get_tk_widget().place(x=150,y=380)
                                            pr=Label(text='Pie Chart Report',font=('Regular',20),bg='white')
                                            pr.place(x=50,y=370) 
                                            
                                           
                                            def closesuccess():              
                                                successwin.destroy()
                                                gv2.destroy()    

                                            #cancel button img import
                                            tgv_bg=PhotoImage(file='button/close.png')
                                            tgv=Button(successwin,image=tgv_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=closesuccess)
                                            tgv.place(x=230,y=370)
                                            
                                            successwin.mainloop()
                                        else:
                                            #already voted...................
                                            alwin=Toplevel()
                                            alwin.title('Already Voted')
                                            alwin.geometry('550x680+487+25')
                                            alwin.wm_iconbitmap('icon/feedback.ico')
                                            alwin.resizable(False,False)
                                            #alwin.attributes('-fullscreen',True)
                                            alwin.overrideredirect(1)

                                            note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                                            #background...
                                            gv_img=PhotoImage(file='themes/voteback.png')
                                            gv_l=Label(alwin,image=gv_img,width=500,height=600)
                                            gv_l.place(x=30,y=10) 

                                            warning_img=PhotoImage(file='logo/warning.png')
                                            war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                                            war_l.place(x=180,y=70)

                                            not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                                            not_l.place(x=85,y=200)
                                            #cancel button img import
                                            canc_bg=PhotoImage(file='button/close.png')
                                            canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                                            canc.place(x=225,y=370)
                                            alwin.mainloop()
                                    else:
                                        #print('wrong otp')                                
                                        w_l=Label(gv2,text='Please Enter Valid OTP',fg='red',width=50)
                                        w_l.place(x=130,y=430)
                                #otp..........
                                otp_l=Label(gv2,text='Enter OTP ',font=('Regular',18))
                                otp_l.place(x=110,y=400)
                                otp_s=Label(gv2,text='4 Digit OTP Send Your Mobile Number',font=('Regular',8))
                                otp_s.place(x=245,y=430)
                                otp_e=Entry(gv2,font=('Regular',18),bg='#DFF6FF',width=16,textvar=rsotp)
                                otp_e.place(x=245,y=400)  
                                #login button img import
                                #sub1_img=PhotoImage(file='button/u_login.png')
                                sub1=Button(gv2,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=urs_otp)
                                sub1.place(x=140,y=490)
                                #cancel button img import
                                #canc_bg=PhotoImage(file='button/cancel.png')
                                canc=Button(gv2,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:gv2.destroy())
                                canc.place(x=310,y=490)                    
                        #choose party.......
                        cp_l=Label(gv2,text='Choose Your Favourite Party',font=('Regular',22),fg='blue')
                        cp_l.place(x=96,y=200)

                        cp1_e=Radiobutton(gv2,text='BJP',font=('times new roman',18),fg='#FF9F29',activebackground='white',value=1,cursor='hand2',variable=v1)
                        cp1_e.place(x=110,y=265)
                        cp2_e=Radiobutton(gv2,text='TMC',font=('times new roman',18),fg='green',activebackground='white',value=2,cursor='hand2',variable=v1)
                        cp2_e.place(x=220,y=265)
                        cp3_e=Radiobutton(gv2,text='Congress',font=('times new roman',18),fg='red',activebackground='white',value=3,cursor='hand2',variable=v1)
                        cp3_e.place(x=340,y=265)

                        #gvote_bg=PhotoImage(file='button/verify.png')
                        gvote=Button(gv2,text='✓ Verify ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=give)
                        gvote.place(x=210,y=330)

                                
                    else:
                        # print('cant not take vote')
                        #already voted...................
                        alwin=Toplevel()
                        alwin.title('Already Voted')
                        alwin.geometry('550x680+487+25')
                        alwin.wm_iconbitmap('icon/feedback.ico')
                        alwin.resizable(False,False)
                        
                        #alwin.attributes('-fullscreen',True)
                        alwin.overrideredirect(1)

                        note='One user can give vote at once time\nYou Have Already Voted...\nSorry you can\'t give vote again\n Because Our System Checks You...'
                        #background...
                        gv_img=PhotoImage(file='themes/voteback.png')
                        gv_l=Label(alwin,image=gv_img,width=500,height=600)
                        gv_l.place(x=30,y=10) 

                        warning_img=PhotoImage(file='logo/warning.png')
                        war_l=Label(alwin,image=warning_img,width=200,height=100,bg='white')
                        war_l.place(x=180,y=70)

                        not_l=Label(alwin,text=note,font=('Regular',18),bg='white',fg='blue')
                        not_l.place(x=85,y=200)
                        #cancel button img import
                        canc_bg=PhotoImage(file='button/close.png')
                        canc=Button(alwin,image=canc_bg,font=('Regular',18),bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:alwin.destroy())
                        canc.place(x=225,y=370)
                        alwin.mainloop()

                else:
                    #print('Phone number not match')
                    invalid_card=Label(gv2,text='Please Enter Valid Voter ID',font=('times new roman',8),fg='red')
                    invalid_card.place(x=250,y=90)
                
            #label of phone number
            card_num=Label(gv2,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
            card_num.place(x=50,y=55)
            #enter phone number
            card_num_e=Entry(gv2,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
            card_num_e.place(x=250,y=50)

            send_card_otp=Button(gv2,text=' Submit ', fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sub_vot_otp)
            send_card_otp.place(x=210,y=130)

            gv2.mainloop()





        #required to login......
        def required_to_login():        
            def update_verify():
                update_verify_win=Toplevel()
                update_verify_win.title('Update Details')
                update_verify_win.geometry('550x580+485+95')
                update_verify_win.wm_iconbitmap('icon/notap.ico')
                update_verify_win.resizable(False,False)

                entcard=StringVar()
                #send OTP
                def sendcardotp():
                    cardn=entcard.get()
                    cr.execute('select card_no from registration')
                    sc_data=cr.fetchall()
                    cfetch=0
                    for sc in sc_data:
                        sc1=sc[0]
                        if cardn==sc1:
                            cfetch=1
                            break
                        else:
                            cfetch=0
                    if cfetch==1:
                        # print('valid card number')
                        # print(sc1)
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_card=Label(update_verify_win,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_card.place(x=250,y=94)
                        #resend button
                        send_card_otp=Button(update_verify_win,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                        send_card_otp.place(x=198,y=130)

                        cr.execute(f'select phone from registration where card_no={sc1}')
                        fetchcard_phone=cr.fetchall()
                        for fpp in fetchcard_phone:
                            cpn=fpp[0]
                        # print(cpn)
                        #generate otp.........
                        viewotp=str(random.randint(1111,9999))
                        # print('otp is: ',viewotp)
                        #       
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        # account_sid = 'AC714959399352b0bebabaac962eb62449'
                        # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        # client = Client(account_sid, auth_token)
                        # too='+91'+cpn
                        # msg='Online Voting System\nFor card verification\nyour OTP is: '+viewotp
                        # client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                        '''--------------------- Testing Otp ----------------------'''  

                        otpnote_view='Only for Testing Purpose OTP: '+viewotp
                        testing=Label(update_verify_win,text=otpnote_view,font=('Regular',8),fg='red')
                        testing.place(x=5,y=0)

                        #update otp..............
                        cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                        db.commit()
                        # print('changed/update otp')
                        view_l=Button(update_verify_win,text='  ',fg='white',font=('Regular',15),bd=0,cursor='hand2',padx=10,width=70)
                        view_l.place(x=100,y=400)

                        ue_otp=StringVar()
                        def verify_ue_otp():
                            rs_otp=ue_otp.get()
                            cr.execute(f'select otp from registration where phone={cpn}')
                            f_otpdata=cr.fetchall()
                            for dotpp in f_otpdata:
                                ot=dotpp[0]

                            if ot==rs_otp:
                                # print('otp match')
                                Verifyotpp=Button(update_verify_win,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                                Verifyotpp.place(x=205,y=290)


                                def edit():
                                    update_verify_win.destroy()
                                    log_result=messagebox.askyesno('Login Required','You Can\'t Change/Update any Details Now\n It\'s Possiable After UpComming Update\n Our Team Workin On This System for better Upgrad...\n         \nAre You Want To Login Now ?')
                                    if log_result == True:
                                        LoginForm()

                                updatenow=Button(update_verify_win,text="Click here to Edit Your Details",font=("times new roman",14),bg="blue",fg="white",cursor="hand2", command=edit)
                                updatenow.place(x=155,y=390)

                                
                                







                                

                                

                        #verify otp..........
                        otp_t1=Label(update_verify_win,text='Enter OTP ',font=('Regular',18))
                        otp_t1.place(x=110,y=200)
                        otp_w1=Label(update_verify_win,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_w1.place(x=245,y=230)
                        otp_ee=Entry(update_verify_win,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                        otp_ee.place(x=245,y=200) 

                        Verifyotpp=Button(update_verify_win,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                        Verifyotpp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_card=Label(update_verify_win,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                        invalid_card.place(x=250,y=90)
                #label of phone number
                card_num=Label(update_verify_win,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
                card_num.place(x=50,y=55)
                #enter phone number
                card_num_e=Entry(update_verify_win,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                card_num_e.place(x=250,y=50)

                send_card_otp=Button(update_verify_win,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                send_card_otp.place(x=198,y=130)

                update_verify_win.mainloop()



            update_verify()

            
        #Track Application..................................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        def trackapplication():

            trackwin=Toplevel()
            trackwin.geometry('550x680+490+50')
            trackwin.wm_iconbitmap('icon/track.ico')
            trackwin.title('Track Application Status')
            trackwin.resizable(False,False)
            trackwin.config(background='#EAF6F6')
            db=sqlite3.connect('voting management system.db')
            cr=db.cursor()

            tid=StringVar()
            def aptrack():
                apno=tid.get()
                #print(apno)
                cr.execute('select application_no from registration')
                data=cr.fetchall()
                db.commit()
                for i in data:
                    a=i[0]
                    check=0
                    if apno==a:
                        check=1
                        break
                    else:
                        check=0        
                if check==1:
                    cr.execute(f'select card_no from registration where application_no={a}')
                    card_no=cr.fetchall()
                    for k in card_no:
                        card=k[0]
                    
                    w='You are Voter Id is ' +card            
                    track = Label(trackwin, text=w, font=('Regular', 16), fg='blue',width=45,bg='#EAF6F6')
                    track.place(x=0, y=270)
                else:
                    track1 = Label(trackwin, text='Please Enter Valid Application No', font=('Regular', 8), fg='red',bg='#EAF6F6')
                    track1.place(x=240, y=135)            


            L2=Label(trackwin,text='Application No :',font=('times new roman',20,'bold'),bg='#EAF6F6',fg='black',bd=0)
            L2.place(x=25,y=100)

            E1=Entry(trackwin,font=('times new roman',20,'bold'),textvar=tid)
            E1.place(x=240,y=100)

            B1_img=PhotoImage(file='button/appsearch.png')    
            B1=Button(trackwin,image=B1_img,bd=0,bg='#EAF6F6',fg='black',command=aptrack,cursor='hand2')
            B1.place(x=200,y=185)


            trackwin.mainloop()

        def adminlogin_from():    
            adlogwin=Toplevel()
            adlogwin.title('Administrator Login')
            adlogwin.geometry('550x670+485+25')
            adlogwin.wm_iconbitmap('icon/admin.ico')
            adlogwin.resizable(False,False)
            #frame bg image import
            fbg=PhotoImage(file='themes/adlog.png')
            login_background=Label(adlogwin,image=fbg,width=518,height=654)
            login_background.place(x=15,y=8)
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Database Connect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            null=0
            uid=StringVar()
            upass=StringVar()
            def adlogin():
                userid=uid.get()
                upassword=upass.get()
                    
                #userid.................
                userid_length=0
                userid_length=len(userid)
                if null == userid_length:
                    #validation.....                 
                    validation=Label(adlogwin,text='Please Enter User ID',font=('Regular',10),fg='red',bg='white')
                    validation.place(x=240,y=270)
                else:
                    #password..............
                    password_length=len(upassword)
                if null == password_length:
                    p='Please Enter Password'
                    validation=Label(adlogwin,text=p,font=('Regular',10),fg='red',bg='white')
                    validation.place(x=240,y=360)
                else:
                    cr.execute("select uid,password from admin")
                    data=cr.fetchall()
                    check=0
                    for i in data:
                        a=i[0]
                        b=i[1]

                        if userid==a and upassword==b:
                            check=1
                            break
                        else:
                            check=0
                    if check == 1:

                        #//////////////////////////////////////<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        # admin login successfull

                        adlogwin.destroy()   

                        adminwin=Toplevel()
                        adminwin.title('Admin Panel')
                        adminwin.geometry('600x600')
                        adminwin.minsize(600,400)
                        adminwin.wm_iconbitmap('icon/admin.ico')
                        adminwin.resizable(False,False)#maximize option disable
                        adminwin.attributes('-fullscreen',True)
                        adminwin.state('zoomed')#default open fullscreen
                        #-------------------------------------- Main Body ---------------------------------------- #
                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        #approved candidate
                        s=ttk.Style()
                        s.theme_use('clam')
                        s.configure('Treeview', rowheight=20)

                        tv1=ttk.Treeview(adminwin)
                        tv1['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16')
                        tv1.column('#0',width='0')
                        tv1.column('1',width='40')
                        tv1.column('2',width='150')
                        tv1.column('3',width='60')
                        tv1.column('4',width='50')
                        tv1.column('5',width='150')
                        tv1.column('6',width='70')
                        tv1.column('7',width='80')
                        tv1.column('8',width='100')
                        tv1.column('9',width='100')
                        tv1.column('10',width='50')
                        tv1.column('11',width='80')
                        tv1.column('12',width='80')
                        tv1.column('13',width='60')
                        tv1.column('14',width='88')
                        tv1.column('15',width='85')
                        tv1.column('16',width='80')

                        # name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,Voted by
                        tv1.heading('#0',text='+')
                        tv1.heading('1',text='Sl No')
                        tv1.heading('2',text='Name')
                        tv1.heading('3',text='DOB')
                        tv1.heading('4',text='Gender')
                        tv1.heading('5',text='Father Name')
                        tv1.heading('6',text='Phone No')
                        tv1.heading('7',text='Aadhaar No')
                        tv1.heading('8',text='Village')
                        tv1.heading('9',text='Post')
                        tv1.heading('10',text='Pin')
                        tv1.heading('11',text='District')
                        tv1.heading('12',text='State')
                        tv1.heading('13',text='Application No')
                        tv1.heading('14',text='Card No')
                        tv1.heading('15',text='Voting Status')
                        tv1.heading('16',text='Voted By')

                        def displayAll_1():
                            cr.execute('select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,account_status from registration')
                            adata=cr.fetchall()
                            fdata=0
                            a=0
                            tv1.delete(*tv1.get_children())
                            for i in adata:
                                f=i[12]
                                if f!='Not Generated':
                                    fdata += 1
                                    a += 1    
                                    tv1.insert(parent="", index="end", iid=i, text="", values=((a,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14])))
                        displayAll_1()



                        tv1.place(x=90,y=130)

                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        # not approve candidate..........

                        tv=ttk.Treeview(adminwin)
                        tv['columns']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16')
                        tv.column('#0',width='0')
                        tv.column('1',width='40')
                        tv.column('2',width='150')
                        tv.column('3',width='60')
                        tv.column('4',width='50')
                        tv.column('5',width='150')
                        tv.column('6',width='70')
                        tv.column('7',width='80')
                        tv.column('8',width='100')
                        tv.column('9',width='100')
                        tv.column('10',width='50')
                        tv.column('11',width='80')
                        tv.column('12',width='80')
                        tv.column('13',width='60')
                        tv.column('14',width='88')
                        tv.column('15',width='85')
                        tv.column('16',width='80')

                        # name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,Voted by
                        tv.heading('#0',text='+')
                        tv.heading('1',text='Sl No')
                        tv.heading('2',text='Name')
                        tv.heading('3',text='DOB')
                        tv.heading('4',text='Gender')
                        tv.heading('5',text='Father Name')
                        tv.heading('6',text='Phone No')
                        tv.heading('7',text='Aadhaar No')
                        tv.heading('8',text='Village')
                        tv.heading('9',text='Post')
                        tv.heading('10',text='Pin')
                        tv.heading('11',text='District')
                        tv.heading('12',text='State')
                        tv.heading('13',text='Application No')
                        tv.heading('14',text='Card No')
                        tv.heading('15',text='Voting Status')
                        tv.heading('16',text='Voted By')

                        def displayAll_2():
                            cr.execute('select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,application_no,card_no,voting_status,account_status from registration')
                            adata=cr.fetchall()
                            fdata=0
                            a=0
                            tv.delete(*tv.get_children())
                            for i in adata:
                                f=i[12]
                                if f=='Not Generated':
                                    fdata += 1
                                    a += 1    
                                    tv.insert(parent="", index="end", iid=i, text="", values=((a,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14])))
                        displayAll_2()
                        

                        tv.place(x=90,y=420)

                        #>......>>>>>>>>>>>>>>............>>>>>>>>>>>>>>>...................>>>>>>>>>>>>>>>>..............>>>>>>>>>>>>>>>>.
                        topnav=Label(adminwin,text='Welcome to Administrator Panel',font=('times new roman',28),fg='white',bg='blue')
                        topnav.pack(fill=X)

                        candidate=Label(adminwin,text='Approved Candidate Details',font=('times new roman',20),fg='blue')
                        candidate.place(x=90,y=90)

                        exit=Button(adminwin,text='Exit / Logout', font=('times new roman',14),fg='white',bg='#FF8B8B',command=lambda:adminwin.destroy(),cursor='hand2')
                        exit.place(x=1270,y=90)

                        notapcandidate=Label(adminwin,text='Not Approved Candidate Details',font=('times new roman',20),fg='blue')
                        notapcandidate.place(x=90,y=380)

                        def approved():
                            approvewin=Toplevel()
                            approvewin.title('Generate Card Number')
                            approvewin.geometry('550x680+485+25')
                            approvewin.wm_iconbitmap('icon/aprove.ico')
                            approvewin.resizable(False,False)

                            entcard=StringVar()
                            #send OTP
                            def sendcardotp():
                                ll=0
                                cardn=entcard.get()
                                cr.execute('select application_no,card_no from registration')
                                sc_data=cr.fetchall()
                                cfetch=0
                                for sc in sc_data:
                                    sc1=sc[0]
                                    crd=sc[1]
                                    if cardn==sc1:
                                        cfetch=1
                                        break
                                    else:
                                        cfetch=0

                                if ll != len(cardn):
                                    if cfetch==1:
                                        invalid_phone=Label(approvewin,text='',font=('times new roman',8),width=50)
                                        invalid_phone.place(x=265,y=90)
                                        
                                        if crd=='Not Generated': 
                                    
                                            invalid=Label(approvewin,text='',font=('times new roman',18),fg='red',width=30)
                                            invalid.place(x=135,y=300)

                                            c1=random.randint(1111111111,9999999999)
                                            cr.execute('update registration set card_no=? where application_no=?',(c1,sc1))
                                            db.commit()
                                            approvewin.destroy()
                                            apsuccesswin=Toplevel()    
                                            apsuccesswin.title('Generate Card Number')
                                            apsuccesswin.geometry('550x680+485+25')
                                            apsuccesswin.wm_iconbitmap('icon/aprove.ico')
                                            apsuccesswin.resizable(False,False)            

                                            warning_img=PhotoImage(file='logo/check.png')
                                            war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                            war_l.place(x=165,y=70)

                                            ge=Label(apsuccesswin,text="Successfully Generated Candidate Card Number...",font=('times new roman',14),fg='blue')
                                            ge.place(x=80,y=200) 
                                            displayAll_1()
                                            displayAll_2()                                        
                                            apsuccesswin.mainloop()
                                            entcard.set("")
                                        else:
                                            apsuccesswin=Toplevel()    
                                            apsuccesswin.title('Already Generate Card Number')
                                            apsuccesswin.geometry('550x680+485+25')
                                            apsuccesswin.wm_iconbitmap('icon/notap.ico')
                                            apsuccesswin.resizable(False,False)            
                                            
                                            warning_img=PhotoImage(file='logo/warning.png')
                                            war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                            war_l.place(x=165,y=70)

                                            ge=Label(apsuccesswin,text="Already Generated Card Number...",font=('times new roman',14),fg='blue')
                                            ge.place(x=135,y=200)                                
                                            apsuccesswin.mainloop()

                                    else:
                                        invalid=Label(approvewin,text='Invalid Application Number',font=('times new roman',18),fg='red')
                                        invalid.place(x=135,y=300)
                                else:
                                    invalid_phone=Label(approvewin,text='Please Enter Valid Application Number',font=('times new roman',8),fg='red')
                                    invalid_phone.place(x=265,y=90)

                            #label of phone number
                            card_num=Label(approvewin,text='Enter Application No: ',font=('times new roman',18,'bold'),fg='black',bd=0)
                            card_num.place(x=30,y=55)
                            #enter phone number
                            card_num_e=Entry(approvewin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                            card_num_e.place(x=265,y=50)

                            send_card_otp=Button(approvewin,text=' Generated ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                            send_card_otp.place(x=205,y=130)
                            approvewin.mainloop()

                        def suspend():
                            approvewin=Toplevel()
                            approvewin.title('Suspend / Delete User')
                            approvewin.geometry('550x680+485+25')
                            approvewin.wm_iconbitmap('icon/suspend.ico')
                            approvewin.resizable(False,False)

                            entcard=StringVar()
                            #send OTP
                            def sendcardotp():
                                cardn=entcard.get()
                                l=0                    
                                if l != len(cardn):
                                    cr.execute('select application_no,card_no,phone from registration')
                                    sc_data=cr.fetchall()
                                    cfetch=0
                                    for sc in sc_data:
                                        sc1=sc[0]
                                        crd=sc[1]
                                        ph=sc[2]
                                        if cardn==sc1 or cardn==crd:
                                            cfetch=1
                                            break
                                        else:
                                            cfetch=0
                    
                                    if cfetch==1:
                                        invalid_phone=Label(approvewin,text=' ',font=('times new roman',8),width=50)
                                        invalid_phone.place(x=265,y=90)

                                        invalid2=Label(approvewin,text=' ',font=('times new roman',18),fg='red',width=50,height=30)
                                        invalid2.place(x=25,y=300)


                                        cr.execute('delete from registration where phone=?',(ph,))
                                        db.commit()

                                        approvewin.destroy()
                                        apsuccesswin=Toplevel()         
                                        apsuccesswin.title('Generate Card Number')
                                        apsuccesswin.geometry('550x680+485+25')
                                        apsuccesswin.wm_iconbitmap('icon/suspend.ico')
                                        apsuccesswin.resizable(False,False)         

                                        warning_img=PhotoImage(file='logo/check.png')
                                        war_l=Label(apsuccesswin,image=warning_img,width=200,height=100)
                                        war_l.place(x=165,y=70)

                                        ge=Label(apsuccesswin,text="Candidate Card Number Permanently Deleted...",font=('times new roman',14),fg='red')
                                        ge.place(x=80,y=200)  
                                        displayAll_1()
                                        displayAll_2()          
                                        apsuccesswin.mainloop()
                                    else:                                
                                        invalid2=Label(approvewin,text='Enter Application / Card Number Already Suspend \nor\n Not Registered Our System',font=('times new roman',18),fg='red')
                                        invalid2.place(x=25,y=300)

                                else:
                                    invalid_phone=Label(approvewin,text='Enter Valid Application / Card Number',font=('times new roman',8),fg='red')
                                    invalid_phone.place(x=272,y=90)
                                    
                            
                            #label of phone number
                            card_num=Label(approvewin,text='Application / Card No: ',font=('times new roman',18,'bold'),fg='black',bd=0)
                            card_num.place(x=20,y=55)
                            #enter phone number
                            card_num_e=Entry(approvewin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
                            card_num_e.place(x=275,y=50)

                            send_card_otp=Button(approvewin,text=' Suspend ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                            send_card_otp.place(x=198,y=130)

                            approvewin.mainloop()



                        approve=Button(adminwin,text=' Generate Card Number', font=('times new roman',14),bg='#00FFDD',cursor='hand2',command=approved)
                        approve.place(x=520,y=700)

                        suspend=Button(adminwin,text='Suspend Candidate', font=('times new roman',14),bg='#FC4F4F',cursor='hand2',command=suspend)
                        suspend.place(x=780,y=700)

                        adminwin.mainloop()

                        #//////////////////////////////////////<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    else:
                        #cancel button img import
                        wp=Label(adlogwin,text='Wrong User ID or Password',bg='white',fg='red')
                        wp.place(x=195,y=180)                


            def forgetadminpass():
                forgetwin=Toplevel()
                forgetwin.title('Forget User ID or Password')
                forgetwin.geometry('550x680+485+25')
                forgetwin.wm_iconbitmap('icon/admin.ico')
                forgetwin.resizable(False,False)
                entphone=StringVar()
                #send OTP
                def sendotpp():
                    fphone_num=entphone.get()
                    cr.execute('select phone from admin')
                    fp_data=cr.fetchall()
                    fcheck=0
                    for ff in fp_data:
                        fp=ff[0]
                        if fphone_num==fp:
                            fcheck=1
                            break
                        else:
                            fcheck=0
                    if fcheck==1:
                        # print('phone nummber matched')
                        #hide invalid phone number error
                        invalid_phone=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                        invalid_phone.place(x=250,y=94)
                        #resend button
                        sendotp=Button(forgetwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                        sendotp.place(x=198,y=130)

                        '''------------------------------------------------------'''
                        #generate otp.........
                        fotp=str(random.randint(1111,9999))
                        #print('otp is: ',fotp)
                        #              
                        '''-------------------TESTING OTP-------------------------'''

                        '''------------------Twillo OTP Service------------------'''
                        account_sid = 'AC714959399352b0bebabaac962eb62449'
                        auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                        client = Client(account_sid, auth_token)
                        too='+91'+fp
                        msg='Online Voting System\nForget Admin Password OTP: '+fotp
                        client.messages.create(body=msg,from_='+19788308309',to=too)

                        '''-------------------------------------------------------'''

                        #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
                        '''--------------------- Testing Otp ----------------------'''          
                        otpnote='Only for Testing Purpose OTP: '+fotp
                        testing=Label(forgetwin,text=otpnote,font=('Regular',8),fg='red')
                        testing.place(x=5,y=650)

                        #update otp..............
                        cr.execute('update admin set otp=? where phone=?',(fotp,fp))
                        db.commit()
                        #print('changed otp')

                        rotp=StringVar()
                        def verifyfotp():
                            rsotp=rotp.get()
                            cr.execute(f'select uid,otp from admin where phone={fp}')
                            fetchotp=cr.fetchall()
                            for fe in fetchotp:
                                ud=fe[0]
                                dotp=fe[1]

                            #if matched otp............
                            if dotp==rsotp:
                                #hide invalid otp error
                                invalid_OTP=Label(forgetwin,text=' ',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)
                                #verified otp button
                                Verifyotp=Button(forgetwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                                Verifyotp.place(x=205,y=290)

                                pass1=StringVar()
                                pass2=StringVar()
                                def changepass():
                                    pass11=pass1.get()
                                    pass22=pass2.get()
                                    if pass11==pass22:
                                        cr.execute('update admin set password=? where phone=?',(pass11,fp))
                                        db.commit()
                                        # print('pass changed')  

                                        #close forgetwindow............
                                        forgetwin.destroy()

                                        changedwin=Toplevel()
                                        changedwin.title('Successfully changed Password')
                                        changedwin.geometry('550x680+485+25')
                                        changedwin.wm_iconbitmap('icon/login.ico')
                                        changedwin.resizable(False,False)
                                        changedwin.overrideredirect()


                                        ch_img=PhotoImage(file='logo/check.png')
                                        ch_l=Label(changedwin,image=ch_img)
                                        ch_l.place(x=215,y=100)

                                        ph_l=Label(changedwin,text='Your Password Successfully changed',font=('times new roman',20),fg='blue')
                                        ph_l.place(x=70,y=230)

                                        changedwin.mainloop()

                                    else:
                                        # print('conform pass not match')
                                        #password not match
                                        invalid_pass=Label(forgetwin,text='Conform Password Not Matched',font=('times new roman',8),fg='red')
                                        invalid_pass.place(x=250,y=462)

                                #import password image
                                pass_f=Label(forgetwin,text='New Password',font=('times new roman',18),bg='white')
                                pass_f.place(x=80,y=400)
                                #entry password
                                pass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,textvar=pass1)
                                pass_fe.place(x=250,y=400)
                                #import conform password image
                                con_pass_e=Label(forgetwin,text='Re... Password',font=('times new roman',18),bg='white')
                                con_pass_e.place(x=80,y=450)
                                #entry conform password
                                conpass_fe=Entry(forgetwin,font=('timew new roman',18),bd=1,bg='#EFEFE0',width=15,show='*',textvar=pass2)
                                conpass_fe.place(x=250,y=450)

                                #import uid
                                uuid='Your User ID: '+ud
                                puid_f=Label(forgetwin,text=uuid,font=('times new roman',14),fg='red')
                                puid_f.place(x=180,y=345)


                                #login button img import
                                #sub1_img=PhotoImage(file='button/u_login.png')
                                sub11=Button(forgetwin,text='Submit',font=('Regular',18),fg='white',bg='#3CCF4E',cursor='hand2',command=changepass)
                                sub11.place(x=145,y=550)
                                #cancel button img import
                                #canc_bg=PhotoImage(file='button/cancel.png')
                                canc1=Button(forgetwin,text='Cancel',font=('Regular',18),fg='white',bg='#F55353',cursor='hand2',command=lambda:forgetwin.destroy())
                                canc1.place(x=295,y=550)  
                            else:
                                # print('Please Enter Valid OTP')
                                invalid_OTP=Label(forgetwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                                invalid_OTP.place(x=134,y=231)



                        #verify otp..........
                        otp_l1=Label(forgetwin,text='Enter OTP ',font=('Regular',18))
                        otp_l1.place(x=110,y=200)
                        otp_s1=Label(forgetwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                        otp_s1.place(x=245,y=230)
                        otp_e1=Entry(forgetwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=rotp)
                        otp_e1.place(x=245,y=200) 

                        Verifyotp=Button(forgetwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verifyfotp)
                        Verifyotp.place(x=205,y=290)
                    else:
                        #print('Phone number not match')
                        invalid_phone=Label(forgetwin,text='Please Enter Registered Phone Number',font=('times new roman',8),fg='red')
                        invalid_phone.place(x=250,y=90)

                #label of phone number
                fphone=Label(forgetwin,text='Phone Number :',font=('times new roman',18,'bold'),fg='black',bd=0)
                fphone.place(x=50,y=50)
                #enter phone number
                fphone_e=Entry(forgetwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entphone)
                fphone_e.place(x=250,y=50)


                sendotp=Button(forgetwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendotpp)
                sendotp.place(x=198,y=130)

                forgetwin.mainloop()



            #uid label img import
            uid_bg=PhotoImage(file='button/uid.png')
            uid_l=Label(adlogwin,image=uid_bg,bd=0,bg='white')
            uid_l.place(x=70,y=230)

            #uid input   ----*** Entry Box ***----
            uid_e=Entry(adlogwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',textvar=uid)
            uid_e.place(x=240,y=232)

            #password label img import
            pass_bg=PhotoImage(file='button/password.png')
            password=Label(adlogwin,image=pass_bg,bd=0,bg='white')
            password.place(x=70,y=310)

            #password input  ----*** Entry Box ***----
            pass_e=Entry(adlogwin,font=('times new roman',24),bd=1,width=15,bg='#EFEFE0',show='*',textvar=upass)
            pass_e.place(x=240,y=312)


            #login button img import
            log_bg=PhotoImage(file='button/login.png')
            login=Button(adlogwin,image=log_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=adlogin)
            login.place(x=70,y=410)

            #cancel button img import
            cancel_bg=PhotoImage(file='button/cancel.png')
            cancel=Button(adlogwin,image=cancel_bg,bd=0,bg='white',activebackground='white',cursor='hand2',command=lambda:adlogwin.destroy())
            cancel.place(x=240,y=410)

            #forget button img import
            #forget_bg=PhotoImage(file='button/forget.png')
            forget=Button(adlogwin,text='Forget User ID or Pasword?',font=('Regular',11),bd=0,bg='white',fg='blue',activebackground='white',cursor='hand2',command=forgetadminpass)
            forget.place(x=75,y=480)

            adlogwin.mainloop()


        #screen-1
        def setting():
            setting_root=Toplevel()
            setting_root.geometry('100x200+1405+610')
            setting_root.overrideredirect(True)
            setting_root.config(bg='#C9C5C5')

            def set_s():
                exit_res=messagebox.askyesno('Exit','Are you sure you want to Close This Application?')
                if exit_res==True:
                    root.destroy()


                    # function 
                    page_url = 'https://github.com/Developer-Amit-Mandal/Online-Voting-Management-System#online-voting-management-system-dashboard'

                    def open_url():
                        try: 
                            webbrowser.open_new(page_url)
                            print('Opening URL...')  
                        except: 
                            print('Failed to open URL. Unsupported variable type.')

                    # initialize 
                    toaster = ToastNotifier()

                    # showcase
                    toaster.show_toast(
                        "Online Voting Management System 1.0",
                        "Thank you for Using, Visit  For More Info..",
                        icon_path= 'icon/votingicon.ico', threaded=True, callback_on_click=open_url, duration=10
                        )
                

            themeimg=PhotoImage(file='button/set.png')
            theme_appm=Label(setting_root,bd=0,image=themeimg,background='#C9C5C5')
            theme_appm.pack()

            close_app_img=PhotoImage(file='button/exitset.png')
            close_app=Button(setting_root,bd=0,image=close_app_img,cursor='hand2',background='white',activebackground='white',command=set_s)
            close_app.place(x=25,y=25)

            def theme_old():
                root.destroy()
                old_dashboard()
                

          
            theme_app_img=PhotoImage(file='button/change.png')
            theme_app=Button(setting_root,bd=0,image=theme_app_img,cursor='hand2',background='white',activebackground='white',command=theme_old)
            theme_app.place(x=25,y=85)
            

            themephoto=PhotoImage(file='button/cross.png')
            theme_color=Button(setting_root,bd=0,image=themephoto,cursor='hand2',background='white',activebackground='white',command=lambda:setting_root.destroy())
            theme_color.place(x=30,y=150)


            setting_root.mainloop()     

            
        


        #------------------------------------ Top Nav Area --------------------------------------- #
        #Background Themes
        theme_img=PhotoImage(file='themes/background_theme.png')
        theme=Label(root,image=theme_img)
        theme.pack()

        #Top Nav button------------->

        #About Button
        about_logo=PhotoImage(file='button/about.png')
        about_button=Button(theme,image=about_logo,bd=0,bg='#1A1A1A',activebackground='#1A1A1A',cursor='hand2',command=about)
        about_button.place(x=1350,y=14)

        #feedback.........
        feedback_logo=PhotoImage(file='button/feedback.png')
        feedback_button=Button(theme,image=feedback_logo,bd=0,bg='#1A1A1A',activebackground='#1A1A1A',cursor='hand2',command=feedback)
        feedback_button.place(x=1180,y=14)

        #Admin Button
        admin_logo=PhotoImage(file='button/adminlogin.png')
        admin_button=Button(theme,image=admin_logo,bd=0,bg='#1A1A1A',cursor='hand2',activebackground='#1A1A1A',command=adminlogin_from)
        admin_button.place(x=1005,y=14)
        
        #title img......
        vote_title=Label(theme,text='Online Voting Management System',bd=0,bg='#1A1A1A',fg='white',font=('Regular',24))
        vote_title.place(x=40,y=14)
        
        #------------------------------------ Top Nav End --------------------------------------- #






        #------------------------------------- Main Body End -------------------------------------- #

        #################################### Voting Count Area ######################################
        # l1=Label(theme,height=8,width=20,bg='red')
        # l1.place(x=50,y=120)

        # l2=Label(theme,height=8,width=20,bg='blue')
        # l2.place(x=230,y=120)

        # l3=Label(theme,height=8,width=20,bg='blue')
        # l3.place(x=410,y=120)

        # l3=Label(theme,height=8,width=20,bg='blue')
        # l3.place(x=590,y=120)





        def viewvoter_card():
            viewcardwin=Toplevel()
            viewcardwin.title('View Voter Card')
            viewcardwin.geometry('550x680+485+25')
            viewcardwin.wm_iconbitmap('icon/ind.ico')
            viewcardwin.resizable(False,False)

            entcard=StringVar()
            #send OTP
            def sendcardotp():
                cardn=entcard.get()
                cr.execute('select card_no from registration')
                sc_data=cr.fetchall()
                cfetch=0
                for sc in sc_data:
                    sc1=sc[0]
                    if cardn==sc1:
                        cfetch=1
                        break
                    else:
                        cfetch=0
                if cfetch==1:
                    # print('valid card number')
                    # print(sc1)
                    # print('phone nummber matched')
                    #hide invalid phone number error
                    invalid_card=Label(viewcardwin,text=' ',font=('times new roman',8),fg='red',width=50)
                    invalid_card.place(x=250,y=94)
                    #resend button
                    send_card_otp=Button(viewcardwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                    send_card_otp.place(x=198,y=130)

                    cr.execute(f'select phone from registration where card_no={sc1}')
                    fetchcard_phone=cr.fetchall()
                    for fpp in fetchcard_phone:
                        cpn=fpp[0]
                    # print(cpn)
                    #generate otp.........
                    viewotp=str(random.randint(1111,9999))
                    # print('otp is: ',viewotp)
                    #       
                    '''-------------------TESTING OTP-------------------------'''

                    '''------------------Twillo OTP Service------------------'''
                    # account_sid = 'AC714959399352b0bebabaac962eb62449'
                    # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                    # client = Client(account_sid, auth_token)
                    # too='+91'+cpn
                    # msg='Online Voting System\nYour card verification OTP is: '+viewotp
                    # client.messages.create(body=msg,from_='+19788308309',to=too)

                    '''-------------------------------------------------------'''

                    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                    '''--------------------- Testing Otp ----------------------'''  

                    otpnote_view='Only for Testing Purpose OTP: '+viewotp
                    testing=Label(viewcardwin,text=otpnote_view,font=('Regular',8),fg='red')
                    testing.place(x=5,y=0)
                    #update otp..............
                    cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                    db.commit()
                    # print('changed/update otp')

                    ue_otp=StringVar()
                    def verify_ue_otp():
                        rs_otp=ue_otp.get()
                        cr.execute(f'select otp from registration where phone={cpn}')
                        f_otpdata=cr.fetchall()
                        for dotpp in f_otpdata:
                            ot=dotpp[0]

                        if ot==rs_otp:
                            # print('otp match')
                            Verifyotpp=Button(viewcardwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                            Verifyotpp.place(x=205,y=290)

                            def view():
                                #successfully login  
                                cv=Toplevel()
                                cv.title('View Voter Card')
                                cv.geometry('550x680+485+25')
                                cv.wm_iconbitmap('icon/ind.ico')
                                cv.resizable(False,False)
                                #successfully login  
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''---------------------- Profile Area----------------------'''
                                #bg thems..............
                                vc_p=PhotoImage(file='themes/cardimg.png')
                                vc_l=Label(cv,image=vc_p)
                                vc_l.place(x=70,y=120)

                                fp = io.BytesIO(myphoto)
                                # load the image
                                image = Image.open(fp)
                                res=image.resize((85,100))
                                # drawing image to top window
                                userimg = ImageTk.PhotoImage(res)                      

                                userphoto=Label(cv,image=userimg)
                                userphoto.place(x=125,y=185)
                                #------------------------------------
                                #card no
                                ucard_no=Label(cv,text='Voter ID: ',font=('Regular',8),bg='#44FFDD')
                                ucard_no.place(x=111,y=295)

                                ucard_p=Label(cv,text=cd,font=('Regular',8),bg='#44FFDD')
                                ucard_p.place(x=160,y=295)

                                #>>>>>>>>>>>>>>>>>>>>>>>

                                #name
                                uname=Label(cv,text='Name: ',font=('Regular',8),bg='#44FFDD')
                                uname.place(x=90,y=325)
                                uname_p=Label(cv,text=n,font=('Regular',8),bg='#44FFDD')
                                uname_p.place(x=170,y=325)

                                #father name
                                fname=Label(cv,text='Father Name: ',font=('Regular',8),bg='#44FFDD')
                                fname.place(x=90,y=349)
                                fname_p=Label(cv,text=f,font=('Regular',8),bg='#44FFDD')
                                fname_p.place(x=170,y=349)

                                #gender
                                ugender=Label(cv,text='Gender: ',font=('Regular',8),bg='#44FFDD')
                                ugender.place(x=90,y=373)
                                ugender_p=Label(cv,text=g,font=('Regular',8),bg='#44FFDD')
                                ugender_p.place(x=170,y=373)

                                # #date of birth
                                udob=Label(cv,text='Date Of Birth: ',font=('Regular',8),bg='#44FFDD')
                                udob.place(x=90,y=398)
                                udob_p=Label(cv,text=d,font=('Regular',8),bg='#44FFDD')
                                udob_p.place(x=170,y=398)

                                # #phone no
                                # uphone=Label(cv,text='Phone Number : ',font=('Regular',8),bg='#44FFDD')
                                # uphone.place(x=70,y=370)
                                # uphone_p=Label(cv,text=p,font=('Regular',8),bg='#44FFDD')
                                # uphone_p.place(x=170,y=370)

                                # #aadhaar no
                                # uaadhaar=Label(cv,text='Linked Aadhaar: ',font=('Regular',8),bg='#44FFDD')
                                # uaadhaar.place(x=70,y=400)
                                # uaadhaar_p=Label(cv,text=aah,font=('Regular',8),bg='#44FFDD')
                                # uaadhaar_p.place(x=170,y=400)

                                # uvstatus=Label(cv,text='Voting Status _: ',font=('Regular',8),bg='#44FFDD')
                                # uvstatus.place(x=70,y=430)
                                # uvstatus_p=Label(cv,text=vs,font=('Regular',8),bg='#44FFDD',fg='red')
                                # uvstatus_p.place(x=170,y=430)

                                # #>>>>>>>>>>>>
                                #village
                                uvill=Label(cv,text='Vill: ',font=('Regular',8),bg='#44FFDD')
                                uvill.place(x=300,y=145)
                                uvill_p=Label(cv,text=vill,font=('Regular',8),bg='#44FFDD')
                                uvill_p.place(x=340,y=145)

                                #post
                                upost=Label(cv,text='Post: ',font=('Regular',8),bg='#44FFDD')
                                upost.place(x=300,y=165)
                                upost=Label(cv,text=po,font=('Regular',8),bg='#44FFDD')
                                upost.place(x=340,y=165)

                                #Pin
                                upin=Label(cv,text='Pin : ',font=('Regular',8),bg='#44FFDD')
                                upin.place(x=300,y=187)
                                upin=Label(cv,text=pin,font=('Regular',8),bg='#44FFDD')
                                upin.place(x=340,y=187)

                                #district
                                udist=Label(cv,text='Dist: ',font=('Regular',8),bg='#44FFDD')
                                udist.place(x=300,y=207)
                                udist=Label(cv,text=dist,font=('Regular',8),bg='#44FFDD')
                                udist.place(x=340,y=207)

                                #signature........
                                sign_img=PhotoImage(file='img/sig.png')
                                sig_l=Label(cv,image=sign_img,bg='#44FFDD')
                                sig_l.place(x=355,y=235)
                                cv.mainloop()
                            view()
                            # view_l=Button(viewcardwin,text=' View Card ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=view)
                            # view_l.place(x=205,y=380)
                        else:
                            # print('Please Enter Valid OTP')
                            invalid_OTP=Label(viewcardwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                            invalid_OTP.place(x=134,y=231)

                    #verify otp..........
                    otp_t1=Label(viewcardwin,text='Enter OTP ',font=('Regular',18))
                    otp_t1.place(x=110,y=200)
                    otp_w1=Label(viewcardwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                    otp_w1.place(x=245,y=230)
                    otp_ee=Entry(viewcardwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                    otp_ee.place(x=245,y=200) 

                    Verifyotpp=Button(viewcardwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                    Verifyotpp.place(x=205,y=290)
                else:
                    #print('Phone number not match')
                    invalid_card=Label(viewcardwin,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                    invalid_card.place(x=250,y=90)
            #label of phone number
            card_num=Label(viewcardwin,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
            card_num.place(x=50,y=55)
            #enter phone number
            card_num_e=Entry(viewcardwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
            card_num_e.place(x=250,y=50)

            send_card_otp=Button(viewcardwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
            send_card_otp.place(x=198,y=130)
            viewcardwin.mainloop()



        def download():
            viewcardwin=Toplevel()
            viewcardwin.title('Download Voter Card')
            viewcardwin.geometry('550x680+485+25')
            viewcardwin.wm_iconbitmap('icon/download.ico')
            viewcardwin.resizable(False,False)    

            entcard=StringVar()
            #send OTP
            def sendcardotp():
                cardn=entcard.get()
                cr.execute('select card_no from registration')
                sc_data=cr.fetchall()
                cfetch=0
                for sc in sc_data:
                    sc1=sc[0]
                    if cardn==sc1:
                        cfetch=1
                        break
                    else:
                        cfetch=0
                if cfetch==1:
                    # print('valid card number')
                    # print(sc1)
                    # print('phone nummber matched')
                    #hide invalid phone number error
                    invalid_card=Label(viewcardwin,text=' ',font=('times new roman',8),fg='red',width=50)
                    invalid_card.place(x=250,y=94)
                    #resend button
                    send_card_otp=Button(viewcardwin,text=' Resend OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
                    send_card_otp.place(x=198,y=130)

                    cr.execute(f'select phone from registration where card_no={sc1}')
                    fetchcard_phone=cr.fetchall()
                    for fpp in fetchcard_phone:
                        cpn=fpp[0]
                    # print(cpn)
                    #generate otp.........
                    viewotp=str(random.randint(1111,9999))
                    # print('otp is: ',viewotp)
                    #       
                    '''-------------------TESTING OTP-------------------------'''

                    '''------------------Twillo OTP Service------------------'''
                    # account_sid = 'AC714959399352b0bebabaac962eb62449'
                    # auth_token = 'bd34f59f0b125972149e401266a9e3e2'
                    # client = Client(account_sid, auth_token)
                    # too='+91'+cpn
                    # msg='Online Voting System\nFor card verification\nyour OTP is: '+viewotp
                    # client.messages.create(body=msg,from_='+19788308309',to=too)

                    '''-------------------------------------------------------'''

                    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

                    '''--------------------- Testing Otp ----------------------'''  

                    otpnote_view='Only for Testing Purpose OTP: '+viewotp
                    testing=Label(viewcardwin,text=otpnote_view,font=('Regular',8),fg='red')
                    testing.place(x=5,y=0)

                    #update otp..............
                    cr.execute('update registration set otp=? where phone=?',(viewotp,cpn))
                    db.commit()
                    # print('changed/update otp')
                    view_l=Button(viewcardwin,text='  ',fg='white',font=('Regular',15),bd=0,cursor='hand2',padx=10,width=70)
                    view_l.place(x=100,y=400)

                    df_d1=Label(viewcardwin,text='  ',fg='white',font=('Regular',11),padx=20,width=100)
                    df_d1.place(x=102,y=520) 

                    df_d=Label(viewcardwin,text='  ',fg='white',font=('Regular',15),padx=20,width=100)
                    df_d.place(x=123,y=480) 

                    ue_otp=StringVar()
                    def verify_ue_otp():
                        rs_otp=ue_otp.get()
                        cr.execute(f'select otp from registration where phone={cpn}')
                        f_otpdata=cr.fetchall()
                        for dotpp in f_otpdata:
                            ot=dotpp[0]

                        if ot==rs_otp:
                            # print('otp match')
                            Verifyotpp=Button(viewcardwin,text='✓ Verified ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                            Verifyotpp.place(x=205,y=290)

                            def view():
                                #successfully login  
                                cv=Toplevel()
                                cv.title('View Voter Card')
                                cv.geometry('550x680+485+25')
                                cv.wm_iconbitmap('icon/ind.ico')
                                cv.resizable(False,False)
                                #successfully login  
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''---------------------- Profile Area----------------------'''
                                
                                #bg thems..............
                                vc_p=PhotoImage(file='themes/cardimg.png')
                                vc_l=Label(cv,image=vc_p)
                                vc_l.place(x=70,y=120)

                                #////////////////////////////////                        
                                fp = io.BytesIO(myphoto)
                                # load the image
                                image = Image.open(fp)
                                res=image.resize((85,100))
                                # drawing image to top window
                                userimg = ImageTk.PhotoImage(res)                      

                                userphoto=Label(cv,image=userimg)
                                userphoto.place(x=125,y=185)
                                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                #------------------------------------
                                #card no
                                ucard_no=Label(cv,text='Voter ID: ',font=('Regular',8),bg='#44FFDD')
                                ucard_no.place(x=111,y=295)

                                ucard_p=Label(cv,text=cd,font=('Regular',8),bg='#44FFDD')
                                ucard_p.place(x=160,y=295)

                                #>>>>>>>>>>>>>>>>>>>>>>>

                                #name
                                uname=Label(cv,text='Name: ',font=('Regular',8),bg='#44FFDD')
                                uname.place(x=90,y=325)
                                uname_p=Label(cv,text=n,font=('Regular',8),bg='#44FFDD')
                                uname_p.place(x=170,y=325)

                                #father name
                                fname=Label(cv,text='Father Name: ',font=('Regular',8),bg='#44FFDD')
                                fname.place(x=90,y=349)
                                fname_p=Label(cv,text=f,font=('Regular',8),bg='#44FFDD')
                                fname_p.place(x=170,y=349)

                                #gender
                                ugender=Label(cv,text='Gender: ',font=('Regular',8),bg='#44FFDD')
                                ugender.place(x=90,y=373)
                                ugender_p=Label(cv,text=g,font=('Regular',8),bg='#44FFDD')
                                ugender_p.place(x=170,y=373)

                                # #date of birth
                                udob=Label(cv,text='Date Of Birth: ',font=('Regular',8),bg='#44FFDD')
                                udob.place(x=90,y=398)
                                udob_p=Label(cv,text=d,font=('Regular',8),bg='#44FFDD')
                                udob_p.place(x=170,y=398)

                                # #phone no
                                # uphone=Label(cv,text='Phone Number : ',font=('Regular',8),bg='#44FFDD')
                                # uphone.place(x=70,y=370)
                                # uphone_p=Label(cv,text=p,font=('Regular',8),bg='#44FFDD')
                                # uphone_p.place(x=170,y=370)

                                # #aadhaar no
                                # uaadhaar=Label(cv,text='Linked Aadhaar: ',font=('Regular',8),bg='#44FFDD')
                                # uaadhaar.place(x=70,y=400)
                                # uaadhaar_p=Label(cv,text=aah,font=('Regular',8),bg='#44FFDD')
                                # uaadhaar_p.place(x=170,y=400)

                                # uvstatus=Label(cv,text='Voting Status _: ',font=('Regular',8),bg='#44FFDD')
                                # uvstatus.place(x=70,y=430)
                                # uvstatus_p=Label(cv,text=vs,font=('Regular',8),bg='#44FFDD',fg='red')
                                # uvstatus_p.place(x=170,y=430)

                                # #>>>>>>>>>>>>
                                #village
                                uvill=Label(cv,text='Vill: ',font=('Regular',8),bg='#44FFDD')
                                uvill.place(x=300,y=145)
                                uvill_p=Label(cv,text=vill,font=('Regular',8),bg='#44FFDD')
                                uvill_p.place(x=340,y=145)

                                #post
                                upost=Label(cv,text='Post: ',font=('Regular',8),bg='#44FFDD')
                                upost.place(x=300,y=165)
                                upost=Label(cv,text=po,font=('Regular',8),bg='#44FFDD')
                                upost.place(x=340,y=165)

                                #Pin
                                upin=Label(cv,text='Pin : ',font=('Regular',8),bg='#44FFDD')
                                upin.place(x=300,y=187)
                                upin=Label(cv,text=pin,font=('Regular',8),bg='#44FFDD')
                                upin.place(x=340,y=187)

                                #district
                                udist=Label(cv,text='Dist: ',font=('Regular',8),bg='#44FFDD')
                                udist.place(x=300,y=207)
                                udist=Label(cv,text=dist,font=('Regular',8),bg='#44FFDD')
                                udist.place(x=340,y=207)

                                #signature........
                                sign_img=PhotoImage(file='img/sig.png')
                                sig_l=Label(cv,image=sign_img,bg='#44FFDD')
                                sig_l.place(x=355,y=235)
                                cv.mainloop()

                            def createpdf():  
                                df_d1=Label(viewcardwin,text='  ',fg='white',font=('Regular',11),padx=20,width=100)
                                df_d1.place(x=102,y=520) 

                                df_d=Label(viewcardwin,text='  ',fg='white',font=('Regular',15),padx=20,width=100)
                                df_d.place(x=123,y=480) 
                                # Progress bar widget                            
                                progress = ttk.Progressbar(viewcardwin, orient = HORIZONTAL,length = 300, mode = 'determinate')
                                # of the progress bar value
                                def bar():
                                    import time
                                    progress['value'] = 20
                                    root.update_idletasks()
                                    time.sleep(1)
                                    progress['value'] = 60
                                    root.update_idletasks()
                                    time.sleep(1)
                                    progress['value'] = 100  
                                progress.place(x=125,y=480)                            
                                bar()


                                #select data from data base....                        
                                cr.execute(f'select name,dob,gender,father_name,phone,aadhaar,village,post,pin,dist,state,card_no,voting_status,photo from registration where phone={cpn}')
                                data=cr.fetchall()
                                for i in data:
                                    n=i[0]
                                    d=i[1]
                                    g=i[2]
                                    f=i[3]
                                    p=i[4]
                                    aah=i[5]
                                    vill=i[6]
                                    po=i[7]
                                    pin=i[8]
                                    dist=i[9]
                                    state=i[10]
                                    cd=i[11]
                                    vs=i[12]
                                    myphoto=i[13]

                                '''---------------------- Profile Area----------------------'''    
                                #------------------------------------
                                #card no
                                cardnum='Voter ID: '
                                cd #card number
                                carduser_name='Name: '
                                n #holder name
                                father='Father Name: '
                                f #father name
                                gender='Gender: '
                                g #gender
                                dob='Date Of Birth: '
                                d #dob..
                                phone='Phone Number : '
                                p #phone    

                                village='Vill: '
                                vill
                                post='Post'
                                po
                                pn='Pin : '
                                pin
                                dst='Dist: '
                                dist
                                st='State: '
                                state  
                                
                                #step 1
                                def convert_data(data, file_name):     
                                    # Convert binary format to
                                    # images or files data
                                    with open(file_name, 'wb') as file:
                                        file.write(data)
                                    img = Image.open(file_name)
                                    #declear image type global
                                    global image_type
                                    image_type=img.format  
                                    # print(image_type) 
                                img_path=os.getcwd()+'\\temp\\'+cd+'.png'
                                convert_data(myphoto,img_path)
                                tc=image_type.lower()
                                
                                #step 2    
                                if(image_type != 'PNG'):    
                                    os.remove(img_path)
                                    # print('not png')
                                    def convert_data(data, file_name):     
                                        # Convert binary format to
                                        # images or files data
                                        with open(file_name, 'wb') as file:
                                            file.write(data)
                                        img = Image.open(file_name)
                                        #declear image type global
                                        global image_type
                                        image_type=img.format  
                                        # print(image_type) 
                                    img_path=os.getcwd()+'\\temp\\'+cd+'.'+tc
                                    convert_data(myphoto,img_path)


                                pdf=FPDF()
                                pdf.add_page()
                                pdf.image('themes/cardimg.png',x=33,y=20)
                                pdf.image('temp/'+cd+'.'+tc,56,42,25,30)
                                pdf.image('img/sig.png',x=135,y=70)
                                pdf.set_font("Arial",size=10) #set font size 10
                                pdf.set_text_color(0,0,0)
                                #>>>>>>>>>>>>>>>>>> font  <<<<<<<<<<<<<<<<<<<<<<<
                                pdf.text(52,80,txt=cardnum)
                                pdf.text(67,80,txt=cd)

                                pdf.set_font("Arial",size=10) #set font size 8

                                pdf.text(38,90,txt=carduser_name)
                                pdf.text(64,90,txt=n)

                                pdf.text(38,98,txt=father)
                                pdf.text(64,98,txt=f)
                                
                                pdf.text(38,106,txt=gender)
                                pdf.text(64,106,txt=g)

                                pdf.text(38,114,txt=dob)
                                pdf.text(64,114,txt=d)

                                pdf.text(38,122,txt=phone)
                                pdf.text(64,122,txt=p)

                                #>>>>>>>>>>>>>>>>>> Back  <<<<<<<<<<<<<<<<<<<<<<<
                                pdf.text(114,32,txt=village)
                                pdf.text(125,32,txt=vill)

                                pdf.text(114,40,txt=post)
                                pdf.text(125,40,txt=po)

                                pdf.text(114,48,txt=pn)
                                pdf.text(125,48,txt=pin)

                                pdf.text(114,56,txt=dst)
                                pdf.text(125,56,txt=dist)

                                pdf.text(114,64,txt=st)
                                pdf.text(125,64,txt=state)                                         
            
                                path=os.environ['USERPROFILE']
                                savefile=path+'\\'+'OneDrive\Desktop\\'+cd+'.pdf'
                                pdf.output(savefile)

                                #delete temp img
                                os.remove(img_path)
                                
                                showpath='Path: '+savefile
                                df_d1=Label(viewcardwin,text=showpath,fg='red',font=('Regular',11),padx=20)
                                df_d1.place(x=102,y=520) 

                                df_d=Label(viewcardwin,text='File Downloaded On Desktop',fg='white',font=('Regular',15),bg='red',padx=20)
                                df_d.place(x=123,y=480) 

                            down_l=Button(viewcardwin,text='  Download  ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=createpdf)
                            down_l.place(x=120,y=400)

                            view_l=Button(viewcardwin,text=' View Card ',fg='white',font=('Regular',15),bd=0,bg='green',cursor='hand2',padx=10,command=view)
                            view_l.place(x=300,y=400)    
                        
                            #>>>>>>>>>>>>
                        else:
                            # print('Please Enter Valid OTP')
                            invalid_OTP=Label(viewcardwin,text='Enter Valid OTP',font=('times new roman',8),fg='red',width=50)
                            invalid_OTP.place(x=134,y=231)

                    #verify otp..........
                    otp_t1=Label(viewcardwin,text='Enter OTP ',font=('Regular',18))
                    otp_t1.place(x=110,y=200)
                    otp_w1=Label(viewcardwin,text='OTP Send Your Mobile Number',font=('Regular',8))
                    otp_w1.place(x=245,y=230)
                    otp_ee=Entry(viewcardwin,font=('Regular',18),bg='#DFF6FF',width=13,textvar=ue_otp)
                    otp_ee.place(x=245,y=200) 

                    Verifyotpp=Button(viewcardwin,text='Verify OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=verify_ue_otp)
                    Verifyotpp.place(x=205,y=290)
                else:
                    #print('Phone number not match')
                    invalid_card=Label(viewcardwin,text='Please Enter Voter ID',font=('times new roman',8),fg='red')
                    invalid_card.place(x=250,y=90)
            #label of phone number
            card_num=Label(viewcardwin,text='Enter Voter ID :',font=('times new roman',18,'bold'),fg='black',bd=0)
            card_num.place(x=50,y=55)
            #enter phone number
            card_num_e=Entry(viewcardwin,font=('Regular',24),width=14,bg='#D4F6CC',textvar=entcard)
            card_num_e.place(x=250,y=50)

            send_card_otp=Button(viewcardwin,text='✓ Send OTP ',fg='white',font=('Regular',15),bd=0,bg='#1BB3A5',cursor='hand2',padx=10,command=sendcardotp)
            send_card_otp.place(x=198,y=130)


            viewcardwin.mainloop()

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        #################################### User Panel / Area  #######################################

        #button theme...
        button_area_theme=PhotoImage(file='themes/back_theme_vt.png')
        button_area_img=Label(root,image=button_area_theme,bg='#C9C5C5')
        button_area_img.place(x=753,y=75)
        
        #row --------------->  1 
        button_back_color='#C9C5C5'
        button_active_bg_color='#C9C5C5'
        #give vote
        give_img=PhotoImage(file='button/givevote.png')
        give_vote_b=Button(root,image=give_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=givevote_now)
        give_vote_b.place(x=780,y=100)

        #view card
        view_img=PhotoImage(file='button/viewcard.png')
        view_card_b=Button(root,image=view_img,bg=button_back_color,bd=0,activebackground=button_active_bg_color,cursor='hand2',command=viewvoter_card)
        view_card_b.place(x=1032,y=100)

        #track application
        search_img=PhotoImage(file='button/searchstatus.png')
        search_app_status_b=Button(root,image=search_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=trackapplication)
        search_app_status_b.place(x=1280,y=100)


        #row --------------->  2
        #registration
        new_img=PhotoImage(file='button/regc.png')
        new_b=Button(root,image=new_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=RegistrationForm)
        new_b.place(x=780,y=295)
        #download
        download_img=PhotoImage(file='button/download.png')
        download_b=Button(root,image=download_img,bg=button_back_color,bd=0,activebackground=button_active_bg_color,cursor='hand2',command=download)
        download_b.place(x=1032,y=295)
        #update
        update_img=PhotoImage(file='button/update.png')
        update_card_b=Button(root,image=update_img,bg=button_back_color,bd=0,activebackground=button_active_bg_color,cursor='hand2',command=required_to_login)
        update_card_b.place(x=1280,y=295)


        #row --------------->  3
        log_img=PhotoImage(file='button/loginc.png')
        log_b=Button(root,image=log_img,bd=0,bg=button_back_color,activebackground=button_active_bg_color,cursor='hand2',command=LoginForm)
        log_b.place(x=780,y=488)

        #settingTheme.........
        themephoto_setting=PhotoImage(file='button/setting.png')
        theme_color_setting=Button(root,bd=0,image=themephoto_setting,activebackground=button_active_bg_color,cursor='hand2',background=button_back_color,command=setting)
        theme_color_setting.place(x=1440,y=750)




        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  left side old <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        # #rbjp --------------->  
        # bjp_img=PhotoImage(file='logo/bjp logo.png')
        # bjp_b=Label(root,image=bjp_img ,bg='#C9C5C5')
        # bjp_b.place(x=20,y=121)
        # #count......
        # bjp1_b=Label(root,bg='white',width=60,height=10)
        # bjp1_b.place(x=250,y=123)

        # bjp_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
        # bjp_l1.place(x=300,y=180)
        # #show count
        # bjp_s=Label(root,text=bjp,font=('Regular',20),bg='white',fg='blue')
        # bjp_s.place(x=440,y=180)

        # #percentage
        # tperentage=bjp+cong+tmc
        # cpercentage_bjp=round((bjp/tperentage)*100,2) ,"%"
        # bjp_p=Label(root,text=cpercentage_bjp,font=('Regular',16),bg='white',fg='blue')
        # bjp_p.place(x=560,y=235)


        # #progress
        # for i in range(0,len(cpercentage_bjp)):
        #     bjp_percentage=round(cpercentage_bjp[0])
        #     break
        # # print(type(bjp_percentage))

        # progressbar_bjp=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
        # progressbar_bjp['value']=bjp_percentage
        # progressbar_bjp.place(x=300,y=240)

        # ####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................................................................

        # #tmc..........
        # tmc_img=PhotoImage(file='logo/tmc logo.png')
        # tmc_b=Label(root,image=tmc_img ,bg='#C9C5C5')
        # tmc_b.place(x=16,y=310)
        # #count........
        # tmc1_b=Label(root,bg='white',width=60,height=10)
        # tmc1_b.place(x=250,y=312)

        # tmc_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
        # tmc_l1.place(x=300,y=370)
        # #show count
        # tmc_s=Label(root,text=tmc,font=('Regular',20),bg='white',fg='blue')
        # tmc_s.place(x=440,y=370)
        

        # #percentage
        # cpercentage_tmc=round((tmc/tperentage)*100,2) ,"%"
        # tmc_p=Label(root,text=cpercentage_tmc,font=('Regular',16),bg='white',fg='blue')
        # tmc_p.place(x=560,y=425)

        # #progress
        # for i in range(0,len(cpercentage_tmc)):
        #     tmc_percentage=round(cpercentage_tmc[0])
        #     break
        # # print(type(tmc_percentage))

        # progressbar_tmc=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
        # progressbar_tmc['value']=tmc_percentage
        # progressbar_tmc.place(x=300,y=430)


        # ####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....................................................................



        # #conj......
        # conj_img=PhotoImage(file='logo/cong logo.png')
        # conj_b=Label(root,image=conj_img ,bg='#C9C5C5')
        # conj_b.place(x=20,y=499)
        # #count.....
        # conj_b=Label(root,bg='white',width=60,height=10)
        # conj_b.place(x=250,y=501)

        # conj_l1=Label(root,text='Total Vote: ',font=('Regular',20),bg='white')
        # conj_l1.place(x=300,y=560)
        # #show count
        # conj_s=Label(root,text=cong,font=('Regular',20),bg='white',fg='blue')
        # conj_s.place(x=440,y=560)

        # #percentage
        # cpercentage_cong=round((cong/tperentage)*100,2) ,"%"
        # cong_p=Label(root,text=cpercentage_cong,font=('Regular',16),bg='white',fg='blue')
        # cong_p.place(x=560,y=610)

        # #progress
        # for i in range(0,len(cpercentage_cong)):
        #     cong_percentage=round(cpercentage_cong[0])
        #     break
        # # print(type(cong_percentage))

        # progressbar_cong=ttk.Progressbar(root,orient=HORIZONTAL,length=250,mode='determinate')
        # progressbar_cong['value']=cong_percentage
        # progressbar_cong.place(x=300,y=615)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  left side new <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        total_report_bg=PhotoImage(file='logo/total.png')
        total_report=Label(root,image=total_report_bg,bg='#C9C5C5')
        total_report.place(x=28,y=75)

        #vote count....
        bjp_s=Label(root,text=bjp,font=('Regular',20),bg='#BCEAD5',fg='blue')
        bjp_s.place(x=190,y=232)
        tmc_s=Label(root,text=tmc,font=('Regular',20),bg='#BCEAD5',fg='blue')
        tmc_s.place(x=410,y=232)
        conj_s=Label(root,text=cong,font=('Regular',20),bg='#BCEAD5',fg='blue')
        conj_s.place(x=630,y=232)


        #pie chart.....
        figure2=Figure(figsize=(4,4),dpi=100)
        subplot2=figure2.add_subplot(111)

        vot_per=[bjp,tmc,cong]
        party_name=['BJP','TMC','CONGRESS']
        exp=[0,0,0]
        color_pi=['#FF9700','#00FF17','#FBFF00']

        subplot2.pie(vot_per, labels=party_name, explode=exp, autopct='%2.2f%%', colors=color_pi)
        pie2=FigureCanvasTkAgg(figure2,root)
        pie2.get_tk_widget().place(x=150,y=380)

        pr=Label(root,text='Pie Chart Report',font=('Regular',20),bg='white')
        pr.place(x=50,y=370)


        root.mainloop()


    splash_screen.after(4000,main_screen)
    splash_screen.mainloop()




def check_connection():
    try:
        request.urlopen("https://www.google.com/",timeout=5)
        print('online')
        lunch_first_body()

    except OSError:
        print('offline')
        def second_body():
            second_body=Tk()
            second_body.geometry('1080x920')
            second_body.attributes('-fullscreen',True)
            second_body.config(bg='white')
            my_label = Label(second_body,bg='white')
            my_label.place(x=160,y=150)
            player = tkvideo("video/107013-loader-for-wi-fi-connection.mp4", my_label, loop = 1, size = (500,500))
            player.play()
            def notconnect():
                second_body.destroy()
                ifnot()
            

            nosig_img=PhotoImage(file='button/nosignal.png')
            nosig_label=Label(second_body,image=nosig_img,bd=0,bg='white')
            nosig_label.place(x=870,y=235)

            re_img=PhotoImage(file='button/retry.png')
            re_button=Button(second_body,image=re_img,command=notconnect,bg='white',activebackground='white',bd=0,cursor='hand2')
            re_button.place(x=1035,y=515)
        
            second_body.mainloop()
        second_body()
def ifnot():
    check_connection()
check_connection()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

