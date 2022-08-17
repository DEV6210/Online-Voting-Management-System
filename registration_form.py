from msilib.schema import ComboBox
from operator import concat
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlalchemy import null
from tkinter import filedialog
import sqlite3
import random


try:
    db=sqlite3.connect('voting management system.db')
    cr=db.cursor()
    cr.execute('create table registration(name text,dob text,gender text,father_name text,phone text,email text,aadhaar text,village text,post text,pin text,dist text,state text,password text,conform_password text,photo blob,ststus text,application_no text,card_no text,voting_status text,otp text)')
    db.commit()
except:
    print('Database is running...')
    

regwin=Tk()
regwin.geometry('1367x700')
regwin.attributes('-fullscreen',True)
regwin.wm_iconbitmap('icon/reg.ico')
regwin.title('Registration Form')
regwin.state('zoomed')
regwin.config(bg='#D9D9D9')
#import reg_background image
reg_back=PhotoImage(file='themes/registration form.png')
reg_them=Label(regwin,bg='#D9D9D9',image=reg_back,width=1050,height=780)
reg_them.place(x=240,y=10)

#x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x
name=StringVar()

dd=StringVar()
mm=StringVar()
yy=StringVar()

fathername=StringVar()
phone=StringVar()
aadhaar=StringVar()
password=StringVar()
conformpassword=StringVar()
email=StringVar()
village=StringVar()
post=StringVar()
pincode=StringVar()
dist=StringVar()
state=StringVar()
g=IntVar()

def cancel():
    regwin.destroy()
    import OnlineVotingManagementSystem



get_image=0
#File dialog to select files
def filedialogs():
    global get_image
    get_image=0
    get_image = filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=(("Allfile", "*.*"), ("png", "*.png"), ("jpg" , "*.jpg")))

    #photo name...............
    photoname=Label(regwin,text=get_image,font=('Regular',10),fg='green',bg='white')
    photoname.place(x=650,y=565)

#Image need to be conver into binary before insert into database
def conver_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image


