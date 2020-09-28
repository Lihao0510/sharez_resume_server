from . import db
import datetime


# 系统用户表, 记录用户基础信息
class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, default=1)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        props = self.__dict__
        return props

    def __repr__(self):
        return '<User:%r>' % self.name
