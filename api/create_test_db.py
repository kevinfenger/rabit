import sys 
import os
from cassandra.cluster import Cluster

sys.path.append(os.getcwd())
from cassandra.cqlengine.management import sync_table 
from app import app
from app.connection import connect 
connect()
from app.mod_video.models import Video 
sync_table(Video)