def submit():
    null = 0 #assign null value
    
    name1=name.get()
    dd1=dd.get()
    mm1=mm.get()
    yy1=yy.get()

    fathername1=fathername.get()
    phone1=phone.get()
    aadhaar1=aadhaar.get()
    password1=password.get()
    password2=conformpassword.get()
    email1=email.get()
    village1=village.get()
    post1=post.get()
    pincode1=pincode.get()
    dist1=dist.get()
    state1=state.get()

    gender=g.get()


    # print(name1)
    # print(dob)
    # print(fathername1)
    # print(phone1)
    # print(aadhaar1)
    # print(password1)
    # print(password2)
    # print(email1)
    # print(village1)
    # print(post1)
    # print(pincode1)
    # print(dist1)
    # print(state1)
    # print(g)


    #name.................
    length_of_name=len(name1)#set leangth 0
    if null == length_of_name:
        messagebox.showerror('Worning','Please Enter Your Name')
    else:
        # print(name1)

        #date of birth..................
        if dd1 == 'DD' or mm1 == 'MM' or yy1 == 'YY':
            messagebox.showerror('Worning','Please Choose Correct Date of Birth')
        else:
            day=int(dd1)
            month=int(mm1)
            year=int(yy1)
            if day <= 31 and month <= 12 and year <= 2050:
                d1=str(day)
                m1=str(month)
                y1=str(year)
                dob=d1 + '/'+ m1 +'/'+y1                
                # print(dob)

                #father name..........................
                length_of_father=len(fathername1)
                if null == length_of_father:
                    messagebox.showerror('Worning','Please Enter Father Name')
                else:
                    # print(fathername1)

                    #phone...........................
                    length_of_phone=len(phone1)
                    if null == length_of_phone:
                        messagebox.showerror('Worning','Please Enter Phone Number')
                    elif phone1.isdigit()==False:
                        messagebox.showwarning('Worning','Please Enter only Phone digit')
                    elif length_of_phone != 10:
                        messagebox.showwarning('Worning','Please Enter 10 digit Phone Number')
                    else:
                        # print(phone1)
                        
                        #aadhaar card...................
                        alength_of_aadhaar=len(aadhaar1)
                        if null == alength_of_aadhaar:
                            messagebox.showerror('Worning','Please Enter aadhaar card number')
                        elif aadhaar1.isdigit()==False:
                            messagebox.showwarning('Worning','Please Enter only Aadhaar digit')
                        elif alength_of_aadhaar !=12:
                            messagebox.showwarning('Worning','Please Enter 12 digit Aadhaar Number')
                        else:
                            # print(aadhaar1)

                            #village.......................
                            length_of_village=len(village1)
                            if null == length_of_village:
                                messagebox.showerror('Worning','Please Enter village Name')
                            else:
                                # print(village1)

                                #post.........................
                                length_of_post=len(post1)
                                if null == length_of_post:
                                    messagebox.showerror('Worning','Please Enter post office name')
                                else:
                                    # print(post1)

                                    #pin..........................
                                    length_of_pin=len(pincode1)
                                    if null == length_of_pin:
                                        messagebox.showerror('Worning','Please Enter pincode')
                                    elif pincode1.isdigit()==False:
                                        messagebox.showwarning('Worning','Please Enter only pin digit ')
                                    else:
                                        # print(pincode1)

                                        #district...............
                                        length_of_dist=len(dist1)
                                        if null == length_of_dist:
                                            messagebox.showerror('Worning','Please Enter district Name')
                                        else:
                                            # print(dist1)

                                            #stste........................
                                            length_of_state=len(state1)
                                            if null == length_of_state:
                                                messagebox.showerror('Worning','Please Enter state Name')
                                            else:
                                                # print(state1)

                                                #password..................
                                                length_of_pass=len(password1)
                                                if null == length_of_pass:
                                                    messagebox.showerror('Worning','Please Enter Password')
                                                else:
                                                    # print(password1)
                                                    #password match............
                                                    if password1 != password2:
                                                        messagebox.showerror('Worning','Conform Password Not Match')
                                                    else:
                                                        
                                                        
                                                        #generate application no.................
                                                        app1=random.randint(10000000,99999999)                                            
                                                        appid=str(app1)
                                                        notemessage='Application No: '+ appid+' \nPhone Number is Your Login Id...'
                                                        voterid='Not Generated'
                                                        votstatus='Not Voted'

                                                        #gender........................
                                                        if gender == null:
                                                            messagebox.showerror('Worning','Please Select Gender')
                                                        elif gender == 1:
                                                            gender='Male'

                                                            #photo...........
                                                            def insert_data():
                                                                # image_database = sqlite3.connect("Image_data.db")
                                                                # data = image_database.cursor()

                                                                if get_image == 0:
                                                                    messagebox.showerror('Worning','Please Select Image')
                                                                else:
                                                                    cr.execute('select phone from registration')                                                                   
                                                                    data=cr.fetchall()
                                                                    check=0
                                                                    for i in data:
                                                                        p1=i[0]
                                                                        #a1=i[1]    #for aadhaar card validation 
                                                                        if phone1==p1:                                                                            
                                                                            check=1
                                                                            break
                                                                        else:
                                                                            check=0
                                                                    if check == 1:
                                                                        messagebox.showwarning('Exist User','Your Phone Number is Already Registered...')
                                                                    else:                                                                        
                                                                        result=messagebox.askyesno('Confirmation','Are You Sure All Details is Correct?')
                                                                        if result == True:
                                                                            for image in get_image:
                                                                                insert_photo = conver_image_into_binary(image)

                                                                                
                                                                                cr.execute('insert into registration(name,dob,gender,father_name,phone,email,aadhaar,village,post,pin,dist,state,password,conform_password,photo,application_no,card_no,voting_status) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name1,dob,gender,fathername1,phone1,email1,aadhaar1,village1,post1,pincode1,dist1,state1,password1,password2,insert_photo,appid,voterid,votstatus))
                                                                                db.commit()
                                                                                db.close()
                                                                                messagebox.showinfo('','Application submit Successfull')
                                                                                messagebox.showinfo('Please Note Down Your Application No',notemessage)

                                                                                regwin.destroy()
                                                                                import OnlineVotingManagementSystem
                                                                                # data.execute("INSERT INTO Image Values(:image)", {'image': insert_photo })
                                                                                #print('success')
                                                                                # image_database.commit()
                                                                                # image_database.close()
                                                            insert_data()
                                                                                                                        
                                                        else:

                                                            gender='Female'
                                                        
                                                            #photo...........
                                                            def insert_image():
                                                                # image_database = sqlite3.connect("Image_data.db")
                                                                # data = image_database.cursor()

                                                                if get_image == 0:
                                                                    messagebox.showerror('Worning','Please Select Image')
                                                                else:
                                                                    cr.execute('select phone from registration')                                                                   
                                                                    data=cr.fetchall()
                                                                    check=0
                                                                    for i in data:
                                                                        p1=i[0]
                                                                        #a1=i[1]    #for aadhaar card validation 
                                                                        if phone1==p1:                                                                            
                                                                            check=1
                                                                            break
                                                                        else:
                                                                            check=0
                                                                    if check == 1:
                                                                        messagebox.showwarning('Exist User','Your Phone Number is Already Registered...')
                                                                    else:                                                                        
                                                                        result=messagebox.askyesno('Confirmation','Are You Sure All Details is Correct?')
                                                                        if result == True:
                                                                            for image in get_image:
                                                                                insert_photo = conver_image_into_binary(image)

                                                                                
                                                                                cr.execute('insert into registration(name,dob,gender,father_name,phone,email,aadhaar,village,post,pin,dist,state,password,conform_password,photo,application_no,card_no,voting_status) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name1,dob,gender,fathername1,phone1,email1,aadhaar1,village1,post1,pincode1,dist1,state1,password1,password2,insert_photo,appid,voterid,votstatus))
                                                                                db.commit()
                                                                                db.close()
                                                                                messagebox.showinfo('','Application submit Successfull')
                                                                                messagebox.showinfo('Please Note Down Your Application No',notemessage)

                                                                                regwin.destroy()
                                                                                import OnlineVotingManagementSystem
                                                                                # data.execute("INSERT INTO Image Values(:image)", {'image': insert_photo })
                                                                                #print('success')
                                                                                # image_database.commit()
                                                                                # image_database.close()
                                                            insert_image()
                                                            
                                                            
                                                            


            else:
                messagebox.showwarning('Worning','Choose Correct Date of Birth')









#-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x
'''------------------------------------left side----------------------------------------'''


#import name image
name_img=PhotoImage(file='button/name.png')
name_l=Label(regwin,image=name_img,bg='white')
name_l.place(x=285,y=195)
#entry name
name_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=name)
name_e.place(x=520,y=197)


#import dob image
dob_img=PhotoImage(file='button/dob.png')
dob_l=Label(regwin,image=dob_img,bg='white')
dob_l.place(x=285,y=250)


#entry date of birth
dob_d=ttk.Combobox(regwin,font=('timew new roman',22),width=3,cursor='hand2',textvar=dd)
dob_d['value']=['DD',1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28,29,30,31]
dob_d.current(0)
dob_d.place(x=520,y=252)

dob_m=ttk.Combobox(regwin,font=('timew new roman',22),width=4,cursor='hand2',textvar=mm)
dob_m['value']=['MM',1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dob_m.current(0)
dob_m.place(x=598,y=252)

dob_y=ttk.Combobox(regwin,font=('timew new roman',22),width=5,cursor='hand2',textvar=yy)
dob_y['value']=['YY',1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
dob_y.current(0)
dob_y.place(x=690,y=252)




#importfather name image
father_img=PhotoImage(file='button/fathers_name.png')
fathername_l=Label(regwin,image=father_img,bg='white')
fathername_l.place(x=285,y=300)
#entry father name
father_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=fathername)
father_e.place(x=520,y=302)


#import phone image
phone_img=PhotoImage(file='button/phone.png')
phone_l=Label(regwin,image=phone_img,bg='white')
phone_l.place(x=285,y=350)
#entry phone
phone_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=phone)
phone_e.place(x=520,y=352)

#import Aadhaar image
aadhaar_img=PhotoImage(file='button/aadhaar.png')
aadhaar_l=Label(regwin,image=aadhaar_img,bg='white')
aadhaar_l.place(x=285,y=400)
#entry aadhar 
aadhaar_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=aadhaar)
aadhaar_e.place(x=520,y=402)

