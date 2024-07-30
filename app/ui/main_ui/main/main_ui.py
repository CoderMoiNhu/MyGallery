from app.setting.lib import *
from app.ui.main_ui.extra.header_ui import HeaderUI
from app.ui.main_ui.main.right_side_ui import RightSideUI
from app.ui.main_ui.main.left_side_ui import LeftSideUI
from app.ui.main_ui.main.main_screen_ui import MainScreenUI
from app.ui.main_ui.main.album_ui import AlbumUI
from app.ui.main_ui.main.edit_ui import EditUI
from app.db.orm.user_orm import UserORM
from app.db.orm.file_orm import FileORM
from app.db.orm.image_info_orm import ImageInfoORM
class MainUI:
     def __init__(self,authen_ui,username):
          self.main_app=CTk()
          self.main_app.title('MyGallery')
          self.main_app.geometry('1680x950+100+20')
          self.main_app.resizable(False,False)
          self.username=username
          self.authen_ui=authen_ui
          self.user_orm=UserORM()
          self.file_orm=FileORM()    
          self.image_info_orm=ImageInfoORM()
          self.account=self.user_orm.read(username=self.username)
          self.first_album_list=[ BASE_DIR/'asset'/'feather'/'img11.jpeg',
                                BASE_DIR/'asset'/'feather'/'img12.jpeg',
                                BASE_DIR/'asset'/'feather'/'img13.jpeg',
                                BASE_DIR/'asset'/'feather'/'img14.jpeg',
                                BASE_DIR/'asset'/'feather'/'img15.jpeg',
                                BASE_DIR/'asset'/'feather'/'img16.jpeg',
                                BASE_DIR/'asset'/'feather'/'img17.jpeg',
                                BASE_DIR/'asset'/'feather'/'img18.jpeg',
                                BASE_DIR/'asset'/'feather'/'img19.jpeg',
                                BASE_DIR/'asset'/'feather'/'img20.jpeg']
        
          self.second_album_list=[BASE_DIR/'asset'/'feather'/'img21.jpeg',
                                BASE_DIR/'asset'/'feather'/'img22.jpeg',
                                BASE_DIR/'asset'/'feather'/'img23.jpeg',
                                BASE_DIR/'asset'/'feather'/'img24.jpeg',
                                BASE_DIR/'asset'/'feather'/'img25.jpeg',
                                BASE_DIR/'asset'/'feather'/'img26.jpeg',
                                BASE_DIR/'asset'/'feather'/'img27.jpeg',
                                BASE_DIR/'asset'/'feather'/'img28.jpeg',
                                BASE_DIR/'asset'/'feather'/'img29.jpeg',
                                BASE_DIR/'asset'/'feather'/'img30.jpeg']
        
          self.third_album_list=[BASE_DIR/'asset'/'feather'/'img31.jpeg',
                                BASE_DIR/'asset'/'feather'/'img32.jpeg',
                                BASE_DIR/'asset'/'feather'/'img33.jpeg',
                                BASE_DIR/'asset'/'feather'/'img34.jpeg',
                                BASE_DIR/'asset'/'feather'/'img35.jpeg',
                                BASE_DIR/'asset'/'feather'/'img36.jpeg',
                                BASE_DIR/'asset'/'feather'/'img37.jpeg',
                                BASE_DIR/'asset'/'feather'/'img38.jpeg',
                                BASE_DIR/'asset'/'feather'/'img39.jpeg',
                                BASE_DIR/'asset'/'feather'/'img40.jpeg']
          self.preload_gallery1=[]
          self.preload_gallery2=[]
          self.preload_gallery3=[]
          self.preload_images()
          self.edit_image()
          self.init_ui()
     def preload_images(self):
        for i in range(10):
            image1=Image.open(self.first_album_list[i]).resize((668,866),Image.BILINEAR)
            image1=CTkImage(dark_image=image1,size=(668,866))
            self.preload_gallery1.append(image1)
        for i in range(10):
            image2=Image.open(self.second_album_list[i]).resize((506,420),Image.BILINEAR)
            image2=CTkImage(dark_image=image2,size=(506,420))
            self.preload_gallery2.append(image2)
        for i in range(10):
            image3=Image.open(self.third_album_list[i]).resize((506,354),Image.BILINEAR)
            image3=CTkImage(dark_image=image3,size=(506,354))
            self.preload_gallery3.append(image3)

     def edit_image(self):
          self.preload_images_list=[]
          self.path_img=[]
          self.image_file=self.file_orm.read_all(file_user_id=self.account.id)
          if self.image_file:
               for number,file in enumerate(self.image_file,start=1):
                    if not os.path.exists(file.path_name):
                         self.file_orm.delete(file_user_id=self.account.id,id2=number)
                         self.image_info_orm.delete(file_user_id=self.account.id,id2=number)
                         files = [file for file in self.file_orm.read_all(file_user_id=self.account.id)]
                         files.sort(key=lambda x: x.id2)
                         for new_id, file in enumerate(files, start=1):
                              self.file_orm.update(idd=file.id2,file_user_id=self.account.id,id2=new_id)
                         info_file=[file for file in self.image_info_orm.read_all(file_user_id=self.account.id)]
                         for new_id, file in enumerate(info_file, start=1):
                              self.image_info_orm.update(idd=file.id2,file_user_id=self.account.id,id2=new_id)
                         self.edit_image()
                  
                    image= Image.open(file.path_name)
                    self.path_img.append(file.path_name)
                    width,height=image.size
                    res1=width/height
                    if res1 <=1.3:
                         image1=image.resize((270,370),Image.BILINEAR)
                         image=CTkImage(dark_image=image1,size=(270,370))
                         self.preload_images_list.append(image)
                    elif res1 >1.3 and res1<=1.8:
                         image1=image.resize((270,300),Image.BILINEAR)
                         image=CTkImage(dark_image=image1,size=(270,300))
                         self.preload_images_list.append(image)
                    elif res1 >1.8:
                         image1=image.resize((270,200),Image.BILINEAR)
                         image=CTkImage(dark_image=image1,size=(270,200))
                         self.preload_images_list.append(image)

          

    
     def init_ui(self):
        self.header_frame=CTkFrame(master=self.main_app,height=65,fg_color='#0C0C0C')
        self.header_frame.pack(side='top',fill='x')
        self.header=HeaderUI(master=self.header_frame,super_master=self,fg_color='#111111',id=self.account,authen_ui=self.authen_ui)

        self.main_frame=CTkFrame(master=self.main_app,fg_color='#333333')
        self.main_frame.pack(fill='both',expand=True)

        self.right_side_frame=CTkFrame(master=self.main_frame,fg_color='#333333',width=235)
        self.right_side_frame.pack(fill='y',side='right')
        self.right_side=RightSideUI(master=self.right_side_frame,fg_color='transparent')


        self.left_side_frame=CTkFrame(master=self.main_frame,fg_color='#0C0C0C',width=230)
        self.left_side_frame.pack(fill='y',side='left')
        self.left_side=LeftSideUI(master=self.left_side_frame,controller=self,fg_color='#0C0C0C',width=230)
       
        self.main_screen=MainScreenUI(master=self.main_frame,fg_color='#333333',super_master=self)
    
     def remove_gallery_edit_frame(self):
          if hasattr(self,'main_screen'):
             self.main_screen.destroy()
          if hasattr(self,'edit_ui'):
             self.edit_ui.destroy()
          self.right_side_frame.pack_forget()
     def remove_album_edit_frame(self):
          if hasattr(self,'album_ui'):
             self.album_ui.destroy()
          if hasattr(self,'edit_ui'):
             self.edit_ui.destroy()
          self.right_side_frame.pack_forget()
     def remove_album_gallery_frame(self):
          if hasattr(self,'main_screen'):
               self.main_screen.destroy()
          if hasattr(self,'album_ui'):
               self.album_ui.destroy()
          self.right_side_frame.pack_forget()
     def add_album_frame(self):
        self.remove_gallery_edit_frame()
        self.album_ui=AlbumUI(master=self.main_frame,super_master=self,super_master2=self.left_side,width=1450,height=890,fg_color='#0C0C0C',bg_color='#0C0C0C')
     def add_gallery_frame(self):
          self.remove_album_edit_frame()
          self.right_side_frame.pack(fill='y',side='right')
          self.main_screen=MainScreenUI(master=self.main_frame,fg_color='#333333',super_master=self)
     def add_edit_frame(self,image_path):
          self.remove_album_gallery_frame()
          self.edit_ui=EditUI(master=self.main_app,super_master=self,image_path=image_path, super_master2=self.left_side,width=1450,height=890,fg_color='#0C0C0C',bg_color='#0C0C0C')
     def reset_album_ui(self):
          self.album_ui.destroy()
          self.edit_image()
          self.album_ui=AlbumUI(master=self.main_frame,super_master=self,super_master2=self.left_side,width=1450,height=890,fg_color='#0C0C0C',bg_color='#0C0C0C')
         
     def run_ui(self):
        self.main_app.mainloop()