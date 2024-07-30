from app.db.orm.interface import Interface
from app.db.database import db_connect,ImageInfo
from typing import List



session=db_connect()
class ImageInfoORM(Interface):
    def create(self,infor: ImageInfo):
        session.add(infor)
        session.commit()
        return infor
    def read(self,**kwargs):
        return session.query(ImageInfo).filter_by(**kwargs).first()
    
    def update(self,idd,file_user_id,**kwargs):
        info=session.query(ImageInfo).filter_by(id2=idd,file_user_id=file_user_id).first()
        if not info: return
        for key,value in kwargs.items():
            if hasattr(info,key):
                setattr(info,key,value)
            else: None
        try:
            session.commit()
        except Exception as e:
            session.rollback()
    def update_by_file_id(self,file,**kwargs):
        info=session.query(ImageInfo).filter_by(file_id=file).first()
        if not info: return
        for key,value in kwargs.items():
            if hasattr(info,key):
                setattr(info,key,value)
            else: None
        try:
            session.commit()
        except Exception as e:
            session.rollback()
    def delete(self,**kwargs):
        fileinfo= session.query(ImageInfo).filter_by(**kwargs).first()
        if not fileinfo: return
        session.delete(fileinfo)
        session.commit()
    def delete_all(self):
        info_list=session.query(ImageInfo).all()
        if not info_list: return
        for file in info_list:
            session.delete(file)
            session.commit
    def count(self,**kwargs):
        pass
    def read_all(self,**kwargs):
        return session.query(ImageInfo).filter_by(**kwargs).all() 
    