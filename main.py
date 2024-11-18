from flask import Flask
from flask_restful import Api
from server.routes import (
    user
)

app = Flask(__name__)
api = Api(app)

app.register_blueprint(user.users_blueprint)

if __name__ == '__main__':
    app.run(debug=True)