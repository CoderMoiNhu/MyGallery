from app.setting.setting import *
from app.db.database import *
from app.ui.main_ui.main.main_ui import MainUI
from app.db.orm.user_orm import UserORM
class LoginUI:
    def __init__(self):
        self.login_app=select_app('main')           #khởi tạo giao diện
        self.login_app.title('MyGallery')
        self.login_app.resizable(False,False)   #không cho phóng to nhỏ
        self.login_app.geometry('500x500+600+200')
        set_appearance_mode('dark')
        self.user_orm=UserORM()
        self.init_ui()
    def init_ui(self):  #hàm tạo giao diện ban đầu
        self.container_frame=CTkFrame(master=self.login_app,fg_color='#1B1B1F',bg_color='#1B1B1F')    #khung cha
        self.container_frame.pack(fill='both',expand=True)
        self.login_title=CTkLabel(master=self.container_frame,text='SIGN IN',font=get_style('font_xl_bold'),text_color='#2563EB')
        self.login_title.pack(pady=(40,0))
        self.build_login()
    def build_login(self): 
        if hasattr(self,'message_label'):
            self.message_label.destroy()
        self.login_frame=CTkFrame(master=self.container_frame,fg_color=get_style('transparent'))
        self.login_frame.pack(fill='x',pady=(30,0))
        self.user_name_frame= CTkFrame(master=self.login_frame,fg_color=get_style('transparent'))
        self.user_name_frame.pack(fill='x',pady=10)
        self.user_name_entry= CTkEntry(master=self.user_name_frame,border_width=0,corner_radius=0,height=35,width=350,font=get_style('font_lg'),placeholder_text='Enter your username')
        self.user_name_entry.pack()
        self.pass_word_frame= CTkFrame(master=self.login_frame,fg_color=get_style('transparent'))
        self.pass_word_frame.pack(fill='x',pady=10) 
        self.pass_word_entry= CTkEntry(master=self.pass_word_frame,border_width=0,corner_radius=0,height=35,width=350,show='*',placeholder_text='Enter your password',font=get_style('font_lg'))
        self.pass_word_entry.pack()
        self.pass_word_label=CTkButton(master=self.login_frame,width=35,border_width=0,height=35,text='Show',font=('Roboto',18),text_color='white',fg_color='#1B1B1F',bg_color='#1B1B1F',hover_color='#111111')
        self.pass_word_label.place(y=65,x=425)
        self.pass_word_label.bind('<Button-1>',lambda e: self.show_password(0))
        self.button_frame= CTkFrame(master=self.container_frame,fg_color=get_style('transparent'))
        self.button_frame.pack(fill='x',pady=(0,0),expand=True)
        self.button2_frame= CTkFrame(master=self.button_frame,fg_color=get_style('transparent'))
        self.button2_frame.pack(fill='x',pady=(0,215),expand=True)
        self.button_button= CTkButton(master=self.button2_frame,text='Sign In',hover_color='#111111',
                                      fg_color=get_style('primary'),font=get_style('font_lg'),command= lambda : self.get_infor_login())    #commandlà lệnh được thực thi và cụ thể là hàm
        self.button_button.place(x=180,y=10)
        self.both_lable=CTkLabel(master=self.button_frame,text='No Account ?',font=get_style('font_md'),text_color=get_style('white'))
        self.both_lable.place(y=55,relx=(0.425))
        self.footer_frame=CTkFrame(master=self.button_frame,fg_color='transparent')
        self.footer_frame.place(relx=0.3,rely=0.9)
        self.footer_lable=CTkLabel(master=self.footer_frame,font=get_style('font_md'),text='Forgot Passwword ?',text_color=get_style('white'))
        self.footer_lable.place(relx=0.23)
        self.footer_lable.bind('<Button-1>',lambda x: self.move_to_authenticate_account())
        self.both_lable.bind('<Button-1>',lambda e :self.button_function_regist())
    def button_function_regist(self):    #hàm tạo các nút bấm   : #nút bấm khi chuyển qua giao diện đăng kí
        self.button_frame.destroy()
        if hasattr(self,'message_label'):
            self.message_label.destroy()
        self.login_title.configure(text='SIGN UP')
        self.button_frame.destroy()  #xoá bỏ nút bấm ở giao diện mặc định
        self.regist_frame=CTkFrame(master=self.container_frame,fg_color=get_style('transparent'))     #tạo khung mới nhưng vẫn dùng cùng khung giao diện đăng nhập và chỉ thêm 1 số giao diện
        self.regist_frame.pack(fill='x',pady=0)
        self.confirm_password_frame= CTkFrame(master=self.regist_frame,fg_color=get_style('transparent'))
        self.confirm_password_frame.pack(fill='x',pady=10)
        self.confirm_password_entry= CTkEntry(master=self.confirm_password_frame,border_width=0,font=get_style('font_lg'),corner_radius=0,height=35,width=350,placeholder_text='Enter password again ',show='*')
        self.confirm_password_entry.pack()
        self.confirm_password_label=CTkButton(master=self.regist_frame,width=35,border_width=0,height=35,text='Show',font=('Roboto',18),text_color='white',fg_color='#1B1B1F',bg_color='#1B1B1F',hover_color='#111111')
        self.confirm_password_label.place(y=10,x=425)
        self.confirm_password_label.bind('<Button-1>',lambda e: self.show_password(1))
        self.phonenumber_frame=CTkFrame(master=self.regist_frame,fg_color=get_style('transparent'))
        self.phonenumber_frame.pack(fill='x',pady=10)
        self.phonenumber_entry= CTkEntry(master=self.phonenumber_frame,border_width=0,font=get_style('font_lg'),corner_radius=0,height=35,width=350,placeholder_text='Enter your phone number')
        self.phonenumber_entry.pack()
        self.email_frame= CTkFrame(master=self.regist_frame,fg_color=get_style('transparent'))
        self.email_frame.pack(fill='x',pady=10)
        self.email_entry= CTkEntry(master=self.email_frame,border_width=0,font=get_style('font_lg'),corner_radius=0,height=35,width=350,placeholder_text='Enter your email address')
        self.email_entry.pack()
        self.sign_up_frame= CTkFrame(master=self.container_frame,fg_color='transparent')
        self.sign_up_frame.pack(pady=10)
        self.sign_up_Button = CTkButton(master=self.sign_up_frame,hover_color='#111111',font=get_style('font_lg'),text='SIGN UP',command= lambda : self.get_infor_register())   #command là lệnh được thực thi và cụ thể là hàm
        self.sign_up_Button.pack(padx=(10,10))
        self.both_lable=CTkLabel(master=self.sign_up_frame,text='Already have an account ?',font=get_style('font_md'),text_color=get_style('white'))
        self.both_lable.pack(side='bottom',pady=30)
        self.both_lable.unbind('<Button-1>')
        self.both_lable.bind('<Button-1>',lambda x: self.button_function_login()) 

    def button_function_login(self):
        self.container_frame.destroy()
        self.init_ui()
         # chuyển qua hàm xác thực lại tài khoản nếu bấm vào chữ quên mật khẩu

    def move_to_authenticate_account(self):   #hàm xác thực người quên mật khẩu
        self.container_frame.destroy() 
                                  #xoá cả khung cha đi và bắt đầu tạo 1 khung mới không liên quan gì đến 2 giao diện đăng nhập và đăng kí
        self.authen_frame_all=CTkFrame(master=self.login_app,fg_color='#1B1B1F',bg_color='#1B1B1F')
        self.authen_frame_all.pack(fill='both', expand=True)
        self.authen_frame=CTkFrame(master=self.authen_frame_all,fg_color='transparent',bg_color='transparent',height=300)  #tạo khung cho phần xác thực
        self.authen_frame.pack(fill='x',pady=40)
        self.authen_lable=CTkLabel(master=self.authen_frame,text='GET PASSWORD',font=get_style('font_xl_bold'),text_color=get_style('gray_light'))  
        self.authen_lable.pack(padx=20)
        self.get_email_entry=CTkEntry(master=self.authen_frame,border_width=0,corner_radius=0,font=get_style('font_lg'),placeholder_text='Enter registered email',height=35,width=350)
        self.get_email_entry.pack(pady=(28,0))
        self.send_email_button=CTkButton(master=self.authen_frame,hover_color='#111111',text='SEND CODE',corner_radius=0,font=get_style('font_lg'),fg_color=get_style('primary'),width=300)
        self.send_email_button.pack(pady=10)
        self.back_lable=CTkLabel(master=self.authen_frame,text='Come back to login page ?',font=get_style('font_md'),text_color=get_style('gray_light'))
        self.back_lable.pack(pady=(20,5))
        self.back_lable.bind('<Button-1>',lambda x: self.move_to_first_ui())        #khi nhấn vào sẽ quay trở lại giao diện đầu qua hàm move_to_first_ui

    def move_to_first_ui(self):
        self.authen_frame_all.destroy()
        self.init_ui()
    #xoá khung xác thực đi
                    #khởi tạo khung mặc định cũ
    def get_infor_register(self):
        self.error=0
        self.email_check=0
        self.pass_word_check=0
        username=self.user_name_entry.get().strip()
        password=self.pass_word_entry.get().strip()
        password_again=self.confirm_password_entry.get().strip()
        email=self.email_entry.get().strip()
        phone_number=self.phonenumber_entry.get().strip()
        if len(password)<=8 :
            self.message(3)
            self.error+=1
            self.pass_word_check=1
        a=email.count('@gmail.com')
        b=email.count('@yahoo.com')
        c=email.count('@outlook.com')
        d=email.count('@icloud.com')
        if a+b+c+d==1:
            self.error=self.error
        else:
            self.error+=1
        if password!=password_again:
            self.error +=1
            self.pass_word_check=0

        all_user=self.user_orm.read_all()
        if all_user is not None:
            number=phone_number[1::]
            if username in [i.username for i in all_user ]: 
                self.error+=1
            elif number in [str(i.phone_number) for i in all_user]:
                self.error+=1
            elif email in [i.email for i in all_user]:
                self.error+=1   
        if len(username) and len(password) and len(email) and len(phone_number) and len(password_again) >0 and self.error==0:  
                mail_lists=['@gmail.com','@yahoo.com','@outlook.com','@icloud.com']
                type=filter(lambda x: username.count(x),mail_lists)
                type=list(type)
                if type:
                    for i in type:
                        show_name=username.replace(i,'')
                else:
                    show_name=username
                self.user_orm.create(UserInfo(username=username,
                                            password=password,
                                            phone_number=phone_number,
                                            email=email,
                                            show_name=show_name,
                                            avatar=str(BASE_DIR/'asset'/'feather'/'default-avatar.png'),
                                            background=str(BASE_DIR/'asset'/'feather'/'img30.jpeg' ))) 
                self.message(1)
        else: 
            if self.error>=1 and self.pass_word_check==0 :
                self.message(0)
            elif self.error>=1 and self.pass_word_check ==1:
                self.message(3)
            
        
        

    def get_infor_login(self):
        try:       #hàm check thông tin người đăng nhập
            username=self.user_name_entry.get().strip()         #    lấy tên user ứng với username vừa nhập và so với cái
            password=self.pass_word_entry.get().strip()      #    username trong cơ sở dữ liệu đầu tiên trùng với username vừa nhập đó
            user=self.user_orm.read(username=username)
            if user is not None:
                if user.password==password:
                    self.login_app.destroy()
                    self.main_ui=MainUI(authen_ui=LoginUI,username=user.username)
                    self.main_ui.run_ui()
                elif user.password!=password:
                    self.message(2)
            if user is None:
                self.message(2)
        except Exception: pass
    def show_password(self,index):
        if index==0:
            if self.pass_word_entry.cget('show')=='*':
                self.pass_word_entry.configure(show='')
                self.pass_word_label.configure(text='Hide')
            elif self.pass_word_entry.cget('show')=='':
                self.pass_word_entry.configure(show='*')
                self.pass_word_label.configure(text='Show')
        elif index==1:
            if self.confirm_password_entry.cget('show')=='*':
                self.confirm_password_entry.configure(show='')
                self.confirm_password_label.configure(text='Hide')
            elif self.confirm_password_entry.cget('show')=='':
                self.confirm_password_entry.configure(show='*')
                self.confirm_password_label.configure(text='Show')
    def message(self,type):
        if hasattr(self,'message_label'):
            self.message_label.destroy()

        message_list= ['Invalid registration,\n please try again',
                       'Registered successfully ',
                       'Login failed,\n please try again',
                       'Password needs to be\nlonger than 8 characters'    
                    ]
        
        self.message_label=CTkLabel(master=self.container_frame,text=message_list[type],text_color='white',font=('Roboto',12,'italic'))
        self.message_label.place(x=330,y=390)
        self.message_label.after(3000,lambda : self.message_label.destroy())

    def run_ui(self):       #hàm chạy chương trình
        self.login_app.mainloop()
    
    