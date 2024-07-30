from app.setting.lib import *


class LeftSideUI(CTkFrame):
    def __init__(self,master,controller,**kwargs):
        super().__init__(master=master,**kwargs)
        self.controller=controller
        self.pack(fill='y',expand=True)
        
        self.init_ui()
    def init_ui(self):
        self.contents_frame=CTkFrame(master=self,height=450,width=230,fg_color='#0C0C0C')
        self.contents_frame.pack()

        self.gallery_frame=CTkFrame(master=self.contents_frame,height=60,width=230,fg_color='#222222')
        self.gallery_frame.place(x=20,y=50)

        self.gallery_icon=CTkLabel(master=self.gallery_frame,
    text='',image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'gallery.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.gallery_icon.place(x=10,y=10)
        self.gallery_label=CTkLabel(master=self.gallery_frame,text='Gallery',font=('Roboto',24,),text_color='white')
        self.gallery_label.place(x=55,y=16)
        self.gallery_frame.bind('<ButtonPress-1>',lambda e: self.change_your_gallery_frame())
        self.gallery_icon.bind('<ButtonPress-1>',lambda e: self.change_your_gallery_frame())
        self.gallery_label.bind('<ButtonPress-1>',lambda e: self.change_your_gallery_frame())

        self.your_album_frame=CTkFrame(master=self.contents_frame,height=60,width=230,fg_color='#0C0C0C')
        self.your_album_frame.place(x=20,y=130)
        self.your_album_icon=CTkLabel(master=self.your_album_frame, text='',
                image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'album.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.your_album_icon.place(x=10,y=10)
        self.your_album_label=CTkLabel(master=self.your_album_frame,text='Album',font=('Roboto',24,),text_color='white')
        self.your_album_label.place(x=55,y=16)
        self.your_album_frame.bind('<ButtonPress-1>',lambda e: self.change_your_album_frame())
        self.your_album_icon.bind('<ButtonPress-1>',lambda e: self.change_your_album_frame())
        self.your_album_label.bind('<ButtonPress-1>',lambda e: self.change_your_album_frame())

        self.edit_image_frame=CTkFrame(master=self.contents_frame,height=60,width=230,fg_color='#0C0C0C')
        self.edit_image_frame.place(x=20,y=210)
        self.edit_image_icon=CTkLabel(master=self.edit_image_frame, text='',
                image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'edit.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.edit_image_icon.place(x=10,y=10)
        self.edit_image_label=CTkLabel(master=self.edit_image_frame,text='Editing',font=('Roboto',24,),text_color='white')
        self.edit_image_label.place(x=55,y=18)
        self.edit_image_frame.bind('<ButtonPress-1>',lambda e: self.change_your_edit_frame(image_path=None))
        self.edit_image_icon.bind('<ButtonPress-1>',lambda e: self.change_your_edit_frame(image_path=None))
        self.edit_image_label.bind('<ButtonPress-1>',lambda e: self.change_your_edit_frame(image_path=None))
    def reset_image_frame(self):
        self.gallery_frame.configure(fg_color='#0C0C0C') 
        self.your_album_frame.configure(fg_color='#0C0C0C') 
        self.edit_image_frame.configure(fg_color='#0C0C0C') 
    def change_your_gallery_frame(self):
        if self.gallery_frame.cget('fg_color')=='#0C0C0C':
            self.controller.add_gallery_frame()
            self.reset_image_frame()
            self.gallery_frame.configure(fg_color='#222222')
    def change_your_album_frame(self):
        if self.your_album_frame.cget('fg_color')=='#0C0C0C':
            self.controller.add_album_frame()
            self.reset_image_frame()
            self.your_album_frame.configure(fg_color='#222222')

    def change_your_edit_frame(self,image_path):
        if image_path == None:
            pass
        if self.edit_image_frame.cget('fg_color')=='#0C0C0C':
            self.controller.add_edit_frame(image_path)
            self.reset_image_frame()
            self.edit_image_frame.configure(fg_color='#222222')