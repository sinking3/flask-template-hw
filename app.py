from flask import Flask
from controllers.event_controller import event_blueprint

app = Flask(__name__)
app.register_blueprint(event_blueprint)
