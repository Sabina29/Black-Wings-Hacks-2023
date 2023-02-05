from flask import Flask

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY']= 'Encrypt cookie data'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix= '/explore')
    app.register_blueprint(auth, url_prefix= '/explore')

    return app