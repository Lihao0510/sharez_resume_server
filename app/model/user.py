from . import db
import datetime


# 用户表, 记录用户基础信息, 基于微信openId作为区分
class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    real_name = db.Column(db.String(50), unique=False, index=True, nullable=True)
    nick_name = db.Column(db.String(50), unique=False, index=True, nullable=True)
    mobile = db.Column(db.String(20), unique=True, index=True, nullable=True)
    open_id = db.Column(db.String(100), unique=True, index=True, nullable=False)
    level = db.Column(db.Integer, default=1)
    gender = db.Column(db.Integer, default=1)
    avatar_url = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now)
    device_message = db.Column(db.Text, unique=False, nullable=True)

    def to_json(self):
        dict_data = self.__dict__
        if "_sa_instance_state" in dict_data:
            del dict_data["_sa_instance_state"]
        return dict_data

    def __repr__(self):
        return '<User:%d, %r, %s, %s>' % (self.id, self.open_id, self.mobile, self.nick_name)
