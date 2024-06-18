# # ORM: 테이블 → 객체화
# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = "newuser"   # 실제 테이블 명
#
#     no = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String, nullable=False)
#     password = Column(String, nullable=False)
#     birthdate = Column(DateTime, nullable=False)
#     create_date = Column(DateTime, nullable=False)
#
#     def __init__(self, name, email, password, birthdate, create_date):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.birthdate = birthdate
#         self.create_date = create_date