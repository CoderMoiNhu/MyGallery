from app.setting.lib import *
from app.setting.lib import find_chrome_path
class MainScreenUI(CTkFrame):
    def __init__(self,master,super_master,**kwargs):
        super().__init__(master=master,**kwargs)
        self.super_master=super_master
        self.pack(fill='both',expand=True)
        self.album1_index=0
        self.album2_index=0
        self.album3_index=0
        self.preload_images_list1=self.super_master.preload_gallery1
        self.preload_images_list2=self.super_master.preload_gallery2
        self.preload_images_list3=self.super_master.preload_gallery3
        self.init_ui()
    def init_ui(self):
        self.big_frame=CTkFrame(master=self,fg_color='#333333')
        self.big_frame.pack(fill='both',expand=True)
        self.frame1=CTkFrame(master=self.big_frame,width=668,height=866,fg_color='transparent')
        self.frame1.place(x=10,y=10)
        self.frame1_label=CTkLabel(master=self.frame1,text='',image=self.preload_images_list1[self.album1_index]
            ,width=668,height=866)
        self.frame1_label.pack()
        self.frame1_label.bind('<ButtonPress-1>',lambda e: self.change_first_album_frame())

        self.frame2=CTkFrame(master=self.big_frame,width=506,height=420,fg_color='transparent')
        self.frame2.place(x=688,y=10)
        self.frame2_label=CTkLabel(master=self.frame2,text='', image=self.preload_images_list2[self.album2_index]
           ,width=506,height=420)
        self.frame2_label.pack()
        self.frame2_label.bind('<ButtonPress-1>',lambda e: self.change_second_album_frame())

        self.frame3=CTkFrame(master=self.big_frame,width=506,height=354,fg_color='transparent')
        self.frame3.place(x=688,y=440)
        self.frame3_label=CTkLabel(master=self.frame3,text='',image=self.preload_images_list3[self.album3_index]
           ,width=506,height=354)
        self.frame3_label.pack()
        self.frame3_label.bind('<ButtonPress-1>',lambda e: self.change_third_album_frame())

        self.frame4=CTkFrame(master=self.big_frame,height=60,width=300,fg_color='transparent')
        self.frame4.place(y=810,x=790)
        self.more_icon=CTkLabel(master=self.frame4,
    text='',image=CTkImage(dark_image=Image.open( BASE_DIR/'asset'/'feather'/'more.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.more_icon.place(x=65,y=10)
        self.more_label=CTkLabel(master=self.frame4,text='ViewMore',font=('Roboto',24,'underline'),text_color='white',fg_color='transparent')
        self.more_label.place(x=115,y=16)
        self.more_icon.bind('<ButtonPress-1>',lambda e: self.move_to_google_picture_web())
        self.more_label.bind('<ButtonPress-1>',lambda e: self.move_to_google_picture_web())

    def change_first_album_frame(self):
        self.album1_index+=1
        if self.album1_index >=len(self.preload_images_list1):
             self.album1_index=0
        self.frame1_label.configure(image=self.preload_images_list1[self.album1_index])
    def change_second_album_frame(self):
        self.album2_index+=1
        if self.album2_index >=len(self.preload_images_list2):
            self.album2_index=0
        self.frame2_label.configure(image=self.preload_images_list2[self.album2_index])
    def change_third_album_frame(self):
        self.album3_index+=1
        if self.album3_index >=len(self.preload_images_list3):
            self.album3_index=0
        self.frame3_label.configure(image=self.preload_images_list3[self.album3_index])
    def move_to_google_picture_web(self):
        url='https://www.pexels.com/vi-vn/'
        chrome_path=find_chrome_path()
        if chrome_path:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url) 


        