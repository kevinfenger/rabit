from cassandra.cqlengine import management 
from cassandra.cqlengine.connection import setup 

def connect(): 
    setup(["127.0.0.1"], "videos")
    management.create_keyspace('videos', 'SimpleStrategy',replication_factor=1)