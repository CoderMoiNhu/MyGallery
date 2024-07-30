from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()

class UserInfo(Base):
    __tablename__='UserInfo'
    id=Column(Integer,primary_key=True)
    index=Column(String,nullable=True)
    username=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    phone_number=Column(Integer,nullable=False,unique=True)
    show_name=Column(String,nullable=True)
    birthday=Column(String,nullable=True)
    gender=Column(String,nullable=True)
    avatar=Column(String,nullable=False)
    background=Column(String,nullable=False)
    file_id=relationship('File',back_populates='user_id')
    image_info=relationship('ImageInfo',back_populates='user_id')
class File(Base):
    __tablename__='File'
    id=Column(Integer,primary_key=True)
    path_name=Column(String)
    id2=Column(String,nullable=True)
    file_user_id=Column(String,ForeignKey('UserInfo.id'),nullable=True)
    user_id=relationship('UserInfo',back_populates='file_id')
class ImageInfo(Base):
    __tablename__='ImageInfo'
    id=Column(Integer,primary_key=True,)
    name_image=Column(String,nullable=False)
    size=Column(String,nullable=False)
    memory=Column(String,nullable=False)
    time=Column(String,nullable=False)
    describe=Column(String,nullable=False)
    id2=Column(String,nullable=True)
    file_user_id=Column(String,ForeignKey('UserInfo.id'),nullable=True)
    user_id=relationship('UserInfo',back_populates='image_info')

def db_connect():
    engine=create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    return session
