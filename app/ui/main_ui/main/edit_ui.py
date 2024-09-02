from app.setting.lib import *
from app.ui.main_ui.main.album_ui import AlbumUI

class EditUI(CTkFrame):
    def __init__(self,master,super_master,super_master2,image_path,**kwargs):
        super().__init__(master=master,**kwargs)
        self.super_master=super_master
        self.super_master2=super_master2
        self.image_path=image_path
        self.place(x=230,y=65)
        self.icon_list1=[BASE_DIR/'asset'/'feather'/'crop.png',
                         BASE_DIR/'asset'/'feather'/'resize.png',
                         BASE_DIR/'asset'/'feather'/'rotate.png',
                         BASE_DIR/'asset'/'feather'/'flip.png',
                         BASE_DIR/'asset'/'feather'/'text.png',
                         BASE_DIR/'asset'/'feather'/'shape.png',
                         BASE_DIR/'asset'/'feather'/'brightness.png',
                         BASE_DIR/'asset'/'feather'/'contrast.png',
                         BASE_DIR/'asset'/'feather'/'color_filter.icon.png',
                         BASE_DIR/'asset'/'feather'/'loading.png',
                         BASE_DIR/'asset'/'feather'/'loading.png',
                         BASE_DIR/'asset'/'feather'/'loading.png',
                         BASE_DIR/'asset'/'feather'/'loading.png',
                         BASE_DIR/'asset'/'feather'/'loading.png',
                                                                 ]
        self.filter_list=[BASE_DIR/'asset'/'feather'/'none.png',
                          BASE_DIR/'asset'/'feather'/'vintage.png',
                         BASE_DIR/'asset'/'feather'/'bright_fresh.png',
                         BASE_DIR/'asset'/'feather'/'cool_blue.png',
                         BASE_DIR/'asset'/'feather'/'warm_autumn.png',
                         BASE_DIR/'asset'/'feather'/'black_white.png',
                         BASE_DIR/'asset'/'feather'/'muted_tones.png',
                         BASE_DIR/'asset'/'feather'/'high_contrast.png',
                         BASE_DIR/'asset'/'feather'/'dramatic.png',
                         BASE_DIR/'asset'/'feather'/'vivid_colors.png',
                         BASE_DIR/'asset'/'feather'/'soft_pastel.png',
                                  ]
        self.introduce_options1 = [
     "Cut out desired areas.",   "Adjust image size.","Spin the image.", "Mirror the image.",
    "Overlay text.", "Insert shapes.", "Modify brightness.","Fine-tune contrast.", "Enhance colors.","Loading","Loading","Loading","Loading","Loading"
        ]
        self.color_value3={'Blue': (0, 0, 255),
                'Red': (255, 0, 0),
                'Green': (0, 255, 0),
                'Black': (0, 0, 0),
                'White': (255, 255, 255),
                'Yellow': (255, 255, 0),
                'Purple': (128, 0, 128),
                'Orange': (255, 165, 0),
                'Pink': (255, 192, 203),
                'Teal': (0, 255, 128)}
        self.crop_list=[]
        self.init_ui()
        if not self.image_path:
            self.ask_choose_image_to_edit()             
                                    
                                   
    def ask_choose_image_to_edit(self):
        self.ask_frame=CTkFrame(master=self,width=800,height=600,fg_color='transparent',border_width=0)
        self.ask_frame.place(x=310,y=200)
        self.bg_label=CTkLabel(master=self.ask_frame,width=800,height=600,text='',
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'blur.jpeg').resize((800,600),Image.LANCZOS),size=(800,600)))
        self.bg_label.place(x=0,y=0)
        self.label=CTkLabel(master=self.ask_frame,width=600,height=100,fg_color='#0C0C0C',font=('Roboto',30,'bold'),text_color='white',
            text='CHOOSE AN IMAGE TO EDIT')
        self.label.place(x=100,y=50)
        self.return_album_frame=CTkButton(master=self.ask_frame,width=80,height=80,text='',hover='disabled',fg_color='#0C0C0C',command=self.return_album_frame,
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'album.png').resize((70,70),Image.BILINEAR),size=(70,70)))
        self.return_album_frame.place(x=225,y=200)
        self.return_album_label=CTkLabel(master=self.ask_frame,width=80,height=80,fg_color='#0C0C0C',font=('Roboto',24,'bold'),text_color='white',
            text='Come To My Album  ')
        self.return_album_label.place(x=305,y=200)

        self.choose_directly=CTkButton(master=self.ask_frame,width=80,height=80,text='',hover='disabled',fg_color='#0C0C0C',command=self.choose_directly,
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'folder.png').resize((60,60),Image.BILINEAR),size=(60,60)))
        self.choose_directly.place(x=225,y=300)
        self.choose_directly_label=CTkLabel(master=self.ask_frame,width=80,height=80,fg_color='#0C0C0C',font=('Roboto',24,'bold'),text_color='white',
            text='Come To My Folder   ')
        self.choose_directly_label.place(x=300,y=300)
        self.preview_image_frame.bind('<ButtonPress>',lambda e: self.ask_frame.destroy())

    def init_ui(self):
        self.work_with_image_frame=CTkFrame(master=self,width=1440,height=147,fg_color='#333333',bg_color='#333333')
        self.work_with_image_frame.place(x=10,y=0)
        self.options_frame=CTkFrame(master=self.work_with_image_frame,width=1420,height=80,fg_color='#333333',bg_color='#333333')
        self.options_frame.place(x=10,y=10)
        self.first_option_ui()
        self.preview_image_frame=CTkFrame(master=self,height=716,width=1440,fg_color='#333333',bg_color='#333333')
        self.preview_image_frame.place(x=10,y=160)
        if self.image_path:
            self.upload_main_image()
    def first_option_ui(self):
        compact_page=CTkButton(master=self.options_frame,fg_color='transparent',height=50,width=50,text='',hover='disabled',command=self.compact_options,
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'back.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        compact_page.place(x=1360,y=8)
        x=0
        for i in range(14):
            feature=CTkButton(master=self.options_frame,image=CTkImage(dark_image=Image.open(self.icon_list1[i]).resize((70,70),Image.BILINEAR),size=(70,70)),
                    fg_color='transparent',hover_color='#222222',width=85,height=80,text='')
            feature.place(x=x,y=0)
            x+=97
            feature.bind('<Enter>',lambda e,index=i,feature=feature: intro_options(index,feature))
            feature.bind('<ButtonPress-1>',lambda e, index=i,feature=feature:choose_options(index,feature))
            
        def intro_options(index,feature):
            x=feature.winfo_x()+8
            y=feature.winfo_y()+95
            introduce_ui=CTkLabel(master=self.work_with_image_frame,width=80,height=30,text=self.introduce_options1[index],
    font=('Roboto',14),text_color='white',fg_color='#222222'
                                )
            introduce_ui.place(x=x,y=y)
            feature.bind('<Leave>',lambda e: close_introduce(introduce_ui))
            def close_introduce(introduce_ui):
                introduce_ui.place_forget()
        def choose_options(index,feature):
            if index==0 and self.image_path:
                self.compact_options()
                self.move_to_crop_feature()
            if index==1 and self.image_path:
                self.compact_options()
                self.move_to_resize_feature()
            if index==2 and self.image_path:
                self.compact_options()
                self.move_to_rotate_feature()
            if index==3 and self.image_path:
                self.compact_options()
                self.move_to_flip_feature()
            if index==4 and self.image_path:
                self.compact_options()
                self.move_to_text_feature()
            if index==5 and self.image_path:
                self.compact_options()
                self.move_to_shape_feature()
            if index==6 and self.image_path:
                self.compact_options()
                self.move_to_brightness_feature()
            if index==7 and self.image_path:
                self.compact_options()
                self.move_to_contrast_feature()
            if index==8 and self.image_path:
                self.compact_options()
                self.move_to_filter_color_feature()
    def compact_options(self):
        self.work_with_image_frame.destroy()
        self.work_with_image_frame=CTkFrame(master=self,width=1440,height=147,fg_color='#333333',bg_color='#333333')
        self.work_with_image_frame.place(x=10,y=0)
        self.all_options=CTkButton(master=self.work_with_image_frame,fg_color='transparent',height=50,width=50,text='',hover='disabled',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'next.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.all_options.bind('<ButtonPress-1>',lambda e: self.all_optionss(image=None))
        self.all_options.place(x=20,y=18)
    def all_optionss(self,image):
        if image !=None:
            self.all_options.unbind('<ButtonPress-1>')
            self.main_image.unbind('<Button-3>')
            self.main_image.unbind('<ButtonPress-1>')
            self.main_image.unbind('<Motion-B1>')
            self.virtual_storage.close()
            self.virtual_storage=None
            gc.collect()
            self.virtual_storage = BytesIO()
            image.save(self.virtual_storage, format=self.format)
        self.work_with_image_frame.destroy()
        self.work_with_image_frame=CTkFrame(master=self,width=1440,height=147,fg_color='#333333',bg_color='#333333')
        self.work_with_image_frame.place(x=10,y=0)
        self.options_frame=CTkFrame(master=self.work_with_image_frame,width=1420,height=80,fg_color='#333333',bg_color='#333333')
        self.options_frame.place(x=10,y=10)
        self.first_option_ui()

    def return_album_frame(self):
        self.destroy()
        self.super_master2.change_your_album_frame()
    def choose_directly(self):
        file=filedialog.askopenfilename(title='Choose Files',
                                        filetypes=(('Image Files','*.png;*.jpg;*.jpeg;*.gif'),)
        )
        if file:
            self.image_path=file
            self.ask_frame.destroy()
            self.upload_main_image()
    def upload_main_image(self):
        self.transparent_image_list=[]
        self.transparent_image_shape=[]
        global width,height,image
        image=Image.open(self.image_path)
        self.only_image=image
        width,height=image.size
        self.format=image.format
        self.virtual_storage=BytesIO()
        image.save(self.virtual_storage,format=self.format)
        if width<=height:
                scale=716/height
                new_height=int(height*scale)
                new_width=int(width*scale)
        if width>height:
            scale=height/(width/1440)
            if width>1440:
                if scale<716:
                    new_height=int(height/(width/1440))
                    new_width=1440
                if scale>716:
                        new_height=716
                        new_width=int(width*(new_height/height))
            elif width<=1440:
                scale=716/height
                new_height=716
                new_width=int(width*scale)
        self.only_width=new_width
        self.only_height=new_height
        image=CTkImage(dark_image=Image.open(self.image_path).resize((self.only_width,self.only_height),Image.LANCZOS),size=(self.only_width,self.only_height))
        self.main_image=CTkLabel(master=self.preview_image_frame,image=image,text='')
        self.main_image.place(x=(1440-self.only_width)/2,y=(716-self.only_height)/2)


    def move_to_crop_feature(self):
        self.all_crop_frame=CTkFrame(master=self.work_with_image_frame,width=1430,height=147,fg_color='#333333')
        self.all_crop_frame.place(x=0,y=0)
        self.all_options.destroy()
        self.all_options=CTkButton(master=self.all_crop_frame,fg_color='transparent',height=50,width=50,text='',hover='disabled',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'next.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.all_options.bind('<ButtonPress-1>',lambda e: self.all_optionss(image=None))
        self.all_options.place(x=20,y=18)

        self.cut_information=CTkLabel(master=self.work_with_image_frame,width=40,height=40,text='',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'information.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.cut_information.place(x=135,y=105)
        self.cut_information.bind('<Enter>',lambda e: self.crop_information_func())
        self.cut_information.bind('<Leave>',lambda e:   self.cut_information_frame.destroy())

        reset=CTkButton(master= self.all_crop_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',command=self.reset_crop_img,corner_radius=30,
  text='', image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'reset.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        reset.place(x=1250,y=10)
        
        save=CTkButton(master= self.all_crop_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',command=self.save_crop_img
       ,corner_radius=30,image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        save.place(x=1250,y=80)

        cut_btn=CTkButton(master=self.all_crop_frame,width=120,height=100,fg_color='#0C0C0C',hover_color='#222222',text='',command=self.cut_crop_img,
image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'cut.png').resize((120,100),Image.BILINEAR),size=(120,100)))
        cut_btn.place(x=660,y=23.5)


        self.xl=0
        self.xr=self.only_width
        self.yt=0
        self.ym=self.only_height
        self.lmask=None
        self.rmask=None
        self.tmask=None
        self.mmask=None
        self.width_topleft=0
        self.height_topleft=0
        self.virtual_storage.seek(0)
        self.origin_crop_img=self.virtual_storage.read()
        self.origin_crop_img=Image.open(BytesIO(self.origin_crop_img))
        if len(self.crop_list)<1:
            self.crop_list.append(self.origin_crop_img)
        self.base_width,self.base_height=self.origin_crop_img.size
        self.width_res=self.base_width / self.only_width
        self.height_res=self.base_height / self.only_height 
        self.width_bottomright=self.only_width *self.width_res
        self.height_bottomright=self.only_height *self.height_res

        self.final_image_crop=self.origin_crop_img
        self.main_image.bind('<ButtonPress-1>',lambda e: self.get_crop_coord_1(e))
    
    def crop_information_func(self):
        self.cut_information_frame=CTkFrame(master=self,height=110,width=300,fg_color='#0C0C0C')
        self.cut_information_frame.place(x=30,y=140)
        first=CTkLabel(master=self.cut_information_frame,text='‧ Move border to crop the image',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        first.place(x=10,y=10)
        second=CTkLabel(master=self.cut_information_frame,text='‧ Click the reset button to return\n to the original image',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        second.place(x=10,y=50)
        

    def get_crop_coord_1(self,event):
        x=event.x
        y=event.y
        self.only_left=list(product([i for i in range(self.xl,self.xl+10)],[i for i in range(10,self.only_height-9)]))
        self.only_right=list(product([i for i in range(self.xr-9,self.xr+1)],[i for i in range(10,self.only_height-9)]))
        self.only_top=list(product([i for i in range(10,self.only_width-9)],[i for i in range(self.yt,self.yt+10)]))
        self.only_bottom=list(product([i for i in range(10,self.only_width-9)],[i for i in range(self.ym-9,self.ym+1)]))
        self.crop_coord1=(x,y)
        self.main_image.unbind('<B1-Motion>')
        self.main_image.bind('<B1-Motion>',lambda e: self.get_crop_coord_2(e))
    
    def get_crop_coord_2(self,event):
        x=event.x
        y=event.y
        self.crop_coord2=(x,y)
        if self.crop_coord1 in self.only_left or self.crop_coord1 in self.only_right or self.crop_coord1 in self.only_top or self.crop_coord1 in self.only_bottom :
            if self.crop_coord1 in self.only_left:
                if self.lmask:
                    self.lmask.destroy()
                self.lmask= CTkFrame(master=self.preview_image_frame,fg_color='#333333',bg_color='#333333',width=x,height=self.only_height)
                self.lmask.place(x=(1440-self.only_width)/2,y=0)
                if x>0: self.xl=x
                else:   
                    self.xl=0
                    x=0
                self.width_topleft=int(x*self.width_res)
            elif self.crop_coord1 in self.only_right:
                if self.rmask:
                    self.rmask.destroy()
                self.rmask=CTkFrame(master=self.preview_image_frame,fg_color='#333333',bg_color='#333333',width=self.only_width-x,height=self.only_height)
                self.rmask.place(x=(1440-self.only_width)/2+x,y=0)
                if x<self.only_width: self.xr=x
                else:
                    self.xr=self.only_width
                    x=0
                self.width_bottomright=int(x * self.width_res)
            elif self.crop_coord1 in self.only_top:
                if self.tmask:
                    self.tmask.destroy()
                self.tmask=CTkFrame(master=self.preview_image_frame,fg_color='#333333',bg_color='#333333',width=self.only_width,height=y)
                self.tmask.place(x=(1440-self.only_width)/2,y=0)
                if y>0: self.yt=y
                else:   
                    self.yt=0
                    y=0
                self.height_topleft=int(y*self.height_res)
            elif self.crop_coord1 in self.only_bottom:
                if self.mmask:
                    self.mmask.destroy()
                self.mmask=CTkFrame(master=self.preview_image_frame,fg_color='#333333',bg_color='#333333',width=self.only_width,height=self.only_height-y)
                self.mmask.place(x=(1440-self.only_width)/2,y=(716-self.only_height)/2+y)
                if y<self.only_height: self.ym=y
                else:
                    self.ym=self.only_height
                    y=0
                self.height_bottomright=int(y * self.height_res)

    def cut_crop_img(self):
        image_crop=self.origin_crop_img.crop((self.width_topleft,self.height_topleft,self.width_bottomright,self.height_bottomright))
        self.final_image_crop=image_crop.copy()
        width,height=self.final_image_crop.size
        if width<=height:
                scale=716/height
                new_height=int(height*scale)
                new_width=int(width*scale)
        if width>height:
            scale=height/(width/1440)
            if width>1440:
                if scale<716:
                    new_height=int(height/(width/1440))
                    new_width=1440
                if scale>716:
                        new_height=716
                        new_width=int(width*(new_height/height))
            elif width<=1440:
                scale=716/height
                new_height=716
                new_width=int(width*scale)
        self.only_width=new_width
        self.only_height=new_height            
        self.virtual_storage.close()
        self.virtual_storage=None
        gc.collect()
        self.virtual_storage=BytesIO()
        self.final_image_crop.save(self.virtual_storage,self.format)
        self.apply_to_main_image(self.final_image_crop,self.only_width,self.only_height)
        self.all_crop_frame.destroy()
        self.move_to_crop_feature()

        
    def reset_crop_img(self):
        self.virtual_storage.close()
        self.virtual_storage=None
        gc.collect()
        self.virtual_storage=BytesIO()
        for i in self.crop_list:
            i.save(self.virtual_storage,self.format)
        self.apply_to_main_image(i,self.only_width,self.only_height)
        self.all_crop_frame.destroy()
        self.move_to_crop_feature()
        self.cut_crop_img()
    def save_crop_img(self):
        file_save=filedialog.asksaveasfilename(title='Save As',
                 defaultextension='*.png',
                     filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_save:
            self.final_image_crop.save(file_save)

            
            




             


    def move_to_resize_feature(self):
        try:
            current_size=f'{width} x {height}'
            self.current_size_label= CTkLabel(master=self.work_with_image_frame,text=f'Current:     {current_size} pixels'
  ,font=('Roboto',24,'bold'),text_color='white')
            self.current_size_label.place(x=520,y=10)

            self.new_size_label=CTkLabel(master=self.work_with_image_frame,font=('Roboto',24,'bold'),text_color='white'
            ,text='New:')
            self.new_size_label.place(x=520,y=60)
            self.new_width_size=CTkEntry(master=self.work_with_image_frame,font=('Roboto',24,'bold'),text_color='white',border_width=1,
            fg_color='#0C0C0C',width=100,height=30,)
            self.new_width_size.place(y=55,x=625)
            CTkLabel(master=self.work_with_image_frame,text='x',font=('Roboto',24,'bold'),text_color='white',).place(x=730,y=60)
            self.new_height_size=CTkEntry(master=self.work_with_image_frame,font=('Roboto',24,'bold'),text_color='white',border_width=1,
            fg_color='#0C0C0C',width=100,height=30)
            self.new_height_size.place(y=55,x=750)
            CTkLabel(master=self.work_with_image_frame,text='pixels',font=('Roboto',24,'bold'),text_color='white',).place(x=860,y=60)
            self.new_percent_size=CTkEntry(master=self.work_with_image_frame,font=('Roboto',24,'bold'),text_color='white',
            fg_color='#0C0C0C',width=100,height=30,border_width=1,)
            self.new_percent_size.place(y=100,x=750)
            CTkLabel(master=self.work_with_image_frame,text='%',font=('Roboto',24,'bold'),text_color='white',).place(x=860,y=105)
            save_button=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',command=self.save_resize_image,text='',corner_radius=30,
 image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)))
            save_button.place(x=1250,y=70)


        except Exception:
            pass
    def save_resize_image(self):
        try:
            self.width_suggest=self.new_width_size.get()
            self.height_suggest=self.new_height_size.get()
            self.percent_suggest=self.new_percent_size.get()
            image=Image.open(self.image_path)
            width,height=image.size
            if self.percent_suggest:

                percent = int(self.percent_suggest)
                new_width1 = int(width * percent / 100)
                new_height1 = int(height * percent / 100)
            elif self.width_suggest and self.height_suggest:
                    new_width1 = int(self.width_suggest)
                    new_height1 = int(self.height_suggest)
            else: pass
            if new_width1<=3840 and new_height1<=2160:
                image=image.resize((new_width1,new_height1),Image.LANCZOS)
                file_save=filedialog.asksaveasfilename(title='Save As',
                defaultextension='*.png',
                    filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
                if file_save:
                    image.save(file_save)
          
        except Exception:
            pass

    def move_to_rotate_feature(self):
        left=CTkButton(master=self.work_with_image_frame,width=80,height=40,text='',hover_color='#222222',fg_color='#0C0C0C',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'left.png').resize((40,80),Image.BILINEAR),size=(40,80)))
        left.place(x=520,y=30)
        left.bind('<ButtonPress-1>',lambda e: self.save_rotate_image('left'))
        right=CTkButton(master=self.work_with_image_frame,width=80,height=40,text='',hover_color='#222222',fg_color='#0C0C0C',
            image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'right.png').resize((40,80),Image.BILINEAR),size=(40,80)))
        right.place(x=620,y=30)
        right.bind('<ButtonPress-1>',lambda e: self.save_rotate_image('right'))
        up=CTkButton(master=self.work_with_image_frame,width=80,height=40,text='',fg_color='#0C0C0C',hover_color='#222222',
            image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'up.png').resize((40,80),Image.BILINEAR),size=(40,80)))
        up.place(x=720,y=30)
        up.bind('<ButtonPress-1>',lambda e: self.save_rotate_image('up'))
        down=CTkButton(master=self.work_with_image_frame,width=80,height=40,text='',fg_color='#0C0C0C',hover_color='#222222',
            image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'down.png').resize((40,80),Image.BILINEAR),size=(40,80)))
        down.place(x=820,y=30)
        down.bind('<ButtonPress-1>',lambda e: self.save_rotate_image('down'))
        self.save_button=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',command=None,text='',corner_radius=30,
 image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.save_button.place(x=1250,y=80)

    def save_rotate_image(self,anchor):
        try:
            self.virtual_storage.seek(0)
            image=self.virtual_storage.read()
            image=BytesIO(image)
            image=Image.open(image)
            if anchor =='right':
                rotated_image=image.rotate(-90,expand=True)
            elif anchor=='left':
                rotated_image=image.rotate(90,expand=True)
            elif anchor=='up':
                rotated_image=image.rotate(180)
            elif anchor=='down':
                rotated_image=image.rotate(-180)
            self.virtual_storage.close()
            self.virtual_storage=None
            gc.collect()
            self.virtual_storage=BytesIO()
            rotated_image.save(self.virtual_storage,self.format)
            width,height=rotated_image.size
            if width<=height:
                    scale=716/height
                    new_height2=int(height*scale)
                    new_width2=int(width*scale)
            if width>height:
                scale=height/(width/1440)
                if width>1440:
                    if scale<716:
                        new_height2=int(height/(width/1440))
                        new_width2=1440
                    if scale>716:
                            new_height2=716
                            new_width2=int(width*(new_height2/height))
                elif width<=1440:
                    scale=716/height
                    new_height2=716
                    new_width2=int(width*scale)
            self.only_width=new_width2
            self.only_height=new_height2
            self.apply_to_main_image(rotated_image,self.only_width,self.only_height)
            self.save_button.bind('<ButtonPress-1>',lambda e: save_rotate_img())
            def save_rotate_img():
                file_save=filedialog.asksaveasfilename(title='Save As',
                 defaultextension='*.png',
                     filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
                if file_save:
                    rotated_image.save(file_save)
        except Exception:
            pass
            
    def move_to_flip_feature(self):
        flip_btn=CTkButton(master=self.work_with_image_frame,width=120,height=100,fg_color='#0C0C0C',hover_color='#222222',text='',
image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'flip.png').resize((120,100),Image.BILINEAR),size=(120,100)))
        flip_btn.place(x=660,y=23.5)
        flip_btn.bind('<ButtonPress-1>',lambda e: self.add_flip_image())
        self.save_button22=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',command=self.save_resize_image,text='',corner_radius=30,
  image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.save_button22.place(x=1250,y=80)
        self.save_button22.bind('<ButtonPress-1>',lambda e: self.save_flip_image())
    def add_flip_image(self):
        global image1
        self.virtual_storage.seek(0)
        image=self.virtual_storage.read()
        image=BytesIO(image)
        image=Image.open(image)
        image1=image.transpose(Image.FLIP_LEFT_RIGHT)
        self.virtual_storage.close()
        self.virtual_storage=None
        gc.collect()
        self.virtual_storage=BytesIO()
        image1.save(self.virtual_storage,self.format)
        self.apply_to_main_image(image1,self.only_width,self.only_height)
    def save_flip_image(self):
        file_name=filedialog.asksaveasfilename(title='Save As',defaultextension='*.png',
                     filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_name:
            image1.save(file_name)



    def move_to_text_feature(self):
        self.main_image.unbind('<ButtonPress-1>')
        self.main_image.unbind('<Button-3>')
        self.setting=''
        self.text_logo=CTkLabel(text='',master=self.work_with_image_frame,width=60,height=60,
            image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'writing.png').resize((60,60),Image.BILINEAR),size=(60,60)))
        self.text_logo.place(x=130,y=15)
        self.text_information=CTkLabel(master=self.work_with_image_frame,width=40,height=40,text='',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'information.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.text_information.place(x=135,y=105)
        self.text_information.bind('<Enter>',lambda e: self.text_information_func())
        self.text_information.bind('<Leave>',lambda e: self.text_information_func1())
        self.text_box=CTkTextbox(master=self.work_with_image_frame,width=500,height=118,fg_color='#0C0C0C',text_color='white',font=('Roboto',24))
        self.text_box.place(x=200,y=15)
        value1=[str(i) for i in range(8,52,2)]
        self.size_list=CTkOptionMenu(corner_radius=20,master=self.work_with_image_frame,width=200,height=40,fg_color='#0C0C0C',button_color='#0C0C0C',font=('Roboto',20),button_hover_color='#111111',
        values=value1,dropdown_font=('Roboto',16),dropdown_fg_color='#0C0C0C',dropdown_text_color='white',dropdown_hover_color='#222222')
        self.size_list.place(x=750,y=30)
        value2=['Roboto','Arial','Times New Roman']
        self.font_list=CTkOptionMenu(corner_radius=20,master=self.work_with_image_frame,width=250,height=40,fg_color='#0C0C0C',button_color='#0C0C0C',font=('Roboto',20),button_hover_color='#111111',
        values=value2,dropdown_font=('Roboto',16),dropdown_fg_color='#0C0C0C',dropdown_text_color='white',dropdown_hover_color='#222222')
        self.font_list.place(x=750,y=80)
        self.bold_btn=CTkButton(master=self.work_with_image_frame,width=40,height=40,hover_color='#222222',text='',fg_color='#555555',
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'bold.png').resize((40,40),Image.BILINEAR),size=(40,40)),command=self.add_bold)
        self.bold_btn.place(x=1030,y=20)
        self.italic_btn=CTkButton(master=self.work_with_image_frame,width=40,height=40,hover_color='#222222',text='',fg_color='#555555',
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'italic.png').resize((40,40),Image.BILINEAR),size=(40,40)),command=self.add_italic)
        self.italic_btn.place(x=1090,y=20)
        self.color_list=CTkOptionMenu(corner_radius=20,master=self.work_with_image_frame,width=120,height=40,fg_color='#0C0C0C',button_color='#0C0C0C',font=('Roboto',20),button_hover_color='#111111',
        values=[value for value in self.color_value3.keys()],dropdown_font=('Roboto',16),dropdown_fg_color='#0C0C0C',dropdown_text_color='white',dropdown_hover_color='#222222',)
        self.color_list.place(x=1030,y=80)
        add_text=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',command=self.add_text,text="",
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'add.png').resize((50,50),Image.BILINEAR),size=(50,50)),corner_radius=30)
        add_text.place(x=1250,y=10)
        save=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',command=self.save_text_image,
         image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)),corner_radius=30)
        save.place(x=1250,y=80)


       
    def text_information_func(self):
        self.text_information_frame=CTkFrame(master=self,height=190,width=245,fg_color='#0C0C0C')
        self.text_information_frame.place(x=30,y=140)
        first=CTkLabel(master=self.text_information_frame,text='‧ Click the Add button to\n add new text',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        first.place(x=10,y=10)
        second=CTkLabel(master=self.text_information_frame,text='‧ Click on the Image to\n change text position',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        second.place(x=10,y=70)
        third=CTkLabel(master=self.text_information_frame,text='‧ Left click on the Image\n to delete the text ',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        third.place(x=10,y=130)

    def text_information_func1(self):
        self.text_information_frame.destroy()

    def add_bold(self):
        if 'Bold' not in self.setting:
            self.setting += 'Bold'
        self.bold_btn.configure(fg_color='#0C0C0C')
        self.bold_btn.unbind('<ButtonPress-1>')
        self.bold_btn.bind('<ButtonPress-1>', lambda e: self.remove_bold())

    def remove_bold(self):
        if 'Bold' in self.setting:
            self.setting = self.setting.replace('Bold', '')
        self.bold_btn.configure(fg_color='#555555')
        self.bold_btn.unbind('<ButtonPress-1>')
        self.bold_btn.bind('<ButtonPress-1>', lambda e: self.add_bold())

    def add_italic(self):
        if 'Italic' not in self.setting:
            self.setting += 'Italic'
        self.italic_btn.configure(fg_color='#0C0C0C')
        self.italic_btn.unbind('<ButtonPress-1>') 
        self.italic_btn.bind('<ButtonPress-1>', lambda e: self.remove_italic())

    def remove_italic(self):
        if 'Italic' in self.setting:
            self.setting = self.setting.replace('Italic', '')
        self.italic_btn.configure(fg_color='#555555')
        self.italic_btn.unbind('<ButtonPress-1>')  
        self.italic_btn.bind('<ButtonPress-1>', lambda e: self.add_italic())
    def add_text(self):
        global text,font,color
        text=self.text_box.get(1.0,'end').strip()
        size=int(self.size_list.get())*5
        color=self.color_value3[self.color_list.get()]
        font=self.font_list.get()
        setting=self.setting
        if setting=='ItalicBold':
            setting='BoldItalic'
        font=font+setting
        font=ImageFont.truetype(font=BASE_DIR/'asset'/'font'/f'{font}.ttf',size=size)
        self.virtual_storage.seek(0)
        self.origin_text_image=self.virtual_storage.read()
        self.origin_text_image = BytesIO(self.origin_text_image)
        self.origin_text_image=Image.open(self.origin_text_image)
        self.combined_image1=self.origin_text_image.convert('RGBA')
        self.width_origin1,self.height_origin1=self.origin_text_image.size
        transparent_image1=Image.new('RGBA',(self.width_origin1,self.height_origin1),(0,0,0,0))
        draw=ImageDraw.Draw(transparent_image1)
        draw.text((self.width_origin1/2,self.height_origin1/2),text=text,fill=color,font=font)
        self.transparent_image_list.append(transparent_image1)
        if self.main_image:
            self.show_all_text()
            self.main_image.bind('<ButtonPress-1>',self.config_text_location)
    def config_text_location(self,event):
        try:
            if self.transparent_image_list:
                self.transparent_image_list.pop()
            x_mouse=(event.x-30) *(self.width_origin1/self.only_width)
            y_mouse=(event.y-20) *(self.height_origin1/self.only_height)

            transparent_image=Image.new('RGBA',(self.width_origin1,self.height_origin1),(0,0,0,0))
            draw=ImageDraw.Draw(transparent_image)
            draw.text((x_mouse,y_mouse),text=text,fill=color,font=font)
            self.transparent_image_list.append(transparent_image)
            self.show_all_text()
            self.main_image.bind('<ButtonPress-1>',self.config_text_location)  
            self.main_image.unbind('<Button-3>')
            self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_text()) 
        except Exception:
            pass
    def delete_nearest_text(self):
        if self.transparent_image_list:
            self.transparent_image_list.pop()
            self.show_all_text()
    def show_all_text(self):
        self.final_image = self.combined_image1.copy()
        for trans_img in self.transparent_image_list:
            if trans_img.mode != 'RGBA':
                trans_img = trans_img.convert('RGBA')
            self.final_image = Image.alpha_composite(self.final_image, trans_img)
        self.final_image=self.final_image.convert('RGB')
        if self.main_image:
            self.apply_to_main_image(self.final_image,self.only_width,self.only_height)
            self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_text()) 
            self.all_options.unbind('<ButtonPress-1>')
            self.all_options.bind('<ButtonPress-1>',lambda e: self.all_optionss(image=self.final_image))

    def save_text_image(self):
        file_save=filedialog.asksaveasfilename(title='Save As',
                defaultextension='*.png',
                filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_save:
            self.final_image.save(file_save)



    def move_to_shape_feature(self):
        self.main_image.unbind('<ButtonPress-1>')
        self.main_image.unbind('<Button-3>')
        self.geometric_logo=CTkLabel(master=self.work_with_image_frame,width=60,height=60,fg_color='#333333',text='',
  image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'geomertic.png').resize((60,60),Image.BILINEAR),size=(60,60)))
        self.geometric_logo.place(x=545,y=40)   
        self.line=CTkButton(master=self.work_with_image_frame,width=50,height=50,fg_color='#555555',hover_color='#222222',text='',command=lambda: self.toggle_shape(0),
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'line.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.line.place(x=400,y=40)
        self.rectangle=CTkButton(master=self.work_with_image_frame,width=50,height=50,fg_color='#555555',hover_color='#222222',text='',command=lambda: self.toggle_shape(1),
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'rectangle.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.rectangle.place(x=470,y=40)
        self.circle=CTkButton(master=self.work_with_image_frame,width=50,height=50,fg_color='#555555',hover_color='#222222',text='',command=lambda: self.toggle_shape(2),
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'circle.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.circle.place(x=610,y=40)
        self.triangle=CTkButton(master=self.work_with_image_frame,width=50,height=50,fg_color='#555555',hover_color='#222222',text='',command=lambda: self.toggle_shape(3),
    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'triangle.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        self.triangle.place(x=680,y=40)
        self.geometric_list_name=[self.line,self.rectangle,self.circle,self.triangle]

        self.shape_color=CTkOptionMenu(corner_radius=20,master=self.work_with_image_frame,width=200,height=40,fg_color='#0C0C0C',button_color='#0C0C0C',font=('Roboto',20),button_hover_color='#111111',
        values=[value for value in self.color_value3.keys()],dropdown_font=('Roboto',16),dropdown_fg_color='#0C0C0C',dropdown_text_color='white',dropdown_hover_color='#222222')
        self.shape_color.place(x=780,y=50)

        self.add_shape=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',
   image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'add.png').resize((50,50),Image.BILINEAR),size=(50,50)),corner_radius=30,command=self.add_shape_func)
        self.add_shape.place(x=1250,y=10)
        self.shape_information=CTkLabel(master=self.work_with_image_frame,width=40,height=40,text='',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'information.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.shape_information.place(x=135,y=105)
        self.shape_information.bind('<Enter>',lambda e: self.shape_information_func())
        self.shape_information.bind('<Leave>',lambda e: self.shape_information_frame.destroy())
        
        save=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',
image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)),corner_radius=30,command=self.save_shape_image)
        save.place(x=1250,y=80)
        
       
        self.all_options.bind('<ButtonPress-1>',lambda e: self.all_optionss(self.origin_shape_image))
        
    def shape_information_func(self):
        self.shape_information_frame=CTkFrame(master=self,height=190,width=245,fg_color='#0C0C0C')
        self.shape_information_frame.place(x=30,y=140)
        first=CTkLabel(master=self.shape_information_frame,text='‧ Click the Add button to\n add new shape',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        first.place(x=10,y=10)
        second=CTkLabel(master=self.shape_information_frame,text='‧ Click on the Image to\n change text position',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        second.place(x=10,y=70)
        third=CTkLabel(master=self.shape_information_frame,text='‧ Left click on the Image\n to delete the shape ',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        third.place(x=10,y=130)
    
    def toggle_shape(self,index):
        global index1
        index1=index
        for i,value in enumerate(self.geometric_list_name):
            if i==index1:
                value.configure(fg_color='#222222')
            else:
                value.configure(fg_color='#555555')

    def add_shape_func(self):
        try:
            if index1==0:
                self.add_shape_func2(0)
            elif index1==1:
                self.add_shape_func2(1)
            elif index1==2:
                self.add_shape_func2(2)
            elif index1==3:
                self.add_shape_func2(3)
        except Exception:
            pass
    def add_shape_func2(self,index):
        global shape_color
        self.shape_coord=[]
        shape_color=self.color_value3[self.shape_color.get()]
        self.virtual_storage.seek(0)
        self.origin_shape_image=self.virtual_storage.read()
        self.origin_shape_image = BytesIO(self.origin_shape_image)
        self.origin_shape_image=Image.open(self.origin_shape_image)
        self.width_origin2,self.height_origin2=self.origin_shape_image.size
        self.combined_image2=self.origin_shape_image.convert('RGBA')
        self.transparent_image1=Image.new('RGBA',(self.width_origin2,self.height_origin2),(0,0,0,0))
        self.draw_shape=ImageDraw.Draw(self.transparent_image1)
        self.add_coord(index=index)
    def add_coord(self,index):
        self.main_image.bind('<ButtonPress-1>',lambda e,index=index: self.add_coord2(e,index))
    def add_coord2(self,event,index):
        mouse_x=event.x *(self.width_origin2/self.only_width)
        mouse_y=event.y *(self.height_origin2/self.only_height)
        coord=(mouse_x,mouse_y)
        if len(self.shape_coord)>=3:
            self.shape_coord=[]
        self.shape_coord.append(coord)
        if index==0:    self.config_line()
        if index==1:    self.config_rectangle()
        if index==2:    self.config_circle()
        if index==3:    self.config_triangle()
        
    def config_line(self):
        try:
            if len(self.shape_coord)==2:
                self.draw_shape.line(self.shape_coord,fill=shape_color,width=5)
                self.transparent_image_shape.append(self.transparent_image1)
                self.main_image.unbind('<Button-3>')
                self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_shape())
                self.add_coord(0)  
                self.show_all_shape()  
                self.shape_coord=[]
        except Exception:
            pass
    def config_rectangle(self):
        try:
            if len(self.shape_coord)==2:
                self.draw_shape.rectangle(self.shape_coord,fill=shape_color,width=5)
                self.transparent_image_shape.append(self.transparent_image1)
                self.main_image.unbind('<Button-3>')
                self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_shape())
                self.add_coord(1)
                self.show_all_shape()
                self.shape_coord=[]
        except Exception:
            pass

    def config_circle(self): 
        try:
            if len(self.shape_coord)==2:
                self.draw_shape.ellipse(self.shape_coord,fill=shape_color,width=5)
                self.transparent_image_shape.append(self.transparent_image1)
                self.main_image.unbind('<Button-3>')
                self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_shape())
                self.add_coord(2)
                self.show_all_shape()
                self.shape_coord=[]
        except Exception:
            pass

    def config_triangle(self):
        try:
            if len(self.shape_coord)==2:
                self.main_image.bind('<ButtonPress-1>',lambda e:self.add_triangle_c_coord(e))
            if len(self.shape_coord)==3:
                self.draw_shape.polygon(self.shape_coord,fill=shape_color,width=5)
                self.transparent_image_shape.append(self.transparent_image1)
                self.main_image.unbind('<Button-3>')
                self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_shape())
                self.add_coord(3)
                self.show_all_shape()
                self.shape_coord=[]
        except Exception:
            pass
                
    def add_triangle_c_coord(self,event):
        x=event.x
        y=event.y
        coord=(x,y)
        self.shape_coord.append(coord)

    def delete_nearest_shape(self):
        if self.transparent_image_shape:
            self.transparent_image_shape.pop()
            self.show_all_shape()
    def show_all_shape(self):
        self.final_image1=self.combined_image2.copy()
        for trans_img in self.transparent_image_shape:
            if trans_img.mode != 'RGBA':
                trans_img = trans_img.convert('RGBA')
            self.final_image1=Image.alpha_composite(self.final_image1,trans_img)
        self.final_image1=self.final_image1.convert('RGB')
        if self.main_image:
            self.apply_to_main_image(self.final_image1,self.only_width,self.only_height)
            self.main_image.unbind('<Button-3>')
            self.main_image.bind('<Button-3>',lambda e:self.delete_nearest_shape()) 
            self.all_options.unbind('<ButtonPress-1>')
            self.all_options.bind('<ButtonPress-1>',lambda e : self.all_optionss(self.final_image1))
    def save_shape_image(self):
        file_save=filedialog.asksaveasfilename(title='Save As',
                defaultextension='*.png',
                filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_save:
            self.final_image1.save(file_save)


    def move_to_brightness_feature(self):
        self.setting_brightness=CTkSlider(master=self.work_with_image_frame,width=900,height=20,fg_color='#0C0C0C',button_color='black',button_hover_color='#222222',
        button_corner_radius=30,from_=-200,to=200,number_of_steps=400,corner_radius=30,button_length=5)
        self.setting_brightness.place(x=230,y=60)
        self.setting_brightness.bind('<B1-Motion>',lambda e:self.reset_current_value())
        self.setting_brightness.bind('<ButtonPress-1>',lambda e:self.reset_current_value())
        self.current_value=self.setting_brightness.get()
        self.current_value_label=CTkLabel(master=self.work_with_image_frame,width=30,height=20,fg_color='#0C0C0C',font=('Roboto',16),text_color='white',text=self.current_value)
        self.current_value_label.place(x=635,y=45)

        self.brightness_information=CTkLabel(master=self.work_with_image_frame,width=40,height=40,text='',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'information.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.brightness_information.place(x=135,y=105)
        self.brightness_information.bind('<Enter>',lambda e: self.bright_information_func())
        self.brightness_information.bind('<Leave>',lambda e: self.bright_information_frame.destroy())
        reset=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',corner_radius=30,command=self.reset_brightness,text='',
   image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'reset.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        reset.place(x=1250,y=10)
        
        save=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)),command=self.save_bright_image)
        save.place(x=1250,y=80)
        self.virtual_storage.seek(0)
        image=self.virtual_storage.read()
        image=BytesIO(image)
        self.origin_image_brightness=Image.open(image)
        self.main_image.bind('<ButtonPress-1>',lambda e: self.change_brightness_image())
        self.final_image_bright=self.origin_image_brightness
        self.all_options.bind('<ButtonPress-1>',lambda e: self.all_optionss(self.final_image_bright))
    def bright_information_func(self):
        self.bright_information_frame=CTkFrame(master=self,height=70,width=240,fg_color='#0C0C0C')
        self.bright_information_frame.place(x=30,y=140)
        first=CTkLabel(master=self.bright_information_frame,text='‧ Click on the picture to\n change the brightness',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        first.place(x=10,y=10)
    def reset_current_value(self):
        self.current_value=self.setting_brightness.get()
        self.current_value_label.configure(text=self.current_value)
        self.brightness_value=self.current_value
        
    def change_brightness_image(self):
        image_np=np.array(self.origin_image_brightness)
        image_np=np.clip(image_np+self.brightness_value,0,255).astype(np.uint8)
        self.final_image_bright=Image.fromarray(image_np)
        if self.main_image:
            self.apply_to_main_image(self.final_image_bright,self.only_width,self.only_height)
            self.main_image.bind('<ButtonPress-1>',lambda e: self.change_brightness_image())
    def reset_brightness(self):
        self.setting_brightness.destroy()
        self.setting_brightness=CTkSlider(master=self.work_with_image_frame,width=900,height=20,fg_color='#0C0C0C',button_color='black',button_hover_color='#222222',
        button_corner_radius=30,from_=-200,to=200,number_of_steps=400,corner_radius=30,button_length=5)
        self.setting_brightness.place(x=230,y=60)
        self.reset_current_value()
        self.change_brightness_image()
    def save_bright_image(self):
        file_save=filedialog.asksaveasfilename(title='Save As',
                defaultextension='*.png',
                filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_save:
            self.final_image_bright.save(file_save)

    def move_to_contrast_feature(self): 
        self.setting_contrast=CTkSlider(master=self.work_with_image_frame,width=900,height=20,fg_color='#0C0C0C',button_color='black',button_hover_color='#222222',
        button_corner_radius=30,from_=0,to=2,number_of_steps=100,corner_radius=30,button_length=5)
        self.setting_contrast.place(x=230,y=60)
        self.setting_contrast.bind('<B1-Motion>',lambda e:self.reset_current_value1())
        self.setting_contrast.bind('<ButtonPress-1>',lambda e:self.reset_current_value1())
        self.current_value2=f'{self.setting_contrast.get():.2f}'
        self.current2_value_label=CTkLabel(master=self.work_with_image_frame,width=30,height=20,fg_color='#0C0C0C',font=('Roboto',16),text_color='white',text=self.current_value2)
        self.current2_value_label.place(x=635,y=45)

        self.contrast_information=CTkLabel(master=self.work_with_image_frame,width=40,height=40,text='',
        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'information.png').resize((40,40),Image.BILINEAR),size=(40,40)))
        self.contrast_information.place(x=135,y=105)
        self.contrast_information.bind('<Enter>',lambda e: self.contrast_information_func())
        self.contrast_information.bind('<Leave>',lambda e: self.contrast_information_frame.destroy())
        
        reset=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',command=self.reset_contrast,corner_radius=30,
  text='', image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'reset.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        reset.place(x=1250,y=10)
        
        save=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',command=self.save_contrast_image
       ,corner_radius=30,image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)))
        save.place(x=1250,y=80)
        self.virtual_storage.seek(0)
        image=self.virtual_storage.read()
        image=BytesIO(image)
        self.origin_image_contrast=Image.open(image)
        self.main_image.bind('<ButtonPress-1>',lambda e: self.change_contrast_image())
        self.enhance_img=self.origin_image_contrast
        self.all_options.bind('<ButtonPress-1>',lambda e: self.all_optionss(self.enhance_img))
    def contrast_information_func(self):
        self.contrast_information_frame=CTkFrame(master=self,height=70,width=240,fg_color='#0C0C0C')
        self.contrast_information_frame.place(x=30,y=140)
        first=CTkLabel(master=self.contrast_information_frame,text='‧ Click on the picture to\n change the brightness',
        text_color='white',font=('Roboto',20),fg_color='#0C0C0C')
        first.place(x=10,y=10)
    def reset_current_value1(self):
        self.current_value2=f'{self.setting_contrast.get():.2f}'
        self.current2_value_label.configure(text=self.current_value2)
        self.contrast_value=float(self.current_value2)
    def change_contrast_image(self):
        image=self.origin_image_contrast
        enhance=ImageEnhance.Contrast(image)
        self.enhance_img=enhance.enhance(self.contrast_value)
        if self.main_image:
            self.apply_to_main_image(self.enhance_img,self.only_width,self.only_height)
    def reset_contrast(self):
        self.setting_contrast.destroy()
        self.setting_contrast=CTkSlider(master=self.work_with_image_frame,width=900,height=20,fg_color='#0C0C0C',button_color='black',button_hover_color='#222222',
        button_corner_radius=30,from_=0,to=2,number_of_steps=100,corner_radius=30,button_length=5)
        self.setting_contrast.place(x=230,y=60)
        self.reset_current_value1()
        self.change_contrast_image()
    def save_contrast_image(self):
        file_save=filedialog.asksaveasfilename(title='Save As',
                defaultextension='*.png',
                filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_save:
            self.enhance_img.save(file_save)
    def move_to_filter_color_feature(self):
        self.virtual_storage.seek(0)
        image=self.virtual_storage.read()
        image=BytesIO(image)
        self.origin_image_filter=Image.open(image)
        self.filter_img_width,self.filter_img_height=self.origin_image_filter.size
        self.full_filter=[]
        x=220
        for i in range(0,11):
            filter=CTkButton(master=self.work_with_image_frame,width=70,height=70,text='',fg_color='#222222',hover='disabled',corner_radius=5,
            image=CTkImage(dark_image=Image.open(self.filter_list[i]).resize((60,60),Image.BILINEAR),size=(60,60)),command=lambda index=i,:  self.move_to_choose_filter(index))
            filter.place(x=x,y=40)
            self.full_filter.append(filter)
            x+=80

        save=CTkButton(master=self.work_with_image_frame,width=150,height=50,hover_color='#222222',fg_color='#0C0C0C',text='',
image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'save.png').resize((50,50),Image.BILINEAR),size=(50,50)),corner_radius=30,command=self.save_filter_image)
        save.place(x=1250,y=80)
        self.current_filter_image=self.origin_image_filter
        self.all_options.bind('<ButtonPress-1>',lambda e:self.all_optionss(self.current_filter_image))        
    def move_to_choose_filter(self,index):
        for i,f in enumerate(self.full_filter):
            if index==i:
                f.configure(fg_color='white')
            elif index !=i:
                f.configure(fg_color='#222222')
        if index==0:
            self.move_to_none_filter()
        elif index==1:
            self.move_to_vintage_filter()
        elif index==2:
            self.move_to_bright_fresh_filter()
        elif index==3:
            self.move_to_cool_blue_filter()
        elif index==4:
            self.move_to_warm_autumn_filter()
        elif index==5:
            self.move_to_black_white_filter()
        elif index==6:
            self.move_to_muted_tones_filter()
        elif index==7:
            self.move_to_contrast_filter()
        elif index==8:
            self.move_to_dramatic_filter()
        elif index==9:
            self.move_to_vivid_filter()
        elif index==10:
            self.move_to_soft_pastel_filter()


    def move_to_none_filter(self):
        self.apply_to_main_image(self.origin_image_filter,self.only_width,self.only_height)
        self.current_filter_image= self.origin_image_filter
        
    def move_to_vintage_filter(self):
        zoom_out_img=self.origin_image_filter.resize((int(self.filter_img_width*0.5),int(self.filter_img_height*0.5)),Image.LANCZOS)
        sepia_image = zoom_out_img.convert("RGB")
        sepia_data = [(int(r * 0.393 + g * 0.769 + b * 0.189),
                    int(r * 0.349 + g * 0.686 + b * 0.168),
                    int(r * 0.272 + g * 0.534 + b * 0.131)) for (r, g, b) in sepia_image.getdata()]
        sepia_image.putdata(sepia_data)
        enhancer = ImageEnhance.Contrast(sepia_image)
        vintage_image = enhancer.enhance(0.8)
        vintage_image.resize((self.filter_img_width, self.filter_img_height),Image.LANCZOS)
        self.current_filter_image = vintage_image
        self.apply_to_main_image(vintage_image,self.only_width,self.only_height)
    def move_to_bright_fresh_filter(self):
        enhancer = ImageEnhance.Brightness(self.origin_image_filter)
        bright_image = enhancer.enhance(1.2)
        enhancer = ImageEnhance.Color(bright_image)
        fresh_image = enhancer.enhance(1.4)
        self.current_filter_image =fresh_image
        self.apply_to_main_image(fresh_image,self.only_width,self.only_height)
    def move_to_cool_blue_filter(self):
        zoom_out_img=self.origin_image_filter.resize((int(self.filter_img_width*0.5),int(self.filter_img_height*0.5)),Image.LANCZOS)
        cool_data = [(int(r * 0.5), int(g * 0.5), b) for (r, g, b) in zoom_out_img.getdata()]
        blue_image = Image.new("RGB", zoom_out_img.size)
        blue_image.putdata(cool_data)
        enhancer = ImageEnhance.Contrast(blue_image)
        cool_image = enhancer.enhance(1.15)
        cool_image.resize((self.filter_img_width, self.filter_img_height),Image.LANCZOS)
        self.current_filter_image = cool_image
        self.apply_to_main_image(cool_image,self.only_width,self.only_height)
    def move_to_warm_autumn_filter(self):
        zoom_out_img=self.origin_image_filter.resize((int(self.filter_img_width*0.5),int(self.filter_img_height*0.5)),Image.LANCZOS)
        warm_data = [(int(r * 1.2), int(g * 0.8), int(b * 0.6)) for (r, g, b) in  zoom_out_img.getdata()]
        warm_image = Image.new("RGB", zoom_out_img.size)
        warm_image.putdata(warm_data)
        enhancer = ImageEnhance.Contrast(warm_image)
        autumn_image = enhancer.enhance(1.1)
        autumn_image.resize((self.filter_img_width, self.filter_img_height),Image.LANCZOS)
        self.current_filter_image = autumn_image
        self.apply_to_main_image(autumn_image,self.only_width,self.only_height)

    def move_to_black_white_filter(self):
        bw_image = self.origin_image_filter.convert("L")
        enhancer = ImageEnhance.Contrast(bw_image)
        contrast_image = enhancer.enhance(1.2)
        self.current_filter_image = contrast_image
        self.apply_to_main_image(contrast_image,self.only_width,self.only_height)


    def move_to_muted_tones_filter(self):
        enhancer = ImageEnhance.Color(self.origin_image_filter)
        muted_image = enhancer.enhance(0.6)
        enhancer = ImageEnhance.Brightness(muted_image)
        muted_image = enhancer.enhance(0.9)
        self.current_filter_image = muted_image
        self.apply_to_main_image(muted_image,self.only_width,self.only_height)
    def move_to_contrast_filter(self):
        enhancer = ImageEnhance.Contrast(self.origin_image_filter)
        high_contrast_image = enhancer.enhance(1.8)
        self.current_filter_image = high_contrast_image
        self.apply_to_main_image(high_contrast_image,self.only_width,self.only_height)

    def move_to_dramatic_filter(self):
        bw_image = self.origin_image_filter.convert("L")
        enhancer = ImageEnhance.Contrast(bw_image)
        contrast_image = enhancer.enhance(1.4)
        self.current_filter_image=contrast_image
        self.apply_to_main_image(contrast_image,self.only_width,self.only_height)

    def move_to_vivid_filter(self):
        enhancer = ImageEnhance.Color(self.origin_image_filter)
        vivid_image = enhancer.enhance(2.0)
        self.current_filter_image = vivid_image
        self.apply_to_main_image(vivid_image,self.only_width,self.only_height)

    def move_to_soft_pastel_filter(self):
        zoom_out_img=self.origin_image_filter.resize((int(self.filter_img_width*0.5),int(self.filter_img_height*0.5)),Image.LANCZOS)
        enhancer = ImageEnhance.Contrast(zoom_out_img)
        soft_image = enhancer.enhance(0.7)
        pastel_data = [(int(r * 1.2), int(g * 1.1), int(b * 1.3)) for (r, g, b) in soft_image.getdata()]
        pastel_image = Image.new("RGB", soft_image.size)
        pastel_image.putdata(pastel_data)
        pastel_image.resize((self.filter_img_width, self.filter_img_height),Image.LANCZOS)
        self.current_filter_image = pastel_image
        self.apply_to_main_image(pastel_image,self.only_width,self.only_height)
    def save_filter_image(self):
        file_save=filedialog.asksaveasfilename(title='Save As',
                defaultextension='*.png',
                filetypes=(('PNG Files','*.png'),('JPG Files','*.jpg'),('JPEG Files','*.jpeg'),('GIF Files','*.gif')))
        if file_save:
            self.current_filter_image.save(file_save)



    def apply_to_main_image(self,image,width,height):
        self.main_image.destroy()
        image=CTkImage(dark_image=image.resize((width,height),Image.LANCZOS),size=(width,height))
        self.main_image=CTkLabel(master=self.preview_image_frame,image=image,text='')
        self.main_image.place(x=(1440-width)/2,y=(716-height)/2)
