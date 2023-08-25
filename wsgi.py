# wsgi.py

from flask import Flask
from db.sampleData import add_sample_data
from routes.item import item_bp
from routes.restaurant import restaurant_bp
from routes.login import login_bp
from db.init import startDb
from routes.user import user_bp

app = Flask(__name__)
app.register_blueprint(restaurant_bp)
app.register_blueprint(login_bp)
app.register_blueprint(item_bp)
app.register_blueprint(user_bp)

startDb()
add_sample_data()

if __name__ == '__main__':
    app.run()

