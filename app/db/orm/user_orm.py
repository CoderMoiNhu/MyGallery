from app.db.orm.interface import Interface
from app.db.database import db_connect,UserInfo
from base64 import b64encode

session=db_connect()
class UserORM(Interface):
    def create(self,user:UserInfo):
        session.add(user)
        session.commit()
        index=b64encode(str(user.id).encode()).decode()
        self.update(idd=user.id,index=index)
        return user
    def read(self,username):
        user=session.query(UserInfo).filter(UserInfo.username==username).first()
        if user:
            return user
    def update(self,idd,**kwargs):
        user=session.query(UserInfo).filter_by(id=idd).first()
        if not user: return
        for key,value in kwargs.items():
            if hasattr(user,key):
                setattr(user,key,value)
            else: None
        try:
            session.commit()
        except Exception as e:
            session.rollback()
    def delete(self,**kwargs):
        pass
    def count(self,**kwargs):
        pass
    def read_all(self,**kwargs):
        all_file=session.query(UserInfo).filter_by(**kwargs).all()
        return all_file
    