from app.db.orm.interface import Interface
from app.db.database import db_connect,File

session=db_connect()
class FileORM(Interface):
    def create(self,file: File):
        session.add(file)
        session.commit()
        return file
    def read(self,**kwargs:File):
        file=session.query(File).filter_by(**kwargs).first()
        return file

    def update(self,idd,file_user_id,**kwargs):
        file=session.query(File).filter_by(id2=idd,file_user_id=file_user_id).first()
        if not file: return
        for key,value in kwargs.items():
            if hasattr(file,key):
                setattr(file,key,value)
            else: None
        try:
            session.commit()
        except Exception as e:
            session.rollback()
    def delete(self,**kwargs):
        file=session.query(File).filter_by(**kwargs).first()
        if not file: return
        session.delete(file)
        session.commit()
    def count(self,**kwargs):
        pass
    def read_all(self,**kwargs):
        return session.query(File).filter_by(**kwargs).all()
    