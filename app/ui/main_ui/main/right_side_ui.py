from app.setting.lib import *
class RightSideUI(CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.pack(fill='y',expand=True)
        self.first_album_list=[ BASE_DIR/'asset'/'feather'/'img1.jpeg',
                                 BASE_DIR/'asset'/'feather'/'img2.jpeg',
                                 BASE_DIR/'asset'/'feather'/'img3.jpeg',
                                 BASE_DIR/'asset'/'feather'/'img4.jpeg',
                                BASE_DIR/'asset'/'feather'/'img5.jpeg']
        
        self.second_album_list=[BASE_DIR/'asset'/'feather'/'img6.jpeg',
                                BASE_DIR/'asset'/'feather'/'img7.jpeg',
                                BASE_DIR/'asset'/'feather'/'img8.jpeg',
                                BASE_DIR/'asset'/'feather'/'img9.jpeg',
                                BASE_DIR/'asset'/'feather'/'img10.jpeg',]

        self.album1_index=0
        self.album2_index=0
        self.preload_images_list1=[]
        self.preload_images_list2=[]
        self.preload_images()
        self.init_ui()
    def preload_images(self):
        for i in range(5):
            image1=Image.open(self.first_album_list[i]).resize((235,413),Image.BILINEAR)
            image1=CTkImage(dark_image=image1,size=(235,413))
            self.preload_images_list1.append(image1)
        for i in range(5):
            image2=Image.open(self.second_album_list[i]).resize((235,427),Image.BILINEAR)
            image2=CTkImage(dark_image=image2,size=(235,427))
            self.preload_images_list2.append(image2)
        
    def init_ui(self):
        self.first_album_frame=CTkFrame(master=self,fg_color='#333333',height=413,width=235,border_width=0,border_color='#333333')
        self.first_album_frame.pack(pady=10)
        self.first_album_label=CTkLabel(master=self.first_album_frame,fg_color='#333333',text='',height=413,width=235,
        image=self.preload_images_list1[self.album1_index])
        self.first_album_label.pack()
        self.first_album_label.bind('<ButtonPress-1>',lambda e: self.change_first_album_frame())

        self.second_album_frame=CTkFrame(master=self,fg_color='#333333',height=427,width=235,border_width=0,border_color='#333333')
        self.second_album_frame.pack(padx=(10,10),pady=(17,0))
        self.second_album_label=CTkLabel(master=self.second_album_frame,fg_color='#333333',text='',height=427,width=235,
        image=self.preload_images_list2[self.album2_index])
        self.second_album_label.pack()
        self.second_album_label.bind('<ButtonPress-1>',lambda e: self.change_second_album_frame())
    

        self.brand_label=CTkLabel(master=self,text='MyGallery',height=20,font=('Impact',20),text_color='#CCCCCC',fg_color='transparent')
        self.brand_label.place(x=82,y=423)



    

    def change_first_album_frame(self):
        self.album1_index+=1
        if self.album1_index >=len(self.preload_images_list1):
             self.album1_index=0
        self.first_album_label.configure(image=self.preload_images_list1[self.album1_index])
    def change_second_album_frame(self):
        self.album2_index+=1
        if self.album2_index >=len(self.preload_images_list2):
            self.album2_index=0
        self.second_album_label.configure(image=self.preload_images_list2[self.album2_index])