from app.db.orm.user_orm import UserORM
from app.setting.lib import *

class HeaderUI(CTkFrame):
    def __init__(self,master,super_master,id,authen_ui,**kwargs):
        self.super_master = super_master
        self.user_name=id.show_name
        self.id=id.id
        self.birthday=id.birthday
        self.gender=id.gender
        self.authen_ui=authen_ui
        self.password=id.password
        self.phone_number=id.phone_number
        self.avatar_path=id.avatar
        self.bg_path=id.background
        super().__init__(master=master,**kwargs)
        self.pack(fill='x')
        self.user_orm=UserORM()
        self.init_ui()
    def init_ui(self):
        self.left_frame=CTkFrame(master=self,fg_color='transparent',height=65,width=250)
        self.left_frame.pack(side='left')
        self.logo_label=CTkLabel(master=self.left_frame,text='MyGallery',font=('Impact',30,),text_color='#CCCCCC')
        self.logo_label.place(x=25,y=15)

        self.mid_frame=CTkFrame(master=self,fg_color='transparent',height=65,width=800)
        self.mid_frame.pack(side='left')
        self.search_frame=CTkFrame(master=self.mid_frame,fg_color='transparent',height=50,width=700,)
        self.search_frame.pack(side='left')
        self.search_entry=CTkEntry(master=self.search_frame,corner_radius=30,height=50,width=700,border_width=1,state='disabled',
        fg_color='#111111',text_color='white')
        self.search_entry.pack()
        self.search_button=CTkButton(master=self.search_frame,height=25,width=25,fg_color='#111111',text=''
            ,image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'search.png').resize((25,25),Image.BILINEAR),size=(25,25)),
            hover_color='#111111',border_width=0)
        self.search_button.place(x=20,y=10)
        self.search_button.bind('<ButtonPress-1>',lambda e: self.move_to_suggest_handle())
        self.search_main_entry=CTkEntry(master=self.search_frame,height=40,width=500,font=('Helvetica',25),
            fg_color='#111111',text_color='white',placeholder_text='Search',border_width=0)
        self.search_main_entry.place(x=70,y=7)
        self.search_main_entry.bind('<Return>',lambda e: self.move_to_suggest_handle())




        self.right_frame=CTkFrame(master=self,fg_color='transparent',height=65)
        self.right_frame.pack(fill='x')
        self.button_frame=CTkFrame(master=self.right_frame,width=510,height=65,fg_color='#111111')
        self.button_frame.pack(side='left')

        self.profile_button=CTkCanvas(master=self.button_frame,width=84,height=65,bg='#111111',highlightthickness=0)
        self.profile_button.place(x=426)
        self.image1=Image.open(self.avatar_path).resize((50,50),Image.BILINEAR)
        self.image1=ImageTk.PhotoImage(self.image1)
 
        self.profile_button.create_oval(20,54.5,64,10.5)
        self.profile_button.create_image(42,32.5,image=self.image1)
        
        self.profile_button.bind('<Button-1>',lambda e: self.open_profile())

    def open_profile(self):
        self.open_profile_frame=CTkFrame(master=self.super_master.main_app,width=175,height=140,fg_color='#0C0C0C',
            bg_color='#0C0C0C' )
        self.open_profile_frame.place(x=1450,y=40)

        self.account_information=CTkFrame(master=self.open_profile_frame,width=180,height=50,fg_color='#0C0C0C')
        self.account_information.place(x=0,y=0)
        self.account_information_logo=CTkLabel(master=self.account_information,text='',width=30,height=30,
                    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'acc-inf.png').resize((50,50),Image.BILINEAR),size=(30,30)))
        self.account_information_logo.place(x=10,y=10)
        self.account_information_label=CTkLabel(master=self.account_information,text='Informations',font=('Roboto',20,),fg_color='#0C0C0C',text_color='white')
        self.account_information_label.place(x=50,y=12)
        self.account_information.bind('<Button-1>',lambda e: self.open_informations_ui())
        self.account_information_logo.bind('<Button-1>',lambda e: self.open_informations_ui())
        self.account_information_label.bind('<Button-1>',lambda e: self.open_informations_ui())



        self.account_setting=CTkFrame(master=self.open_profile_frame,width=180,height=50,fg_color='#0C0C0C')
        self.account_setting.place(x=0,y=45)
        self.setting_logo=CTkLabel(master=self.account_setting,text='',width=30,height=30,
                    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'settings.png').resize((50,50),Image.BILINEAR),size=(30,30)))
        self.setting_logo.place(x=10,y=10)
        self.setting_label=CTkLabel(master=self.account_setting,text='Settings',font=('Roboto',20,),fg_color='#0C0C0C',text_color='white')
        self.setting_label.place(x=50,y=12)
        self.account_setting.bind('<ButtonPress-1>',lambda e: self.open_account_setting())
        self.setting_logo.bind('<ButtonPress-1>',lambda e: self.open_account_setting())
        self.setting_label.bind('<ButtonPress-1>',lambda e: self.open_account_setting())

        self.log_out=CTkFrame(master=self.open_profile_frame,width=180,height=50,fg_color='#0C0C0C')
        self.log_out.place(x=0,y=90)
        self.log_out_logo=CTkLabel(master=self.log_out,text='',width=30,height=30,
                    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'log-out.png').resize((30,30),Image.BILINEAR),size=(30,30)))
        self.log_out_logo.place(x=10,y=10)
        self.log_out_label=CTkLabel(master=self.log_out,text='Log Out',font=('Roboto',20,),fg_color='#0C0C0C',text_color='white')
        self.log_out_label.place(x=50,y=12)
        self.log_out.bind('<ButtonPress-1>',lambda e: self.ask_to_log_out())
        self.log_out_logo.bind('<ButtonPress-1>',lambda e: self.ask_to_log_out())
        self.log_out_label.bind('<ButtonPress-1>',lambda e: self.ask_to_log_out())

        self.profile_button.unbind('<Button-1>')
        self.profile_button.bind('<Button-1>',lambda e: self.destroy_profile())
    def destroy_profile(self):
        self.open_profile_frame.destroy()
        self.profile_button.unbind('<Button-1>')
        self.profile_button.bind('<Button-1>',lambda e: self.open_profile())
    def open_account_setting(self):
        self.destroy_profile()
        if hasattr(self,'setting_ui'):
            self.setting_ui.destroy()
        self.setting_ui=CTkFrame(master=self.super_master.main_app,width=800,height=600,fg_color='#222222',bg_color='#222222' )
        self.setting_ui.place(x=450,y=100)
        logo=CTkButton(master=self.setting_ui,width=30,height=30,fg_color='transparent',text='',hover=False,
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'close.png').resize((30,30),Image.BILINEAR),size=(30,30)))
        logo.place(x=760,y=-6)
        logo.bind('<ButtonPress-1>',lambda e:self.destroy_setting())
        self.left_setting_side=CTkFrame(master=self.setting_ui,height=570,width=220,fg_color='#0C0C0C',bg_color='#0C0C0C')
        self.left_setting_side.place(x=0,y=30)
        account_security=CTkFrame(master=self.left_setting_side,fg_color='#333333',bg_color='#333333',height=70,width=220)
        account_security.place(x=0,y=0)
        account_logo=CTkLabel(master=account_security,text='',width=40,height=40,image=
        CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'account.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        account_logo.place(x=10,y=15)
        account_label=CTkLabel(master=account_security,text='Account Security',font=('Roboto',17,'bold'),fg_color='transparent',
                    text_color='white')
        account_label.place(x=55,y=20)
        self.init_right_setting_side()
    def destroy_setting(self):
        self.setting_ui.destroy()   
    def init_right_setting_side(self):
        
        self.right_setting_side=CTkFrame(master=self.setting_ui,height=560,width=580,fg_color='#111111',bg_color='#111111')
        self.right_setting_side.place(x=220,y=30)
        change_password_label=CTkLabel(master=self.right_setting_side,text='Login Password',font=('Roboto',20,'bold'),text_color='white')
        change_password_label.place(x=50,y=15)
        change_password_frame=CTkFrame(master=self.right_setting_side,width=580,height=80,fg_color='#222222')
        change_password_frame.place(x=0,y=50)
        change_password_label2=CTkLabel(master=change_password_frame,text='Change Password',font=('Roboto',20,),text_color='white')
        change_password_label2.place(x=400,y=20)
        arrow=CTkLabel(master=change_password_frame,text='',width=50,height=20,image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'arrow.png').resize((50,20),Image.BILINEAR),size=(50,20)))
        arrow.place(x=500,y=50)
        change_password_frame.bind('<Button-1>',lambda e: self.move_to_change_password())
        change_password_label2.bind('<Button-1>',lambda e: self.move_to_change_password())
        arrow.bind('<Button-1>',lambda e: self.move_to_change_password())
    def move_to_change_password(self):
        self.right_setting_side.destroy()
        self.right_setting_side=CTkFrame(master=self.setting_ui,height=560,width=580,fg_color='#111111',bg_color='#111111')
        self.right_setting_side.place(x=220,y=30)
        self.right_setting_side.bind('<Button-1>',lambda e: self.right_setting_side.focus())
        back_logo=CTkLabel(master=self.right_setting_side,text='',width=50,height=50,image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'arrow2.png').resize((50,20),Image.BILINEAR),size=(50,20)))
        back_logo.place(x=30,y=10)
        back_label=CTkLabel(master=self.right_setting_side,text='Change Password',font=('Roboto',20,'bold'),text_color='white')
        back_label.place(x=100,y=20)
        back_logo.bind('<Button-1>',lambda e: self.destroy_change_password())
        current_password_label=CTkLabel(master=self.right_setting_side,text='Current Password',font=('Roboto',20),text_color='white')
        current_password_label.place(x=50,y=90)
        self.current_password_changing =CTkEntry(master=self.right_setting_side,width=500,height=30,border_width=0,
                show='*',font=('Roboto',20,'bold'))
        self.current_password_changing.place(x=20,y=120)
        self.show_password1_btn=CTkButton(master=self.right_setting_side,width=30,height=30,text='Show',font=('Roboto',18),text_color='white',fg_color='#111111',hover_color='#222222')
        self.show_password1_btn.place(x=520,y=120)
        self.show_password1_btn.bind('<Button-1>',lambda e: self.show_password1(0))

        new_password_label=CTkLabel(master=self.right_setting_side,text='New Password',font=('Roboto',20),text_color='white')
        new_password_label.place(x=50,y=170)
        self.new_password_changing1 =CTkEntry(master=self.right_setting_side,width=500,height=30,border_width=0,
                show='*',font=('Roboto',20,'bold'))
        self.new_password_changing1.place(x=20,y=200)
        self.show_password2_btn=CTkButton(master=self.right_setting_side,width=30,height=30,text='Show',font=('Roboto',18),text_color='white',fg_color='#111111',bg_color='#111111',hover_color='#222222')
        self.show_password2_btn.place(x=520,y=200)
        self.show_password2_btn.bind('<Button-1>',lambda e: self.show_password1(1))
        new_password_label=CTkLabel(master=self.right_setting_side,text='Confirm Password',font=('Roboto',20),text_color='white')
        new_password_label.place(x=50,y=250)
        self.new_password_changing2 =CTkEntry(master=self.right_setting_side,width=500,height=30,border_width=0,show='*',font=('Roboto',20,'bold'))
        self.new_password_changing2.place(x=20,y=280)
        self.show_password3_btn=CTkButton(master=self.right_setting_side,width=30,height=30,text='Show',font=('Roboto',18),text_color='white',fg_color='#111111',bg_color='#555555',hover_color='#555555')
        self.show_password3_btn.place(x=520,y=280)
        self.show_password3_btn.bind('<Button-1>',lambda e: self.show_password1(2))
        cancel_button=CTkButton(master=self.right_setting_side,width=50,height=50,text='Cancel',font=('Roboto',24,'bold'),bg_color='#555555',hover_color='#555555',
                                text_color='black',fg_color='white',command=self.destroy_change_password2)
        cancel_button.place(x=300,y=400)
        self.update_button=CTkButton(master=self.right_setting_side,width=50,height=50,text='Update',font=('Roboto',24,'bold'),bg_color='#2563EB',hover_color='#111111',
                    text_color='black',fg_color='#0099CC')
        self.update_button.place(x=400,y=400)
        self.update_button.bind('<Button-1>',lambda e: self.change_password_handle())
    def show_password1(self,index):
        entry=[self.current_password_changing,self.new_password_changing1,self.new_password_changing2]
        show=[self.show_password1_btn,self.show_password2_btn,self.show_password3_btn]
        if entry[index].cget('show')=='*':
            entry[index].configure(show='')
            show[index].configure(text='Hide')
        elif entry[index].cget('show')=='':
            entry[index].configure(show='*')
            show[index].configure(text='Show')
    def destroy_change_password2(self):
        self.right_setting_side.destroy()
        self.init_right_setting_side()
    def change_password_handle(self):
        current_password = self.current_password_changing.get()
        new_password=self.new_password_changing1.get()
        confirm_password=self.new_password_changing2.get()
        if new_password==confirm_password and len(new_password)>8:
            password_true=self.password
            if password_true==current_password:
                self.password=new_password
                self.user_orm.update(idd=self.id,password=new_password)
                self.show_message_success()
            else:
                self.show_message_error()
        else:
            self.show_message_error()   
    def show_message_error(self):
        message_error=CTkLabel(master=self.right_setting_side,text_color='white',font=('Roboto',14),fg_color='#111111',text='Please check your password again')
        message_error.place(x=180,y=320)
        message_error.after(5000,lambda : message_error.destroy())
    def show_message_success(self):
        message_error=CTkLabel(master=self.right_setting_side,text_color='white',font=('Roboto',14),fg_color='#111111',text='Changed password successfully')
        message_error.place(x=180,y=320)
        message_error.after(5000,lambda : message_error.destroy())
    def destroy_change_password(self):
        self.right_setting_side.destroy()
        self.init_right_setting_side()
    def ask_to_log_out(self):
        self.super_master.main_app.destroy()
        self.login_ui=self.authen_ui()
        self.login_ui.run_ui()

    def move_to_suggest_handle(self):
        pass


    def open_informations_ui(self):
        if hasattr(self,'info_ui'):
            self.info_ui.destroy()
        self.open_profile_frame.destroy()
        self.profile_button.unbind('<Button-1>')
        self.profile_button.bind('<Button-1>',lambda e: self.open_profile())
        self.info_ui=CTkFrame(master=self.super_master.main_app,width=400,height=600,fg_color='#111111',bg_color='#111111' )
        self.info_ui.place(x=650,y=100) 
        bar=CTkFrame(master=self.info_ui,width=400,height=40,fg_color='#222222',bg_color='#222222')   
        bar.place(x=0,y=0)
        logo=CTkButton(master=bar,width=40,height=40,fg_color='transparent',text='',hover=False,
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'close.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        logo.place(x=350,y=-6)
        logo.bind('<ButtonPress-1>',lambda e:self.destroy_info_ui())  
        self.profile_label=CTkLabel(master=bar,font=('Roboto',20,'bold'),text_color='white',fg_color='transparent',text='Profile')
        self.profile_label.place(x=10,y=5)
        self.background_frame=CTkFrame(master=self.info_ui,width=400,height=200,fg_color='#111111',bg_color='#111111')
        self.background_frame.place(x=0,y=40)

        background_default=CTkLabel(master=self.background_frame,text='',image=
        CTkImage(dark_image=Image.open(self.bg_path).resize((400,200),Image.LANCZOS),size=(400,200)))
        background_default.place(x=0,y=0)

        self.avatar_path=self.avatar_path
        self.image_avt=ImageTk.PhotoImage(Image.open(self.avatar_path).resize((75,75),Image.BILINEAR))
        self.profile_canvas=CTkCanvas(master=self.info_ui,width=80,height=80,bg='#111111',highlightthickness=0)
        self.profile_canvas.place(x=20,y=210)
        self.profile_canvas.create_oval((10,70,70,10))
        self.profile_canvas.create_image(40,40,image=self.image_avt)
        text=self.user_name
        self.name_user=CTkLabel(master=self.info_ui,text=text,font=('Roboto',22,'bold'),text_color='white',fg_color='#111111')
        self.name_user.place(x=110,y=245)

        self.infor_frame=CTkFrame(master=self.info_ui,width=400,height=300,fg_color='#111111')
        self.infor_frame.place(x=0,y=290)
        infor_frame_label=CTkLabel(master=self.infor_frame,text='Personal Information',font=('Roboto',20,'bold'),text_color='white',fg_color='#111111')
        infor_frame_label.place(x=8,y=10)
        gender_frame=CTkFrame(master=self.infor_frame,width=400,height=60,fg_color='transparent')
        gender_frame.place(x=0,y=45)
        gender_label=CTkLabel(master=gender_frame,text='Gender',font=('Roboto',18),text_color='#87CEFA',fg_color='#111111')
        gender_label.place(x=15,y=10)
        typegender=self.gender
        if typegender==None:    typegender='Update'
        self.gender_label=CTkLabel(master=gender_frame,text=typegender,font=('Roboto',16),text_color='white',fg_color='transparent')
        self.gender_label.place(x=160,y=10)

        birthday_frame=CTkFrame(master=self.infor_frame,width=400,height=60,fg_color='transparent')
        birthday_frame.place(x=0,y=85)
        birthday_label=CTkLabel(master=birthday_frame,text='Birthday',font=('Roboto',18),text_color='#87CEFA',fg_color='#111111')
        birthday_label.place(x=15,y=10)
        dob=self.birthday
        if dob==None:
            dob='Update'
        self.birthday_label=CTkLabel(master=birthday_frame,text=dob,font=('Roboto',16),text_color='white',fg_color='transparent')
        self.birthday_label.place(x=160,y=10)

        phone_number_frame=CTkFrame(master=self.infor_frame,width=400,height=60,fg_color='transparent')
        phone_number_frame.place(x=0,y=125)
        phone_number_label=CTkLabel(master=phone_number_frame,text='Phone Number',font=('Roboto',18),text_color='#87CEFA',fg_color='#111111')
        phone_number_label.place(x=15,y=10)
        phone_number=self.phone_number
        self.phone_label=CTkLabel(master=phone_number_frame,text=phone_number,font=('Roboto',16),text_color='white',fg_color='transparent')
        self.phone_label.place(x=160,y=10)

        update_button=CTkButton(master=self.infor_frame,width=400,height=70,text_color='white',fg_color='#0C0C0C',hover_color='#111111',image=
        CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'change.png').resize((50,50),Image.BILINEAR),size=(50,50)),text='')
        update_button.place(x=0,y=200)
        update_button.bind('<ButtonPress-1>',lambda e:self.update_information())
    


    def update_information(self):
        self.profile_label.configure(text='Edit your profile')
        self.background_frame.destroy()
        self.profile_canvas.destroy()
        self.name_user.destroy()
        self.infor_frame.destroy()  
        self.update_frame=CTkFrame(master=self.info_ui,fg_color='#111111',width=400,height=550)
        self.update_frame.place(x=0,y=40)
        change_show_name_label=CTkLabel(master=self.update_frame,text='Display Name',font=('Roboto',20,'bold'),text_color='#87CEFA',fg_color='#111111')
        change_show_name_label.place(x=10,y=20)
        self.change_show_name=CTkEntry(master=self.update_frame,fg_color='#222222',font=('Roboto',17),width=350,height=30,bg_color='#222222',border_width=1)
        self.change_show_name.place(x=25,y=60)
        
        gender_label=CTkLabel(master=self.update_frame,text='Gender',font=('Roboto',20,'bold'),text_color='#87CEFA',fg_color='#111111')
        gender_label.place(x=10,y=100)
        gender_list=['Male','Female','Other']
        self.gender_option=CTkOptionMenu(master=self.update_frame,values=gender_list,font=('Roboto',17),dropdown_font=('Roboto',17),fg_color='#222222',width=350,
         height=30,dropdown_fg_color='#111111',button_color='#222222',button_hover_color='#111111',bg_color='#111111')
        self.gender_option.place(x=25,y=140)

        birthday_label=CTkLabel(master=self.update_frame,text='Birthday',font=('Roboto',20,'bold'),text_color='#87CEFA',fg_color='#111111')
        birthday_label.place(x=10,y=180)
        self.birthday_entry=CTkEntry(master=self.update_frame,fg_color='#222222',font=('Roboto',17),width=350,height=30,bg_color='#222222',border_width=1)
        self.birthday_entry.place(x=25,y=220)

        update_phonenum_label=CTkLabel(master=self.update_frame,text='Phone Number',font=('Roboto',20,'bold'),text_color='#87CEFA',fg_color='#111111')
        update_phonenum_label.place(x=10,y=260)
        self.update_phonenum_entry=CTkEntry(master=self.update_frame,fg_color='#222222',font=('Roboto',17),width=350,height=30,bg_color='#222222',border_width=1)
        self.update_phonenum_entry.place(x=25,y=300)
        
        avatar=CTkLabel(master=self.update_frame,text='Avatar',font=('Roboto',20,'bold'),text_color='#87CEFA',fg_color='#0C0C0C')
        avatar.place(x=10,y=340)
        self.avtar_btn=CTkButton(master=self.update_frame,width=350,height=30,text='Choose Image',fg_color='#222222',bg_color='#222222',border_width=1,hover='disabled')
        self.avtar_btn.place(x=25,y=380)
        self.avtar_btn.bind('<Button-1>',lambda e: self.open_avatar_dialog())

        background=CTkLabel(master=self.update_frame,text='Profile Background',font=('Roboto',20,'bold'),text_color='#87CEFA',fg_color='#111111')
        background.place(x=10,y=420)
        self.background_btn=CTkButton(master=self.update_frame,text='Choose Image',fg_color='#222222',width=350,height=30,bg_color='#222222',border_width=1,hover='disabled')
        self.background_btn.place(x=25,y=460)
        self.background_btn.bind('<Button-1>',lambda e: self.open_background_dialog())

        self.update_succes=CTkButton(master=self.update_frame,width=410,height=40,text_color='white',fg_color='#222222',
                hover_color='#111111',text='Update',font=('Roboto',24,'bold'))
        self.update_succes.place(x=0,y=510)
        self.update_succes.unbind('<Button-1>')
        self.update_succes.bind('<Button-1>',lambda e: self.update_information_handle())

    def open_avatar_dialog(self):
        try:
            self.avatar_path_demo=filedialog.askopenfilename(title='Choose Avatar',filetypes=(('Image Files','*.jpg;*.png;*.jpeg'),))
            if self.avatar_path_demo:
                self.avtar_btn.configure(text='Selected')
        except Exception:
            pass
    def open_background_dialog(self):
        try:
            self.background_path_demo=filedialog.askopenfilename(title='Choose Background',filetypes=(('Image Files','*.jpg;*.png;*.jpeg'),))
            if self.background_path_demo:
                self.background_btn.configure(text='Selected')
        except Exception:
            pass                
    def update_information_handle(self):
        try:
            self.name_config=self.change_show_name.get()
            if self.name_config: 
                self.user_orm.update(idd=self.id,show_name=self.name_config)
                self.user_name=self.name_config
            self.gender_config=self.gender_option.get()
            if self.gender_config:  
                self.user_orm.update(idd=self.id,gender=self.gender_config)
                self.gender=self.gender_config

            self.dob_config=self.birthday_entry.get()
            self.dob_config=self.dob_config.replace(' ','')
            for i in self.dob_config:
                if i in ['/','-','_']:
                    self.dob_config=self.dob_config.replace(i,'-')
            if len(self.dob_config)>10:
                self.dob_config=None
            if self.dob_config: 
                self.user_orm.update(idd=self.id,birthday=self.dob_config)
                self.birthday=self.dob_config
            self.phone_number_config=self.update_phonenum_entry.get()
            if self.phone_number_config: 
                self.user_orm.update(idd=self.id,phone_number=self.phone_number_config)
                self.phone_number=self.phone_number_config
            if self.avatar_path_demo:
                self.avatar_path=self.avatar_path_demo
                self.user_orm.update(idd=self.id,avatar=self.avatar_path)
            if self.background_path_demo:
                self.bg_path=self.background_path_demo
                self.user_orm.update(idd=self.id,background=self.bg_path)
        except Exception:
            pass




    def destroy_info_ui(self):
        self.info_ui.destroy()
        self.profile_button.destroy()
        self.profile_button=CTkCanvas(master=self.button_frame,width=84,height=65,bg='#111111',highlightthickness=0)
        self.profile_button.place(x=426)
        self.image1=Image.open(self.avatar_path).resize((50,50),Image.BILINEAR)
        self.image1=ImageTk.PhotoImage(self.image1)
        self.profile_button.create_oval(20,54.5,64,10.5)
        self.profile_button.create_image(42,32.5,image=self.image1)
        self.profile_button.bind('<Button-1>',lambda e: self.open_profile())
