from flask import Flask, render_template
# 导入配置文件
import config
# 导入后台蓝图
from apps.cms import bp as cms_bp
#导入前台蓝图
from apps.front import bp as front_bp
# 导入通过功能蓝图
from apps.common import bp as common_bp
# 导入三方模块
from exts import db
#导入防止跨站攻击模块
from flask_wtf import CSRFProtect

# 初始化app
app = Flask(__name__)

#注册蓝图
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(common_bp)

#导入配置文件
app.config.from_object(config)
db.init_app(app)

#注册csrf模块
csrf = CSRFProtect()
csrf.exempt(front_bp)
csrf.exempt(cms_bp)
csrf.exempt(common_bp)
csrf.init_app(app)

# 处理404错误
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#处理500错误
@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'),500


# 主程序运行
if __name__ == "__main__":
    app.run(host='172.21.13.111',port = 8000)