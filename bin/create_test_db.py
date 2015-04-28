import sys 
import os
from cassandra.cluster import Cluster

sys.path.append(os.getcwd())
from cqlengine.management import sync_table 
from app.api.connection import connect 
connect()

from app.api.mod_video.models import Video 
sync_table(Video)