#import password image
pass_img=PhotoImage(file='button/pass.png')
password_l=Label(regwin,image=pass_img,bg='white')
password_l.place(x=285,y=450)
#entry password
pass_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=password)
pass_e.place(x=520,y=452)


#import conform password image
con_img=PhotoImage(file='button/con_pass.png')
con_pass=Label(regwin,image=con_img,bg='white')
con_pass.place(x=285,y=500)
#entry conform password
conpass_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,show='*',textvar=conformpassword)
conpass_e.place(x=520,y=502)

#import upload image
upload_img=PhotoImage(file='button/upload.png')
upload_l=Label(regwin,image=upload_img,bg='white')
upload_l.place(x=285,y=555)

#import browse button image
browse_img=PhotoImage(file='button/browse.png')
browse_l=Button(regwin,image=browse_img,bg='white',activebackground='white',bd=0,command=filedialogs)
browse_l.place(x=520,y=557)


'''------------------------------------right side----------------------------------------'''
#import email image
email_img=PhotoImage(file='button/email.png')
email_l=Label(regwin,image=email_img,bg='white')
email_l.place(x=830,y=195)
#entry email
email_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=email)
email_e.place(x=975,y=197)

#email optional..............
email_op_img=PhotoImage(file='button/E-mail Optional.png')
email_op=Label(regwin,image=email_op_img,font=('Regular',8),fg='red',bg='white')
email_op.place(x=974,y=235)

