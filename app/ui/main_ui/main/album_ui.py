from app.setting.lib import *
from app.db.orm.file_orm import FileORM
from app.db.database import File,ImageInfo
from app.db.orm.image_info_orm import ImageInfoORM

class AlbumUI(CTkFrame):
    def __init__(self,master,super_master,super_master2,**kwargs,):
        self.super_master=super_master
        self.super_master2=super_master2
        super().__init__(master=master,**kwargs)
        self.place(x=230,y=0)
        self.file_orm=FileORM()
        self.image_info_orm=ImageInfoORM()
        self.count=0
        self.all_count=0
        self.choose_count=1
        self.choose_all_count=1
        self.choose_list1=[]
        self.total_files=0
        self.account_id=self.super_master.account.id
        self.init_ui() 

    def init_ui(self):

        self.work_frame=CTkFrame(master=self,height=100,width=1430,fg_color='#333333',border_width=0,bg_color='#333333')
        self.work_frame.place(x=10,y=0)
        self.upload_btn=CTkButton(master=self.work_frame,height=70,width=70,command=self.upload_files,fg_color='#333333',hover_color='#333333',
        text='',image=CTkImage(dark_image=Image.open( BASE_DIR/'asset'/'feather'/'upload.png').resize((70,70),Image.BILINEAR),size=(70,70)))
        self.upload_btn.place(x=120,y=12)

        self.choose_btn=CTkButton(master=self.work_frame,height=70,width=70,command=self.choose_files,fg_color='#333333',hover_color='#333333',
        text='',image=CTkImage(dark_image=Image.open( BASE_DIR/'asset'/'feather'/'choose.png').resize((70,70),Image.BILINEAR),size=(70,70)))
        self.choose_btn.place(x=402.5,y=12)
        
        self.choose_all_btn=CTkButton(master=self.work_frame,height=70,width=70,command=self.choose_all_files,fg_color='#333333',hover_color='#333333',
        text='',image=CTkImage(dark_image=Image.open( BASE_DIR/'asset'/'feather'/'select-all.png').resize((70,70),Image.BILINEAR),size=(70,70)))
        self.choose_all_btn.place(x=685,y=12)
        self.delete_btn=CTkButton(master=self.work_frame,height=70,width=70,command=self.delete_files,fg_color='#333333',hover_color='#333333',
        text='',image=CTkImage(dark_image=Image.open( BASE_DIR/'asset'/'feather'/'bin.png').resize((70,70),Image.BILINEAR),size=(70,70)))
        self.delete_btn.place(x=967.5,y=12)

        self.edit_btn=CTkButton(master=self.work_frame,height=70,width=70,command=self.edit_files,fg_color='#333333',hover_color='#333333',
        text='',image=CTkImage(dark_image=Image.open( BASE_DIR/'asset'/'feather'/'edit.png').resize((70,70),Image.BILINEAR),size=(70,70)))
        self.edit_btn.place(x=1250,y=12)



        self.your_album_frame=CTkFrame(master=self,height=757,width=1430,fg_color='#333333',bg_color='#333333')
        self.your_album_frame.place(x=10,y=120)
        self.scroll_album_frame=CTkScrollableFrame(master=self.your_album_frame,height=747,width=1410,orientation='vertical',
            scrollbar_button_color='#333333',scrollbar_button_hover_color='#333333',fg_color='#333333')
        self.scroll_album_frame.place(x=0,y=0)
        self.show_image=CTkFrame(master=self.scroll_album_frame,fg_color='#333333')
        self.show_image.pack(fill='x',expand=True)
        self.upload_image()
     

    def upload_image(self):
        self.y1=0
        self.count_columns=0
        self.label_check=[]
        for image in (self.super_master.preload_images_list[::-1]):
            if self.count_columns% 5 ==0:
                x2=0
                row=CTkFrame(master=self.show_image,fg_color='#333333',width=1400,height=370)
                row.place(x=14,y=self.y1)
                self.y1+=380
            up=CTkLabel(master=row,text='',image=image,width=270,height=370,fg_color='#C0C0C0')
            up.place(x=x2,y=0)
          

            self.label_check.append(up)
            x2+=280
            self.count_columns+=1
            self.show_image.configure(height=max(self.y1,747))
        self.choose_options()
    def choose_options(self):
            for index,label_img in enumerate(self.label_check):
                label_img.bind('<ButtonPress-1>',lambda e,img_index=index, label_img=label_img: choose_img(img_index,label_img))

                def choose_img(img_index,label_img):
                    global new_width,new_height
                    global path
                        
                    path_img=self.super_master.path_img[::-1]
                    path=path_img[img_index]
                    image=Image.open(path)
                    width,height=image.size
                    if width<=height:
                            scale=850/height
                            new_height=math.trunc(height*scale)
                            new_width=math.trunc(width*scale)
                    if width>height:
                        scale=height/(width/1600)
                        if width>1600:
                            if scale<850:
                                new_height=math.trunc(height/(width/1600))
                                new_width=1600
                            if scale>850:
                                    new_height=850
                                    new_width=math.trunc(width*(new_height/height))
                        elif width<=1600:
                            scale=850/height
                            new_height=850
                            new_width=math.trunc(width*scale)
                    image=CTkImage(dark_image=Image.open(path).resize((new_width,new_height),Image.LANCZOS),size=(new_width,new_height))
                    if self.all_count==0:
                        open_image(image,img_index)
                    if self.all_count==1:
                        choose_images(img_index,label_img)

   

                def open_image(image,img_index):
                    global name_img_firstshow,image_id
                    self.total_files=len(self.file_orm.read_all(file_user_id=self.account_id))
                    image_id=self.total_files -img_index
                    open_image_frame=CTkFrame(master=self.super_master.main_app,width=1600,height=900,fg_color='#222222')
                    open_image_frame.place(x=40,y=25)
                    main_frame=CTkFrame(master=open_image_frame,width=1600,height=850,fg_color='#333333')
                    main_frame.place(x=0,y=50)
                    full_image=CTkLabel(master=main_frame,image=image,text='')
                    full_image.place(x=(1600-new_width)/2,y=(850-new_height)/2)
                    header_frame=CTkFrame(master=open_image_frame,width=1600,height=50,fg_color='transparent')
                    header_frame.place(x=0,y=0)
                    close_button=CTkButton(master=header_frame,width=40,height=40,fg_color='transparent',text='',hover=False,
                    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'close.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                    close_button.place(x=1552,y=-6)
                    close_button.bind('<ButtonPress-1>',lambda e: close_open_img(open_image_frame))
                    image_name_logo=CTkLabel(master=header_frame,width=40,height=40,fg_color='transparent',text='',
                    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'picture.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                    image_name_logo.place(x=10,y=5)
                    infor_logo=CTkLabel(master=header_frame,width=40,height=40,fg_color='transparent',text='',
                    image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'information.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                    infor_logo.place(x=1200,y=5)
                    final_image=self.image_info_orm.read(file_user_id=self.account_id,id2=image_id)

                    text=final_image.name_image
                    if text in 'Add image name': text=''
                    else: text=text
        
                    CTkLabel(master=header_frame,text=text,font=('Roboto',18,'bold'),text_color='white').place(x=57,y=13)

                    infor_logo.bind('<Enter>',lambda e: step1_to_show_infor(open_image_frame))
                    infor_logo.bind('<Leave>',lambda e: step11_to_show_infor())
                    infor_logo.bind('<ButtonPress-1>',lambda e: step2_to_show_infor(open_image_frame))

                    def step1_to_show_infor(open_image_frame):
                        global info_frame
                        info_frame=CTkLabel(master=open_image_frame,text='  Image Information  ',font=('Roboto',14),fg_color='#CCCCCC',
                        text_color='black',width=70,height=30)
                        info_frame.place(x=1150,y=50)
                    def step11_to_show_infor():
                        info_frame.destroy()
                    def step2_to_show_infor(open_image_frame):
                        global name
                        name=final_image.name_image
                        size=final_image.size
                        memory=final_image.memory
                        time=final_image.time
                        describe=final_image.describe
                        if self.count %2==0:
                            global show_infor_frame
                            info_frame.destroy()
                            show_infor_frame=CTkFrame(master=open_image_frame, width=350,height=400,fg_color='#111111')
                            show_infor_frame.place(x=1200,y=50)
                            name_label=CTkLabel(master=show_infor_frame,fg_color='#111111',width=40,height=40,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'picture.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                            name_label.place(x=10,y=10)
                            name_label_2=CTkLabel(master=show_infor_frame,fg_color='transparent',text=name,font=('Roboto',18),text_color='white',wraplength=250)
                            name_label_2.place(x=60,y=15)
                            name_label_3=CTkLabel(master=show_infor_frame,width=20,height=20,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'change.png').resize((20,20),Image.BILINEAR),size=(20,20)))
                            name_label_3.place(x=315,y=20)
                            name_label_3.bind('<ButtonPress-1>',lambda e: write_img_name_entry())

                            folder_label=CTkLabel(master=show_infor_frame,fg_color='#111111',width=40,height=60,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'folder.png').resize((40,60),Image.BILINEAR),size=(40,60)))
                            folder_label.place(x=10,y=60)
                            folder_label_2=CTkTextbox(master=show_infor_frame,fg_color='transparent',font=('Roboto',18),
                                                    text_color='white',width=270,height=65,border_width=0,)
                            folder_label_2.insert('1.0',path)
                            folder_label_2.configure(state='disabled')
                            folder_label_2.place(x=60,y=55)

                            size_label=CTkLabel(master=show_infor_frame,fg_color='#111111',width=40,height=40,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'size.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                            size_label.place(x=10,y=130)
                            size_label_2=CTkLabel(master=show_infor_frame,fg_color='transparent',text=size,font=('Roboto',18),text_color='white')
                            size_label_2.place(x=60,y=135)


                            memory_label=CTkLabel(master=show_infor_frame,fg_color='#111111',width=40,height=40,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'memory.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                            memory_label.place(x=10,y=180)
                            memory_label_2=CTkLabel(master=show_infor_frame,fg_color='transparent',text=f'{memory} KB',font=('Roboto',18),text_color='white')
                            memory_label_2.place(x=60,y=185)

                            calender_label=CTkLabel(master=show_infor_frame,fg_color='#111111',width=40,height=40,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'calendar.png').resize((40,40),Image.BILINEAR),size=(40,40)))
                            calender_label.place(x=10,y=230)
                            calender_label_2=CTkLabel(master=show_infor_frame,fg_color='transparent',text=time[0:10],font=('Roboto',18),text_color='white')
                            calender_label_2.place(x=60,y=235)


                            describe_label=CTkLabel(master=show_infor_frame,fg_color='#111111',width=40,height=60,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'writing.png').resize((40,60),Image.BILINEAR),size=(40,60)))
                            describe_label.place(x=10,y=310)
                            describe_label_2=CTkTextbox(master=show_infor_frame,width=250,height=110,fg_color='transparent',font=('Roboto',18),border_width=0,
                                text_color='white')
                            describe_label_2.insert('1.0',describe)
                            describe_label_2.configure(state='disabled')
                            describe_label_2.place(x=55,y=280)

                            describe_label_3=CTkLabel(master=show_infor_frame,fg_color='#111111',width=20,height=20,text='',
                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'change.png').resize((20,20),Image.BILINEAR),size=(20,20)))
                            describe_label_3.place(x=315,y=330)
                            describe_label_3.bind('<ButtonPress-1>',lambda e: write_img_describe_entry())



                            def write_img_name_entry():
                
                                name_label_2.place_forget()
                                name_label_3.place_forget()
                                describe_label_3.place_forget()
                                enter_img_name=CTkEntry(master=show_infor_frame,height=50,width=250,border_width=1,fg_color='#111111',font=('Roboto',18),text_color='white')
                                enter_img_name.place(x=60,y=8)
                                enter_img_name.bind('<Return>',lambda e: update_img_name_succes(enter_img_name))
                            def update_img_name_succes(enter_img_name):
                                if len(enter_img_name.get().strip())>0:
                                    self.image_info_orm.update(idd=image_id,file_user_id=self.account_id,name_image=enter_img_name.get())
                                elif len(enter_img_name.get().strip())==0:
                                    self.image_info_orm.update(idd=image_id,file_user_id=self.account_id,name_image='Add image name')
                                name_label_2.configure(text=self.image_info_orm.read(file_user_id=self.account_id,id2=image_id).name_image)
                                enter_img_name.destroy()
                                name_label_2.place(x=60,y=15)
                                name_label_3.place(x=315,y=20)
                                describe_label_3.place(x=315,y=330)

                            def write_img_describe_entry():
                                describe_label_2.place_forget()
                                describe_label_3.place_forget()
                                name_label_3.place_forget()
                                enter_img_describe=CTkTextbox(master=show_infor_frame,height=110,width=250,border_width=1,fg_color='#111111',font=('Roboto',18),text_color='white')
                                enter_img_describe.place(x=60,y=280)
                                enter_img_describe.bind('<Return>',lambda e: update_img_describe_succes(enter_img_describe))
                            def update_img_describe_succes(enter_img_describe):
                                if len(enter_img_describe.get('1.0','end').strip())>0:
                                    self.image_info_orm.update(idd=image_id,file_user_id=self.account_id,describe=enter_img_describe.get('1.0','end'))
                                elif len(enter_img_describe.get('1.0','end').strip())==0:
                                    self.image_info_orm.update(idd=image_id,file_user_id=self.account_id,describe='Add description')
                                describe_label_2.configure(state='normal')
                                describe_label_2.delete('1.0','end')
                                describe_label_2.insert('1.0',self.image_info_orm.read(file_user_id=self.account_id,id2=image_id).describe)
                                describe_label_2.configure(state='disabled')
                                enter_img_describe.destroy()
                                describe_label_2.place(x=55,y=280)
                                describe_label_3.place(x=315,y=330)
                                name_label_3.place(x=315,y=20)
                            
                        elif self.count %2==1:
                            info_frame.destroy()
                            show_infor_frame.destroy() 
                        self.count +=1
                
                def close_open_img(open_image_frame):
                    open_image_frame.destroy()
                
                def choose_images(img_index,label_img):
                    x=label_img.winfo_x()+14+233
                    y=(img_index//5)*380
                    select_icon=CTkButton(master=self.show_image,text='',hover=False,width=20,height=20,bg_color='#2196f3',border_width=0,
                                        image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'select.png').resize((30,30),Image.BILINEAR),size=(20,20)))
                    select_icon.place(x=x,y=y)


                    select_icon.bind('<ButtonPress-1>',lambda e: cancel_select1(img_index,select_icon))
                    label_img.bind('<ButtonPress-1>',lambda e: cancel_select2(select_icon))
                    if img_index not in self.choose_list1: 
                            self.choose_list1.append(img_index)
                    def cancel_select1(img_index,select_icon):
                        select_icon.place_forget()
                        if img_index in self.choose_list1:
                            self.choose_list1.remove(img_index)
                            
                    def cancel_select2(select_icon):
                        select_icon.place_forget()


     

    def upload_files(self):
        self.all_count=0
        files = filedialog.askopenfilenames(title='Choose Files',
        filetypes=(('Image Files', '*.png;*.jpg;*.jpeg;*.gif'),))
        for file in files:
            file_object = File(path_name=file, file_user_id=self.account_id)
            self.file_orm.create(file_object)
            name='Add image name'
            img=Image.open(file)
            width,height=img.size
            size=f'{width}x{height}'
            memory=int(os.path.getsize(file)/1024)
            time=datetime.datetime.now()
            describe='Add description'
            Image_object=ImageInfo(name_image=name,size=size,memory=memory,time=time,describe=describe,
        file_user_id=self.account_id)
            self.image_info_orm.create(Image_object)
        for i in range(1, self.account_id + 1):
            all_files = self.file_orm.read_all(file_user_id=i)
            all_current_id = [file.id2 for file in all_files]
            new = [new_id for new_id in range(1, 1 + len(all_files))]
            
            for current_id, new_id in zip(all_current_id, new):
                self.file_orm.update(idd=current_id,file_user_id=self.account_id, id2=new_id)
                self.image_info_orm.update(idd=current_id,file_user_id=self.account_id,id2=new_id)

        self.super_master.reset_album_ui()
    def choose_files(self):
        self.choose_count+=1
        if self.choose_count %2==0:
            self.all_count=1
            self.choose_btn.configure(fg_color='#222222')
            self.choose_btn.configure(hover_color='#222222')

        if self.choose_count %2==1:
            self.all_count=0
            self.upload_image()
            self.choose_list1=[]
            self.choose_btn.configure(fg_color='#333333')
            self.choose_btn.configure(hover_color='#333333')
  
    def delete_files(self):
        self.total_files=len(self.file_orm.read_all(file_user_id=self.account_id))
        ids_to_delete = []
        for img_index in self.choose_list1:
            file_id = self.total_files - img_index
            ids_to_delete.append(file_id)
        for file_id in ids_to_delete:
            self.file_orm.delete(file_user_id=self.account_id,id2=file_id)
            self.image_info_orm.delete(file_user_id=self.account_id,id2=file_id)
        remaining_files = [file for file in self.file_orm.read_all(file_user_id=self.account_id) if file.id2 not in ids_to_delete and file.id2 is not None]
        remaining_files.sort(key=lambda x: x.id2)
        for new_id, file in enumerate(remaining_files, start=1):
            self.file_orm.update(idd=file.id2,file_user_id=self.account_id,id2=new_id)

        info_file=[file for file in self.image_info_orm.read_all(file_user_id=self.account_id) if file.id2 not in ids_to_delete and file.id2 is not None]
        for new_id, file in enumerate(info_file, start=1):
            self.image_info_orm.update(idd=file.id2,file_user_id=self.account_id,id2=new_id)

        
        self.super_master.edit_image()
        self.work_frame.destroy()
        self.init_ui()
        self.all_count=0
        self.choose_list1=[]
        self.choose_btn.configure(fg_color='#333333')
        self.choose_btn.configure(hover_color='#333333')
    def choose_all_files(self):
        self.choose_all_count+=1
        if self.choose_all_count %2==0:
            self.select_icon_list=[]
            self.all_count=3
            for index1,label in enumerate(self.label_check):
                x=label.winfo_x()+14+225
                y=(index1//5)*380
                select_icon=CTkButton(master=self.show_image,text='',hover=False,width=30,height=30,
                                image=CTkImage(dark_image=Image.open(BASE_DIR/'asset'/'feather'/'select.png').resize((30,30),Image.BILINEAR),size=(30,30)))
                select_icon.place(x=x,y=y)
                if index1 not in self.choose_list1:
                    self.choose_list1.append(index1)
                self.select_icon_list.append(select_icon)
            for index,icon in enumerate(self.select_icon_list):
                icon.bind('<ButtonPress-1>',lambda e,icon2=icon,index2=index: cancel(icon2,index2))
                def cancel(icon,index):
                        icon.place_forget()
                        self.choose_list1.remove(index)
                


        if self.choose_all_count %2==1:
            for icon in self.select_icon_list:
                icon.place_forget()
            self.choose_list1=[]
            self.all_count=0


    def edit_files(self):

        all_files=len(self.file_orm.read_all(file_user_id=self.super_master.account.id))
        if self.choose_list1:
            image_id= self.file_orm.read(id=all_files-self.choose_list1[0])
            image_path=image_id.path_name
            self.destroy()
            self.super_master2.change_your_edit_frame(image_path)