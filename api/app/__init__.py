from flask import Flask, jsonify

app = Flask(__name__)

from app.connection import connect 
connect()

from app.mod_video.controllers import mod_video as mv 
app.register_blueprint(mv)
#from app.api.mod_video.models import Video 
#sync_table(Video)