#import village image
vill_img=PhotoImage(file='button/vill.png')
vill_l=Label(regwin,image=vill_img,bg='white')
vill_l.place(x=830,y=250)
#entry village
vill_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=village)
vill_e.place(x=975,y=252)

#import post image
post_img=PhotoImage(file='button/post.png')
post_l=Label(regwin,image=post_img,bg='white')
post_l.place(x=830,y=300)
#entry post
post_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=post)
post_e.place(x=975,y=302)

#import pin code image
pin_img=PhotoImage(file='button/pincode.png')
pin_l=Label(regwin,image=pin_img,bg='white')
pin_l.place(x=830,y=350)
#entry pincode
pin_e=Entry(regwin,font=('timew new roman',24),bd=1,bg='#EFEFE0',width=15,textvar=pincode)
pin_e.place(x=975,y=352)

#import district image
dist_img=PhotoImage(file='button/district.png')
dist_l=Label(regwin,image=dist_img,bg='white')
dist_l.place(x=830,y=400)
#entry district
dist_e=ttk.Combobox(regwin,font=('timew new roman',24),width=14,cursor='hand2',textvar=dist)
dist_e['value']=["Alipurduar","Bankura","Birbhum","Cooch Behar","Darjeeling","Hooghly","Howra","Jalpaiguri","Jhargram","Kalimpong","Kolkata","Malda","Murshidabad","Nadia","North 24 Parganas","Purulia","Araria","Arwal","Aurangabad","Banka","Begusarai","Bhagalpur","Bhojpur","Buxar","Darbhanga","Gaya","Gopalganj","North Goa","South Goa",'Ahmedabad','Amreli','Anand','Aravalli','Bhavnagar','Dahod',"Jalandhar","Kapurthala","Ludhiana","Mansa","Moga","Muktsar","Pathankot",'Agra','Aligarh','Allahabad','Azamgarh','Baghpat','Bahraich','Ballia','Balrampur','Banda','Barabanki','Bokaro','Chatra','Deoghar','Dhanbad','Dumka','East', 'Singhbhum','Garhwa','Giridih','Srikakulam','Vizianagaram','Anakapalli','Kakinada','Eluru','NTR','Palnadu','Guntur']
dist_e.current(12)
dist_e.place(x=975,y=402)


#import state image
state_img=PhotoImage(file='button/state.png')
state_l=Label(regwin,image=state_img,bg='white')
state_l.place(x=830,y=450)
#entry state
state_e=ttk.Combobox(regwin,font=('timew new roman',24),width=14,cursor='hand2',textvar=state)
state_e['value']=["Andhra Pradesh", "Bihar" ,"Goa" ,"Gujarat" , "Jharkhand" ,"Punjab","Uttar Pradesh" ,"West Bengal"]
state_e.current(7)
state_e.place(x=975,y=452)

#import gender image
gender_img=PhotoImage(file='button/gender.png')
gender_l=Label(regwin,image=gender_img,bg='white')
gender_l.place(x=830,y=500)
#entry gender
gender1_e=Radiobutton(regwin,text='Male',font=('times new roman',18),fg='blue',bg='white',activebackground='white',value=1,cursor='hand2',variable=g)
gender1_e.place(x=990,y=502)
gender2_e=Radiobutton(regwin,text='Female',font=('times new roman',18),fg='blue',bg='white',activebackground='white',value=2,cursor='hand2',variable=g)
gender2_e.place(x=1080,y=502)





'''----------------------------------------- End ------------'---------------------------'''





'''-----------------------------------submit / cancel-------------------------------------'''
#import submit image
submit_img=PhotoImage(file='button/u_login.png')
submit=Button(regwin,image=submit_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=submit)
submit.place(x=595,y=700)

#import cancel image
cancel_img=PhotoImage(file='button/cancel.png')
cancel=Button(regwin,image=cancel_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=cancel)
cancel.place(x=785,y=700)



regwin.mainloop()
