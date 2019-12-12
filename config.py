# 配置文件

import os
from datetime import timedelta

#开启DEBUG
DEBUG = True

#mysql数据库
HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'jesselee_program'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(username = USERNAME,password = PASSWORD,host = HOST,port = PORT,database = DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MIDIFICATION = False

#session 密钥
SECRET_KEY = os.urandom(24)

#设置session生存时间
PERMANENT_SESSION_LIFETIME = timedelta(days = 1)

#后端用户常量
CMS_USER_ID = 'JesseleeAndNaomiMeetAt20170913'
#前端用户常量
FRONT_USER_ID = 'JesseleeAndNaomiSepreteAt20180312'

#配置CSRF防跨域攻击模块
WTF_CSRF_CHECK_DEFAULT = True

#json数据编码
JSON_AS_ASCII = False

# 设置存储区域地址
UPLOAD_FOLDER = '/StorageErea'

#设置文件接收允许的格式
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
