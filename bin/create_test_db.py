import sys 
import os
from cassandra.cluster import Cluster

sys.path.append(os.getcwd())
from cqlengine.management import sync_table 
from app.api.models.connection import connect 
connect()

from app.api.models.videos import Video 
sync_table(Video)
#from app.api.models.connection import connect
#connect()
#try: 
#    cluster = Cluster()
#    session = cluster.connect()
#except Exception as e: 
#    print 'can not connect to a cluster'

#try: 
#    session.execute("CREATE KEYSPACE IF NOT EXISTS videos WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }")
#    session.execute("USE videos")
#    session.execute("CREATE TABLE IF NOT EXISTS vids (video_id text, images text, PRIMARY KEY (video_id)) WITH caching = '{\"keys\":\"ALL\", \"rows_per_partition\":\"10\"}'")
#except Exception as e: 
#    print e
#    print 'something went wrong in setting up the DB' 
