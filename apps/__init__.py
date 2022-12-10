from flask import Flask
import settings
from apps.count.view import count_bp
from apps.music.view import music_bp
from apps.ocr.view import ocr_bp


def create_app():
    app=Flask(__name__,static_folder='../static')
    # 进行全局配置
    app.config.from_object(settings)
    # 在app上注册蓝图
    app.register_blueprint(ocr_bp)
    app.register_blueprint(music_bp)
    app.register_blueprint(count_bp)
    return app