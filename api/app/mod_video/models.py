from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model 

class Video(Model):
    __caching__ = '{"keys":"ALL", "rows_per_partition":"10"}' 
    video_id = columns.Text(primary_key=True)
    imgs = columns.Text()
